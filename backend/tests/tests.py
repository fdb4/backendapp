import pytest
from tests import client
import pytest_mock
import mock
from mock import call
import tests.Mockservice
import json
from flask import jsonify
@mock.patch("api.getClientsController.getClients",side_effect=tests.Mockservice.getClients)
def test_clients(clients,client):
    cl=client.get("/clients")
    assert cl.json["email"]=="saminC@example.com"
    assert cl.json["firstname"] == "Samin"
    assert cl.json["lastname"]=="Test"
@mock.patch("api.signUpController.signUpClient",side_effect=tests.Mockservice.signUpClient)
def test_register(User,client):
    data={"email": "email@email.com",
        "firstname":"email",
        "lastname":"jason",
        "password":"password",
        "userType":"1"}
    cl=client.post("/signup",data=json.dumps(data),content_type='application/json')
    assert cl.json["message"] == "User with email email@email.com already exists"
    data = {"email": "User@email.com",
            "firstname": "email",
            "lastname": "jason",
            "password": "password",
            "userType": "1"}
    cl = client.post("/signup", data=json.dumps(data), content_type='application/json')
    assert cl.json["message"] == "User created successfuly"
@mock.patch("api.clientSurveyController.survey",side_effect=tests.Mockservice.survey)
def test_signupclient(clientSur,client):
    data={
        "clientID":100,
        "height":1.6,
        "weight": 100,
        "goalweight":223,
        "movement": "Very Active",
        "age":1,
        "gender":0,
        "cycling":1,
        "strength":0,
        "running":1,
        "sports":0,
        "yoga":1,
        "swimming":1,
        "martialarts":1,
        "other":"IDK"
    }
    cl=client.post("/survey",data=json.dumps(data),content_type='application/json')
    assert cl.json["message"] == "Client preferences updated"
@mock.patch("api.signUpCoachController.signUpCoach",side_effect=tests.Mockservice.signUpCoach)
def test_signupcoach(coachSur,client):
    data={
        "clientID":1,
        "price":100.00,
        "experience":100,
        "bio":"Just a coach",
        "gym":"Pokemon Gym",
        "town":"Pokemon town",
        "state":"Pokemon State"

    }
    cl=client.post("/coachSignUp",data=json.dumps(data),content_type='application/json')
    assert cl.json["message"] == "Coach created successfully"

@mock.patch("api.getCoachesController.getCoaches", side_effect=tests.Mockservice.getCoaches)
def test_getCoaches(coaches,client):
    cl=client.get("/coaches")
    assert cl.json[0]["clientID"]==1
    assert cl.json[0]["specializations"] == ["cycling", "running", "sports", "swimming", "martialarts"]
    assert cl.json[1]["clientID"] == 2
    assert cl.json[1]["specializations"] ==["strength", "running", "yoga"]
@mock.patch("api.MessageController.getMessage", side_effect=tests.Mockservice.getMessage)
def test_getMessages(message,client):
    cl=client.get("/message/1014/1")
    assert cl.json[0]["message"]=="Hi"
    assert cl.json[1]["message"] == "Hey"
    assert cl.json[2]["message"] == "what you want"
@mock.patch("api.MessageController.postMessage", side_effect=tests.Mockservice.postMessage)
def test_postMessages(message,client):
    data = {"message": "What kind of food are you click here for more info",
            "clientID": 1738}
    cl = client.post("/message/2", data=json.dumps(data), content_type='application/json')
    assert cl.json["message"]=="Message successfuly sent"
@mock.patch("api.getWorkoutsController.getWorkouts", side_effect=tests.Mockservice.getWorkouts)
def test_getWorkout(message,client):
    cl= client.get("/workouts")
    assert cl.json[0]["workoutID"]==2
    assert cl.json[0]["equipment"]=="inlcine bench, barbell or dumbbells"
    assert cl.json[1]["workoutID"] == 4
    assert cl.json[1]["equipment"] == "cable machine"
@mock.patch("api.dailyLogController.dailyLog", side_effect=tests.Mockservice.dailyLog)
def test_postDailyLog(message,client):
    data = {"clientID":23,
        "calorie":2000,
        "water":2000,
        "mood":5,}
    cl = client.post("/dailyLog", data=json.dumps(data), content_type='application/json')
    assert cl.json["message"] == "Daily Log Recorded"
@mock.patch("api.filterWorkoutsByEquipmentController.filterWorkoutsByEquipment", side_effect=tests.Mockservice.filterWorkoutsByEquipment)
def test_filterworkoutbyEquipment(message,client):
    cl = client.get("workouts/filter/equipment/inlcine bench, barbell or dumbbells")
    assert cl.json[0]["workoutname"] == "Incline Bench Press"
    cl = client.get("workouts/filter/equipment/barbell, dumbells")
    assert cl.json[0]["workoutname"] == "Bent Over Rows"
    assert cl.json[1]["workoutname"] == "Military Press"
@mock.patch("api.filterCoachesByGymController.filterByGym", side_effect=tests.Mockservice.filterByGym)
def test_filter_coaches_by_Gym(message,client):
    cl = client.get("/coaches/filter/gym/Quimba")
    assert cl.json[0]["firstname"] == "Samin"
    assert cl.json[0]["lastname"] == "Test"
    assert cl.json[0]["price"] == 53.68
    cl = client.get("/coaches/filter/gym/Flashspan")
    assert cl.json[0]["firstname"] == "Pauli"
    assert cl.json[0]["lastname"] == "Blondin"
    assert cl.json[0]["price"] == 89.47

@mock.patch("api.handleRequestController.handleRequest", side_effect=tests.Mockservice.handleRequest)
def test_handleRequests(message,client):
    data = {"coachID":101,
        "clientID":1,
        "decision":1}
    cl = client.post("/coaches/requests", data=json.dumps(data), content_type='application/json')
    assert cl.json["message"] == "User is not a coach"
    data = {"coachID": 1,
            "clientID": 1,
            "decision": 1}
    cl = client.post("/coaches/requests", data=json.dumps(data), content_type='application/json')
    assert cl.json["message"] == "Update successful"

@mock.patch("api.viewCoachClientsController.viewCoachClients", side_effect=tests.Mockservice.viewCoachClients)
def test_viewCoachClients(message,client):
    cl = client.get("/coaches/clients/1")
    assert cl.json[0]["clientID"] == 1178
    assert cl.json[1]["clientID"] == 1212

@mock.patch("api.deleteCoachProfileController.delete_coach_profile", side_effect=tests.Mockservice.delete_coach_profile)
def test_deleteCoach(message,client):
    cl = client.delete("/coach/delete/3000")
    assert cl.json["message"]=="Coach profile deleted successfully"
    assert cl.status_code==200

