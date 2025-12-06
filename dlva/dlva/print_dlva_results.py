#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: DLVA Tool
"""
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import sklearn.metrics

from os import listdir
from os.path import isfile, join
files = [f for f in listdir('.') if isfile(join('.', f))]

for dlva_pred_file in files:
    if dlva_pred_file.startswith('DLVA_Predictions_for_'):
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

            
                        print('confusion_matrix')
                        tn, fp, fn, tp = sklearn.metrics.confusion_matrix(y_true, predictions).ravel()
                
                        
                        print("\t TP:", tp)
                        print("\t TN:", tn)
                        print("\t FN:", fn)
                        print("\t FP:", fp)
                
                        
                
                        
                
                                            
                        print("-"*60)
                        Accuracy = (tp + tn)/(tp + fp + tn +fn)
                        print("\t Accurcy:", round(Accuracy*100, 1))
                                    
                        print("-"*60)
                                            
                        print("\t TPR (detection rate):  {:0.1f}\t%".format( tp/(tp+fn)*100 ))
                        TPR = round( tp/(tp+fn)*100 , 1 )
                                        
                        print("\t FPR (false alarm):     {:0.1f}\t%".format( fp/(fp+tn)*100 ))
                        FPR = round( fp/(fp+tn)*100 , 1 )
                                
                        print("\t TNR (specificity):     {:0.1f}\t%".format( tn/(fp+tn)*100 ))
                        TNR = round( tn/(fp+tn)*100 , 1 )
                            
                        print("\t FNR (miss rate):       {:0.1f}\t%".format( fn/(tp+fn)*100 ))
                        FNR = round( fn/(tp+fn)*100 , 1 )
                                    
                        print("-"*60)
                                    
                        precision = sklearn.metrics.precision_score(y_true, predictions, average='weighted')
                        recall = sklearn.metrics.recall_score(y_true, predictions, average='weighted')
                        f1 = sklearn.metrics.f1_score(y_true, predictions, average='weighted')

                        print("\t Precision:             {:0.1f}\t%".format( precision*100 ))
                        print("\t Recall:                {:0.1f}\t%".format( recall*100 ))
                        print("\t F1:                    {:0.1f}\t%".format( f1*100 ))
                                    
                
                        print("-"*60)
                                    
                        print('classification_report (specificity,sensitivity,f1)')
                        print(sklearn.metrics.classification_report(y_true, predictions))
                        
print("#"*80)
print("Done!")
                        
                
