#importing qr library 
import qrcode
#taking site location 
target_qr = input("entger your site url: ").strip()
#taking file name to store qr
file_name = input("enter the file name for qr image").strip()
#make function from library
img = qrcode.make(target_qr)
#saving img qr
img.save(file_name+".png")