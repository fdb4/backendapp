from flask import jsonify
def getClients():
    return {"email": "saminC@example.com","firstname": "Samin","lastname": "Test"}
def signUpClient(email, password, firstname, lastname, userType):
    if email=="email@email.com":
        return jsonify({"message": f"User with email "+email+" already exists"})
    else:
        return jsonify({"message": "User created successfuly"})
def survey(clientID, height, weight, goalweight, movement, age, gender, cycling, strength, running, sports, yoga, swimming, martialarts, other):
    return jsonify({"message": "Client preferences updated"})
def signUpCoach(clientID, price, experience, bio, gym, town, state):
    return jsonify({"message": "Coach created successfully"})
def getCoaches():
    return [{"clientID": 1, "email": "saminC@example.com", "firstname": "Samin", "lastname": "Test", "price": 53.68, "rating": 10, "experience": 1, "bio": "Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.", "gym": "Quimba", "town": "Santa Monica", "state": "ARKANSAS", "specializations": ["cycling", "running", "sports", "swimming", "martialarts"]}, {"clientID": 2, "email": "wtanslie1@ucoz.ru", "firstname": "Waverly", "lastname": "Tanslie", "price": 55.93, "rating": 10, "experience": 2, "bio": "Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.", "gym": "Topiclounge", "town": "Chanika", "state": "SOUTH CAROLINA", "specializations": ["strength", "running", "yoga"]}]
def getMessage(clientID,clientID2):
    return[{"message": "Hi", "SenderFN": "Christina", "SenderLN": "Elldred", "lastmodified": "2023-12-09T15:18:01"}, {"message": "Hey", "SenderFN": "Chris", "SenderLN": "Elldred", "lastmodified": "2023-12-09T15:57:21"}, {"message": "what you want", "SenderFN": "Christina", "SenderLN": "Elldred", "lastmodified": "2023-12-12T16:58:17"}, {"message": "im out bye", "SenderFN": "Christ", "SenderLN": "Elldred", "lastmodified": "2023-12-12T16:59:54"}]
def postMessage(clientIDS,clientIDR,messageT):
    return jsonify({"message": "Message successfuly sent"})
def delete_coach_profile(coach_id):
    return {"message": "Coach profile deleted successfully"}, 200
def getWorkouts():
    return [
    {
        "workoutID": 2,
        "workoutname": "Incline Bench Press",
        "videolink": "https://www.youtube.com/embed/ajdFwa-qM98",
        "description": "This is a chest exercise performed on an inclined bench. It targets the upper chest muscles. User a barbell or dumbbells and press them upwards while laying on the incline bench",
        "musclegroup": "chest",
        "equipment": "inlcine bench, barbell or dumbbells"
    },
    {
        "workoutID": 4,
        "workoutname": "Cable Cross",
        "videolink": "https://www.youtube.com/embed/taI4XduLpTk?si=KopWEkjJLa1BwdpN",
        "description": "Cable crowssovers target the chest muscles by pulling cables from opposite sides, crowssing them in front of the body.",
        "musclegroup": "chest",
        "equipment": "cable machine"
    }]
def dailyLog(clientID, calorie, water, mood):
    return jsonify({"message": "Daily Log Recorded"})
def filterWorkoutsByEquipment(equipment):
    if equipment =="inlcine bench, barbell or dumbbells":
        return  [{
        "workoutID": 2,
        "workoutname": "Incline Bench Press",
        "videolink": "https://www.youtube.com/embed/ajdFwa-qM98",
        "description": "This is a chest exercise performed on an inclined bench. It targets the upper chest muscles. User a barbell or dumbbells and press them upwards while laying on the incline bench",
        "musclegroup": "chest",
        "equipment": "inlcine bench, barbell or dumbbells"
    }]
    if equipment=="barbell, dumbells":
        return [
            {
                "workoutID": 7,
                "workoutname": "Bent Over Rows",
                "videolink": "https://www.youtube.com/embed/FWJR5Ve8bnQ?si=0aDw47IpWIrWSG77",
                "description": "Bent over rows target the muscles in the upper and middle back. Bend at the hips, keep your back straight, and pull the weight (barbell or dumbbells) towards your lower chest while keeping your elbows close to your body.",
                "musclegroup": "back",
                "equipment": "barbell, dumbells"
            },
    {
        "workoutID": 11,
        "workoutname": "Military Press",
        "videolink": "https://www.youtube.com/embed/QAQ64hK4Xxs?si=3Xdi5TXI7Afm33qA",
        "description": "The military press targets the deltoid muscles. While standing or sitting, press the weight (barbell or dumbbells) overhead from shoulder height.",
        "musclegroup": "shoulder",
        "equipment": "barbell, dumbells"
    }
    ]
def filterByGym(gym):
    if gym=='Quimba' :
        return [
    {
        "clientID": 1,
        "email": "saminC@example.com",
        "firstname": "Samin",
        "lastname": "Test",
        "price": 53.68,
        "rating": 10,
        "experience": 1,
        "bio": "Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.",
        "gym": "Quimba",
        "town": "Santa Monica",
        "state": "ARKANSAS",
        "specializations": [
            "cycling",
            "running",
            "sports",
            "swimming",
            "martialarts"
        ]
    }]

    elif gym=='Flashspan':
        return [{
        "clientID": 3,
        "email": "pblondin2@seattletimes.com",
        "firstname": "Pauli",
        "lastname": "Blondin",
        "price": 89.47,
        "rating": 0,
        "experience": 1,
        "bio": "Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.",
        "gym": "Flashspan",
        "town": "Suchy Dąb",
        "state": "ARIZONA",
        "specializations": [
            "strength",
            "sports",
            "yoga",
            "swimming",
            "other"
        ]
    }]
def handleRequest(coachID, clientID, decision):
    if coachID==101:
        return {"message":"User is not a coach"},401
    if coachID==1:
        return {"message": "Update successful"}
def viewCoachClients(clientID):
    if  clientID==1:
        return [
    {
        "clientID": 1178,
        "firstname": "Sandeep",
        "lastname": "Singh"
    },
    {
        "clientID": 1212,
        "firstname": "FNN",
        "lastname": "LNN"
    }
]
