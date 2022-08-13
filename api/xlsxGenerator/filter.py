from datetime import datetime

class Filter:

    def filter(self,events:list, targets:list=['title','start_time','end_time','day'])->list:
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
        weekdays:dict={'1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday','5':'Friday','6':'Saturday','7':'Sunday'}
        for event in events:
            event['day']=weekdays[event['day']]

            event['start_time']=event['start_time'][:-3]
            event['end_time']=event['end_time'][:-3]
            if event['start_time'][0]=='0':
                event['start_time']=event['start_time'][1:]
            if event['end_time'][0]=='0':
                event['end_time']=event['end_time'][1:]
        return events