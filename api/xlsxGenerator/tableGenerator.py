from openpyxl.styles import PatternFill, Border, Side, Alignment, Font
from random import choice
from .base import Base
from .filter import Filter
from django.conf import settings
from os import path


class Node():
    current_index:int=0
    used:int=0
    next_index:int=0


class TableGenerator:
    
    def __init__(self,data:list,title:str,timing:dict={'startTime': {'hours':8, 'minutes':00},'endTime':{'hours':24,'minutes':00}},):

        self.data=Filter().filter(data)
        self.title=f'Time table {title}'
        self.timing=timing
        self.fileName=f'{self.title}.xlsx'
        self.dirName=path.join(settings.BASE_DIR, 'xlsxFiles')
        # self.fileName=path.join(self.dirName, f'{self.title}.xlsx')

        self.week_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        self.columns=['A','B','C','D','E','F','G','H']

        self.base=Base(self.fileName)
        print(self.base)
        self.sheet=self.base.getWorkSheet()

    def setData(self,):
        colorFill=[ 'FFCCCC','FFE5CC','FFFFCC','E5FFCC','CCFFCC','CCFFE5','CCFFFF','CCE5FF','CCCCFF','E5CCFF','FFCCFF','FFCCE5',
                    'FFFF99','FFCC99','FF99FF','FF99CC','FF9999','CCFF99','CC99FF','99FFFF','99FFCC','99FF99','99CCFF','9999FF'
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
            color=choice(colorFill)
            if name in subjectColor:
                color=subjectColor[name]
            else:
                subjectColor[name]=color
                colorFill.remove(color)

            for i, row in enumerate(self.sheet['A']):
                if row.value==val['start_time']:
                    row_A=i #1
                if row.value==val['end_time']:
                    row_B=i#2
            for i, column in enumerate(self.sheet[3]):
                if column.value==val['day']:
                    column_A=i
            cellDesc:str=f'{name}\n\n{start_time}-{end_time}'
            self.__colorCell(column=self.columns[column_A],row=row_A+1, color=subjectColor[name])
            self.sheet.merge_cells(f'{self.columns[column_A]}{row_A+1}:{self.columns[column_A]}{row_B}')
            self.__writeText(column=self.columns[column_A],row=row_A+1,text=cellDesc, fontType='class')

    
        self.base.saveXlsx()
        
    def __getTemplate(self):

        self.sheet.merge_cells('B1:H1')
        self.sheet.row_dimensions[1].height=25
        self.__colorCell(column='B',row=1,color='E0E0E0')
        self.__colorCell(column='A',row=1,color='E0E0E0')
        self.__writeText(column='B', row=1, text=self.title,fontType='title')
        
        for i, cell in enumerate(self.columns):
            self.sheet.merge_cells(f'{self.columns[i]}3:{self.columns[i]}4')
            self.__colorCell(column=self.columns[i],row=3)
            if cell=='A':
                self.sheet.column_dimensions['A'].width=15
                self.__writeText(column='A',row=3,text='Duration')
            else:
                self.sheet.column_dimensions[cell].width=35
                self.__writeText(column=cell, row=3, text=self.week_list[i-1],fontType='general')
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
                    break 
                self.__writeText(column='A', row=row, text=time_var,fontType='general')
                self.__colorCell(column='A', row=row)
                self.sheet.row_dimensions[row].height=30
        
        self.__clearNode()

    def __textLocation(self,column:str,row:int,wrap_text=True):
        self.sheet[f'{column}{row}'].alignment=Alignment(horizontal='center',vertical='center',wrap_text=wrap_text)

    def __fontText(self,column:str,row:int,fontType:str):
        locStyles:dict={'general':{'name':'Arial','size':16,'bold':False,'color':'00000000'},
                        'generalBold':{'name':'Arial','size':16,'bold':True,'color':'00000000'},
                        'title':{'name':'Arial','size':22,'bold':True,'color':'00000000'},
                        'event':{'name':'Arial','size':16,'bold':False,'color':'00000000'},
                        'class':{'name':'Arial','size':16,'bold':True,'color':'00000000'},
                        'personal':{},}
        self.sheet[f'{column}{row}'].font=Font(**locStyles[fontType])

    def __colorCell(self,column:str,row:int,color=None):
        if color is None:
            color='E0E0E0'
        self.sheet[f'{column}{row}'].fill=PatternFill(fill_type='solid',start_color=color,end_color=color, )
    
    def __borderStyle(self,column:str,row:int,borderType:str):
        locBorder=Side(border_style=borderType)
        self.sheet[f'{column}{row}'].border=Border(left=locBorder,right=locBorder,bottom=locBorder,top=locBorder)

    def __writeText(self,column:str,row:int,text:str,fontType:str='general',wrapText:bool=True):
        self.sheet[f'{column}{row}']=text
        self.__textLocation(column=column,row=row,wrap_text=wrapText)
        self.__fontText(column=column,row=row,fontType=fontType)
    
    def getFile(self):
        return path.join(self.dirName, self.fileName)
    
    def getDir(self):
        return self.dirName

    def __getIndex(self,initial_index:int=0):
        local_index:int=Node.current_index+initial_index
        Node.current_index+=1
        return local_index

    def __clearNode(self,):
        Node.current_index=0
        Node.used=0
        Node.next_index=0



