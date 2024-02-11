from itertools import groupby
from operator import itemgetter
import os
import pickle

fname = os.path.join('dev', 'complaints-best.pickle')
with open(fname, 'rb') as handle:
    complaints = pickle.load(handle)
print('Rows: ', len(complaints))

keyfunc = itemgetter(1)
complaints = sorted(complaints.items(), key=keyfunc)
for complaint, group in groupby(complaints, keyfunc):
    rows = list(group)
    print(complaint, len(rows))
    if complaint == 'other':
        print('Other: ', [code for code, _ in rows])
