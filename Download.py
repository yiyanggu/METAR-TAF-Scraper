import urllib3
import json

class Download():
    
    def __init__(self,airport):
        self.airport=airport
        self.metar=[]
        self.taf=[]
        http=urllib3.PoolManager()
        url="http://www.avt7.com/Home/AirportMetarInfo"
        response=http.request('GET',url,fields={'airport4code':self.airport})
        data=json.loads(response.data.decode('utf-8'))
        metar=data['metarContentList']['rows']
        taf=data['tafContentList']['rows']
        for i in range(0,len(metar)):
            self.metar.append(metar[i]['content'])
        for i in range(0,len(taf)):
            self.taf.append(taf[i]['content'])
    

