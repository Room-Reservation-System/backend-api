from typing import NamedTuple, Tuple


class QRcodeType(NamedTuple):
    
    webSiteUrl:str
    description:str 
    use: str 
    
    
class PicSize(NamedTuple):
    
    height:float
    width:float


class SquareBorder(NamedTuple):

    length:float


