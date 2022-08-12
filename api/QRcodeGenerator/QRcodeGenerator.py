import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
# from django.conf import settings
from os import link, path, mkdir
# from PIL import ImageFont, ImageDraw, Image

class QRcodeGenerator:
	# __logoPath= 'D:\Programming\Python\QRcodeGenerator\logo.jpg'
    # def getDirName(self):
    #     # return path.join(settings.BASE_DIR, 'QRCode')
	# 	ret
    
    def getQRcode(self, fileName:str,siteLink:str, aboutQR:dict={'description':'Hello I am QRcode','url':'http://mysite.com','use':'Scan me!'}, image=True, size=(2280,2480)):
        qrCode=self.generateQRcode(siteLink=siteLink, image=image, size=size)
        qrCode.save(f'{fileName}.jpg')
		# try:
        #     # mkdir(self.getDirName)
        #     qrCode.save(f'{fileName}.jpg')
        # except FileExistsError: 
        #     qrCode.save(f'{fileName}.jpg')
		
        # return path.join(self.getDirName, f'{fileName}.jpg')
        # qrCodeParams=qrCode.size
        # self.drawText(object=qrCode, **aboutQR, imageSize=qrCodeParams)

    @staticmethod
    def generateQRcode(siteLink:str,image=False, size =(2280,2480)):
        qrCode=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,version=1,box_size=42, border=4)
        qrCode.add_data(siteLink)
        qrCode=qrCode.make_image(image_factory=StyledPilImage, color_masks=RadialGradiantColorMask,)
        return qrCode
data={1:'https://room-schedule.vercel.app/schedule/1',
	  2:'https://room-schedule.vercel.app/schedule/2',
	  3:'https://room-schedule.vercel.app/schedule/4',
	  4:'https://room-schedule.vercel.app/schedule/6',
	  5:'https://room-schedule.vercel.app/schedule/7',
	  6:'https://room-schedule.vercel.app/schedule/8',
	  }
for k,v in data.items():
	QRcodeGenerator().getQRcode(fileName=f'{k}',siteLink=v)

	# 	if image:
	# 		qrCodeBase=Base.createBase(size=size)
	# 		posQRcode=(qrCodeBase.size[0]//2-qrCode.size[0]//2,qrCodeBase.size[1]//2-qrCode.size[1]//2-130)
	# 		qrCodeBase.paste(qrCode,posQRcode)
	# 		return qrCodeBase
	# 	else: 
	# 		return qrCode
	# # @staticmethod
	# def drawFrame(object):
	# 	draw=ImageDraw.Draw(object)
	# 	def rotate(degree:int):
			
	# 		# draw.rectangle((200, 100, 300, 200), fill=(0,0,0), outline=(255, 255, 255))
	# 		pass 


	# @staticmethod
	# def drawText(object,description,url,use,imageSize=None,font=None,text_color="#000000"):
	# 	draw = ImageDraw.Draw(object)
	# 	# x1,y1=370,417
	# 	# x2,y2=410,590
	# 	# draw.rectangle((397, 340, 620, 380), fill=(0,0,0))
	# 	# draw.rectangle((370, 345, 410, 590), fill=(0,0,0))

	# 	# draw.rectangle((1680, 1910, 1970, 1970), fill=(0,0,0))
	# 	# draw.rectangle((2380, 110, 2320, 600), fill=(0,0,0))

	# 	# draw.rectangle((110, 2370, 170, 1870), fill=(0,0,0))
	# 	# draw.rectangle((110, 2370, 600, 2300), fill=(0,0,0))

	# 	# draw.rectangle((1880, 2370, 2370, 2310), fill=(0,0,0))
	# 	# draw.rectangle((2310, 1870, 2370,2360), fill=(0,0,0))
	# 	if imageSize is None:
	# 		imgHeight,imgWidth=object.size
	# 	else:
	# 		imgHeight,imgWidth=imageSize
	# 	if font is None:
	# 		font=ImageFont.truetype("fonts\InsightSansSSi.ttf", 150)
	# 	draw.text(xy=((imgWidth//2-draw.textlength(text=use, font=font)//2-115),1935), text=use,font=ImageFont.truetype("fonts\InsightSansSSi.ttf", 150),fill='#000000')
		# draw.text(xy=(1440,2321), text=url,font=ImageFont.truetype("fonts\InsightSansSSi.ttf", 75),fill='#000000')
		# draw.text(xy=(190,2321), text=description,font=ImageFont.truetype("fonts\InsightSansSSi.ttf", 75),fill='#000000')
		
	
	# @staticmethod
	# def createBase(size=None, color=None,):
		
	# 	if size is None:
	# 		size=(2480,3508)
	# 	if color is None:
	# 		color=(255,255,255)
	# 	image=Image.new(mode='RGB',size=size,color=color)
		
	# 	return image
