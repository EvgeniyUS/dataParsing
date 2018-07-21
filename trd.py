# -*- coding: UTF-8 -*-
from datetime import datetime
from pprint import pprint

db = {}
with open('trd.csv', 'r') as f:
  for row in f:
    r = row.split(',')
    t = datetime.time(datetime.strptime(r[0].split('.')[0], '%I:%M:%S'))
    b = r[3].replace('\n', '')
    del r[3]
    del r[0]
    if b in db.keys():
      if t in db[b].keys():
        db[b][t].append(r)
      else:
        db[b][t] = []
        db[b][t].append(r)
    else:
      db[b] = {}
      db[b][t] = []
      db[b][t].append(r)
  ans = {}
  for b, t_data in db.items():
    ans[b] = {}
    ans[b]['quantity'] = 0
    ans[b]['time'] = ''
    for k, v in t_data.items():
      if len(v) > ans[b]['quantity']:
        ans[b]['quantity'] = len(v)
        ans[b]['time'] = k
  pprint(ans)
  M = {}
  for b, d in ans.items():
    if d['time'] in M.keys():
      M[d['time']] = M[d['time']] + d['quantity']
    else:
      M[d['time']] = d['quantity']
  pprint(M)
