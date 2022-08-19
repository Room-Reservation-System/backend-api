from datetime import datetime
from .objectsType import TypeXlsx
from typing import Literal

class Filter:

    def filter(self,events:list,group:str,header:list,groupMode=False,targets:list=['title','start_time','end_time','day','room'])\
        ->TypeXlsx:
        filtered:list=[]
        for event in events:
            locDict:dict={'group':group}
            for key,val in event.items():
                if key in targets:
                    locDict[key]=val
            filtered.append(locDict)
        filtered=self.converter(events=filtered)
        return TypeXlsx(dataList=filtered,header=self.filterHeader(header=header,groupMode=groupMode))
        # {k:v for k,v in header[0].items() if k in ['major','year']}
    def filterHeader(self, header:dict, groupMode=False)->dict[Literal['major']:str|Literal['year']:int]:
        year=header['year']
        name:str=''
        if groupMode:
    
            for key,val in header.items():
                if key =='major':
                    name+=val
                if '&' not in name:
                    name+=' & '
        else:
            name=header['major']
        return {'major':name,'year':year}

    def mergeTypeXlsx(self, dict1, dict2)->TypeXlsx:
        newList=dict1['dataList']
        newList.extend(dict2['dataList'])
        dict1['dataList']=newList
        return TypeXlsx(dataList=dict1,header=self.filterHeader(header=header,groupMode=groupMode))


    def converter(self,events:list)->list:
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