# Title: Simulation of Waiting Time in Restaurant

## Team Member(s):
Xiaoye Li (Thursday), Pan Zhang, Yujia Wang, Yun Sun


## Monte Carlo Simulation Scenario & Purpose:

The purpose of this simulation is to examine the expected waiting time of the seats for different groups of people.
Besides, help customer to schedule their time properly, so that enhance the customers’ service.

Solution:
When the restaurant is full, calculate the possible departure time of the guests in the restaurant
and sort them according to the random meal time of the previous guests.
Then based on the comparison of the current guest's arrival time and the previous time list,
obtain the waiting time.

### Simulation's variables of uncertainty:

1. Customer eating time
    - Normal distribution (30, 5^2) for 2 customers
    - Normal distribution (40, 5^2) for 4 customers
    - Normal distribution (60, 5^2) for 8 customers
2. The visiting frequency of customer groups for one night
    - Triangular distribution


### Hypothesis before running the simulation:

1. The average number of customer groups for one night is 300.
2. The opening hour is 5pm to 9pm.
3. The restaurant has:
  - 25 tables of size 2 for 1 to 2 customers; 
  - 27 tables of size 4 for 3 to 4 customers; 
  - 5 tables of size 8 for 5 to 8 customers.
4. The possibilities of customer groups going to restaurant: 
  - 1 to 2 customers group: 50%; 
  - 3 to 4 customers group: 45%; 
  - 5 to 8 customers group: 5%.
5. We assume a group of customers as one unit.
6. We assume the simulation running 1000 times which can be revised in the code.


## Analytical Summary of your findings:
1. It takes the longest waiting time around 7pm.
2. Different day of week has different total number of customer groups during the whole opening time.
   And the mode of customer groups' arriving time is different as well.


## Instructions on how to use the program:

1. User input:
 - input the arriving time, for example 5:30, 7:00
 - input the table size you need
 - input specific times you want to simulate
 - input specific day of week


2. Output:
 - The system will output the min, max and average waiting time

## Sources Used:
https://github.com/iSchool-590PR-2018Spring/in-class-examples/blob/master/week_12_Prob_Distributions.ipynb

