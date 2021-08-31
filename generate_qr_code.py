import pyqrcode
import png
from pyqrcode import QRCode
  
# String which represent the QR code 
s = "https://www.youtube.com/watch?v=mRCXh__pexQ&list=PLmdFyQYShrjd4Qn42rcBeFvF6Qs-b6e-L"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8) 