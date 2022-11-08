from yaml import safe_load
from itertools import product, repeat
from pprint import pprint

def html_table(table_, fname_):
   f = open(fname_, 'w')
   lines = []
   for row in table_:
      row = [str(i) for i in row]
      lines.append(','.join(row))
   f.write('\n'.join(lines))
   f.close


def csv_table(table_, fname_):
   f = open(fname_, 'w')
   lines = []
   for row in table_:
      row = [str(i) for i in row]
      lines.append(','.join(row))
   f.write('\n'.join(lines))
   f.close


def gen_combi(dict_):
   idxs = list(repeat(0, len(dict_)))
   keys = list(dict_.keys())
   values = list(dict_.values())
   ret = []

   while True:
      row = list()
      valid = True
      for listid in range(0, len(dict_)):
         org_value = values[listid][idxs[listid]]
         if type(org_value) is dict:
            k = list(org_value.keys())[0]
            value = k
            conditions = org_value[k][0]['condition']
            for i in [i for i in range(0, len(dict_)) if i!=listid ]:
               ref_value = values[i][idxs[i]] if type(values[i][idxs[i]]) is not dict else values[i][idxs[i]]
               for c in conditions:
                  if keys[i] in c and ref_value not in c[keys[i]]:
                     valid = False
                     break
               if not valid:
                  break
         else:
            value = org_value
         if not valid:
            break
         row.append(value)
      if valid:
         ret.append(row)
      n = len(dict_) - 1
      while n >= 1 and idxs[n] >= len(values[n]) - 1:
         n -= 1
      idxs[n] += 1
      if n == 0 and idxs[0] >= len(values[0]) - 1:
         # iter through the last item of 1st list already, so stop here.
         break
      for listid in range(n + 1, len(dict_)):
         # restart indexes of all list on the right
         idxs[listid] = 0
   pprint(ret)
   pprint(len(ret))
   return ret


def main():
   _data = safe_load(open('data.yaml', 'r'))
   # pprint(_data)
   table = []
   table.append(list(_data.keys()))
   table += gen_combi(_data)
   # pprint(table)
   # csv_table(table, 'combi.csv')


if __name__ == '__main__':
   main()
