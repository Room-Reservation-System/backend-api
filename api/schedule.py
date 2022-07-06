from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from time import strftime, gmtime


class Schedule():

    def __init__(self, title:str, classes:dict):
        self.title=title 
        self.classes=classes
        self.max_days=len(classes.keys())
        self._week_list=['Monday',
                         'Tuesday', 
                         'Wednesday', 
                         'Thursday', 
                         'Friday', 
                         'Saturday', 
                         'Sunday']
        self._xlxs_columns=[['A'],  
                            ['B','C'],
                            ['D','E'],
                            ['F','G'],
                            ['H','I'],
                            ['J','K'],
                            ['L','M'],
                            ['N','O'],
                            ]

    def create_schedule(self):

        wb=Workbook()
        sheet=wb.active
        for column in self._xlxs_columns:
            sheet.column_dimensions[column[0]].width=25
            sheet.column_dimensions[column[-1]].width=25

        sheet.merge_cells('A1:L1')
        sheet['A1']=self.title
        sheet['A1'].alignment=Alignment(horizontal='center')
        sheet['A1'].font=Font(b=True,size=18)

        
        sheet.merge_cells('A3:A4')
        sheet['A3']='Duration'
        sheet['A3'].alignment=Alignment(horizontal='center',
                                        vertical='center')
        sheet['A3'].font=Font(b=True,size=14)
        sheet['A3'].fill=PatternFill(start_color="E0E0E0",
                                     end_color="E0E0E0",
                                     fill_type="solid")

        for i in range(1,len(self.classes.keys())+1):
            sheet.merge_cells(f'{self._xlxs_columns[i][0]}3:{self._xlxs_columns[i][1]}3')
            sheet[f'{self._xlxs_columns[i][0]}3']=self._week_list[i-1]
            sheet[f'{self._xlxs_columns[i][0]}3'].alignment=Alignment(horizontal='center',
                                                                      vertical='center')
            sheet[f'{self._xlxs_columns[i][0]}3'].font=Font(b=True,size=16)
            sheet[f'{self._xlxs_columns[i][0]}3'].fill=PatternFill(start_color="E0E0E0",
                                                                     end_color="E0E0E0",
                                                                     fill_type="solid")


        wb.save(filename="test1.xlsx")
# print(strftime('%A', gmtime()))
title='Timetable of Spring period (January - May) of 2021-2022 Academic Years for Undergraduate Year 1 Program.'
classes={'Monday':{},
         'Tuesday':{}, 
         'Wednesday':{}, 
         'Thursday':{}, 
         'Friday':{}, 
        #  'Saturday':{}, 
        #  'Sunday':{}
         }

demo=Schedule(title=title,classes=classes)
demo.create_schedule()
