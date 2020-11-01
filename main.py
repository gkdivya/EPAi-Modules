import sys
import argparse
from image_modules.jpeg2png import convert_jpeg2png
from image_modules.png2jpg import convert_png2jpg

if __name__ == "__main__":
    print("Running from command line")

    # get command, image from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-command',
                        type=str,
                        help='Command "j2p", "p2j"')
    parser.add_argument('-image',
                        type=str,
                        help='Input image path')

    args = parser.parse_args()
    print(args.command)
    print(args.image)

    if(args.command == None):
        print(f'Program expects command line arguments, Allowed image operations are "j2p", "p2j", "res", "crp"')
    elif(args.command == 'j2p'):

        print('JPEG to PNG Converter')
        print(f'j2p: {args.image}')
        convert_jpeg2png(args.image)

    elif(args.command == 'p2j'):
        print('PNG to JPEG Converter')
        convert_png2jpg(image=args.image)

    elif(args.command == 'res_p'):
        pass

    elif(args.command == 'res_w'):
        pass

    elif(args.command == 'res_h'):
        pass

    elif(args.command == 'crp_px'):
        pass

    elif(args.command == 'crp_p'):
        pass
