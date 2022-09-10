import os
from typing import Tuple
from .objectsType import PicSize
from amzqr import amzqr
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings


class QRCode:
	
	def __init__(self,linkData:str,fileName:str='qrcode',logoPath:str=os.path.join(settings.BASE_DIR,'QRCodePic','logoUCA2.jpg'),
				 basePicSize=PicSize(width=420,height=500),backgroundPicSize=PicSize(width=370,height=450),qrCodeSize=PicSize(width=320,height=320)):
		self.linkData = linkData
		self.dirName=os.path.join(settings.BASE_DIR,'QRCodePic')
		self.fileName=f'{fileName}.png'
		self.logoPath=logoPath
		self.basePicSize=basePicSize
		self.backgroundPicSize=backgroundPicSize
		self.qrCodeSize=qrCodeSize


	def settingsQRCode(self):
		
		if not os.path.exists(self.dirName):
			os.path.mkdir(self.dirName)


	def getSimpleQRCode(self):pass

		
	def setSquare(self):pass 


	def generateQRCode(self,color='#000000'):

		pathToQRCode=os.path.join(self.dirName,'qrCode.png')

		version, level, qr_name = amzqr.run(words=self.linkData,version=3,level='H',picture=self.logoPath,colorized=True,contrast=0.6,brightness=1.3,save_name=pathToQRCode)
		
		baseImage=self.__generateBase(color=color)
		localImage=Image.open(pathToQRCode)
		localImage=localImage.resize(self.qrCodeSize)

		imageLocation=(self.basePicSize.width//2-self.qrCodeSize.width//2,  (self.basePicSize.width//2-self.qrCodeSize.height//2))
		baseImage.paste(localImage,imageLocation)
		
		self.__drawText(image=baseImage,text='www.bookaroom.app',textType='link',textLocation=(200,380))
		# self.__drawText(image=baseImage,text='SCAN ME',textType='title',textLocation=(200,400))
		# self.__drawText(image=baseImage,text='TO VIEW ONLINE SCHEDULE',textType='description',textLocation=(200,440))
		baseImage.save(os.path.join(self.dirName,self.fileName))


	def __generateBase(self,color:str):
		
		baseImage=Image.new(mode='RGB', size=(self.basePicSize.width,self.basePicSize.height),color=color)
		localImage=Image.new(mode='RGB',size=(self.backgroundPicSize.width,self.backgroundPicSize.height),color='#FFFFFF')
		imageLocation=(self.basePicSize.width//2-self.backgroundPicSize.width//2,self.basePicSize.height//2-self.backgroundPicSize.height//2)
		
		baseImage.paste(localImage,imageLocation)

		return baseImage
	

	def __drawText(self,image,text:str,color:str='#000000',font=None,textType:str=None,textLocation:Tuple[int,int]=None):

		fonts:dict={'GasaltRegular':'fonts\GasaltRegular.ttf',
					'InsightSansSSi':'fonts\InsightSansSSi.ttf'}
		textTypes:dict={'general':{'size':16,'index':0},
						'link':{'size':35,'index':0},
						'title':{'size':45,'index':0},
						'description':{'size':30,'index':0}}
		textLocations:dict={'general':{'x':16,'y':0},'link':{'x':12,'y':0}, 'title':{'x':20,'y':0},'description':{'x':14,'y':0}}
		
		if textType is None:
			textType='general'
		
		if textLocation is None:
			textLocation=textLocations['general']

		if font is None or font not in fonts:
			font=ImageFont.truetype(font=fonts['GasaltRegular'],**textTypes[textType])
		
		draw=ImageDraw.Draw(image)
		textWidth=draw.textsize(text=text, font=font)[0]
		x,y=textLocation
		draw.text(xy=(self.basePicSize.width//2 - textWidth//2,y),text=text,font=font,fill=color)


	def __generateMiddleBackground(self,color:str='#FFFFFF',level:float=50):pass


	def __checkBorder(self,baseSize:PicSize,targetSize:float):pass