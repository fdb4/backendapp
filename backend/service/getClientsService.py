from data.models import Clients
def getClients():
        clients=Clients.query.all()
        return clients

