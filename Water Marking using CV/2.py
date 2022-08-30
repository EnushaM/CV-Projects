#using ImageDraw

#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open('Dataset/7.jfif')
width, height = im.size
print(im.size)
draw = ImageDraw.Draw(im)
text = "CV Crash course"

font = ImageFont.truetype('Dataset/arial.ttf', 20)


textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
im.show()

#Save watermarked image
im.save('watermarkedimage.jpg')
