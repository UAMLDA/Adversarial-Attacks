import os
import csv
import numpy as np
import shutil

directory = "dataset/" 
for root,dirs,files in os.walk(directory):
    a = 0
    j = 0
    multi_class = []
    binary_class = []
    for file in files:
        if file.endswith(".csv"):
            with open(directory+file, 'r', newline = '') as csvfile:
                dataset = csv.reader(csvfile, delimiter = ',')
                dataset = list(dataset)
                label_col = []
                #_______________________
                #Check number of samples
                #_______________________
                
                sample_size = 0
                for line in dataset:
                    sample_size +=1      
                
                #________________________
                # Check number of features 
                #________________________
                                
                for line1 in dataset:
                    #print("[DEBUG] Entered for loop of features")
                    no_of_feat = len(line1)
                    #print('[DEBUG] No of features ', no_of_feat)
                    if ((no_of_feat>21) & (sample_size>1000)):
                        k = True # Setting up a flag
                        j = j+1
                    else:
                        k = False
                    break
                
                if (k==False): #Skip rest of the code-> go back to for file in files;
                    continue
                
                #_________________________
                # Check for binary classes
                #_________________________
                
                for line in dataset:
                    label_col.append(line[-1])
                    
                if(len(set(label_col))>2):
                    multi_class.append(file)
                    
                elif(len(set(label_col))==2):
                    binary_class.append(file)
                    a = a+1
                else:
                    print("Single label: Not required")
                   
    print("No of files having attributes greater than 20: ", j)
    print("No of files with attributes>=20 and binary classes: ", a)
    
    
writedirname = "BinaryData_Samplesize_greaterthan_1000/"
p = os.path.abspath('.')
path = os.path.join(p, writedirname)
os.mkdir(path)

directory = "UCI_Dataset/" 
for file in binary_class:
    src = directory + file
    dst = writedirname + file
    shutil.copyfile(src, dst)  
