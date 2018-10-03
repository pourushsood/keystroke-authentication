# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:52:24 2018

@author: Manan Khaneja
"""
import fileinput
import os

"""
Expected input data format : Takes in the path of the master directory.  
|-- Master directory (you can put any name for this) (Put the data of all the weeks in one place)
    |-- week 1
        |-- (your roll number)
            |-- the same directory structure as for data submission. 
    |-- week 2
    |-- week 3
    and so on.

Output data format : 
|-- Master directory
    |-- (your roll no.)
        |-- happy.txt
        |-- sad.txt
        |-- neutral.txt
    |-- week 1 
    |-- week 2
    |-- week 3
    and so on.

"""
# A function that concatinates all the files in a given directory with path dir_path
# outpath is path where output file should be stored. outfile_name is the name of file.  
def concatination(dir_path, outpath, outfile_name):
    outfile_path = outpath + "\\" + outfile_name
    filenames = os.listdir(dir_path)
    complete_names=[]
    for index in range(0,len(filenames),1):
        complete_names.append(os.path.join(dir_path,filenames[index]))            
    # appending the data of all the files in "dir_path" to the given outfile. 
    with open(outfile_path, 'a+') as fout , fileinput.input(complete_names) as fin:
        for line in fin:
            fout.write(line)

def main():
    roll = input("Enter your roll number \n")
    user_input =input("Enter the complete path of your master directory:  \n")
    assert os.path.isdir(user_input), "I did not find the directory"
    print("\n")
    all_files=os.listdir(user_input)
    cmd = "mkdir " + user_input + "\\" + roll
    os.system(cmd)
    outpath = user_input + "\\" + roll 
    
    for index in range(len(all_files)):
    #loop on all the weeks
        if "week" or "Week" in all_files[index]:
            address = user_input + "\\" + all_files[index] + "\\" + roll + "\\" + "New Data Collection" 
            directory = os.listdir(address)
            address = address + "\\" + directory[0] + "\\" + "Keyboard Database" + "\\" + "sentence" 
            # getting the addresses of happy, sad and neutral directories.
            address_happy = address + "\\" + "Emotional" + "\\" + "Happy"
            address_sad = address + "\\" + "Emotional" + "\\" + "Sad"
            address_neutral = address + "\\" + "Neutral"
            # appending happy.txt, sad.txt, neutral.txt with the data in "dir_path" address_happy, address_sad, address_neutral respectively. 
            concatination(address_happy, outpath, "happy.txt")
            concatination(address_sad, outpath, "sad.txt")
            concatination(address_neutral, outpath, "neutral.txt")
            
if __name__=='__main__':
    main()
