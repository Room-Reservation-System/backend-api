from datetime import datetime
from hashlib import new
from .objectsType import TypeXlsx
from typing import Literal, List

class Filter:
    
    def __init__(self,targets:list=['title','start_time','end_time','day','room']):
        self.targets=targets

    def filterRoom(self,roomData:List[dict],group=None)->TypeXlsx:
        filtered:list=[]
        for event in roomData:
            locDict:dict={}
            if group is not None:
                locDict['group']=group
            for key, val in event.items():
                if key in self.targets:
                    locDict[key]=val
            filtered.append(locDict)
        filtered=self.converter(events=filtered)
        # return(filtered)
        return TypeXlsx(dataList=filtered)

    def filterHeader(self, header:dict, groupMode=False):
        if type(header) is int or type(header) is str:
            return f'{header}'
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
        return f'{name}-{year}'
    def filterInstractor(self,classes, instructor):
        filteredList:list=[]
        for event in classes:
            locDict:dict={}
            for key, val in event.items():
                if key in self.targets:
                    locDict[key]=val
            filteredList.append(locDict)
        filtered={'classes':self.converter(events=filteredList),
                  'instructor':instructor['name']}
        return filtered
    def filterName(self,major:str,year:int)->str:
        return f'{major}{year}'
        
    def mergeData(self, dict1, dict2)->dict:
        newList=dict1['dataList']
        newList.extend(dict2['dataList'])
        return newList

    def mergeHeader(self,dict1, dict2)->dict:
        name1=dict1['major']
        name2=dict2['major']
        year=dict1['year']
        return f'{name1}&{name2}{year}'

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