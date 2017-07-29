import Download
import Decode
import sqlite3


airportlist=['ZBAA','ZUAS','ZBCF','ZPPP']
metar=Download.Download('ZBAA').metar
taf=Download.Download('ZBAA').taf



#    print(div1)
#    print('#########################      '+airport+' METAR'+'      #########################')
#    print(div1)
def storemetar(metar):
    for i in range(len(metar)):
        TYPE=re.search('(METAR|TAF)',metar).group()
        
#    print(div1)
#    print('##########################      '+airport+' TAF'+'      ##########################')
#    print(div1)    
    for i in range(len(taf)):   
        print(metar[i]['content'])
    

con = sqlite3.connect("weatherdata.db")
  
for item in airportlist:
    download=downloadmetartaf('ZBDS')
    metar=download['metar'][0]['content']
    
con.close()  