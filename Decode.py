# -*- coding: utf-8 -*-
import datetime
import re

class decoder:
    message_type=''
    process_datetime=''
    message_datetime=''
    cor=False
    airport=''
    primary_key=''
    
    def __init__(self,message):
        decode= re.search('(METAR|TAF|SPECI)\s((COR|AMD)\s)?([A-Z]{4})\s(\d{2})(\d{2})(\d{2})Z',message)
        self.message_type=decode.group(1)
        self.process_datetime=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        
        message_datetime=datetime.datetime.utcnow()        
        if int(decode.group(5))<=message_datetime.day:
            message_datetime=message_datetime.replace(day=int(decode.group(5)),
                                                      hour=int(decode.group(6)),
                                                      minute=int(decode.group(7)),
                                                      second=0,microsecond=0)                                                                 
            self.message_datetime=message_datetime.strftime("%Y-%m-%d %H:%M:%S")
            
        else:
            message_datetime=message_datetime.replace(month=message_datetime.month-1,
                                                      day=int(decode.group(5)),
                                                      hour=int(decode.group(6)),
                                                      minute=int(decode.group(7)),
                                                      second=0,microsecond=0)
            self.message_datetime=message_datetime.strftime("%Y-%m-%d %H:%M:%S")

        if decode.group(3)!=None:
            self.cor=True
            
        self.airport=decode.group(4)
        self.primary_key=decode.group(0).replace(' ','')
        