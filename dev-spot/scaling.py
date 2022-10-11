# importing library
from pgmagick.api import Image

img = Image('image.jpeg')

# scaling image
img.scale((150, 100), 'lanczos')
img.write('output/scale_gog.png')
