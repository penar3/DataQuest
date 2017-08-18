#Ruben Pena
#Data Analysis with Pandas: Intermediate Course
	#Challenge: Summarizing Data
#8/17/2017
#Data found at https://github.com/fivethirtyeight/data/tree/master/college-majors
#The Dataset
import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages.head(5))
print(recent_grads.head(5))

#Summarizing Major Categories
# Unique values in Major_category column.
print(all_ages['Major_category'].unique())
aa_cat_counts = dict()
rg_cat_counts = dict()

def tot_major_cat(df):
    categories = df["Major_category"].unique()
    ct_dict = dict()
    
    for x in categories:
        majors = df[df["Major_category"] == x]
        tot = majors["Total"].sum()
        ct_dict[x] = tot
    return ct_dict

aa_cat_counts = tot_major_cat(all_ages)
rg_cat_counts = tot_major_cat(recent_grads)

#Low-wage Job Rates
low_wage_percent = 0.0
low_wage_jobs = recent_grads["Low_wage_jobs"].sum()
totals = recent_grads["Total"].sum()
low_wage_percent = low_wage_jobs/totals
print(float(low_wage_percent))

#Comparing Data Sets
# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0
for x in majors:
    rg_maj_row = recent_grads[recent_grads["Major"] == x]
    aa_maj_row = all_ages[all_ages["Major"] == x]
    
    rg_ur = rg_maj_row.iloc[0]["Unemployment_rate"]
    aa_ur = aa_maj_row.iloc[0]["Unemployment_rate"]
    
    if rg_ur < aa_ur: 
        rg_lower_count += 1
print(rg_lower_count)

#

