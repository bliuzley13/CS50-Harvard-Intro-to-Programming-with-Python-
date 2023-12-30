import sys
import os
from PIL import Image, ImageOps

def main():
    arg_check()
    #below is code from the resources for this program
    # '''# with Image.open(sys.argv[1]) as img:
    # #     PIL.ImageOps.fit(image, size, method=Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
    # #     Image.paste(img, box=None, mask=None)
    # #     Image.save(fp, format=None, **params)'''
    #input file
    muppetFile = Image.open(sys.argv[1])
    #opens shirt file
    shirtImg = Image.open("shirt.png")
    #gives size of the shirt
    size = shirtImg.size
    #resizes input image to fit the shirt
    sizeUp = ImageOps.fit(muppetFile, size)
    #pastes the shirt file
    sizeUp.paste(shirtImg, shirtImg)
    #makes output image
    sizeUp.save(sys.argv[2])


def arg_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #Extension Check
    if "." not in sys.argv[1] or "." not in sys.argv[2]:
        sys.exit("Invalid input")
    #Differing Extension Check
    if ".jpg" not in sys.argv[2]:
        sys.exit("Input and output have different extensions")
    #Checks if the input file exists
    if not os.path.exists(sys.argv[1]):
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()