import os
from itertools import cycle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# plot style
plt.rc('font', size=16)                    # controls default text sizes
plt.rc('axes', titlesize=16)               # fontsize of the axes title
plt.rc('axes', labelsize=16)               # fontsize of the x and y labels
plt.rc('xtick', labelsize=14)              # fontsize of the tick labels
plt.rc('ytick', labelsize=14)              # fontsize of the tick labels
plt.rc('legend', fontsize=14)              # legend fontsize
plt.rc('figure', titlesize=18)             # fontsize of the figure title
plt.rc('lines', linewidth=0.8)             # line width
plt.rc('axes', labelpad=5)                 # fontsize of the x and y labels
plt.rc('font', family='Source Serif Pro')  # font family of normal text
plt.rc('mathtext', fontset='cm')           # font family of math equation


# read data

datapath = os.path.dirname(__file__)
df = pd.read_csv(datapath + '/data/data_processed.csv')


# statistics

countries = ['CN', 'EP', 'US', 'KR', 'WO', 'JP', 'DE', 'GB']
years = np.arange(2000, 2019 + 1)


# hhi
hhi_data = pd.DataFrame()

for y in years:

    hhi_data_item = {'Year': y}

    df_y = df[(df['File Year'] <= y)]

    for c in countries:

        df_c = df_y[df_y['Country'] == c]

        a = df_c['Normalized Assignee'].value_counts()
        try:
            hhi = sum((b/a.sum())**2 for b in a)
        except ZeroDivisionError:
            hhi = 1

        hhi_data_item[c] = hhi

    hhi_data = hhi_data.append(hhi_data_item, ignore_index=True)


lines = ["-", "--", "-.", ":", 'o-', 'D-', 'v-', 'x-', '*-']
linecycler = cycle(lines)

colors = ['b', 'r', 'm', 'g', 'teal', 'orange', 'navy', 'y', 'purple', 'peru']
colorcycler = cycle(colors)


plt.figure(figsize=(8, 4))

lines = []
for _ in countries:
    line = plt.plot(hhi_data['Year'], hhi_data[_], next(linecycler),
                    color=next(colorcycler), label=_)
    lines.append(line[0])

plt.legend(lines, countries, frameon=False, bbox_to_anchor=(1.01, 1), loc='upper left')
plt.xlabel('Year')
plt.ylabel('HHI')
plt.yscale('log')
plt.xticks(years, rotation='45')
plt.subplots_adjust(left=0.12, right=0.83, top=0.98, bottom=0.22)
plt.show()
