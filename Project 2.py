import random
import numpy as np
import csv
import pandas as pd
import copy
import time


start = time.time()
testor = input("tester file: ")
valid = False
while valid == False:
    choice = input("choose algorithm (1 = forward selection, 2 = backwards elimination): ")
    if (choice == "1" or choice == "2"):
        valid = True
    else:
        print("invalid choice try again please")






#TwoD_Arr= np.loadtxt(testor, delimiter="  ", dtype=int)
df = pd.read_csv(testor, sep="  ", header= None, engine="python")
TwoD_Arr = df.iloc[:,:].values




def cross_valid(testor, curr, newFeat):
    if choice == "1":
        Copy = copy.deepcopy(testor)
        for i in range(1,len(Copy[0])):
            if i != newFeat :
                if i not in curr:
                    for j in range(len(Copy)):
                        Copy[j][i] = 0
    elif choice =="2":
        #print("hi")
        Copy = copy.deepcopy(testor)
        for i in range(1,len(Copy[0])):
                if i  in curr:
                  for j in range(len(Copy)):
                        Copy[j][i] = 0
        

    Correct = 0
    for a in range(len(Copy)):
        obj = Copy[a][1:]
        #print (copy[a][1:])
        clas = Copy[a][0]
        NearNeighDist = np.inf
        NearNeighLoc = np.inf
        for b in range(len(Copy)):
            if b != a:
                dist = np.sqrt(sum(pow((obj)- (Copy[b][1:]),2)))
                if NearNeighDist > dist:
                    NearNeighDist = dist
                    NearNeighLoc = b
                    NearNeighClass = Copy[NearNeighLoc][0]

        if NearNeighClass == clas:
            Correct +=1
        

    accuracy = Correct / len(Copy)
    return accuracy

def featSearch1(df):

    curr_set_feats = []
    even_higher = []
    best =0
    for i in range (1, len(df[0])):
        print("on the " + str(i) + "th level of the search tree")
        adding_feat = 0
        highest_acc = 0


        #print(df[i])
        for j in range(1, len(df[0])):
            if(j not in curr_set_feats):
                print("--Considering adding the " + str(j) + " feature")
                acc =   cross_valid(TwoD_Arr, curr_set_feats, j)
                print(" Accuracy for " + str(j) + " is: "+ str(acc))
                if(j not in even_higher):
                    if(acc > highest_acc):
                        highest_acc = acc
                        adding_feat = j

        print  ("Best Accuracy for this level is "+ str(highest_acc))  
              
        curr_set_feats.append(adding_feat)  
        if (best < highest_acc ):
                        best = highest_acc
                        even_higher.append(adding_feat)  
    print("best accuracy is " + str(best))
    print("current set of features are " + str(curr_set_feats))    
    print("best set of features are " + str(even_higher))
    end = time.time() 
    print("time it took: " + str(f'{(end - start):.2f}'))













def featSearch2(df):

    curr_set_feats = []
    temp_remove_set = []
    even_higher = []
   
    best =0
    end = False
    for e in range(1, len(df[0])):
        curr_set_feats.append(e)
    for i in range (1, len(df[0])):
        print("on the " + str(i) + "th level of the search tree")
        adding_feat = 0
        highest_acc = 0

        

        #print(df[i])
        
        for j in range(1, len(df[0])):
            
            temp_remove_set = copy.deepcopy(curr_set_feats)
            if(j in curr_set_feats):
                print("--Considering removing the " + str(j) + " feature")
                temp_remove_set.remove(j)
                if(temp_remove_set == [] ):
                    end = True
                    break
                print(temp_remove_set) 
                print(j)
                acc =   cross_valid(TwoD_Arr, temp_remove_set, j)
                print(" Accuracy for " + str(j) + " is: "+ str(acc))
                if(j not in even_higher):
                    if(acc > highest_acc):
                        highest_acc = acc
                        adding_feat = j

         
        if end == False:    
            print  ("Best Accuracy for this level is "+ str(highest_acc))  
            print(curr_set_feats) 
            curr_set_feats.remove(adding_feat) 
             
            if (best < highest_acc ):
                        best = highest_acc
                        even_higher.append(adding_feat)  
    print("best accuracy is " + str(best))
    print("current set of features are " + str(curr_set_feats))    
    print("best set of features are " + str(even_higher))
    end = time.time() 
    print("time it took: " + str(f'{(end - start):.2f}'))
            

if choice == "1":
    featSearch1(TwoD_Arr)
elif choice =="2":
    featSearch2(TwoD_Arr)



