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
@mock.patch("api.MessageController.getMessage", side_effect=tests.Mockservice.getMessage)
def test_getMessages(message,client):
    cl=client.get("/message/1014/1")
    assert cl.json[0]["message"]=="Hi"
    assert cl.json[1]["message"] == "Hey"
    assert cl.json[2]["message"] == "what you want"
@mock.patch("api.MessageController.postMessage", side_effect=tests.Mockservice.postMessage)
def test_getMessages(message,client):
    data = {"message": "What kind of food are you click here for more info",
            "clientID": 1738}
    cl = client.post("/message/2", data=json.dumps(data), content_type='application/json')
    assert cl.json["message"]=="Message successfuly sent"
@mock.patch("api.deleteCoachProfileController.delete_coach_profile", side_effect=tests.Mockservice.delete_coach_profile)
def test_deleteCoach(message,client):
    cl = client.delete("/coach/delete/3000")
    assert cl.json["message"]=="Coach profile deleted successfully"
    assert cl.status_code==200
