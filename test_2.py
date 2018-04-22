import numpy as np
import random


def num_update(entertime, open_time, count=-1):
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
    return int(entertime), count

arrive_time = input('When will you arrive our restaurant? (Between 5:00 and 10:00, e.g. 5:30)\n')
table_size = input('Which table size do you need? 2, 4, or 8? \n')
table = [2, 4, 8]
table_dict = {"2": 20, "4": 15, "8": 3}
try:
    hour_min = arrive_time.split(":")
    if (int(hour_min[0]) >= 5 and int(hour_min[0]) < 10):
        open_min = (int(hour_min[0]) - 5) * 60 + int(hour_min[1])
        n_sampling = int(open_min / 5)
        all_waiting = []
        for i in range(1):  # simulation times
            former = []
            startime = []
            tri_distribution = np.sort(np.random.triangular(0, 30, 240, 500).astype(np.int))
            need_count = 0
            n_table = table_dict[str(table_size)]
            table_count = n_table
            for j in range(500):
                if tri_distribution[j] < open_min:
                    table_kind = np.random.choice(table, 1, p=[0.5, 0.4, 0.1])
                    if  int(table_kind[0]) == int(table_size):
                        startime.append(tri_distribution[j])

                        time_count = num_update(tri_distribution[j], open_min)
#                        print(time_count)
                        table_count += time_count[1]
                        need_count += 1
                        if need_count > table_count:
                            former.append(time_count[0])
                        if need_count - table_count < n_table:
                        else:

            print (need_count, table_count,len(former))
            if table_count >= need_count:
                waiting_time = 0
                all_waiting.append(waiting_time)
            else:
                former.sort()
                waiting_time = former[need_count - table_count - 1] - open_min
                all_waiting.append(waiting_time)
        average_waiting = sum(all_waiting) / len(all_waiting)
        print(average_waiting)
    else:
        raise ValueError('The restaurant is not open at {} .'.format(arrive_time))
except KeyError:
    print('Invalid arrive time {} given or table size {}! Please check your input.'.format(arrive_time, table_size))
