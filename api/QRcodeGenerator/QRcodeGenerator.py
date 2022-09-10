import os
from typing import Tuple
from .objectsType import QRcodeType, PicSize
from amzqr import amzqr
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings


class QRCode:
	
	def __init__(self,
				 linkData:str,
				 fileName:str='qrcode',
				 logoPath:str=os.path.join(settings.BASE_DIR,'QRCodePic','logoUCA2.jpg'),
				 basePicSize=PicSize(width=420,height=500),
				 backgroundPicSize=PicSize(width=370,height=450),
				 qrCodeSize=PicSize(width=320,height=320),
				 ):
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
		









































# class QRcode:
# 	def __init__(self,dirPath=None):
# 		if dirPath is None:
# 			self.dirPath=path.join(settings.BASE_DIR,'QRCodePic') 
# 		else:
# 			self.dirPath=dirPath
			
# 	def dirConfig(self):
# 		if not path.exists(self.dirPath):
# 			mkdir(self.dirPath)
# 	def simpleDimple(self,fileName:str,url:str):
# 		qr = qrcode.QRCode(
# 			version=1,
# 			error_correction=qrcode.constants.ERROR_CORRECT_L,
# 			box_size=10,
# 			border=4,
# 		)
# 		qr.add_data(url)
# 		qr.make(fit=True)
# 		img = qr.make_image()
# 		img.save(path.join(self.dirPath,f'{fileName}.png'))
# 		return path.join(self.dirPath, f'{fileName}.png')

# 	def getQRcode(self,fileName:str,url:str,aboutQR:QRcodeType\
# 		=QRcodeType(description='Hello I am QRcode',webSiteUrl='http://mysite.com',use='Scan me!'), image=True, size=(1120,1240)):
# 		qrCode=self.generateQRcode(url=url, image=image, size=size)
# 		self.dirConfig()
# 		try:
# 			qrCode.save(path.join(self.dirPath,f'{fileName}.png'))

# 		except FileExistsError:
# 			remove(path.join(self.dirPath,f'{fileName}.png'))
# 			qrCode.save(path.join(self.dirPath,f'{fileName}.png'))
		
# 		return path.join(self.dirPath, f'{fileName}.png')
    
# 	@staticmethod
# 	def generateQRcode(url:str,image=False, size =(2280,2480)):
# 		# if not url.endswith('qrcode=true'):
# 		# 	url=f'{url}&qrcode=true'
# 		# return qrcode.make(url)
# 		qrCode=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,version=1,box_size=42, border=4)
# 		qrCode.add_data(url)
# 		qrCode=qrCode.make_image(image_factory=StyledPilImage, color_masks=RadialGradiantColorMask,)
# 		return qrCode
# 		# if image:
# 		# 	qrCodeBase=Base.createBase(size=size)
# 		# 	posQRcode=(qrCodeBase.size[0]//2-qrCode.size[0]//2,qrCodeBase.size[1]//2-qrCode.size[1]//2-130)
# 		# 	qrCodeBase.paste(qrCode,posQRcode)
# 		# 	return qrCodeBase
# 		# else: 
# 		# 	return qrCode


# 	@staticmethod
# 	def drawText(object,description,url,use,imageSize=None,font=None,text_color="#000000"):
# 		draw = ImageDraw.Draw(object)
# 		x1,y1=370,417
# 		x2,y2=410,590
# 		draw.rectangle((397, 340, 620, 380), fill=(0,0,0))
# 		draw.rectangle((370, 345, 410, 590), fill=(0,0,0))

# 		draw.rectangle((1680, 1910, 1970, 1970), fill=(0,0,0))
# 		draw.rectangle((2380, 110, 2320, 600), fill=(0,0,0))

# 		draw.rectangle((110, 2370, 170, 1870), fill=(0,0,0))
# 		draw.rectangle((110, 2370, 600, 2300), fill=(0,0,0))

# 		draw.rectangle((1880, 2370, 2370, 2310), fill=(0,0,0))
# 		draw.rectangle((2310, 1870, 2370,2360), fill=(0,0,0))
# 		if imageSize is None:
# 			imgHeight,imgWidth=object.size
# 		else:
# 			imgHeight,imgWidth=imageSize
# 		if font is None:
# 			font=ImageFont.truetype("fonts\InsightSansSSi.ttf", 150)
# 		draw.text(xy=((imgWidth//2-draw.textlength(text=use, font=font)//2-115),1935), text=use,font=ImageFont.truetype("fonts\InsightSansSSi.ttf", 150),fill='#000000')
# 		draw.text(xy=(1440,2321), text=url,font=ImageFont.truetype("fonts\InsightSansSSi.ttf", 75),fill='#000000')
# 		draw.text(xy=(190,2321), text=description,font=ImageFont.truetype("fonts\InsightSansSSi.ttf", 75),fill='#000000')
		
	
# 	@staticmethod
# 	def createBase(size=None, color=None,):
		
# 		if size is None:
# 			size=(2480,3508)
# 		if color is None:
# 			color=(255,255,255)
# 		image=Image.new(mode='RGB',size=size,color=color)
		
# 		return image