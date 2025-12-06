#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: DLVA Tool
"""

import warnings
warnings.filterwarnings("ignore")

import os
import time
import pandas as pd
from pathlib import Path
import json
import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join

import sklearn.metrics
from sklearn.metrics import precision_score, recall_score, f1_score



tool_ = list()
vul_ = list()
accuracy_ = list()

tn_ = list()
fp_ = list() 
fn_ = list() 
tp_ = list()
    
tpr_ = list()
fnr_ = list()
fpr_ = list()
tnr_ = list()

recall_ = list()
precision_ = list()
f1_ = list()

t_ = list()



exp_ = list()
exp__ = list()

CR_ = list()




import sys 
stdoutOrigin=sys.stdout 
sys.stdout = open('tools_results.txt', 'w')
print("\nStatic Analysis Tools\n")
print("="*60)





path = '10_tools_files/Elysium-benchmark/'
benchmark = 'Elysium'
print(benchmark,"\n")

df = pd.read_csv('Elysium_benchmark.csv')
print(df)

dfcopy = df.copy()





def addResults(tool, benchmark, bug_type, y_true, predictions, t):

        predictions = np.array(predictions)

        dfcopy[tool+'_'+benchmark+'_'+bug_type+'_'+'predictions'] = predictions
        
        indx = np.where(predictions == 2)[0]

        print("Exceptions: ", len(indx), round(len(indx)/len(predictions)*100, 1),"%")

        tool_.append(tool)
        vul_.append(benchmark+'_'+bug_type)

        exp_.append(len(indx))
        exp__.append(round(len(indx)/len(predictions)*100, 1))
        CR_.append(round(100-(round(len(indx)/len(predictions)*100, 1)),1))

        t_.append(t)
        
        y_true = np.delete(y_true, indx)

        predictions = np.delete(predictions, indx)


        #print("-"*60)
        #print("static analysis:",predictions)
        print("="*60)



        # Prediction Result
        print('confusion_matrix')
        print(pd.DataFrame(sklearn.metrics.confusion_matrix(y_true, predictions)))



        print("-"*60)
        tn, fp, fn, tp = sklearn.metrics.confusion_matrix(y_true, predictions).ravel()
        print("\t TP:", tp)
        tp_.append(tp)
        print("\t TN:", tn)
        tn_.append(tn)
        print("\t FN:", fn)
        fn_.append(fn)
        print("\t FP:", fp)
        fp_.append(fp)

        print("-"*60)
        Accuracy = (tp + tn)/(tp + fp + tn +fn)
        print("\t Accurcy:", round(Accuracy*100, 1))

        accuracy_.append(round(Accuracy*100, 1))
                      
        print("-"*60)

        if tool == 'SoliAudit' and bug_type == 'suicidal':

            print("\t TPR (detection rate):  0" )
            tpr_.append(0)
                
            print("\t FNR (miss rate):       0")
            fnr_.append(0)

        else:
            
            print("\t TPR (detection rate):  {:0.1f}\t%".format( tp/(tp+fn)*100 ))
            tpr_.append(round( tp/(tp+fn)*100 , 1 ))
                
            print("\t FNR (miss rate):       {:0.1f}\t%".format( fn/(tp+fn)*100 ))
            fnr_.append(round( fn/(tp+fn)*100 , 1 ))
            
        print("\t FPR (false alarm):     {:0.1f}\t%".format( fp/(fp+tn)*100 ))
        fpr_.append(round( fp/(fp+tn)*100 , 1 ))
            
        print("\t TNR (specificity):     {:0.1f}\t%".format( tn/(fp+tn)*100 ))
        tnr_.append(round( tn/(fp+tn)*100 , 1 ))
            
        print("-"*60)


        precision = precision_score(y_true, predictions, average='weighted')
        recall = recall_score(y_true, predictions, average='weighted')
        f1 = f1_score(y_true, predictions, average='weighted')

        print("\t Precision:             {:0.1f}\t%".format( precision*100 ))
        print("\t Recall:                {:0.1f}\t%".format( recall*100 ))
        print("\t F1:                    {:0.1f}\t%".format( f1*100 ))

        precision_.append(round(precision*100,1))
        recall_.append(round(recall*100,1))
        f1_.append(round(f1*100,1))

        print("-"*60)
        print('classification_report (specificity,sensitivity,f1)')
        print(sklearn.metrics.classification_report(y_true, predictions))
            
        ###########################################################################

        
        print("="*60)
        print("\n\nTesting Tool", tool,"on", benchmark, bug_type, "is Done...\n")

        print("#"*80)
        print("\n\n")








######################################################################################

tool = 'Oyente'


mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#print(">>> ", files)


##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.evm.json' in files:
        my_file = Path(path+tool+'/'+address+'.evm.json')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
                    
            if '"reentrancy": true' in data:
                label = 1
            else:
                label = 0

        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 5.3

addResults(tool, benchmark, bug_type, y_true, predictions, t)






######################################################################################

tool = 'Osiris'


mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.evm.evm.disasm.json' in files:
        my_file = Path(path+tool+'/'+address+'.evm.evm.disasm.json')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
                    
            if '"reentrancy": true' in data:
                label = 1
            else:
                label = 0

        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 63.6        
addResults(tool, benchmark, bug_type, y_true, predictions, t)







######################################################################################

tool = 'Mythril'


mypath = path+tool+'/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1



    file = ""
                
    for f in onlyfiles:
        if f.startswith(address):
            file = onlyfiles[onlyfiles.index(f)]
            break
                            
    if file != "" and float(file.split(" ")[1][:-4]) < 600:
        my_file = Path(mypath+file)

        f = open(my_file, 'r')
        data = f.read()

        if data != "":
                    
            if 'SWC ID: 107' in data:
                label = 1
            else:
                label = 0

        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 95.5       
addResults(tool, benchmark, bug_type, y_true, predictions, t)





##################################################################
bug_type = 'suicidal'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1



    file = ""
                
    for f in onlyfiles:
        if f.startswith(address):
            file = onlyfiles[onlyfiles.index(f)]
            break
                            
    if file != "" and float(file.split(" ")[1][:-4]) < 600:
        my_file = Path(mypath+file)

        f = open(my_file, 'r')
        data = f.read()

        if data != "":
                    
            if 'SWC ID: 106' in data:
                label = 1
            else:
                label = 0

        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 95.5       
addResults(tool, benchmark, bug_type, y_true, predictions, t)









######################################################################################

tool = 'eThor'


##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

Y = []



mypath = path+tool+'/result1_/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

predictions = []

t = 0

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    theFile = ""
    for file in files:
        if file.startswith('Elysium_benchmark_'+address):
            theFile = file

            t += float(file.split(' ')[1][:-4])

            break

    if theFile != "":
        my_file = Path(path+tool+'/result1_/'+theFile)
        f = open(my_file, 'r')
        data = f.read()


        count = 0
                                
        if ' UNSATISFIABLE' in data:
            label = 0
            count += 1

        if ' SATISFIABLE' in data:
            label = 1
            count += 1
                                
        if count == 2:
            label = 1
                                    
                                
        if count == 0:
            label = 2

                                    
    else:
        label = 2
                  

    predictions.append(label)

print(len(predictions))
Y.append(predictions)


mypath = path+tool+'/result2_/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

predictions = []

t = 0

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    theFile = ""
    for file in files:
        if file.startswith('Elysium_benchmark_'+address):
            theFile = file

            t += float(file.split(' ')[1][:-4])

            break

    if theFile != "":
        my_file = Path(path+tool+'/result2_/'+theFile)
        f = open(my_file, 'r')
        data = f.read()


        count = 0
                                
        if ' UNSATISFIABLE' in data:
            label = 0
            count += 1

        if ' SATISFIABLE' in data:
            label = 1
            count += 1
                                
        if count == 2:
            label = 1
                                    
                                
        if count == 0:
            label = 2

                                    
    else:
        label = 2
                  

    predictions.append(label)
print(len(predictions))
Y.append(predictions)





mypath = path+tool+'/result3_/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

predictions = []

t = 0

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    theFile = ""
    for file in files:
        if file.startswith('Elysium_benchmark_'+address):
            theFile = file

            t += float(file.split(' ')[1][:-4])

            break

    if theFile != "":
        my_file = Path(path+tool+'/result3_/'+theFile)
        f = open(my_file, 'r')
        data = f.read()


        count = 0
                                
        if ' UNSATISFIABLE' in data:
            label = 0
            count += 1

        if ' SATISFIABLE' in data:
            label = 1
            count += 1
                                
        if count == 2:
            label = 1
                                    
                                
        if count == 0:
            label = 2

                                    
    else:
        label = 2
                  

    predictions.append(label)
print(len(predictions))
Y.append(predictions)

#print(Y)


predictions = []

for j in range(0, len(Y[0])):
    l = 2
    for i in range(0,3):
        if Y[i][j] == 1 and l == 2:
            l = 1
        elif Y[i][j] == 0 and l == 2:
            l = 0
    
    predictions.append(l) 
        


t = 250       
addResults(tool, benchmark, bug_type, y_true, predictions, t)






######################################################################################

tool = 'DLVA'



from os import listdir
from os.path import isfile, join
files = [f for f in listdir('.') if isfile(join('.', f))]

for dlva_pred_file in files:
    if dlva_pred_file.startswith('DLVA_Predictions_for_Elysium_benchmark'):
        dlva_df = pd.read_csv(dlva_pred_file)

        for batch_file in files:
            if batch_file == dlva_pred_file[21:]:
                batch_df = pd.read_csv(batch_file)

                print("#"*80)
                print("\n\n\n\nDLVA results: ", dlva_pred_file, "\nGround Truth: ", batch_file)
                print("="*80)

                for vul in dlva_df.columns[1:]:
                    print("\n\nVulnerability:", vul)
                    print("*"*60)

                    if vul not in batch_df.columns:
                        print("ground truth does not exist in", batch_file)
                    else:
                         
                        y_true = batch_df[vul].values
                        predictions = dlva_df[vul].values

                        t = 0.3
                        addResults(tool, benchmark, vul, y_true, predictions, t)






dfcopy.set_index('address', inplace = True)
dfcopy.to_csv('tools_predictions_'+benchmark+'_900.csv')












path = '10_tools_files/Elysium-benchmark/'
benchmark = 'Elysium'
print(benchmark,"\n")

df = pd.read_csv('Elysium_benchmark_59_source_available.csv')
print(df)

dfcopy = df.copy()



def addResults(tool, benchmark, bug_type, y_true, predictions, t):

        predictions = np.array(predictions)

        dfcopy[tool+'_'+benchmark+'_'+bug_type+'_'+'predictions'] = predictions
        
        indx = np.where(predictions == 2)[0]

        print("Exceptions: ", len(indx), round(len(indx)/len(predictions)*100, 1),"%")

        tool_.append(tool)
        vul_.append(benchmark+'_'+bug_type)

        exp_.append(len(indx))
        exp__.append(round(len(indx)/len(predictions)*100, 1))
        CR_.append(round(100-(round(len(indx)/len(predictions)*100, 1)),1))

        t_.append(t)
        
        y_true = np.delete(y_true, indx)

        predictions = np.delete(predictions, indx)


        #print("-"*60)
        #print("static analysis:",predictions)
        print("="*60)



        # Prediction Result
        print('confusion_matrix')
        print(pd.DataFrame(sklearn.metrics.confusion_matrix(y_true, predictions)))



        print("-"*60)
        if tool == 'ConFuzzius' and bug_type == 'suicidal':
            tn, fp, fn, tp = 52, 0, 0, 0
        else:
            tn, fp, fn, tp = sklearn.metrics.confusion_matrix(y_true, predictions).ravel()
        print("\t TP:", tp)
        tp_.append(tp)
        print("\t TN:", tn)
        tn_.append(tn)
        print("\t FN:", fn)
        fn_.append(fn)
        print("\t FP:", fp)
        fp_.append(fp)

        print("-"*60)
        Accuracy = (tp + tn)/(tp + fp + tn +fn)
        print("\t Accurcy:", round(Accuracy*100, 1))

        accuracy_.append(round(Accuracy*100, 1))
                      
        print("-"*60)

        try:
            
            print("\t TPR (detection rate):  {:0.1f}\t%".format( tp/(tp+fn)*100 ))
            tpr_.append(round( tp/(tp+fn)*100 , 1 ))
                
            print("\t FNR (miss rate):       {:0.1f}\t%".format( fn/(tp+fn)*100 ))
            fnr_.append(round( fn/(tp+fn)*100 , 1 ))
                
            print("\t FPR (false alarm):     {:0.1f}\t%".format( fp/(fp+tn)*100 ))
            fpr_.append(round( fp/(fp+tn)*100 , 1 ))
                
            print("\t TNR (specificity):     {:0.1f}\t%".format( tn/(fp+tn)*100 ))
            tnr_.append(round( tn/(fp+tn)*100 , 1 ))

        except:
            print("\t TPR (detection rate):  {:0.1f}\t%".format( 0*100 ))
            tpr_.append(round( 0.0 , 1 ))
                
            print("\t FNR (miss rate):       {:0.1f}\t%".format( 0*100 ))
            fnr_.append(round( 0.0 , 1 ))
                
            print("\t FPR (false alarm):     {:0.1f}\t%".format( fp/(fp+tn)*100 ))
            fpr_.append(round( fp/(fp+tn)*100 , 1 ))
                
            print("\t TNR (specificity):     {:0.1f}\t%".format( tn/(fp+tn)*100 ))
            tnr_.append(round( tn/(fp+tn)*100 , 1 ))
            
        print("-"*60)


        precision = precision_score(y_true, predictions, average='weighted')
        recall = recall_score(y_true, predictions, average='weighted')
        f1 = f1_score(y_true, predictions, average='weighted')

        print("\t Precision:             {:0.1f}\t%".format( precision*100 ))
        print("\t Recall:                {:0.1f}\t%".format( recall*100 ))
        print("\t F1:                    {:0.1f}\t%".format( f1*100 ))

        precision_.append(round(precision*100,1))
        recall_.append(round(recall*100,1))
        f1_.append(round(f1*100,1))

        print("-"*60)
        print('classification_report (specificity,sensitivity,f1)')
        print(sklearn.metrics.classification_report(y_true, predictions))
            
        ###########################################################################

        
        print("="*60)
        print("\n\nTesting Tool", tool,"on", benchmark, bug_type, "is Done...\n")

        print("#"*80)
        print("\n\n")









######################################################################################

tool = 'smartcheck'

df2 = pd.read_csv('10_tools_files/smartbugs/smartbugs_results_Elysium-benchmark.csv')

df2 = df2.loc[df2['toolid']==tool]
#print(df2)

tool = 'SmartCheck'



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'SOLIDITY_CALL_WITHOUT_DATA' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0

    else:
        label = 2
                  

    predictions.append(label)

t = 5.2      
addResults(tool, benchmark, bug_type, y_true, predictions, t)








######################################################################################

tool = 'SoliAudit'



mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.md' in files:
        my_file = Path(path+tool+'/'+address+'.md')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if "_`X`_ Reentrancy" in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 42.4       
addResults(tool, benchmark, bug_type, y_true, predictions, t)


##################################################################
bug_type = 'suicidal'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.md' in files:
        my_file = Path(path+tool+'/'+address+'.md')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if "_`X`_ SelfDestruct" in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 42.4    
addResults(tool, benchmark, bug_type, y_true, predictions, t)











######################################################################################

tool = 'Slither'


mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if '"success": true' in data:
            if '"check": "reentrancy-eth"' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 2        
addResults(tool, benchmark, bug_type, y_true, predictions, t)


##################################################################
bug_type = 'suicidal'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if '"success": true' in data:
            if '"check": "suicidal"' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 2       
addResults(tool, benchmark, bug_type, y_true, predictions, t)





######################################################################################

tool = 'ConFuzzius'


mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if '"swc_id": 107' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 49.6
addResults(tool, benchmark, bug_type, y_true, predictions, t)



##################################################################
bug_type = 'suicidal'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if '"swc_id": 106' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 49.6       
addResults(tool, benchmark, bug_type, y_true, predictions, t)






######################################################################################

tool = 'Sailfish'


mypath = path+tool+'/'

files = list()

for file in os.listdir(mypath):
    d = os.path.join(mypath, file)
    if os.path.isdir(d):
        files.append(d)



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if path+tool+'/'+address in files:
        my_file = Path(path+tool+'/'+address+'/contractlint.log')
        f = open(my_file, 'r')
        data = f.read()

        if 'Analysis finished!' in data:
                    
            if 'DAO dependency detected' in data:
                label = 1
            else:
                label = 0

        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

tool = 'SAILFISH'

t = 26        
addResults(tool, benchmark, bug_type, y_true, predictions, t)









dfcopy.set_index('address', inplace = True)
dfcopy.to_csv('tools_predictions_'+benchmark+'_59_source_available.csv')






















#################################################################################
#################################################################################
#################################################################################
#################################################################################



















path = '10_tools_files/Reentrancy-benchmark/'
benchmark = 'Reentrancy'
print(benchmark,"\n")

df = pd.read_csv('Reentrancy_benchmark.csv')
print(df)

dfcopy = df.copy()



def addResults(tool, benchmark, bug_type, y_true, predictions, t):

        predictions = np.array(predictions)

        dfcopy[tool+'_'+benchmark+'_'+bug_type+'_'+'predictions'] = predictions
        
        indx = np.where(predictions == 2)[0]

        print("Exceptions: ", len(indx), round(len(indx)/len(predictions)*100, 1),"%")

        tool_.append(tool)
        vul_.append(benchmark+'_'+bug_type)

        exp_.append(len(indx))
        exp__.append(round(len(indx)/len(predictions)*100, 1))
        CR_.append(round(100-(round(len(indx)/len(predictions)*100, 1)),1))

        t_.append(t)
        
        y_true = np.delete(y_true, indx)

        predictions = np.delete(predictions, indx)


        #print("-"*60)
        #print("static analysis:",predictions)
        print("="*60)



        # Prediction Result
        print('confusion_matrix')
        print(pd.DataFrame(sklearn.metrics.confusion_matrix(y_true, predictions)))



        print("-"*60)
        tn, fp, fn, tp = sklearn.metrics.confusion_matrix(y_true, predictions).ravel()
        print("\t TP:", tp)
        tp_.append(tp)
        print("\t TN:", tn)
        tn_.append(tn)
        print("\t FN:", fn)
        fn_.append(fn)
        print("\t FP:", fp)
        fp_.append(fp)

        print("-"*60)
        Accuracy = (tp + tn)/(tp + fp + tn +fn)
        print("\t Accurcy:", round(Accuracy*100, 1))

        accuracy_.append(round(Accuracy*100, 1))
                      
        print("-"*60)
            
        print("\t TPR (detection rate):  {:0.1f}\t%".format( tp/(tp+fn)*100 ))
        tpr_.append(round( tp/(tp+fn)*100 , 1 ))
            
        print("\t FNR (miss rate):       {:0.1f}\t%".format( fn/(tp+fn)*100 ))
        fnr_.append(round( fn/(tp+fn)*100 , 1 ))
            
        print("\t FPR (false alarm):     {:0.1f}\t%".format( fp/(fp+tn)*100 ))
        fpr_.append(round( fp/(fp+tn)*100 , 1 ))
            
        print("\t TNR (specificity):     {:0.1f}\t%".format( tn/(fp+tn)*100 ))
        tnr_.append(round( tn/(fp+tn)*100 , 1 ))
            
        print("-"*60)


        precision = precision_score(y_true, predictions, average='weighted')
        recall = recall_score(y_true, predictions, average='weighted')
        f1 = f1_score(y_true, predictions, average='weighted')

        print("\t Precision:             {:0.1f}\t%".format( precision*100 ))
        print("\t Recall:                {:0.1f}\t%".format( recall*100 ))
        print("\t F1:                    {:0.1f}\t%".format( f1*100 ))

        precision_.append(round(precision*100,1))
        recall_.append(round(recall*100,1))
        f1_.append(round(f1*100,1))

        print("-"*60)
        print('classification_report (specificity,sensitivity,f1)')
        print(sklearn.metrics.classification_report(y_true, predictions))
            
        ###########################################################################

        
        print("="*60)
        print("\n\nTesting Tool", tool,"on", benchmark, bug_type, "is Done...\n")

        print("#"*80)
        print("\n\n")








######################################################################################

tool = 'Oyente'


mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#print(">>> ", files)


##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.evm.json' in files:
        my_file = Path(path+tool+'/'+address+'.evm.json')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
                    
            if '"reentrancy": true' in data:
                label = 1
            else:
                label = 0

        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 2.8      
addResults(tool, benchmark, bug_type, y_true, predictions, t)






######################################################################################

tool = 'Osiris'


mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.evm.evm.disasm.json' in files:
        my_file = Path(path+tool+'/'+address+'.evm.evm.disasm.json')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
                    
            if '"reentrancy": true' in data:
                label = 1
            else:
                label = 0

        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 13.7       
addResults(tool, benchmark, bug_type, y_true, predictions, t)







######################################################################################

tool = 'Mythril'


mypath = path+tool+'/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1



    file = ""
                
    for f in onlyfiles:
        if f.startswith(address):
            file = onlyfiles[onlyfiles.index(f)]
            break
                            
    if file != "" and float(file.split(" ")[1][:-4]) < 600:
        my_file = Path(mypath+file)

        f = open(my_file, 'r')
        data = f.read()

        if data != "":
                    
            if 'SWC ID: 107' in data:
                label = 1
            else:
                label = 0

        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 36        
addResults(tool, benchmark, bug_type, y_true, predictions, t)








######################################################################################

tool = 'eThor'


##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

Y = []



mypath = path+tool+'/result1_/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

predictions = []

t = 0

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    theFile = ""
    for file in files:
        if file.startswith('Reentrancy_benchmark_'+address):
            theFile = file

            t += float(file.split(' ')[1][:-4])

            break

    if theFile != "":
        my_file = Path(path+tool+'/result1_/'+theFile)
        f = open(my_file, 'r')
        data = f.read()


        count = 0
                                
        if ' UNSATISFIABLE' in data:
            label = 0
            count += 1

        if ' SATISFIABLE' in data:
            label = 1
            count += 1
                                
        if count == 2:
            label = 1
                                    
                                
        if count == 0:
            label = 2

                                    
    else:
        label = 2
                  

    predictions.append(label)

print(len(predictions))
Y.append(predictions)


mypath = path+tool+'/result2_/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

predictions = []

t = 0

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    theFile = ""
    for file in files:
        if file.startswith('Reentrancy_benchmark_'+address):
            theFile = file

            t += float(file.split(' ')[1][:-4])

            break

    if theFile != "":
        my_file = Path(path+tool+'/result2_/'+theFile)
        f = open(my_file, 'r')
        data = f.read()


        count = 0
                                
        if ' UNSATISFIABLE' in data:
            label = 0
            count += 1

        if ' SATISFIABLE' in data:
            label = 1
            count += 1
                                
        if count == 2:
            label = 1
                                    
                                
        if count == 0:
            label = 2

                                    
    else:
        label = 2
                  

    predictions.append(label)
print(len(predictions))
Y.append(predictions)





mypath = path+tool+'/result3_/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

predictions = []

t = 0

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    theFile = ""
    for file in files:
        if file.startswith('Reentrancy_benchmark_'+address):
            theFile = file

            t += float(file.split(' ')[1][:-4])

            break

    if theFile != "":
        my_file = Path(path+tool+'/result3_/'+theFile)
        f = open(my_file, 'r')
        data = f.read()


        count = 0
                                
        if ' UNSATISFIABLE' in data:
            label = 0
            count += 1

        if ' SATISFIABLE' in data:
            label = 1
            count += 1
                                
        if count == 2:
            label = 1
                                    
                                
        if count == 0:
            label = 2

                                    
    else:
        label = 2
                  

    predictions.append(label)
print(len(predictions))
Y.append(predictions)

#print(Y)


predictions = []

for j in range(0, len(Y[0])):
    l = 2
    for i in range(0,3):
        if Y[i][j] == 1 and l == 2:
            l = 1
        elif Y[i][j] == 0 and l == 2:
            l = 0
    
    predictions.append(l) 
        


t = 200       
addResults(tool, benchmark, bug_type, y_true, predictions, t)






######################################################################################

tool = 'DLVA'



from os import listdir
from os.path import isfile, join
files = [f for f in listdir('.') if isfile(join('.', f))]

for dlva_pred_file in files:
    if dlva_pred_file.startswith('DLVA_Predictions_for_Reentrancy_benchmark'):
        dlva_df = pd.read_csv(dlva_pred_file)

        for batch_file in files:
            if batch_file == dlva_pred_file[21:]:
                batch_df = pd.read_csv(batch_file)

                print("#"*80)
                print("\n\n\n\nDLVA results: ", dlva_pred_file, "\nGround Truth: ", batch_file)
                print("="*80)

                for vul in dlva_df.columns[1:]:
                    print("\n\nVulnerability:", vul)
                    print("*"*60)

                    if vul not in batch_df.columns:
                        print("ground truth does not exist in", batch_file)
                    else:
                         
                        y_true = batch_df[vul].values
                        predictions = dlva_df[vul].values

                        t = 0.15
                        addResults(tool, benchmark, vul, y_true, predictions, t)






dfcopy.set_index('address', inplace = True)
dfcopy.to_csv('tools_predictions_'+benchmark+'_900.csv')












path = '10_tools_files/Reentrancy-benchmark/'
benchmark = 'Reentrancy'
print(benchmark,"\n")

df = pd.read_csv('Reentrancy_benchmark_472_source_available.csv')
print(df)

dfcopy = df.copy()



def addResults(tool, benchmark, bug_type, y_true, predictions, t):

        predictions = np.array(predictions)

        dfcopy[tool+'_'+benchmark+'_'+bug_type+'_'+'predictions'] = predictions
        
        indx = np.where(predictions == 2)[0]

        print("Exceptions: ", len(indx), round(len(indx)/len(predictions)*100, 1),"%")

        tool_.append(tool)
        vul_.append(benchmark+'_'+bug_type)

        exp_.append(len(indx))
        exp__.append(round(len(indx)/len(predictions)*100, 1))
        CR_.append(round(100-(round(len(indx)/len(predictions)*100, 1)),1))

        t_.append(t)
        
        y_true = np.delete(y_true, indx)

        predictions = np.delete(predictions, indx)


        #print("-"*60)
        #print("static analysis:",predictions)
        print("="*60)



        # Prediction Result
        print('confusion_matrix')
        print(pd.DataFrame(sklearn.metrics.confusion_matrix(y_true, predictions)))



        print("-"*60)
        tn, fp, fn, tp = sklearn.metrics.confusion_matrix(y_true, predictions).ravel()
        print("\t TP:", tp)
        tp_.append(tp)
        print("\t TN:", tn)
        tn_.append(tn)
        print("\t FN:", fn)
        fn_.append(fn)
        print("\t FP:", fp)
        fp_.append(fp)

        print("-"*60)
        Accuracy = (tp + tn)/(tp + fp + tn +fn)
        print("\t Accurcy:", round(Accuracy*100, 1))

        accuracy_.append(round(Accuracy*100, 1))
                      
        print("-"*60)

        print("\t TPR (detection rate):  {:0.1f}\t%".format( tp/(tp+fn)*100 ))
        tpr_.append(round( tp/(tp+fn)*100 , 1 ))
                
        print("\t FNR (miss rate):       {:0.1f}\t%".format( fn/(tp+fn)*100 ))
        fnr_.append(round( fn/(tp+fn)*100 , 1 ))
                
        print("\t FPR (false alarm):     {:0.1f}\t%".format( fp/(fp+tn)*100 ))
        fpr_.append(round( fp/(fp+tn)*100 , 1 ))
                
        print("\t TNR (specificity):     {:0.1f}\t%".format( tn/(fp+tn)*100 ))
        tnr_.append(round( tn/(fp+tn)*100 , 1 ))
            
        print("-"*60)


        precision = precision_score(y_true, predictions, average='weighted')
        recall = recall_score(y_true, predictions, average='weighted')
        f1 = f1_score(y_true, predictions, average='weighted')

        print("\t Precision:             {:0.1f}\t%".format( precision*100 ))
        print("\t Recall:                {:0.1f}\t%".format( recall*100 ))
        print("\t F1:                    {:0.1f}\t%".format( f1*100 ))

        precision_.append(round(precision*100,1))
        recall_.append(round(recall*100,1))
        f1_.append(round(f1*100,1))

        print("-"*60)
        print('classification_report (specificity,sensitivity,f1)')
        print(sklearn.metrics.classification_report(y_true, predictions))
            
        ###########################################################################

        
        print("="*60)
        print("\n\nTesting Tool", tool,"on", benchmark, bug_type, "is Done...\n")

        print("#"*80)
        print("\n\n")









######################################################################################

tool = 'smartcheck'

df2 = pd.read_csv('10_tools_files/smartbugs/smartbugs_results_Reentrancy-benchmark.csv')

df2 = df2.loc[df2['toolid']==tool]
#print(df2)

tool = 'SmartCheck'



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'SOLIDITY_CALL_WITHOUT_DATA' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0

    else:
        label = 2
                  

    predictions.append(label)
t = 4.6        
addResults(tool, benchmark, bug_type, y_true, predictions, t)








######################################################################################

tool = 'SoliAudit'



mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.md' in files:
        my_file = Path(path+tool+'/'+address+'.md')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if "_`X`_ Reentrancy" in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 5.3 
addResults(tool, benchmark, bug_type, y_true, predictions, t)


##################################################################





######################################################################################

tool = 'Slither'


mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if '"success": true' in data:
            if '"check": "reentrancy-eth"' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 0.9 
addResults(tool, benchmark, bug_type, y_true, predictions, t)


##################################################################



######################################################################################

tool = 'ConFuzzius'


mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if '"swc_id": 107' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

t = 32.2       
addResults(tool, benchmark, bug_type, y_true, predictions, t)



##################################################################





######################################################################################

tool = 'Sailfish'


mypath = path+tool+'/'

files = list()

for file in os.listdir(mypath):
    d = os.path.join(mypath, file)
    if os.path.isdir(d):
        files.append(d)



##################################################################
bug_type = 'reentrancy-eth'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if path+tool+'/'+address in files:
        my_file = Path(path+tool+'/'+address+'/contractlint.log')
        f = open(my_file, 'r')
        data = f.read()

        if 'Analysis finished!' in data:
                    
            if 'DAO dependency detected' in data:
                label = 1
            else:
                label = 0

        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

tool = 'SAILFISH'

t = 3.5     
addResults(tool, benchmark, bug_type, y_true, predictions, t)









dfcopy.set_index('address', inplace = True)
dfcopy.to_csv('tools_predictions_'+benchmark+'_472_source_available.csv')






















#################################################################################
#################################################################################
#################################################################################
#################################################################################



















path = '10_tools_files/SolidiFI-benchmark/'
benchmark = 'SolidiFI'
print(benchmark,"\n")

df = pd.read_csv('SolidiFI_benchmark.csv')
print(df)

dfcopy = df.copy()



def addResults(tool, benchmark, bug_type, y_true, predictions, t):

        predictions = np.array(predictions)

        dfcopy[tool+'_'+benchmark+'_'+bug_type+'_'+'predictions'] = predictions
        
        indx = np.where(predictions == 2)[0]

        print("Exceptions: ", len(indx), round(len(indx)/len(predictions)*100, 1),"%")

        tool_.append(tool)
        vul_.append(benchmark+'_'+bug_type)

        exp_.append(len(indx))
        exp__.append(round(len(indx)/len(predictions)*100, 1))
        CR_.append(round(100-(round(len(indx)/len(predictions)*100, 1)),1))

        t_.append(t)
        
        y_true = np.delete(y_true, indx)

        predictions = np.delete(predictions, indx)


        #print("-"*60)
        #print("static analysis:",predictions)
        print("="*60)



        # Prediction Result
        print('confusion_matrix')
        print(pd.DataFrame(sklearn.metrics.confusion_matrix(y_true, predictions)))



        print("-"*60)
        tn, fp, fn, tp = sklearn.metrics.confusion_matrix(y_true, predictions).ravel()
        print("\t TP:", tp)
        tp_.append(tp)
        print("\t TN:", tn)
        tn_.append(tn)
        print("\t FN:", fn)
        fn_.append(fn)
        print("\t FP:", fp)
        fp_.append(fp)

        print("-"*60)
        Accuracy = (tp + tn)/(tp + fp + tn +fn)
        print("\t Accurcy:", round(Accuracy*100, 1))

        accuracy_.append(round(Accuracy*100, 1))
                      
        print("-"*60)
            
        print("\t TPR (detection rate):  {:0.1f}\t%".format( tp/(tp+fn)*100 ))
        tpr_.append(round( tp/(tp+fn)*100 , 1 ))
            
        print("\t FNR (miss rate):       {:0.1f}\t%".format( fn/(tp+fn)*100 ))
        fnr_.append(round( fn/(tp+fn)*100 , 1 ))
            
        print("\t FPR (false alarm):     {:0.1f}\t%".format( fp/(fp+tn)*100 ))
        fpr_.append(round( fp/(fp+tn)*100 , 1 ))
            
        print("\t TNR (specificity):     {:0.1f}\t%".format( tn/(fp+tn)*100 ))
        tnr_.append(round( tn/(fp+tn)*100 , 1 ))
            
        print("-"*60)


        precision = precision_score(y_true, predictions, average='weighted')
        recall = recall_score(y_true, predictions, average='weighted')
        f1 = f1_score(y_true, predictions, average='weighted')

        print("\t Precision:             {:0.1f}\t%".format( precision*100 ))
        print("\t Recall:                {:0.1f}\t%".format( recall*100 ))
        print("\t F1:                    {:0.1f}\t%".format( f1*100 ))

        precision_.append(round(precision*100,1))
        recall_.append(round(recall*100,1))
        f1_.append(round(f1*100,1))

        print("-"*60)
        print('classification_report (specificity,sensitivity,f1)')
        print(sklearn.metrics.classification_report(y_true, predictions))
            
        ###########################################################################

        
        print("="*60)
        print("\n\nTesting Tool", tool,"on", benchmark, bug_type, "is Done...\n")

        print("#"*80)
        print("\n\n")

















######################################################################################

tool = 'oyente'

df2 = pd.read_csv('10_tools_files/smartbugs/smartbugs_results_SolidiFI-benchmark.csv')

df2 = df2.loc[df2['toolid']==tool]
#print(df2)

tool = 'Oyente'


##################################################################
bug_type = 'Re-entrancy'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'Re_Entrancy_Vulnerability' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0

    else:
        label = 2
                  

    predictions.append(label)

t = 9.1      
addResults(tool, benchmark, bug_type, y_true, predictions, t)



##################################################################
bug_type = 'Timestamp-Dependency'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'Timestamp_Dependency' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0
            
    else:
        label = 2
                  

    predictions.append(label)

t = 9.1  
addResults(tool, benchmark, bug_type, y_true, predictions, t)





##################################################################
bug_type = 'Overflow-Underflow'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'Integer_Overflow' in data: # or 'Integer_Underflow' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0
            
    else:
        label = 2
                  

    predictions.append(label)

t = 9.1          
addResults(tool, benchmark, bug_type, y_true, predictions, t)









######################################################################################

tool = 'osiris'

df2 = pd.read_csv('10_tools_files/smartbugs/smartbugs_results_SolidiFI-benchmark.csv')

df2 = df2.loc[df2['toolid']==tool]
#print(df2)

tool = 'Osiris'

##################################################################
bug_type = 'Re-entrancy'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'Reentrancy_bug' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0

    else:
        label = 2
                  

    predictions.append(label)

t = 50.9       
addResults(tool, benchmark, bug_type, y_true, predictions, t)



##################################################################
bug_type = 'Timestamp-Dependency'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'Time_dependency_bug' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0
            
    else:
        label = 2
                  

    predictions.append(label)

t = 50.9         
addResults(tool, benchmark, bug_type, y_true, predictions, t)





##################################################################
bug_type = 'Overflow-Underflow'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'Overflow_bugs' in data: # or 'Underflow_bugs' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0
            
    else:
        label = 2
                  

    predictions.append(label)

t = 50.9         
addResults(tool, benchmark, bug_type, y_true, predictions, t)







######################################################################################

tool = 'mythril-0.23.15'

df2 = pd.read_csv('10_tools_files/smartbugs/smartbugs_results_SolidiFI-benchmark.csv')

df2 = df2.loc[df2['toolid']==tool]
#print(df2)

tool = 'Mythril'

##################################################################
bug_type = 'Re-entrancy'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'SWC_107' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0

    else:
        label = 2
                  

    predictions.append(label)

t = 201.1        
addResults(tool, benchmark, bug_type, y_true, predictions, t)



##################################################################
bug_type = 'Timestamp-Dependency'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'SWC_116' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0
            
    else:
        label = 2
                  

    predictions.append(label)

t = 201.1       
addResults(tool, benchmark, bug_type, y_true, predictions, t)





##################################################################
bug_type = 'Overflow-Underflow'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'SWC_101' in data: 
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0
            
    else:
        label = 2
                  

    predictions.append(label)

t = 201.1       
addResults(tool, benchmark, bug_type, y_true, predictions, t)




##################################################################
bug_type = 'tx.origin'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'SWC_115' in data: 
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0
            
    else:
        label = 2
                  

    predictions.append(label)

t = 201.1        
addResults(tool, benchmark, bug_type, y_true, predictions, t)








######################################################################################

tool = 'smartcheck'

df2 = pd.read_csv('10_tools_files/smartbugs/smartbugs_results_SolidiFI-benchmark.csv')

df2 = df2.loc[df2['toolid']==tool]
#print(df2)

tool = 'SmartCheck'



##################################################################
bug_type = 'Re-entrancy'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'SOLIDITY_CALL_WITHOUT_DATA' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0

    else:
        label = 2
                  

    predictions.append(label)
t = 5.6        
addResults(tool, benchmark, bug_type, y_true, predictions, t)



##################################################################
bug_type = 'Timestamp-Dependency'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'SOLIDITY_EXACT_TIME' in data:
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0
            
    else:
        label = 2
                  

    predictions.append(label)
t = 5.6        
addResults(tool, benchmark, bug_type, y_true, predictions, t)





##################################################################
bug_type = 'Overflow-Underflow'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'SOLIDITY_UINT_CANT_BE_NEGATIVE' in data: 
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0
            
    else:
        label = 2
                  

    predictions.append(label)
t = 5.6        
addResults(tool, benchmark, bug_type, y_true, predictions, t)




##################################################################
bug_type = 'tx.origin'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    df3 = df2.loc[df2['basename']==address+'.sol']
    #print(df3)

    if df3.shape[0] != 0:

        data = df3['findings'].values[0]
        #print(data)
        if data != '{}':

            if 'SOLIDITY_TX_ORIGIN' in data: 
                label = 1
            else:
                label = 0
                                        
        else:
            label = 0
            
    else:
        label = 2
                  

    predictions.append(label)

t = 5.6        
addResults(tool, benchmark, bug_type, y_true, predictions, t)







######################################################################################

tool = 'SoliAudit'



mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'Re-entrancy'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.md' in files:
        my_file = Path(path+tool+'/'+address+'.md')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if "_`X`_ Reentrancy" in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)
t = 5.4        
addResults(tool, benchmark, bug_type, y_true, predictions, t)


##################################################################
bug_type = 'Timestamp-Dependency'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.md' in files:
        my_file = Path(path+tool+'/'+address+'.md')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if "_`X`_ BlockTimestamp" in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)
t = 5.4       
addResults(tool, benchmark, bug_type, y_true, predictions, t)


##################################################################
bug_type = 'Overflow-Underflow'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.md' in files:
        my_file = Path(path+tool+'/'+address+'.md')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if "_`X`_ Overflow" in data: # or "_`X`_ Underflow" in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)
t = 5.4        
addResults(tool, benchmark, bug_type, y_true, predictions, t)


##################################################################
bug_type = 'tx.origin'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.md' in files:
        my_file = Path(path+tool+'/'+address+'.md')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if "_`X`_ TxOrigin" in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)
t = 5.4        
addResults(tool, benchmark, bug_type, y_true, predictions, t)













######################################################################################

tool = 'eThor'



mypath = path+tool+'/eThor_result1_/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'Re-entrancy'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

t = 0

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    theFile = ""
    for file in files:
        if file.startswith(address):
            theFile = file

            t += float(file.split(' ')[1][:-4])

            break

    if theFile != "":
        my_file = Path(path+tool+'/eThor_result1_/'+theFile)
        f = open(my_file, 'r')
        data = f.read()


        count = 0
                                
        if ' UNSATISFIABLE' in data:
            label = 0
            count += 1

        if ' SATISFIABLE' in data:
            label = 1
            count += 1
                                
        if count == 2:
            label = 1
                                    
                                
        if count == 0:
            label = 2

                                    
    else:
        label = 2
                  

    predictions.append(label)
t = 160        
addResults(tool, benchmark, bug_type, y_true, predictions, t)











######################################################################################

tool = 'Slither'


mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'Re-entrancy'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if '"success": true' in data:
            if '"check": "reentrancy-eth"' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)
t = 0.9       
addResults(tool, benchmark, bug_type, y_true, predictions, t)


##################################################################
bug_type = 'Timestamp-Dependency'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if '"success": true' in data:
            if '"check": "timestamp"' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)
t = 0.9         
addResults(tool, benchmark, bug_type, y_true, predictions, t)


##################################################################
bug_type = 'tx.origin'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if '"success": true' in data:
            if '"check": "tx-origin"' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)
t = 0.9         
addResults(tool, benchmark, bug_type, y_true, predictions, t)




######################################################################################

tool = 'ConFuzzius'


mypath = path+tool+'/'

files = [f for f in listdir(mypath) if isfile(join(mypath, f))]



##################################################################
bug_type = 'Re-entrancy'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if '"swc_id": 107' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)
t = 32.3        
addResults(tool, benchmark, bug_type, y_true, predictions, t)



##################################################################
bug_type = 'Overflow-Underflow'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if address+'.json' in files:
                    
        my_file = Path(path+tool+'/'+address+'.json')
        f = open(my_file, 'r')
        data = f.read()

        if data != "":
            if '"swc_id": 101' in data:
                label = 1
            else:
                label = 0
        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)
t = 32.3       
addResults(tool, benchmark, bug_type, y_true, predictions, t)






######################################################################################

tool = 'Sailfish'


mypath = path+tool+'/'

files = list()

for file in os.listdir(mypath):
    d = os.path.join(mypath, file)
    if os.path.isdir(d):
        files.append(d)



##################################################################
bug_type = 'Re-entrancy'
y_true = df[bug_type].values



print("*"*80)
print("\n", tool, benchmark, bug_type)
print("*"*80)

unique, counts = np.unique(y_true, return_counts=True)
print("\n", dict(zip(unique, counts)))
print("="*80)

predictions = []

for index, row in df.iterrows():
    address  = row['address']
    label = -1

    if path+tool+'/'+address in files:
        my_file = Path(path+tool+'/'+address+'/contractlint.log')
        f = open(my_file, 'r')
        data = f.read()

        if 'Analysis finished!' in data:
                    
            if 'DAO dependency detected' in data:
                label = 1
            else:
                label = 0

        else:
            label = 2
                                    
    else:
        label = 2
                  

    predictions.append(label)

tool = 'SAILFISH'

t = 3.3
addResults(tool, benchmark, bug_type, y_true, predictions, t)




######################################################################################

tool = 'DLVA'



from os import listdir
from os.path import isfile, join
files = [f for f in listdir('.') if isfile(join('.', f))]

for dlva_pred_file in files:
    if dlva_pred_file.startswith('DLVA_Predictions_for_SolidiFI_benchmark'):
        dlva_df = pd.read_csv(dlva_pred_file)

        for batch_file in files:
            if batch_file == dlva_pred_file[21:]:
                batch_df = pd.read_csv(batch_file)

                print("#"*80)
                print("\n\n\n\nDLVA results: ", dlva_pred_file, "\nGround Truth: ", batch_file)
                print("="*80)

                for vul in dlva_df.columns[1:]:
                    print("\n\nVulnerability:", vul)
                    print("*"*60)

                    if vul not in batch_df.columns:
                        print("ground truth does not exist in", batch_file)
                    else:
                         
                        y_true = batch_df[vul].values
                        predictions = dlva_df[vul].values

                        t = 0.2

                        addResults(tool, benchmark, vul, y_true, predictions, t)


dfcopy.set_index('address', inplace = True)
dfcopy.to_csv('tools_predictions_'+benchmark+'.csv')



















outdf = pd.DataFrame({
        'Tool':tool_,
        'Vulnerability':vul_,
        'tp':tp_,
        'fn':fn_,
        'fp':fp_,
        'tn':tn_,
        'TPR (detection rate)':tpr_,
        'TNR (specificity)':tnr_,
        'FPR (false alarm)':fpr_,
        'FNR (miss rate)':fnr_,
        'Accuracy':accuracy_,
        'Precision':precision_,
        'Recall':recall_,
        'F1':f1_,
        'Average time per contract':t_,
        'Exp_':exp_,
        'Exp':exp__,
        'CR':CR_
    })

outdf = outdf.fillna(0)
    
outdf.set_index('Tool', inplace = True)
        
outdf.to_csv('tools_results.csv')






os.system('clear')










import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Polygon

plt.rcParams['font.size'] = '18'

_dists = ["Oyente","Osiris", "Mythril","SmartCheck","SoliAudit","eThor","Slither","ConFuzzius","SAILFISH","DLVA"]


df = pd.read_csv('tools_results.csv')
#print(df)

cr = []
acc = []
tpr = []
fpr = []
exp = []
timeA = []
i = -1
for tool in _dists:
    i += 1
    dft = df[df['Tool']==tool]
    #print(dft)
    cr.append(dft['CR'].tolist())
    acc.append(dft['Accuracy'].tolist())
    tpr.append(dft['TPR (detection rate)'].tolist())
    fpr.append(dft['FPR (false alarm)'].tolist())
    exp.append(dft['Exp'].tolist())
    timeA.append(dft['Average time per contract'].tolist())


    _dists[i] = tool+' ('+str(dft.shape[0])+')'




#fig, (ax2, ax3, ax4, ax5) =  plt.subplots(1, 4)
fig, (ax1, ax2, ax3, ax4,ax6) =  plt.subplots(5, 1 , figsize=(14, 35))
fig.subplots_adjust(left=0.08, right=0.98, top=0.98, bottom=0.115)




data = cr

bp = ax1.boxplot(data, notch=0, sym='+', vert=1, whis=1.5 ) #, meanline=True, showmeans=True)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)


ax1.set_title('Completion Rate (higher is better)', size='x-large', weight='bold')


# Now fill the boxes with desired colors

box_colors = []
for tool in _dists:
    box_colors.append('purple')
num_boxes = len(data)
medians = np.empty(num_boxes)
means = np.empty(num_boxes)
for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax1.add_patch(Polygon(box_coords, facecolor=box_colors[i]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    #med = bp['means'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax1.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax1.plot(np.average(med.get_xdata()), np.average(data[i]),
             color='w', marker='*', markeredgecolor='k')
    means[i] = np.average(data[i])

# Set the axes ranges and axes labels
ax1.set_xlim(0.5, num_boxes + 0.5)
ax1.set_ylim(-4, 119)
ax1.set_xticklabels(_dists,
                    rotation=90, size='x-large', weight='bold')
ax1.set_xticklabels([])
ax1.set_yticklabels([-4, '0 %', '20 %', '40 %', '60 %', '80 %', '100 %'])
                    

# Due to the Y-axis scale being different across samples, it can be
# hard to compare differences in medians across the samples. Add upper
# X-axis tick labels with the sample medians to aid in comparison
# (just use two decimal places of precision)
pos = np.arange(num_boxes) + 1



upper_labels = [str(round(s, 1)) for s in means]
# weights = ['bold', 'semibold']
for tick, label in zip(range(num_boxes), ax1.get_xticklabels()):
    ax1.text(pos[tick], .92, upper_labels[tick],
             transform=ax1.get_xaxis_transform(),
             horizontalalignment= 'center', size='large', # rotation=90,
             weight='bold', color='black')



ax1.text(-0.3 , 0.92, 'Mean',transform=ax1.get_xaxis_transform(),
             horizontalalignment='left', size='large', # rotation=90,
             weight='bold', color='black')












data = acc

bp = ax2.boxplot(data, notch=0, sym='+', vert=1, whis=1.5 ) #, meanline=True, showmeans=True)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax2.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)


ax2.set_title('Accuracy (higher is better)', size='x-large', weight='bold')

# Now fill the boxes with desired colors
box_colors = []
for tool in _dists:
    box_colors.append('cornflowerblue')

num_boxes = len(data)
medians = np.empty(num_boxes)
means = np.empty(num_boxes)
for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax2.add_patch(Polygon(box_coords, facecolor=box_colors[i]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    #med = bp['means'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax2.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax2.plot(np.average(med.get_xdata()), np.average(data[i]),
             color='w', marker='*', markeredgecolor='k')
    means[i] = np.average(data[i])

# Set the axes ranges and axes labels
ax2.set_xlim(0.5, num_boxes + 0.5)
ax2.set_ylim(-4, 119)
ax2.set_xticklabels(_dists,
                    rotation=90, size='x-large', weight='bold')
ax2.set_xticklabels([])
ax2.set_yticklabels([-4, '0 %', '20 %', '40 %', '60 %', '80 %', '100 %'])

# Due to the Y-axis scale being different across samples, it can be
# hard to compare differences in medians across the samples. Add upper
# X-axis tick labels with the sample medians to aid in comparison
# (just use two decimal places of precision)
pos = np.arange(num_boxes) + 1



upper_labels = [str(round(s, 1)) for s in means]
# weights = ['bold', 'semibold']
for tick, label in zip(range(num_boxes), ax2.get_xticklabels()):
    ax2.text(pos[tick], .92, upper_labels[tick],
             transform=ax2.get_xaxis_transform(),
             horizontalalignment= 'center', size='large', # rotation=90,
             weight='bold', color='black')




ax2.text(-0.3 , 0.92, 'Mean',transform=ax2.get_xaxis_transform(),
             horizontalalignment='left', size='large', # rotation=90,
             weight='bold', color='black')









data = tpr

bp = ax3.boxplot(data, notch=0, sym='+', vert=1, whis=1.5 ) #, meanline=True, showmeans=True)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax3.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)



ax3.set_title('True Positive Rate (detection rate, higher is better)', size='x-large', weight='bold')


# Now fill the boxes with desired colors
box_colors = []
for tool in _dists:
    box_colors.append('springgreen')
num_boxes = len(data)
medians = np.empty(num_boxes)
means = np.empty(num_boxes)
for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax3.add_patch(Polygon(box_coords, facecolor=box_colors[i]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    #med = bp['means'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax3.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax3.plot(np.average(med.get_xdata()), np.average(data[i]),
             color='w', marker='*', markeredgecolor='k')
    means[i] = np.average(data[i])

# Set the axes ranges and axes labels
ax3.set_xlim(0.5, num_boxes + 0.5)
ax3.set_ylim(-4, 119)
ax3.set_xticklabels(_dists,
                    rotation=90, size='x-large', weight='bold')
ax3.set_xticklabels([])
ax3.set_yticklabels([-4, '0 %', '20 %', '40 %', '60 %', '80 %', '100 %'])

# Due to the Y-axis scale being different across samples, it can be
# hard to compare differences in medians across the samples. Add upper
# X-axis tick labels with the sample medians to aid in comparison
# (just use two decimal places of precision)
pos = np.arange(num_boxes) + 1



upper_labels = [str(round(s, 1)) for s in means]
# weights = ['bold', 'semibold']
for tick, label in zip(range(num_boxes), ax3.get_xticklabels()):
    ax3.text(pos[tick], .92, upper_labels[tick],
             transform=ax3.get_xaxis_transform(),
             horizontalalignment= 'center', size='large', # rotation=90,
             weight='bold', color='black')




ax3.text(-0.3 , 0.92, 'Mean',transform=ax3.get_xaxis_transform(),
             horizontalalignment='left', size='large', # rotation=90,
             weight='bold', color='black')








data = fpr

bp = ax4.boxplot(data, notch=0, sym='+', vert=1, whis=1.5 ) #, meanline=True, showmeans=True)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax4.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)


ax4.set_title('False Positive Rate (false alarm rate, lower is better)', size='x-large', weight='bold')

# Now fill the boxes with desired colors

box_colors = []
for tool in _dists:
    box_colors.append('red')
num_boxes = len(data)
medians = np.empty(num_boxes)
means = np.empty(num_boxes)
for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax4.add_patch(Polygon(box_coords, facecolor=box_colors[i]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    #med = bp['means'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax4.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax4.plot(np.average(med.get_xdata()), np.average(data[i]),
             color='w', marker='*', markeredgecolor='k')
    means[i] = np.average(data[i])

# Set the axes ranges and axes labels
ax4.set_xlim(0.5, num_boxes + 0.5)
ax4.set_ylim(-4, 119)
ax4.set_xticklabels(_dists,
                    rotation=90, size='x-large', weight='bold')
ax4.set_yticklabels([-4, '0 %', '20 %', '40 %', '60 %', '80 %', '100 %'])
ax4.set_xticklabels([])


                    

# Due to the Y-axis scale being different across samples, it can be
# hard to compare differences in medians across the samples. Add upper
# X-axis tick labels with the sample medians to aid in comparison
# (just use two decimal places of precision)
pos = np.arange(num_boxes) + 1



upper_labels = [str(round(s, 1)) for s in means]
# weights = ['bold', 'semibold']
for tick, label in zip(range(num_boxes), ax4.get_xticklabels()):
    ax4.text(pos[tick], .92, upper_labels[tick],
             transform=ax4.get_xaxis_transform(),
             horizontalalignment= 'center', size='large', # rotation=90,
             weight='bold', color='black')



ax4.text(-0.3 , 0.92, 'Mean',transform=ax4.get_xaxis_transform(),
             horizontalalignment='left', size='large', # rotation=90,
             weight='bold', color='black')







data = timeA

bp = ax6.boxplot(data, notch=0, sym='+', vert=1, whis=1.5 ) #, meanline=True, showmeans=True)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax6.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)


ax6.set_title('Average time per contract in seconds (log scale, lower is better)', size='x-large', weight='bold')


# Now fill the boxes with desired colors

box_colors = []
for tool in _dists:
    box_colors.append('deepskyblue')
num_boxes = len(data)
medians = np.empty(num_boxes)
means = np.empty(num_boxes)
for i in range(num_boxes):
    box = bp['boxes'][i]
    box_x = []
    box_y = []
    for j in range(5):
        box_x.append(box.get_xdata()[j])
        box_y.append(box.get_ydata()[j])
    box_coords = np.column_stack([box_x, box_y])
    # Alternate between Dark Khaki and Royal Blue
    ax6.add_patch(Polygon(box_coords, facecolor=box_colors[i]))
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    #med = bp['means'][i]
    median_x = []
    median_y = []
    for j in range(2):
        median_x.append(med.get_xdata()[j])
        median_y.append(med.get_ydata()[j])
        ax6.plot(median_x, median_y, 'k')
    medians[i] = median_y[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    ax6.plot(np.average(med.get_xdata()), np.average(data[i]),
             color='w', marker='*', markeredgecolor='k')
    means[i] = np.average(data[i])

# Set the axes ranges and axes labels
ax6.set_xlim(0.5, num_boxes + 0.5)
#ax6.set_ylim(-4, 1000)
ax6.set_xticklabels(_dists,
                    rotation=90, size='x-large', weight='bold')




                    

# Due to the Y-axis scale being different across samples, it can be
# hard to compare differences in medians across the samples. Add upper
# X-axis tick labels with the sample medians to aid in comparison
# (just use two decimal places of precision)
pos = np.arange(num_boxes) + 1



upper_labels = [str(round(s, 1)) for s in means]
# weights = ['bold', 'semibold']
for tick, label in zip(range(num_boxes), ax6.get_xticklabels()):
    ax6.text(pos[tick], .88, upper_labels[tick],
             transform=ax6.get_xaxis_transform(),
             horizontalalignment= 'center', size='large', # rotation=90,
             weight='bold', color='black')



ax6.text(-0.3 , 0.88, 'Mean',transform=ax6.get_xaxis_transform(),
             horizontalalignment='left', size='large', # rotation=90,
             weight='bold', color='black')

ax6.set_yscale('log')
ax6.set_ylim((0.0, 9999.0)) # <-- This is the key line
#ax6.plot(range(1, 1+len(means)), means, 'r')

ax6.set_yticklabels([-9, '0 s' , '1 s', '10 s', '100 s', '1,000 s'])




#ax4.set_axisbelow(True)
ax1.grid(linestyle='-', linewidth='0.5', color='red', axis='y')
ax2.grid(linestyle='-', linewidth='0.5', color='red', axis='y')
ax3.grid(linestyle='-', linewidth='0.5', color='red', axis='y')
ax4.grid(linestyle='-', linewidth='0.5', color='red', axis='y')
#ax5.grid(linestyle='-', linewidth='0.5', color='red', axis='y')
ax6.grid(linestyle='-', linewidth='0.5', color='red', axis='y')



fig.text(0.048, 0.116, '0 s')


fig.text(0.05, 0.01, 'Analyzer (# tests)', rotation=90, color='black', weight='bold',
         size='x-large')


plt.subplots_adjust(wspace=0.03, hspace=0.1)

plt.savefig("DLVA9tools.png", dpi=150)
#plt.show()

os.system('clear')

sys.stdout = stdoutOrigin

print("="*80)
print("\nFigure 1 of DLVA paper is generated as an image at dlva/DLVA9tools.png\n")

print("="*80)

print('\nOpen the “dlva folder”, seven files have been added: \n\n\t1) “tools_results.txt” contains the log performance for all tools based on raw data in “10_tools_files” folder, \n\n\t2) “tools_results.csv” represents the same results as a spreadsheet, \n\n\t3) and five files of “tools_predictions_benchmark.csv” contain labels of all tools for each benchmark.\n')

print("="*80)

print('\nThe tools_results.csv file contains the "fn" and "fp" columns which should match FN and FP of our paper Tables 4, 5 and 6. Figure 1 is generated based on these tables.\n')


print("="*80)
