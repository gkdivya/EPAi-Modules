import os
from PIL import Image

def convert_png2jpg(image):
    '''
    Converts PNG image to JPEG

            Parameters:
                    image: PNG image

            Returns:
                    image: in JPG format
    '''
    if not os.path.isfile(image):
        raise ValueError('Image not exists')  
    filename, extension = os.path.splitext(image)
    im = Image.open(image)
    im.save(filename + '.jpg')
