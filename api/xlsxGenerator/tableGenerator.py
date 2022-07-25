from random import choice
from .base import Base
from .filter import Filter
from .style import Style
from django.conf import settings
from os import path
class Node():
    current_index:int=0
    used:int=0
    next_index:int=0


class TableGenerator(Style):
    def __init__(self,data:list,title:str,timing:dict={'startTime': {'hours':8, 'minutes':00},'endTime':{'hours':24,'minutes':00}},):

        self.data=Filter().filter(data)
        self.title=f"Time table"
        self.timing=timing

        self.week_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.columns=['A','B','C','D','E','F','G','H']

    def setData(self,):
        color_fill=[ #'FFCCCC','FFE5CC','FFFFCC','E5FFCC','CCFFCC','CCFFE5','CCFFFF','CCE5FF','CCCCFF','E5CCFF','FFCCFF','FFCCE5',
                    'FF9999','FFCC99','FFFF99','CCFF99','99FF99','99FFCC','99FFFF','99CCFF','9999FF','CC99FF','FF99FF','FF99CC'
        ]

        self.__getTemplate()

        subjectColor:dict={}
       
        for val in self.data:
            
            row_A:int=0
            row_B:int=0        
            column_A:int=''
            name=val['title'].upper()
            start_time=val['start_time']
            end_time=val['end_time']
            if name not in subjectColor:
                subjectColor[name]=choice(color_fill)
            
            for i, row in enumerate(Base.sheet['A']):
                if row.value==val['start_time']:
                    row_A=i #1
                if row.value==val['end_time']:
                    row_B=i#2
            for i, column in enumerate(Base.sheet[3]):
                if column.value==val['day']:
                    column_A=i
            cellDesc:str=f'{name}\n\n{start_time}-{end_time}'
            self.colorCell(column=self.columns[column_A],row=row_A+1, color=subjectColor[name])
            Base.sheet.merge_cells(f'{self.columns[column_A]}{row_A+1}:{self.columns[column_A]}{row_B}')
            self.writeText(column=self.columns[column_A],row=row_A+1,text=cellDesc, fontType='class')
        dirName=path.join(settings.BASE_DIR, 'xlsxFiles' ,f'{self.title}.xlsx')
        Base.wb.save(filename=dirName)

    def __getTemplate(self):

        Base.sheet.merge_cells('B1:H1')
        Base.sheet.row_dimensions[1].height=25
        self.colorCell(column='B',row=1,color='E0E0E0')
        self.colorCell(column='A',row=1,color='E0E0E0')
        self.writeText(column='B', row=1, text=self.title,fontType='title')
        
        for i, cell in enumerate(self.columns):
            Base.sheet.merge_cells(f'{self.columns[i]}3:{self.columns[i]}4')
            self.colorCell(column=self.columns[i],row=3)
            if cell=='A':
                Base.sheet.column_dimensions['A'].width=15
                self.writeText(column='A',row=3,text='Duration')
            else:
                Base.sheet.column_dimensions[cell].width=35
                self.writeText(column=cell, row=3, text=self.week_list[i-1],fontType='general')
        data_time=[hour%24 for hour in range (self.timing['startTime']['hours'],self.timing['endTime']['hours']+1)]
        start_minute=self.timing['startTime']['minutes']
        minutes=[]
        for hour in data_time:
            row=[]
            for minute in range ((60-start_minute)//30):
                row.append(start_minute)
                start_minute+=30
            minutes.append(row)
            start_minute=0
            if hour==self.timing['endTime']['hours'] and start_minute==self.timing['endTime']['minutes']:
                minutes[-1].append(start_minute)
                break
        for i, value in enumerate(data_time):
            for minute in minutes[i]:
                row=self.__getIndex(initial_index=6)
                time_var:str=f'{value}:{minute}'
                if time_var[-2:]==':0':time_var+='0'
                
                if self.timing['endTime']['hours']%24==value and self.timing['endTime']['minutes']<minute:
                    m=str(self.timing['endTime']['minutes'])
                    if m=='0':m+='0'
                    h=data_time[-1]
                    break 
                self.writeText(column='A', row=row, text=time_var,fontType='general')
                self.colorCell(column='A', row=row)
                Base.sheet.row_dimensions[row].height=30
        
        self.__clearNode()

    def __getIndex(self,initial_index:int=0):
        local_index:int=Node.current_index+initial_index
        Node.current_index+=1
        return local_index

    def __clearNode(self,):
        Node.current_index=0
        Node.used=0
        Node.next_index=0



