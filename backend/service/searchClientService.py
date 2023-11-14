from data.models import Clients

def searchClient(clientID):
        client=Clients.query.get_or_404(clientID)
        return client