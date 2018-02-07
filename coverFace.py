from PIL import Image


#original and cover are PIL images
# The position is a tuple, with a sequense of (top,right,bottom,left)
def coverFace(original, position, cover):
    top, right, bottom, left = position
    
    height = bottom - top
    length = right - left

    cover = cover.resize( (length, height) )
    original.paste(cover,(left,top,right,bottom))


if __name__ == '__main__':
    import getopt
    import sys
    try:
        options, arguments = getopt.getopt(sys.argv[1:],"o:c:",["original=","cover="])
    except getopt.GetoptError:
        print("Argument Error")

    if len(options) != 2:
        print("Argument not correct, go play your balls")
        exit()

    else:
        for name,value in options:
            if name in ("-o","--original"):
                originalFile = Image.open(value)
                originalFile.load()
                print("original file loaded")
            elif name in ("c","--cover"):
                coverFile = Image.open(value)
                coverFile.load()
                print("cover file loaded")
    print("Input top right bottom left accordingly one by one followed by enter.")
    top = int(input())
    right = int(input())
    bottom = int(input())
    left = int(input())
    coverFace(originalFile,(top,right,bottom,left),coverFile)
    originalFile.show()

