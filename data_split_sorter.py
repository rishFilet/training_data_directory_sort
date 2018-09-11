
# coding: utf-8

# # Data split pre processor for classification v1.0

# - This program works with the bash script labeller.sh
# - labeller.sh can be edited for more than two classes
# - After running the current labeller.sh, it will create two classes for 1 and 0
# - The directory where the classes for the data are stored should be the rootpath in the cell below
# 
# **NOTE**: The split is 80/20 for Train/Test and then out of that 80% Train is 80/20 for Train/Valid

# In[135]:


import os
import random
import shutil

rootPath="/Users/rkhan/Downloads/ships-in-satellite-imagery/shipsnet"


# ### Folder, classes setup
# The classes should be all the classes created by labeller.sh which are folders containing the data as now labelled. The folders are standard and don't need to be altered for most problems. Train, valid, test are standard.

# In[136]:


classes = {"ships","no_ships"}
folders = {"train","valid","test"}


# In[ ]:


#The following method creates a directory for each folder if it doesnt exist


# In[137]:


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)  


# In[138]:


#The following method randomises the files in the directory of each each class
def randomise(c):
    files=os.listdir(os.path.join(rootPath,c))
    random.shuffle(files)
    print (int(len(files)*0.8))
    return files


# In[139]:


#Each folder will be iterated, note that using this loop will go through the folders array alphabetically instead
#of index numerically. So test, train, valid is the order.
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


#Outputs the number of files in each folder that has been split
for f in folders:
    for c in classes:
        print (f, "/", c, ": ",len(os.listdir(os.path.join(os.path.join(rootPath,f),c))))


# In[141]:


#Removes the empty class folders
for c in classes:
    os.rmdir(os.path.join(rootPath,c))

