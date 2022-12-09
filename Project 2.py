import random
import numpy
import csv
import pandas as pd


testor = input("tester file")
valid = False
while valid == False:
    choice = input("choose algorithm")
    if (choice == "1" or choice == "2"):
        valid = True







df = pd.read_csv(testor, sep="  ", header= None, engine="python")

print(df)


def cross_valid(testor, curr, newFeat):
    accuracy = random.randint(0,10)
    return accuracy

def featSearch():
    curr_set_feats = []
    for i in range (1, len(df.columns)):
        print("on the " + str(i) + "th level of the search tree")
        adding_feat = 0
        highest_acc = 0

        #print(df[i])
        for j in range(1, len(df.columns)):
            if(j not in curr_set_feats):
                print("--Considering adding the " + str(j) + " feature")
                acc =   cross_valid(testor, curr_set_feats, j)
                if(acc > highest_acc):
                    highest_acc = acc
                    adding_feat = j
            
            print(df[j])
            


featSearch()

