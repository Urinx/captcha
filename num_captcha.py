#! usr/bin/env python
# coding:utf-8
import Image,sys,ImageFilter,ImageEnhance,random,ImageDraw,ImageFont

w,h=100,40

def generate():
	color=(255,255,255)
	ft=ImageFont.truetype('res/1.ttf',30)
	num=''.join([str(random.randint(0,9)) for i in xrange(0,4)])

	im=Image.open('res/bg.png').resize((w,h)).convert('RGB')
	draw=ImageDraw.Draw(im)
	tsw,tsh=draw.textsize(num,font=ft)
	draw.text(((w-tsw)/2,(h-tsh)/2),num,font=ft,fill=color)
	del draw
	return im

def process(im):
	draw=ImageDraw.Draw(im)
	color=(255,255,255)
	for i in xrange(0,20):
		y1,x1,y2,x2=[random.randint(0,i%2*w+(i+1)%2*h) for i in xrange(0,4)]
		draw.line([(x1,y1),(x2,y2)],color)
	del draw

	im=im.transform((im.size[0]+20,im.size[1]+10),Image.AFFINE,(1,-0.3,0,-0.1,1,0))
	im.show()

if __name__=='__main__':
	basic=generate()
	process(basic)