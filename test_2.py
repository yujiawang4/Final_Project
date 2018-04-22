import numpy as np

def findMinValue(list,value):
    list=sorted(list)
    for i in range(len(list)):
        if list[i]>value:
            return i

arrive_time = input('When will you arrive our restaurant? (Between 5:00 and 10:00, e.g. 5:30)\n')
table_size = input('Which table size do you need? 2, 4, or 8? \n')
table = [2, 4, 8]
table_dict = {"2": 20, "4": 15, "8": 3}
try:
    hour_min = arrive_time.split(":")
    if (int(hour_min[0]) >= 5 and int(hour_min[0]) < 10 and int(hour_min[1]) < 60):
        open_min = (int(hour_min[0]) - 5) * 60 + int(hour_min[1])
        all_waiting = []
        for i in range(1000):  # simulation times
            startime = []
            finishtime = []
            tri_distribution = np.sort(np.random.triangular(0, 30, 240, 350).astype(np.int))
#            print(tri_distribution)
            need_count = 0
            n_table = table_dict[str(table_size)]
            table_count = n_table
            for j in range(350):
                if tri_distribution[j] < open_min:
                    table_kind = np.random.choice(table, 1, p=[0.5, 0.4, 0.1])
                    if  int(table_kind[0]) == int(table_size):
                        startime.append(tri_distribution[j])
            former = len(startime)
            workingtime = np.random.normal(loc=30, scale=5, size=former).astype(np.int)
            if former <= n_table:
                waiting_time = 0
                all_waiting.append(waiting_time)
            elif former > n_table:
                for k in range(n_table):
                    finish=startime[k]+ workingtime[k]
                    table_count += 1
                    finishtime.append(finish)
                for h in range(n_table, former):
                    finishtime.sort()
                    if max(finishtime) < tri_distribution[h]:
                        finishtime = []
                        new_finish = tri_distribution[h]+ workingtime[h]
                        finishtime.append(new_finish)
                    elif max(finishtime) > tri_distribution[h]:
                        position = findMinValue(finishtime, tri_distribution[h])
                        del finishtime[:position+1]
                        new_finish = finishtime[position] + workingtime[h]
                        finishtime.append(new_finish)
            finishtime.sort()
            if max(finishtime) < open_min:
                waiting_time = 0
                all_waiting.append(waiting_time)
            else:
                position = findMinValue(finishtime, open_min)
                waiting_time = finishtime[position] - open_min
                all_waiting.append(waiting_time)
        average_waiting = sum(all_waiting) / len(all_waiting)
        print(all_waiting)
        print(int(average_waiting))
    else:
        print ('The restaurant is not open at {}.'.format(arrive_time))
        raise ValueError
except KeyError:
    print('Invalid arrive time {} given or table size {}! Please check your input.'.format(arrive_time, table_size))
