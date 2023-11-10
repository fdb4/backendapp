from data.models import Clients, GeneralInfo
from data.exts import db
def getClientGenInfo(clientID):
    general_info=db.session.query(
        Clients.clientID,
        Clients.firstname, 
        Clients.lastname, 
        Clients.email,
        GeneralInfo.height, 
        GeneralInfo.weight, 
        GeneralInfo.goalweight, 
        GeneralInfo.movement, 
        GeneralInfo.age, 
        GeneralInfo.gender
    ).join(Clients, (Clients.clientID == clientID) & (GeneralInfo.geninfoID == Clients.geninfoID)).all()
    return general_info