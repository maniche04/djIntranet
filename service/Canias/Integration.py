from zeep import Client
import xml.etree.ElementTree as xml
import json
import xmltodict

class Canias:
    #A Class for Communication with Canias ERP
    url = 'http://192.168.200.2:8080/caniasWS603/services/iasWebService?WSDL'

    # Standard User Credentials
    clientcode = '00'
    language = 'EN'
    database = 'JZNTST'
    clientmanager = 'CANIAS'
    serverip = '192.168.200.2'
    username = 'soapclient'
    password = 'forw@rd'

    def __init__(self):
        self.client = Client(self.url)
        if len(self.getSession()) < 1:
            self.login()

    def login(self):
        newSession = self.client.service.login(self.clientcode, self.language, self.database, self.clientmanager, self.serverip, self.username, self.password)
        print ("New Session is " + newSession)
        self.saveSession(newSession)

    def logout(self):
        try:
            self.client.service.logout(self.getSession())
        except:
            self.saveSession('')

    def run(self, service, parameters):
        try:
            pingstate = self.client.service.callIASService(self.getSession(),'JZNPING',1,'STRING',1)
            print("Current Ping State is: " + str(pingstate))
            if (pingstate == 0):
                print("Session Invalid! Logging Out!")
                self.logout()
                self.login()
        except:
            self.logout()
            self.login()
        finally:
            try:
                data = self.client.service.callIASService(self.getSession(),service,parameters,'STRING',1)
                jsondata = json.loads(json.dumps(xmltodict.parse(data)))
                return json.dumps(jsondata[list(jsondata.keys())[0]]['ROW']);
                # return json.dumps(jsondata[jsondata.keys()[0]]['ROW'])
            except:
                return 0

    def getSession(self):
        f = open('/home/manish/intranet/service/Canias/.canias','r')
        return f.readline()

    def saveSession(self, session):
        f = open('/home/manish/intranet/service/Canias/.canias','w')
        f.write(session)
        f.close()