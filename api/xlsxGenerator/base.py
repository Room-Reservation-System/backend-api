from openpyxl import Workbook


class Base:
    wb=Workbook()
    sheet=wb.active