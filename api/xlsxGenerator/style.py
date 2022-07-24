from calendar import c
from openpyxl.styles import PatternFill, Border, Side, Alignment, Font
from .base import Base


class Style:
    
    def textLocation(self,column:str,row:int,wrap_text=True):
        Base.sheet[f'{column}{row}'].alignment=Alignment(horizontal='center',vertical='center',wrap_text=wrap_text)

    def fontText(self,column:str,row:int,fontType:str):
        locStyles:dict={'general':{'name':'Arial','size':16,'bold':False,'color':'00000000'},
                        'generalBold':{'name':'Arial','size':16,'bold':True,'color':'00000000'},
                        'title':{'name':'Arial','size':22,'bold':True,'color':'00000000'},
                        'event':{'name':'Arial','size':16,'bold':False,'color':'00000000'},
                        'class':{'name':'Arial','size':16,'bold':True,'color':'00000000'},
                        'personal':{},}
        Base.sheet[f'{column}{row}'].font=Font(**locStyles[fontType])

    def colorCell(self,column:str,row:int,color=None):
        if color is None:
            color='E0E0E0'
        Base.sheet[f'{column}{row}'].fill=PatternFill(fill_type='solid',start_color=color,end_color=color, )
    
    def borderStyle(self,column:str,row:int,borderType:str):
        locBorder=Side(border_style=borderType)
        Base.sheet[f'{column}{row}'].border=Border(left=locBorder,right=locBorder,bottom=locBorder,top=locBorder)

    def writeText(self,column:str,row:int,text:str,fontType:str='general',wrapText:bool=True):
        Base.sheet[f'{column}{row}']=text
        self.textLocation(column=column,row=row,wrap_text=wrapText)
        self.fontText(column=column,row=row,fontType=fontType)