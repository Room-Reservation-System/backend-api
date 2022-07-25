from datetime import datetime

class Filter:

    def timeColumn(self,timing:dict={'startTime':{'hours':'08','minutes':'00'},'endTime':{'hours':'00','minutes':'00'},'stepMinute': 30},):
        timeSlots:list=[]
        Hour,Minute,stepMinute=map(str,(timing['startTime']['hours'],timing['startTime']['minutes'],timing['stepMinute']))
        endHour,endMinute=map(str,(timing['endTime']['hours'],timing['endTime']['minutes']))
        # while True:
        #     timeSlots.append()
        #     if f'{Hour}{Minute}'==f'{endHour}{endMinute}':
        #         break 
        # print(f'{startHour=}:{startMinute=}:{stepMinute=}')
        # print(f'{endHour=}:{endMinute=}')

    def filter(self,events:list, targets:list=['title','start_time','end_time','date'])->list:
        filtered:list=[]
        for event in events:
            locDict:dict={}
            for key,val in event.items():
                if key in targets:
                    locDict[key]=val
            filtered.append(locDict)
        filtered=self.__converter(events=filtered)
        return filtered

    def __converter(self,events:list)->list:
        for event in events:
            date:list=list(map(int,event['date'].split('-')))
            event['date']=datetime(date[0],date[1],date[-1]).strftime('%A')
            event['day']=event.pop('date')

            event['start_time']=event['start_time'][:-3]
            event['end_time']=event['end_time'][:-3]
            if event['start_time'][0]=='0':
                event['start_time']=event['start_time'][1:]
            if event['end_time'][0]=='0':
                event['end_time']=event['end_time'][1:]
        return events
    


Filter().timeColumn()