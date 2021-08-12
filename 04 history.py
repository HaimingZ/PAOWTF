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
fields = ['gravity-based', 'jacket', 'monopile', 'tripod',
          'tripile', 'suction bucket', 'tlp', 'spar', 'semi-submersible']
years = np.arange(2000, 2019 + 1)

annual_c = pd.DataFrame()  # annual grants by country
total_c = pd.DataFrame()  # total grants by country
annual_f = pd.DataFrame()  # annual grants by field
total_f = pd.DataFrame()  # total grants by field

for y in years:

    annual_c_item = {'Year': y}
    total_c_item = {'Year': y}
    annual_f_item = {'Year': y}
    total_f_item = {'Year': y}

    for _ in countries:
        total_c_item[_] = df[(df['File Year'] <= y) &
                             (df['Country'] == _)].shape[0]
        annual_c_item[_] = df[(df['File Year'] == y) &
                              (df['Country'] == _)].shape[0]

    for _ in fields:
        total_f_item[_] = df[(df['File Year'] <= y) &
                             (df[_] == True)].shape[0]
        annual_f_item[_] = df[(df['File Year'] == y) &
                              (df[_] == True)].shape[0]

    total_c = total_c.append(total_c_item, ignore_index=True)
    annual_c = annual_c.append(annual_c_item, ignore_index=True)
    total_f = total_f.append(total_f_item, ignore_index=True)
    annual_f = annual_f.append(annual_f_item, ignore_index=True)


def draw_history(df, legends, xlabel='', ylabel='', logscale=False):

    lines = ["-", "--", "-.", ":", 'o-', 'D-', 'v-', 'x-', '*-']
    colors = ['b', 'r', 'm', 'g', 'teal',
              'orange', 'navy', 'y', 'purple', 'peru']
    linecycler = cycle(lines)
    colorcycler = cycle(colors)

    plt.figure(figsize=(8, 4))

    lines = []
    for _ in legends:
        line = plt.plot(df['Year'], df[_], next(linecycler),
                        color=next(colorcycler), label=_)
        lines.append(line[0])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(years, rotation='45')

    if logscale:
        plt.yscale('log')
        plt.legend(lines, legends,
                   frameon=False, bbox_to_anchor=(1.01, 1), loc='upper left')
        plt.subplots_adjust(left=0.12, right=0.83, top=0.98, bottom=0.22)
    else:
        plt.legend(lines, legends, frameon=False)
        plt.subplots_adjust(left=0.12, right=0.98, top=0.98, bottom=0.22)

    plt.show()


draw_history(total_c, countries,
             xlabel='Filing Year', ylabel='Total Grants', logscale=True)

draw_history(annual_c, countries,
             xlabel='Filing Year', ylabel='Annual Grants', logscale=True)

draw_history(total_f, fields,
             xlabel='Filing Year', ylabel='Total Grants')

draw_history(annual_f, fields,
             xlabel='Filing Year', ylabel='Annual Grants')
