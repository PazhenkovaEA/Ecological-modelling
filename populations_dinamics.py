#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:38:10 2018

"""

#import libraries and input data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
input_data = pd.read_table("/Users/irina/Desktop/input.csv", header = None, delimiter=" ")

#set main parameters 
cycles = 30
runs = 500

output_1 = {}
output_2 = {}

for n in range(runs):
    matrix = np.zeros((len(input_data), len(input_data))) #Creating the Leslie matrix
    for m in range(2,6): #Initialization of fecundity for each age in this run
        matrix[0,m] = np.random.uniform(low = float(input_data[2][m].split('-')[0]), high = float(input_data[2][m].split('-')[1]))
        parameters = list(matrix[0, 2:6])
    for m in range(1,6): #Initialization of survival rate for each age in this run
        matrix[m, m-1] = np.random.uniform(low = float(input_data[3][m-1].split('-')[0]), high = float(input_data[3][m-1].split('-')[1]))
        parameters.append(matrix[m, m-1])
    output_2[n+1] = parameters #Saving the parameters of the run
    initial_n = np.array(input_data[1]) #Initial number of individuals in each age category
    for c in range(cycles): #Iteranion on reproduction cycles
        initial_n = matrix.dot(initial_n)
        output_1[n+1, c+1] = list(initial_n) #Saving number of run, number of cycle and population size for each age class
#Write output to csv        
outp1 = pd.DataFrame.from_dict(output_1, orient = "index")
outp1.columns = ["0", "1", "2", "3", "4", "5"]
outp1.to_csv("output1.csv", index_label = "(run, cycle)")
outp2 = pd.DataFrame.from_dict(output_2, orient = "index")
outp2.columns = ["F2", "F3", "F4", "F5", "S0", "S1", "S2", "S3", "S4"] 
outp2.to_csv("output2.csv", index_label = "run")

#calculate mean for each group per cycle
outp1["cycles"] = [i[1] for i in list(outp1.index)]
mean_size = outp1.groupby("cycles").mean()
mean_size["all"] = mean_size.apply(lambda x: sum(x), axis=1)



plt.figure(figsize=(18, 16))
colors = ["red", "wheat", "blue", "pink", "lightgreen", "goldenrod", "black"]
for n in range(0,15000,30):
    plt.plot(np.arange(0,30),outp1.iloc[n:n+30, 0:6].apply(lambda x: sum(x), axis=1), color = "black", alpha = 0.01, label = None)
    for m in range(6):
        plt.plot(np.arange(0,30), outp1.iloc[n:n+30, m], color = colors[m], alpha = 0.01, label = None) 
colors1 = ["red", "yellow", "navy", "magenta", "green", "orange", "black"]
for m in range(7):
    plt.plot(np.arange(0,30), mean_size.iloc[:,m], ':', linewidth=5.0, color = colors1[m])




labels = ["Age " + str(a) for a in range(6)]
labels.append("All")
lables = [mpatches.Patch(color = c, label = l) for c, l in zip(colors, labels)]
plt.legend(handles=lables, fontsize = 15)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.xlabel("cycle number", fontsize = 20)
plt.ylabel("population size",  fontsize = 20)
plt.title("Population dynamics",  fontsize = 32)
plt.savefig('population.png', bbox_inches='tight')

