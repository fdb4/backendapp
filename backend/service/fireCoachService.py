from . import unsendRequestService
from data.models import Clients

def fireCoach(clientID, coachID):
    unsendRequestService.unsendRequest(clientID, coachID)
    
    return {"message":"Coach removed succesfully"}

