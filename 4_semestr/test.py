import re

with open('1.txt') as first, open('2.txt','w') as second:

    for line in first:
        line = line.rstrip('\n')
        s = [int(s) for s in str.split(line) if s.isdigit()]
        s = str(s)
        b =''.join(s)
        e = line + " " + b + '\n'
        print(e)
        second.write(e)





















#    lines = first.readlines()
  #  for line in lines:
 #       s = [int(s) for s in str.split(line) if s.isdigit()]
 #       # print(s)
 #       a = str(s)
 #       b = line + ' ' + a
  #      print(b)
  #      second.write(b)
        # print(b)