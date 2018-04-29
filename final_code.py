import numpy as np

def findMinValue(list,value):
    list=sorted(list)
    for i in range(len(list)):
        if list[i] >= value:
            return i

arrive_time = input('When will you arrive our restaurant? (Between 5:00 and 10:00, e.g. 5:30)\n')
table_size = input('Which table size do you need? 2, 4, or 8? \n')
table = [2, 4, 8]
table_dict = {"2": 25, "4": 20, "8": 5}
try:
    hour_min = arrive_time.split(":")
    if (int(hour_min[0]) >= 5 and int(hour_min[0]) < 10):
        open_min = (int(hour_min[0]) - 5) * 60 + int(hour_min[1])
        all_waiting = []
        for i in range(1):  # simulation times
            startime = []
            finishtime =[]
            tri_distribution = np.sort(np.random.triangular(0, 40, 240, 300).astype(np.int))
#            print(tri_distribution)
            need_count = 0
            n_table = table_dict[str(table_size)]
            for j in range(300):
                if tri_distribution[j] < open_min:
                    table_kind = np.random.choice(table, 1, p=[0.5, 0.4, 0.1])
                    if int(table_kind[0]) == int(table_size):
                        startime.append(tri_distribution[j])
            former = len(startime)
            print(former)
            workingtime = np.random.normal(loc=30, scale=5, size=former).astype(np.int)
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
                        position = findMinValue(finishtime, startime[h])
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
                    position = findMinValue(finishtime, open_min)
                    waiting_time = finishtime[position] - open_min
                    all_waiting.append(waiting_time)
        print(all_waiting)
        average_waiting = int(sum(all_waiting) / len(all_waiting))
        print(average_waiting)
    else:
        raise ValueError('The restaurant is not open at {} .'.format(arrive_time))
except KeyError:
    print('Invalid arrive time {} given or table size {}! Please check your input.'.format(arrive_time, table_size))
