#!/usr/bin/env python
# coding: utf-8

# In[371]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#**TASK ONE**

#1a) The average annual income for an employee length of >=10 years is 90,728.00 while the 
#average annual income for an employee length of 1 year is 74,006.87, Overall average = 79222.148.

#b) The average individual who has incurred late fees generates an average income of 74203, considerably lower than
#the overall average. Invididuals who have declared bankruptcy are 25% more likely to have incurred late penalty fees.

#c)Approximately 36% of inividuals do not have a verified income.

#d)Individuals with a minimum of 25 open credit lines have an approximate 23% larger debt-to-income figure than
#the overall average.

#e)DC, Maryland & California are the states with the highest annual incomes, while South Dakota is the lowest.

#**TASK TWO**


class Calculation():
    
    def __init__(self,path):
        self.dataset = pd.read_csv(path)
    
    def stdDev(self, column):
        return(self.dataset[column].std())
        
    def mean(self, column):
        return(self.dataset[column].mean())
    
    def outliers(self):
        #empty Dataframe for outliers
        outliers_df = pd.DataFrame()
        
        #Identify numerical columns for Z-score
        numerical_columns = self.dataset.select_dtypes(include=["int", "float"]).columns
        
        #Z-score threshold
        z_thresh = 3
        #Non-numerical column values threshold - set to 0 due to this specific dataset
        v_thresh = 0
        
        for column in self.dataset.columns:
            if column in numerical_columns:
                #Z-score = (X-mean)/std 
                z_scores = np.abs((self.dataset[column] - self.mean(column)) / self.stdDev(column))
                outliers_possible = self.dataset[z_scores > z_thresh]
                outliers_df = outliers_df.append(outliers_possible)
                
            else:
                #for non-numerical values = outliers are chosen when a value is less than the value threshold
                #i.e It has only appeared < X amount of times. 
                #Process for this specific dataset is not ideal as "employee title" has very unique values. 
                counts = self.dataset[column].value_counts()
                outliers_possible = self.dataset[self.dataset[column].isin(counts[counts <= v_thresh].index)]
                outliers_df = outliers_df.append(outliers_possible)
        
        outliers_df.drop_duplicates(inplace=True)
        #return the series of outliers in list form
        return outliers_df.values.tolist()



