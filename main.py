import os

fileName= ""
filePath = ""
totalSplitted = 0

path = raw_input("Insert the path of the file: ")
path = os.path.normpath(path)
size = os.path.getsize(path)
githubLimit = 1000000 * 100

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

for i in range(len(path), 0):
    if path[i] is '\\':
        filePath = path[0:i]
        fileName = path[i+1:len(path)]
        break

print "Your file size: " + str(size / 1000000) + "MB"

if size < githubLimit:
    print "No need to be splitted"
else:
    totalSplitted = int(size / githubLimit)
    print "File will be splitted to " + str(totalSplitted) + " file(s)."
    
    total_line = file_len(path)
    
    interval = int(total_line / totalSplitted)
    
    file = open(path, "r+")
    files = []
    
    nameTail = path[-4:len(path)]
    nameHead = path[0: -4]
    
    for i in range(totalSplitted):
        newFile = str(filePath) + str(nameHead) + "_" + str(i+1) + str(nameTail)
        fileN = open(newFile, "w+")
        files.append(fileN)
        
    lines = file.readlines()
    i = 0 ## Untuk File
    
    print "Let's start splitting the file"
    
    for j in range(0, total_line):
        if (j+1)%interval == 0 and i != totalSplitted - 1:
            print "..."
            i = i + 1
        files[i].write(lines[j])
        
    print "Job is done"
