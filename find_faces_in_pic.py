from PIL import Image,ImageDraw
import sys
import getopt

print("Boiling vodka, please wait...")
#This would take a little bit long...
import face_recognition
print("Done")

def drawRectangle(pic, top, right, bottom, left):
#Draws a unfilled rectangle
    draw = ImageDraw.Draw(pic)
    draw.line( ((left, top), (right, top)), fill = "#66CCFF", width = 5)
    draw.line( ((left,top), (left, bottom)), fill = "#66CCFF", width = 5)
    draw.line( ((left,bottom), (right, bottom)), fill = "#66CCFF", width = 5)
    draw.line( ((right, top), (right,bottom)), fill = "#66CCFF", width = 5)
    del draw

# Load system arguments. 
try:
    options, arguments = getopt.getopt(sys.argv[1:],"hli:",["help","license","input="])
except getopt.GetoptError:
    print("Argument Error. Exiting...");

if(len(options) !=0):
    for name, value in options:
        if name in ("-h","--help"):
            print("Help is not supported")
        elif name in ("-l","--license"):
            print("no license now")
        elif name in ("-i","--input"):
            filename = value
else:
    filename = input()


# Load the jpg file into a numpy array

image = face_recognition.load_image_file(filename)

# Load the Original File to Process
originalFile = Image.open(filename)
originalFile.load()


# Find all the faces in the image using the default HOG-based model.

# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.

# See also: find_faces_in_picture_cnn.py

face_locations = face_recognition.face_locations(image)



print("I found {} face(s) in this photograph.".format(len(face_locations)))



for face_location in face_locations:



    # Print the location of each face in this image

    top, right, bottom, left = face_location

    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    drawRectangle(originalFile, top, right, bottom, left)

originalFile.show()
