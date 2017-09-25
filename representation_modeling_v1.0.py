'''
Author: Mudra Hegde
Email: mhegde@broadinstitute.org
'''
import pandas as pd
import csv, argparse
import numpy as np
from random import shuffle
from collections import Counter
import time
from datetime import datetime

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',
        type=int,
        default=100,
        help='Number of guides')
    parser.add_argument('-a',
        type=str,
        help='File with abundance parameters')
    parser.add_argument('-x',
        type=int,
        default=1000,
        help='Fold coverage')
    parser.add_argument('-d',
        type=int,
        default=3,
        help='Doublings')
    parser.add_argument('-s',
        type=int,
        default=7,
        help='Number of splits')
    return parser

if __name__ == '__main__':
    start = time.time()
    args = get_parser().parse_args()
    n_guides = args.n
    x_cov = args.x
    d_doub = args.d
    s_spli = args.s
    a_list = list(pd.read_table(args.a,header=None)[0])
    a_list = [int(round(x*x_cov,0)) if x >0 else int(0) for x in a_list]
    outputfile = 'rep_n'+str(n_guides)+'_x'+str(x_cov)+'_s'+str(s_spli)+'_'+str(datetime.now().strftime("%y-%m-%d-%H-%M-%S"))
    guides = ['g'+str(x) for x in range(1,n_guides+1)]
    ini_rep = []
    for i,g in enumerate(guides):
        ini_rep.extend([g]*a_list[i])
    for r in range(1,s_spli+1):
        print r
        rep = []
        for g in ini_rep:
            rep.extend([g]*(2**d_doub))
        print len(rep)
        shuffle(rep)
        ini_rep = rep[0:(n_guides*x_cov)]
        print len(ini_rep)
    c = Counter(ini_rep)
    with open(outputfile,'w') as o:
        w = csv.writer(o,delimiter='\t')
        w.writerow(('Guides','Counts'))
        for g in guides:
            w.writerow((g,c[g]))
    print time.time() - start


