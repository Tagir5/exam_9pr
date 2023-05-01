a  = open('fil.csv')
m = 0
for s in a:
  k = list(map(int , s.split(';')))
  k.sort()
  if min(k) < 5*(sum(k)-min(k)):
    if k[0]*k[1] == k[2]*k[3] or k[0]*k[2] == k[1]*k[3] or k[0]*k[3] == k[2]*k[1]:
      m += 1

print(m)
    