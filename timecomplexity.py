import math
import time
import matplotlib.pyplot as plt
import numpy as np# Sample data - generating random data points using normal distribution
def generate_inputsize(start,end):
    return [2**i for i in range(start, end + 1)]
def calculatetime(n):
    j=2
    start=time.perf_counter()
    while(j<n):
        k=j 
        sum1=0
        while(k<n):
            sum1+=j+k
            k=k*k
        j=j*2
    end=time.perf_counter()
    return end-start
    
inputarray = generate_inputsize(2,50)
timetaken={}
for i in inputarray:
    timetaken[i]=calculatetime(i)
    print(f" Actual Time taken for input size {i} : {timetaken[i]:0.10f}")
theoreticalvalues={}
for i in inputarray:
    theoreticalvalues[i]=theoreticalvalues[i] = timetaken[inputarray[-1]] * (math.log2(i) * math.log2(math.log2(i))) / (math.log2(inputarray[-1]) * math.log2(math.log2(inputarray[-1])))
    print(f" Theoretical Time taken for input size {i} : {theoreticalvalues[i]:0.10f}")
    

plt.plot(inputarray,timetaken.values(), marker='o', linestyle='-', color='r',label='Actual Time')
plt.plot(inputarray,theoreticalvalues.values(),marker='x',color='b',linestyle='--',label='Theoretical log log log n')
plt.title("Time Complexity Comparison")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.legend(loc='lower right')
plt.show()