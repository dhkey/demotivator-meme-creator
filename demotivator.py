from PIL import Image, ImageDraw, ImageFont
import os

def make_meme(text, input, output="result.png", font_size=60):
	image = input.resize((900,750))
	image.save(f'images/temp.png')
	bg = Image.open(f'images/bg.png')
	width, height = bg.size
	draw = ImageDraw.Draw(bg)
	font = ImageFont.truetype('fonts/times.ttf', font_size)
	_, _, text_width, text_height = draw.textbbox((0, 0), text=text, font=font)
	x = (width - text_width) / 2
	y = (height - text_height)-100
	text_color = (255,255,255)

	if text_width >= width:		
		...

	draw.text((x, y), text, font=font, fill=text_color)	
	second = Image.open(f'images/temp.png')
	bg.paste(second, (96, 35))
	bg.save(output)
	bg.close()
	second.close()
	image.close()
	os.remove("images/temp.png")
		


make_meme("when roach dont want to jump", Image.open(f'images/image.png'), "result.png", 70)