# This program creates a profile for all given face file.
# Alpha 1 released by axmmisaka. 2018/02/08 0:43 UTC+8
import sys
import os
import getopt
from PIL import Image
from coverFace import coverFace
def faceRemove(filename, path, maskpath, isFolder, inputName):
    if isFolder:
        #Read all files
        files = os.listdir(filename)
        #Process a little bit so that non-jpg is ignored.
        files = [x for x in files if ".jpg" in x or ".jpeg" in x or ".png" in x]
    else:
        files = [filename]

    masklist = os.listdir(maskpath)

    allFaceEncodings = []
    allNames = []
    faceCounter = 0
    for picname in files:
        #Add _masked before extension, after the original name. E.g. Taki.jpg will be Taki_masked.jpg
        savename = path + picname.rpartition('.')[0] + "_masked." + picname.rpartition('.')[2]
        picture = face_recognition.load_image_file(path+picname)
        originalpic = Image.open(path+picname)
        originalpic.load()
        faceLocations = face_recognition.face_locations(picture)
        faceEncodings = face_recognition.face_encodings(picture, faceLocations)
        
        # Detect if current face has appeared
        for faceEncoding,faceLocation in zip(faceEncodings,faceLocations):

            if not randomizeFace:
                matchedFace = face_recognition.compare_faces(allFaceEncodings, faceEncoding)
                #matchedFace is an numpy.array in a list. Why?
                #It works now. Fuck!
                if not (True in matchedFace):
                    print("I found one unknown face in file {0}.".format(picname))
                    #Not duplicated
                    faceCounter += 1

                    # Will minus 1 afterwards when using faceCounter, so no out of bound worries
                    if faceCounter > len(masklist):
                        print("Insufficent masks. Exiting...")
                        exit()

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
                        # Since there's no name inputted, the code will be used for this person's name
                        allNames.append(str(faceCounter))
                    # use allFaceEncodings here because sometimes matchedFace is not initialized.
                    faceCorrespondingMask = len(allFaceEncodings) - 1
                    print("(DEBUG)I am using {} as the rage.".format(faceCorrespondingMask))
                else:
                    # This is the same as the offical example. As it must be an old face, this is totally ok unlike in line 60
                    firstMatchIndex = matchedFace.index(True)
                    existName = allNames[firstMatchIndex]
                    print("I found an existing face in {0}. This person is probably{1}: ".format(picname, existName))
                    faceCorrespondingMask = firstMatchIndex
                    print("(DEBUG)I am using {} as the rage.".format(faceCorrespondingMask))
            else:
                faceCounter += 1
                # Will minus 1 afterwards when using faceCounter, so no out of bound worries
                if faceCounter > len(masklist):
                        print("Insufficent masks. Exiting...")
                        exit()
                faceCorrespondingMask = faceCounter - 1
                #Copied from top
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
                print("I found a face in file {0}, which is No. {1} face in this run.".format(picname, str(faceCounter)))

            #mask every face
            mask = Image.open(maskpath + "/" + masklist[faceCorrespondingMask])
            coverFace(originalpic, faceLocation, mask)
        originalpic.save(savename)

                    
                    
    print("I found {0} faces, they are: ".format(faceCounter),end="")
    for name in allNames:
        print(name+" ",end = "")
    return zip(allFaceEncodings,allNames)


# Load arguments
if __name__ == '__main__':
    try:
        options, arguments = getopt.getopt(sys.argv[1:],"hnri:f:m:",["help","inputname","random","input=","folder=","masks="])
    except getopt.GetoptError:
        print("Argument Error")
        exit()

    #Process arguments
    inputName = False
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
                print("Name inputting is enabled.")
            elif name in ("-i","--input"):
                isFolder = False
                filename = value
                path = ""
                print("Using file " + filename)
            elif name in ("-f","--folder"):
                if (isFolder!= True):
                    print("Ignoring folder...")
                else:
                    filename = value
                    path = value+"/"
                    print("Using folder " + path)
            elif name in ("-m","--masks"):
                maskpath = value
            elif name in ("-r","--random"):
                randomizeFace = True
                print("Ignoring who the person is...")

    print("Initializing railgun, please wait...")
    import face_recognition
    print("Done.")
    result = faceRemove(filename, path, maskpath, isFolder, inputName)
    print(result)