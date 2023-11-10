from flask import session

def logoutClient(clientID):
    session.pop(clientID)
    return "200"