"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2
import collections
import nsfg
import numpy as np


def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.

    group1: Series or DataFrame
    group2: Series or DataFrame

    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    if hist is not None:
        highest = hist.Smallest(1)[0][0]
        highest_freq = hist.Smallest(1)[0][1]
        for key, freq in hist.Items():
            if freq > highest_freq:
                highest_freq = freq
                highest = key
        return highest
    else:
        return -1


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """

    # posortować słownik malejąco po wartosci
    sorted_hist = collections.OrderedDict(sorted(hist.Items(), key=lambda t: t[1], reverse=True))
    return [(v, k) for v, k in sorted_hist.items()]


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)
    compare_weight()


def compare_weight(dct="2002FemPreg.dct", datafile="2002FemPreg.dat.gz"):
    """ Compare weigth for first children and other """
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    first_babies = live[live.birthord == 1]
    others = live[live.birthord != 1]
    d = CohenEffectSize(first_babies.totalwgt_lb, others.totalwgt_lb)
    print("Weight first vs others: {0}".format(d))


if __name__ == '__main__':
    main(*sys.argv)
