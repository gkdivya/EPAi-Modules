from PIL import Image  
import pathlib

maxsize = (512, 512)
for input_img_path in pathlib.Path("input").iterdir():
    output_img_path = str(input_img_path).replace("input","output")
    with Image.open(input_img_path) as im:
        im.thumbnail(maxsize)
        im.save(output_img_path, "JPEG", dpi=(300,300))
  
# Opens a image in RGB mode  
im = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg")  
  
# Size of the image in pixels (size of orginal image)  
# (This is not mandatory)  
width, height = im.size  
  
# Setting the points for cropped image  
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5
  
# Cropped image of above dimension  
# (It will not change orginal image)  
im1 = im.crop((left, top, right, bottom)) 
newsize = (300, 300) 
im1 = im1.resize(newsize) 
# Shows the image in image viewer  
im1.show()  

if __name__ == '__main__':
    print('running this command line code')

    # get code, input_file_path, output_file_path from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i', '--input', '--input_file', type=str, help='Enter absolute input file path')
    parser.add_argument('-o', '--output', '--output_file', type=str, help='Enter absolute output file path')
    parser.add_argument('-w', '--width', '--resize_width', type=int, help='Enter resize width')

    args = parser.parse_args()
    print('Input_File_Path = ',args.input)
    print('Output_File_Path = ',args.output)
    print('Resize_Width = ',args.width)
    print('\n')

    print(f'res_w: {args.input} {args.output} {args.width} ')