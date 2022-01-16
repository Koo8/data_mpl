import csv
import matplotlib.pyplot as plt
from datetime import datetime
from plotly.graph_objs import Scatter
from plotly import offline
import plotly.express as px
import pandas as pd

# date = datetime.strptime('July,09,2019','%B,%d,%Y').strftime('%Y-%m-%d')
# print(date)

filename = 'stika.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header = next(reader)
    # print(header)
    highs, lows, dates = [],[],[]
    for row in reader:
        current_date = dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        try:
            highs.append(int(row[4]))
        except ValueError as e:
            print(f'{e} for high at {current_date} ')
            highs.append(0)

        try:
            lows.append(int(row[5]))
        except ValueError as e:
            print(f'{e} for low at {current_date} ')
            lows.append(0)

    # fig = Scatter(dates, highs)
    # fig2 = Scatter(dates,highs)
    # offline.plot(fig)
    # offline.plot(fig2)
    fig = px.line(dates,highs)
    # fig.add_hline(lows)
    fig.show()



# with open(filename) as f:
#     reader = csv.reader(f)
#     #IMPORTANT read the title to keep the title away from the data below
#     header = next(reader)
#     # get high temp and date, reader can only be read for once from top to bottom
#     highs, dates, lows = [],[], []
#     for row in reader:
#         current_date  = datetime.strptime(row[2],'%Y-%m-%d')
#         try:
#             high = int(row[4])
#             low = int(row[5])
#         except ValueError:
#             print(f'missing data for {current_date}')
#             # high = 0
#             # low = 0
#
#         highs.append(high)
#         lows.append(low)
#         dates.append(current_date)
#
#     # plot high temperatures
#     plt.style.use('seaborn')
#     fig, ax = plt.subplots(figsize= (8,4), dpi=128)
#     ax.plot(dates,highs,c='red', alpha=0.5)
#     ax.plot(dates, lows,c='blue', alpha=0.5)
#     plt.fill_between(dates, highs, lows, facecolor='blue', alpha =0.1)
#     plt.title('Daily high tem, July 2018', fontsize=14)
#     plt.xlabel('', fontsize = 8)
#     #rotate the xdate label
#     fig.autofmt_xdate()
#     plt.ylabel('Temperature(F)', fontsize=8)
#     plt.tick_params(axis='both', labelsize=10, color="red")
#
#
#     plt.show()




# for index, column in enumerate(header):
#     print(f'{{{index}:"{column}"}}')


