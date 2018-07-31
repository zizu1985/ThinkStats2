"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'code'))
print(sys.path)

import nsfg
import thinkstats2

def ReadFemFile(dct='2002FemResp.dat.gz',file='2002FemResp.dat.gz'):
    """ Read source file with dictionary. Return pandas.DataFrame """
    dct = thinkstats2.ReadStataDct(dct)
    df = dct.ReadFixedWidth(filename=file,compression='gzip')
    return df

def ValidatePregnum(dctpreg,dctresp,pregfile,respfile):
    """ Validate preg and resp in term of pregnum"""
    preg = ReadFemFile(dctpreg, pregfile)
    resp = ReadFemFile(dctresp, respfile)
    # caseid -> list
    m = nsfg.MakePregMap(preg)
    # Iterate over map keys
    for caseid in m:
        pregnumFromPreg = len(m[caseid])
        pregnumFromResp = list(resp[resp.caseid==caseid].pregnum)[0]
        assert pregnumFromResp == pregnumFromPreg
        #print("Resp value : {0} , Preg value : {1}".format(pregnumFromResp,pregnumFromPreg))


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
    df = ReadFemFile(dct='2002FemResp.dct', file='2002FemResp.dat.gz')
    print(df.pregnum.value_counts())
    filter = df['pregnum'] > 6
    print("7+ : {0}".format(df.loc[filter, 'pregnum'].count()))
    ValidatePregnum(dctpreg='2002FemPreg.dct',dctresp='2002FemResp.dct',pregfile='2002FemPreg.dat.gz',respfile='2002FemResp.dat.gz')