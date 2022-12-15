#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

banking = pd.read_csv("nayaone_loan_data 181122.csv")
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
banking.head(100)

#1 Find overall average income as well as avg income of different employee lengths
ann_avg_inc = sum(banking["annual_income"])/len(banking)
ann_avg_inc_10 = sum(banking.loc[banking["emp_length"]>=10.0]["annual_income"])/len(banking.loc[banking["emp_length"]>=10.0]["annual_income"])
ann_avg_inc_1 = sum(banking.loc[banking["emp_length"]==1.0]["annual_income"])/len(banking.loc[banking["emp_length"]==1.0]["annual_income"])

#2 Find the average income of individuals who have been late on fees
late_fees = banking.loc[banking["paid_late_fees"]>0.0]
late_fees_avg_inc = sum(late_fees["annual_income"])/len(late_fees)
bankruptcy = banking.loc[banking["public_record_bankrupt"]>0]
bankruptcy_late_fees = bankruptcy.loc[banking["paid_late_fees"]>0.0]
#The total percentage of late penalty fees incurred by previously bankrupt individuals / late fees incurred by everyone
bankruptcy_higher_rate = (len(bankruptcy_late_fees)/len(bankruptcy))/(len(late_fees)/len(banking))

#3 Percentage of Individuals who do not have a sourced income
non_verified = (len(banking.loc[banking["verified_income"]=="Not Verified"])/len(banking))*100

#4 25 or more open credit lines - debt to income average compared to overall average.
open_credit_25 = banking.loc[banking["open_credit_lines"]>=25]
dti_opencredit = sum(open_credit_25["debt_to_income"])/len(open_credit_25)
#removed 24 rows due to NaN values in debt to income column
#possible other methods, fill in with mean, fill in with Ml algorithm
debt_to_income_overall = banking["debt_to_income"].dropna()
dti_average = sum(debt_to_income_overall)/len(debt_to_income_overall)
percentage_higher_dti = ((dti_opencredit/dti_average)-1)*100

#5 Highest earning states
states = set(banking["state"].tolist())
state_incomes = []
for state in states:
    income = banking.loc[banking["state"]==state]["annual_income"]
    state_incomes.append([state,(sum(income)/len(income))])


