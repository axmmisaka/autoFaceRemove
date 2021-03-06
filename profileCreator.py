# This program creates a profile for all given face file.
import sys
import os
import getopt
from PIL import Image

def profileCreate(filename, path, isFolder, inputName):
    if isFolder:
        #Read all files
        files = os.listdir(filename)
        #Process a little bit so that non-jpg is ignored.
        files = [x for x in files if ".jpg" in x or ".jpeg" in x or ".png" in x]
    else:
        files = [filename]

    allFaceEncodings = []
    allNames = []
    faceCounter = 0;
    for picname in files:
        picture = face_recognition.load_image_file(path+picname)
        faceLocations = face_recognition.face_locations(picture)
        faceEncodings = face_recognition.face_encodings(picture, faceLocations)
        
        #Duplication deletion
        for faceEncoding,faceLocation in zip(faceEncodings,faceLocations):
            matchedFace = face_recognition.compare_faces(allFaceEncodings, faceEncoding)
            #matchedFace is an numpy.array in a list. Why?
            #It works now. Fuck!
            if not (True in matchedFace):
                print("I found one unknown face in file {0}.".format(picname))
                #Not duplicated
                faceCounter += 1
                
                allFaceEncodings.append(faceEncoding)
                if inputName:
                    top, right, bottom, left = faceLocation
                    
                    #Like in example, don't know why there's no error
                    croppedImage = picture[top:bottom,left:right]
                    
                    pilImage = Image.fromarray(croppedImage)
                    pilImage.show()
                    
                    print("Input the name of shown face.")
                    name = input()
                    allNames.append(name)
                else:
                    allNames.append(str(faceCounter))
            else:
                firstMatchIndex = matchedFace.index(True)
                existName = allNames[firstMatchIndex]
                print("I found an existing face and I am ignoring it. This person is probably: "+existName)

    print("I found {0} faces, they are: ".format(faceCounter),end="")
    for name in allNames:
        print(name+" ",end = "")
    return zip(allFaceEncodings,allNames)





# Load arguments
if __name__ == '__main__':
    try:
        options, arguments = getopt.getopt(sys.argv[1:],"hni:f:",["help","inputname","input=","folder="])
    except getopt.GetoptError:
        print("Argument Error")

    #Process arguments
    inputName = False;
    isFolder = True
    if len(options) == 0:
        print("Use --help for help.")
        exit()
    else:
        for name, value in options:
            if name in ("-h","--help"):
                print("Help is not yet implemented")
                exit()
            elif name in ("--inputname","-n"):
                #If this is true, program will ask user to input name for every face found.
                #Otherwise program will automaticlly assign numbers to these faces. 
                inputName = True
            elif name in ("-i","--input"):
                isFolder = False
                filename = value
                path = ""
            elif name in ("-f","--folder"):
                if (isFolder!= True):
                    print("Ignoring folder...")
                else:
                    filename = value
                    path = value+"/"
    print("Initializing railgun, please wait...")
    import face_recognition
    print("Done.")
    result = profileCreate(filename, path, isFolder, inputName)
    print(result)



        

