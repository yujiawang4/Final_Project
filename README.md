# Title: Simulation of Waiting Time in Restaurant

## Team Member(s):
Xiaoye Li (Thursday), Pan Zhang, Yujia Wang, Yun Sun


## Monte Carlo Simulation Scenario & Purpose:

The purpose of this simulation is to examine the average waiting time for the seats in Lao Si Chuan.
Besides, help customer to schedule their time properly, so that enhance the customers’ service.

Solution:
When the restaurant is full, calculate the possible departure time of the guests in the restaurant
and sort them according to the random meal time of the previous guests.
Then based on the comparison of the current guest's arrival time and the previous time list,
obtain the waiting time.

### Simulation's variables of uncertainty:

1. Customer eating time
    - Normal distribution (30, 5^2)
2. The visiting frequency of customer groups for one night
    - Triangle distribution


### Hypothesis before running the simulation:

The average number of customer groups for one night is 350.
The opening hour is 5pm to 8pm.
The restaurant has:
20 tables of size 2 for 1~2 customers
15 tables of size 4 for 3~4 customers
 3 tables of size 8 for 5~8 customers

The possibilities of customer groups going to restaurant:
1-2 customers group: 50%
3-4 customers group: 40%
5-8 customers group: 10%

We assume the simulation running 100 times which can be revised in the code


## Analytical Summary of your findings:
1. It takes the longest waiting time around 7pm.
2. Since we assume the average number of customer groups for one night is 350, which is a large number,
it will results in the longer waiting time. Thus we may change this number in the processing.

## Instructions on how to use the program:

User input:
1. input the arriving time, for example 5:30, 7:00
2. input the table size you need

The system will output the average waiting time

## Sources Used:
https://github.com/iSchool-590PR-2018Spring/in-class-examples/blob/master/week_12_Prob_Distributions.ipynb

