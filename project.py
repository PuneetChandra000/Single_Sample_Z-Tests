import pandas as pd
import plotly.figure_factory as pff
import statistics as st
import random

data = pd.read_csv("sample.csv")

sample = data["Math_score"].tolist()

mean = st.mean(sample)

stdev = st.stdev(sample)

print("------------------------------------------------------")

print("mean of popultion:- ", mean)
print("Standard deviation of popultion:- " , stdev)

# -------------------------------------  Sample of Population ---------------------------------------

datasetOf1000 = []

for i in range(1000):
    dataset_temp = []

    temp_mean = []
    
    for j in range(100):
        dataset_temp.append( random.choice(sample) )
        temp_mean = st.mean(dataset_temp)
        
    datasetOf1000.append(temp_mean)
    

meanSample = st.mean(datasetOf1000)
stdevSample = st.stdev(datasetOf1000)

print("------------------------------------------------------")

print("mean of sample:- ", meanSample)
print("Standard deviation of sample:- " , stdevSample)

zscore = (mean - meanSample )/stdevSample

print("-----------------")
print(zscore)
