import os

def divide_line(words,size=60):
    print('*'*size)
    print(' '*((size-len(words))//2)+words+' '*((size-len(words))//2))
    print('*'*size)

def getallfile(path):
    # get all file name in the dictionary
    allpath=[]
    allname=[]
    allfilelist=os.listdir(path)
    for file in allfilelist:
        filepath=os.path.join(path,file)
        if os.path.isdir(filepath):
            allpath=getallfile(filepath)[0]+allpath
            allname=getallfile(filepath)[1]+allname
        elif os.path.isfile(filepath):
            allpath.append(filepath)
            allname.append(file)
    return allpath, allname

def init_dictionary(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:pass

def divide_list(listTemp, n):
    twoList = [ [] for i in range(n)]
    for i,e in enumerate(listTemp):
        twoList[i%n].append(e)
    return twoList

def cycle(l,length):
    return l*(length//len(l)) if length%len(l)==0 else l*(length//len(l))+l[:length%len(l)]