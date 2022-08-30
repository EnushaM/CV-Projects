#Generating Barcode and Saving it as a image file

from barcode import EAN13

from barcode.writer import ImageWriter

# Make sure to pass the number as string
number = '789654123654'
my_code = EAN13(number, writer=ImageWriter())
#save it as an image file
my_code.save("Sample_barcode")
