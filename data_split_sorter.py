
# coding: utf-8

# In[135]:


import os
import random
import shutil

rootPath="/Users/rkhan/Downloads/ships-in-satellite-imagery/shipsnet"
rootPath


# In[136]:


classes = {"ships","no_ships"}
folders = {"train","valid","test"}


# In[137]:


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)  


# In[138]:


def randomise(c):
    files=os.listdir(os.path.join(rootPath,c))
    random.shuffle(files)
    print (int(len(files)*0.8))
    return files


# In[139]:


for f in folders:
    os.chdir(rootPath)
    createFolder('./'+f+'/')
    os.chdir(os.path.join(rootPath,f))
    print (f)
    for c in classes:
        createFolder('./'+c+'/')
        if (f=="train"):
            shuffledFiles = randomise(c)
            for x in shuffledFiles:
                shutil.move(os.path.join(os.path.join(rootPath,c),x),os.path.join(os.getcwd(),c))
        elif (f=="valid"):
            files=os.listdir(os.path.join(os.path.join(rootPath,"train"),c))
            for x in files[:int((len(files))*0.2)]:
                shutil.move(os.path.join(os.path.join(os.path.join(rootPath,"train"),c),x),os.path.join(os.getcwd(),c))
        elif (f=="test"):
            shuffledFiles = randomise(c)
            for x in shuffledFiles[:int((len(shuffledFiles))*0.2)]:
                shutil.move(os.path.join(os.path.join(rootPath,c),x),os.path.join(os.getcwd(),c))  


# In[140]:


for f in folders:
    for c in classes:
        print (f, "/", c, ": ",len(os.listdir(os.path.join(os.path.join(rootPath,f),c))))


# In[141]:


for c in classes:
    os.rmdir(os.path.join(rootPath,c))

