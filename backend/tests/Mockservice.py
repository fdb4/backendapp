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