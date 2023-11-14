from data.models import Clients, GeneralInfo
from data.exts import db
def getGenInfo():
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
    ).join(Clients, GeneralInfo.geninfoID == Clients.geninfoID, isouter=True).all()
    return general_info