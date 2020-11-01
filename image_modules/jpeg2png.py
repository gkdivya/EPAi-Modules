import os
from PIL import Image


def convert_jpeg2png(image):
    '''
    Converts JPEG image to PNG

            Parameters:
                    image: JPEG image

            Returns:
                    image: in PNG format
    '''
    print("Inside JPEG 2 PNG file")
    if not os.path.isfile(image):
        raise ValueError('Image not exists')  
    filename, extension = os.path.splitext(image)
    im = Image.open(image)
    im.save(filename + '.png')