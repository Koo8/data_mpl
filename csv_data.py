import csv
import json
import pprint
import random
from datetime import datetime
from matplotlib import pyplot as plt

file_name = 'newyorkweather.csv'
with open(file_name, 'r+') as file:
    reader = csv.reader(file)
    first_line = next(reader)  #['STATION', 'NAME', 'DATE', 'WT01', 'WT02', 'WT06', 'WT08']
    # names = []
    # counter = 0


    # print(counter)  # there are 1065 lines after the first line
    # name_set = set(names) # to list all unique name of stations
    # print(len(names))  #1065
    # print(len(name_set)) # 93
    # frequencies = []
    # for n in name_set:
    #     frequencies.append(names.count(n))
    # # print(frequencies)
    #
    # combined = zip(name_set, frequencies)
    # dic = dict(combined)

    # # pprint.pprint(dic, indent=4)
    # with open('name_station.json', 'w') as f:
    #     json.dump(dic,f, indent= 4)

    # retrieve date from the file as datetime format
    dates = []
    for n in reader:
        try:
            dates.append(datetime.strptime(n[2],'%Y-%m-%d'))
        except ValueError:
            print("wrong value input")

    # print(dates)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    # print(len(dates)) #1063
    # print([n for n in range(len(dates))])
    ax.plot(dates[:8], [n for n in range(len(dates))][:8])
    fig.autofmt_xdate()
    plt.show()
