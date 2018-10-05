# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:26:00 2018

@author: Manan Khaneja
"""

import fileinput
import os

"""
Expected input data format : Takes in the path of the master directory.  
|-- Master directory (you can put any name for this) (Put the data of all the weeks in one place under the roll number. And have directories of all the roll numbers)
    |--rollnumber.txt ( a txt file with one roll number in each line)
    |--(roll number 1)
        |-- week 1
            |-- (roll number 1)
                |-- the same directory structure as for data submission. 
        |-- week 2
        |-- week 3
    |--(roll number 2)
    |--(roll number 3)
    and so on.

output format : 
|-- Master directory
    |--output
        |--(roll number 1)
        |--(roll number2)
            |-- happy.txt
            |-- sad.txt
            |-- neutral.txt
    |-- (roll number 1)
    |-- (roll number 2)
    and so on.

"""

# A function that concatinates all the files in a given directory with path dir_path
# outpath is path where output file should be stored. outfile_name is the name of file.  
def concatenation(dir_path, outpath, outfile_name):
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
    user_input =input("Enter the complete path of your master directory:  \n")
    assert os.path.isdir(user_input), "I did not find the directory"
    print("\n")
    
    cmd = "mkdir " + user_input + "\\" + "output"
    os.system(cmd)
    outdatapath = user_input + "\\" + "output"
    with open(user_input + "\\" + "rollnumber.txt") as f:
        rollnumbers = f.readlines()
    rollnumbers = [x.strip() for x in rollnumbers]
    for i in range(len(rollnumbers)):
    #loop on all the roll numbers
        roll = rollnumbers[i]
        cmd = "mkdir " + outdatapath + "\\" + roll
        os.system(cmd)
        outpath = outdatapath + "\\" + roll 
        all_files=os.listdir(user_input + "\\" + roll)
        for index in range(len(all_files)):
        #loop on all the weeks
            if "week" or "Week" in all_files[index]:
                address = user_input + "\\" + roll + "\\" + all_files[index] + "\\" + roll + "\\" + "New Data Collection" 
                directory = os.listdir(address)
                address = address + "\\" + directory[0] + "\\" + "Keyboard Database" + "\\" + "sentence" 
                # getting the addresses of happy, sad and neutral directories.
                address_happy = address + "\\" + "Emotional" + "\\" + "Happy"
                address_sad = address + "\\" + "Emotional" + "\\" + "Sad"
                address_neutral = address + "\\" + "Neutral"
                # appending happy.txt, sad.txt, neutral.txt with the data in "dir_path" address_happy, address_sad, address_neutral respectively. 
                concatenation(address_happy, outpath, "happy.txt")
                concatenation(address_sad, outpath, "sad.txt")
                concatenation(address_neutral, outpath, "neutral.txt")
            
if __name__=='__main__':
    main()
    
