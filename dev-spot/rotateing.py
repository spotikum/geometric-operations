# import the Python Image
# processing Library
from PIL import Image

# Giving The Original image Directory
# Specified
Original_Image = Image.open("image.jpeg")

# Rotate Image By 180 Degree
rotated_image1 = Original_Image.rotate(180)

# This is Alternative Syntax To Rotate
# The Image
rotated_image2 = Original_Image.transpose(Image.ROTATE_90)

# This Will Rotate Image By 60 Degree
rotated_image3 = Original_Image.rotate(60)

rotated_image1.save("output/rotate_180.png")
rotated_image2.save("output/rotate_90.png")
rotated_image3.save("output/rotate_60.png")

# rotated_image1.show()
# rotated_image2.show()
# rotated_image3.show()
