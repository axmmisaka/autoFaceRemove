# autoFaceRemove
Removes faces in a picture using rage comic or something else interesting.   

Built using ageitgey/face\_recognition. A huge thank to this developer!   

This project is inspired by a Zhihu post: https://zhuanlan.zhihu.com/p/32299758, which also uses face\_recognition and PIL.   

## Feature
Recognize all guys in a folder, and then replace their faces with rage comic or something else. For example:   
![Ancelotti with Bundesliga Salad plate](https://github.com/axmmisaka/autoFaceRemove/raw/master/Bayerns/Ancelotti.jpg)
Will be turned into:   
![Ancelotti raged!](https://github.com/axmmisaka/autoFaceRemove/raw/master/Bayerns/Ancelotti_masked.jpg)

Also, right now, in one process, same person will be replaced with the same picture. Disable of this feature and load profile will be added in the future.   

For example, in the same run, famous Ancelotti+Zidane picture turns from this:   
![AnZidaze](https://github.com/axmmisaka/autoFaceRemove/raw/master/Bayerns/AnZidaze.jpg)
will become this:   
![AnZidazeRaged](https://github.com/axmmisaka/autoFaceRemove/raw/master/Bayerns/AnZidaze_masked.jpg)

## Requirements
A computer with linux OS. I am using Ubuntu 17.04 zesty - although its Chinese input is sh\*t.   
Python3 and pip3 - python and pip should be fine, but I didn't test them.   
face\_recognition package. You can find it (here)[https://github.com/ageitgey/face_recognition] and know how to install it.    

## Usage
Use
```bash
python3 find_faces_in_pic.py --input=inputfile.jpg
```
to mark every face that this program can find.   

Use
```bash
python3 faceRemover.py --folder=folderforinput --masks=foldersformasks --inputname(useless, but will give you all face found)
```
to play some awesome stuff.   
Place your jpg or png file correctly in the folder that you indicated.   
For example, the examples I created is by executing:  
```bash
python3 faceRemover.py --folder=Bayerns --masks=rageComics --inputname 
```
## License
Except for all the pictures - they are copyrighted, and you don't have to use them if you don't want to do so, all files are released under GNU GPLv3 - sorry, GNU/user!   
face\_recognition is released under MIT license.
