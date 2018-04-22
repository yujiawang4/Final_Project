import numpy as np
import random

class Restaurant:
    def __int__(self, table_size, time):
        self.table_size = table_size
        self.time = time
        self.star_time = 5
        self.end_time = 10

    @staticmethod
    def num_update(entertime, open_time, count = -1):
        """
        Support the flipping of 2-digit compass directions based on simple_flip().
        Raise exception for any other strings.
        :param direction: a string 'SE', 'SW', 'NE', or 'NW'
        :ret
        """
        random.seed(10)
        while True:
            entertime += np.random.normal(loc=30, scale=5, size=1)
            count += 1
            if entertime > open_time:
                break
        return int(entertime),count

if __name__ == '__main__':
    while True:
        arrive_time = input('When will you arrive our restaurant? (Between 5:00 and 10:00, e.g. 5:30)\n')
        table_size = input('Which table size do you need? 2, 4, or 8? \n')
        table = [2, 4, 8]
        table_dict={"2":50, "4":40, "8":5}
        try:
            hour_min= arrive_time.split(":")
            if (int(hour_min[0]) >= 5 and int(hour_min[0]) < 10):
                open_min = (hour_min[0]-5)* 60 + hour_min[1]
                n_sampling = int(open_min/5)
                all_waiting=[]
                for i in range(100):   # simulation times
                    former=[]
                    tri_distribution = np.random.triangular(0, 30, 240, 480).astype(np.int)
                    need_count = 0
                    for j in range(480):
                        table_count=table_dict[str(table_size)]
                        if tri_distribution[j] < open_min:
                            table_kind = np.random.choice(table,1, p=[0.5,0.4,0.1])
                            if int(table_kind[0]) == int(table_size):
                                time_count = Restaurant.num_update(tri_distribution[j],open_min)
                                former.append(time_count[0])
                                table_count += time_count[1]
                                need_count =+ 1
                    if table_count >= need_count:
                        waiting_time=0
                        all_waiting.append(waiting_time)
                    else:
                        former.sort()
                        waiting_time = former[need_count-table_count-1] - open_min
                        all_waiting.append(waiting_time)
                average_waiting= sum(all_waiting)/len(all_waiting)
                print(average_waiting)
            else:
                raise ValueError('The restaurant is not open at {} .'.format(arrive_time))
        except KeyError:
                print('Invalid arrive time {} given or tale size {}! Please check your time.'.format(arrive_time,table_size))






