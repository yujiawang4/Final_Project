import numpy as np

class Sim:
    def __init__(self,table,table_dict,arrivetime,table_size,day):
        """
        The constructor function of the Sim class, initialize the instance of the
        Sim class.

        :param table: a list that contain the table kind
        :param table_dict: a dictionary that with the table kind as key
        the number of that kind as value
        :param arrivetime: the arrival time of the customer
        :param table_size: the number of party of customer
        :param day: which day customer want to simulate
        """

        self.table=table
        self.table_dict=table_dict
        self.arrivetime=arrivetime
        self.table_size=table_size
        self.day=day


    def findMinValue(self, list, value):
        """
        This function will find the MINIMUM value that
        is greater than a given value

        :param list: a list that we want to search
        :param value: the value we use to compare
        :return: then, will return the position in the list of that minimum value
        """

        list = sorted(list)
        for i in range(len(list)):
            if list[i] >= value:
                return i

    def computDistribution(self,day):
        """
        Compute the distribution of a given day
        :param day: input is the day, ex. Monday, Tuesday
        :return: return an array of distribution of arrival time  of other customer
        """


        if day==1:
            #This methond generate the triangular distribution
            return np.sort(np.random.triangular(0, 40, 240, 250).astype(np.int))
        elif day==2:
            return np.sort(np.random.triangular(0, 30, 240, 350).astype(np.int))
        elif day==3:
            return np.sort(np.random.triangular(0, 35, 240, 350).astype(np.int))
        elif day==4:
            return np.sort(np.random.triangular(0, 30, 240, 368).astype(np.int))
        elif day==5:
            return np.sort(np.random.triangular(0, 40, 240, 500).astype(np.int))
        elif day==6:
            return np.sort(np.random.triangular(0, 30, 240, 450).astype(np.int))

    def simulation(self,time):
        """
        Simulate the waiting time
        :param time: this is the number of simulation user want to have
        :return:
        """
        work_dict = {"2": 30, "4": 40, "8": 60}
        hour_min = self.arrivetime.split(":")
        if (int(hour_min[0]) >= 5 and int(hour_min[0]) < 10):
            open_min = (int(hour_min[0]) - 5) * 60 + int(hour_min[1])
            all_waiting = []
            for i in range(time):  # simulation times
                startime = []
                finishtime =[]
                tri_distribution = self.computDistribution(self.day)
#            print(tri_distribution)
                need_count = 0
                n_table = self.table_dict[str(self.table_size)]
                for j in range(len(tri_distribution)):
                    if tri_distribution[j] < open_min:
                        table_kind = np.random.choice(table, 1, p=[0.5, 0.45, 0.05])
                        if int(table_kind[0]) == int(self.table_size):
                            startime.append(tri_distribution[j])
                former = len(startime)
                #print(former)
                workingtime = np.random.normal(loc=work_dict[str(table_size)], scale=5, size=former).astype(np.int)
                if former < n_table:
                    waiting_time = 0
                    all_waiting.append(waiting_time)
                elif former >= n_table:
                    for k in range(n_table):
                        finish=startime[k]+ workingtime[k]
                        finishtime.append(finish)
                    for h in range(n_table, former):
                        finishtime.sort()
                        if (max(finishtime) <= startime[h]):
                            finishtime = []
                            new_finish = startime[h] + workingtime[h]
                            finishtime.append(new_finish)
                        elif ( max(finishtime) > startime[h] and min(finishtime) <= startime[h]):
                            position = self.findMinValue(finishtime, startime[h])
                            new_finish = startime[h] + workingtime[h]
                            del finishtime[:position+1]
                            finishtime.append(new_finish)
                        elif (len(finishtime) == n_table and min(finishtime) > startime[h]):
                            new_finish= finishtime[0] + workingtime[h]
                            del finishtime[0]
                            finishtime.append(new_finish)
                        elif (len(finishtime) < n_table and min(finishtime) > startime[h]):
                            new_finish = startime[h] + workingtime[h]
                            finishtime.append(new_finish)
                    finishtime.sort()
                    if len(finishtime) < n_table or min(finishtime) <= open_min :
                        waiting_time = 0
                        all_waiting.append(waiting_time)
                    elif min(finishtime) > open_min:
                        position = self.findMinValue(finishtime, open_min)
                        waiting_time = finishtime[position] - open_min
                        all_waiting.append(waiting_time)
            print(all_waiting)
            average_waiting = int(sum(all_waiting) / len(all_waiting))
            print("The max waiting time is ",max(all_waiting))
            print("The average waiting time is ",average_waiting)
            print("The minimum waiting time is ",min(all_waiting))



while True:

    arrive_time = input('When will you arrive our restaurant? (Between 5:00 and 9:00, e.g. 5:30)\n')
    try:
        hour_min = arrive_time.split(":")
        if not (int(hour_min[0]) >= 5 and int(hour_min[0]) < 9):
            print("please enter valid time")
        else:
            break

    except:
        print("Please enter valid time")

while True:

    table_size = eval(input('Which table size do you need? 2, 4, or 8? \n'))
    if table_size not in [2,4,8]:
        print("please enter valid table size")
    else:
        break

numberOfSim=eval(input("How many times of simulations do you want? \n"))

while True:

    day=int(input("Which day do you want to simulate:? \n 1.Monday\n 2.Tuesday\n 3.Wednesday\n 4.Thursday\n 5.Friday\n 6.Saturday"))
    if not(int(day)>=1 and int(day)<7 ):
        print("Please enter valid number to choose your day")
    else:
        break
table = [2, 4, 8]
table_dict = {"2": 25, "4": 27, "8": 5}
simRestaurant=Sim(table,table_dict,arrive_time,table_size,day)
simRestaurant.simulation(numberOfSim)
