#!/usr/bin/env python3

import os
from pyrameters import PRM

def check_nopts(prm, N):
    nopts = len(prm.get_options().keys())
    assert nopts == N, \
        'Missing or extra options introduced. <%d != %d>'%(nopts,N)

def check_nsecs(prm, N):
    nsec = len(prm.get_subsections().keys())
    assert nsec == N, \
        'Missing or extra subsections introduced. <%d != %d>'%(nsec,N)

if __name__ == '__main__':
    testdir = os.path.dirname(os.path.realpath(__file__))
    inputfile = os.path.join(testdir,'testmodel.prm')
    with open(inputfile,'r') as input:
        prm_text = input.read()
        prm = PRM(prm_text)

    check_nopts(prm, 21)
    prm['Foobar'] = 'BAZ'
    check_nopts(prm, 22)

    check_nsecs(prm, 4)
    prm.set('/foOO0/bar/baz/buzz', 15)
    check_nsecs(prm, 5)

    #prmstr = str(prm)
