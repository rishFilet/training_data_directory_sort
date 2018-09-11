# training_data_directory_sort
*Labeller.sh*
This is a simple script which will take all the files in the current directory and place them into specific folders making it easier for classification problems in machine learning. The motive behind this was for fast.ai first lesson and sorting the 4000 images from the kaggle shipsnet dataset

# NOTE TO SELF
Always use bash instead of sh to start the script as sh has less syntax options. This script works with th bash command

*data_split_sorter.py*
This will take the classes that were made in labeller.sh and create train, test, valid directories, randomise the files an split them into 80/20 and then of that 80 for train split into 80/20 for valid(20). Open with Jupyter Notebook to see what needs to be edited. rootPath and classes are the only two variables that need to be edited for your project.
