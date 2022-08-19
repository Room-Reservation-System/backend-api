from typing import List, NamedTuple, TypedDict


class ScheduleTime(NamedTuple):

    startHour:int
    startMinute:int
    endHour:int
    endMinute:int


class Group(NamedTuple):

    groupOne:str
    groupTwo:str


class TypeXlsx(TypedDict):

    dataList:list
    header:list