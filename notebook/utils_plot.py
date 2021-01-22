import os

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF

pd.set_option('max_colwidth', 10000)

colors = {'red': '#e41a1c', 'blue': '#377eb8',
          'green': '#4daf4a', 'grey': '#404040'}


plt.rcParams["figure.figsize"] = [8.5, 4.5]

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Clear Sans'

plt.style.use('fivethirtyeight')

plt.rcParams['axes.linewidth'] = 1

plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False

plt.rcParams['grid.linestyle'] = '--'

plt.rcParams['ytick.color'] = '#333333'
plt.rcParams['xtick.color'] = '#333333'

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

plt.rcParams['axes.edgecolor'] = '#333333'

plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['savefig.facecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'

plt.rcParams['xtick.major.size'] = 12
plt.rcParams['xtick.minor.size'] = 8
plt.rcParams['ytick.major.size'] = 12
plt.rcParams['ytick.minor.size'] = 8

plt.rcParams['xtick.major.pad'] = 15
plt.rcParams['ytick.major.pad'] = 15

plt.rcParams['axes.grid.which'] = 'major'

plt.rcParams['font.size'] = 20

plt.rcParams['lines.linewidth'] = 4

plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18

pd.set_option('precision', 8)


def create_dir(path):
    os.makedirs(path, exist_ok=True)


def to_english_number_format(x, precision=0):
    msk = '{:,.%df}' % precision
    return msk.format(x)


def autolabel(rects, precision=4, fontsize=None):
    """
    Attach a text label above each bar displaying its height
    """
    msk = '{:,.%df}' % precision
    for rect in rects:
        height = rect.get_height()
        if height == 0:
            continue
        plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                 msk.format(height),
                 ha='center', va='bottom', color='#333333', fontsize=fontsize)


def autolabel_bkp(rects, precision=4):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        if height == 0:
            continue
        plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                 f'%.{precision}f' % float(height),
                 ha='center', va='bottom', color='#333333')


def plot_cdf(data, x_label='', y_label='', log=False, interval=None,
             color=None, ax=None, label=None,
             linewidth=None, style='-', alpha=1, y_lim=[0, 1], marker=None, markersize=None):
    if not ax:
        fig, ax = plt.subplots(nrows=1)
    ecdf = ECDF(data)
    ax.plot(ecdf.x, ecdf.y, '-', color=color, label=label,
            linewidth=linewidth, linestyle=style, alpha=alpha, marker=marker, markersize=markersize)
    ax.set_ylim(y_lim)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    if interval:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(interval))
    if log:
        ax.set_xscale('log')
    return ax


def cum_dist(data, x, y, logy=False, logx=False, style='-',
             density=False, filename=None, label=None, ax=None,
             linewidth=None, color=None, x_major_interval=None, x_minor_interval=None, title='',
             marker=None, markersize=None):
    value = data.sum() if density else 1
    ax = (data/value).cumsum().plot(ax=ax, drawstyle='steps',
                                    style=style, label=label, linewidth=linewidth, color=color, marker=None, markersize=None)
    ax.set_xlabel(x['label'])
    ax.set_ylabel(y['label'])
    plt.grid(which='major', axis='both', linestyle='--')
    plt.grid(which='minor', axis='both', linestyle=':')
    plt.xticks(rotation=0, ha="center")
    if x_minor_interval:
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(x_minor_interval))
    if x_major_interval:
        ax.xaxis.set_major_locator(ticker.MultipleLocator(x_major_interval))

    if density:
        ax.set_ylim([0, 1])
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(.1))
    if label:
        plt.legend()
    if logy:
        ax.set_yscale('log')
    if logx:
        ax.set_xscale('log')
    plt.title(title)
    return ax


def plot_scatter(x, y, x_label='', y_label='', log_x=False, log_y=False,
                 color=None, ax=None, label=None, alpha=1, marker=None, size=None):

    ax = plt.scatter(x, y, alpha=alpha, label=label,
                     marker=marker, s=size, color=color)

    ax = plt.gca()

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.grid(which='major', axis='both', linestyle='--')
    plt.grid(which='minor', axis='both', linestyle=':')

    if log_x:
        ax.set_xscale('log')
    if log_y:
        ax.set_yscale('log')

    return ax
