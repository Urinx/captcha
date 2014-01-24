#! usr/bin/env python
# coding:utf-8
import Image,sys,ImageFilter,ImageEnhance,random,ImageDraw,ImageFont

w,h=100,40

def getcn():
	#return unichr(random.randint(0x4E00,0x9FBF))
	head=random.randint(0xB0, 0xCF)
	body=random.randint(0xA, 0xF)
	tail=random.randint(0, 0xF)
	val=( head << 8 ) | (body << 4) | tail
	str="%x" % val
	return str.decode('hex').decode('gb2312')

def generate():
	color=(255,255,255)
	ft=ImageFont.truetype('res/YuppySC-Regular.otf',25)
	cn=''
	for x in xrange(0,4):
		cn+=getcn()

	im=Image.open('res/bg.png').resize((w,h)).convert('RGB')
	draw=ImageDraw.Draw(im)
	tsw,tsh=draw.textsize(cn,font=ft)
	draw.text(((w-tsw)/2,(h-tsh)/2),cn,font=ft,fill=color)
	del draw
	return im

def process(im):
	draw=ImageDraw.Draw(im)
	color=(255,255,255)
	for i in xrange(0,10):
		y1,x1,y2,x2=[random.randint(0,i%2*w+(i+1)%2*h) for i in xrange(0,4)]
		draw.line([(x1,y1),(x2,y2)],color)
	del draw

	#im=im.transform((im.size[0]+20,im.size[1]+10),Image.AFFINE,(1,-0.3,0,-0.1,1,0))
	im.show()

if __name__=='__main__':
	basic=generate()
	process(basic)