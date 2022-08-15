from typing import List, NamedTuple

class ScheduleTime(NamedTuple):
    startHour:int
    startMinute:int
    endHour:int
    endMinute:int

class Group(NamedTuple):
    groupOne:str
    groupTwo:str
