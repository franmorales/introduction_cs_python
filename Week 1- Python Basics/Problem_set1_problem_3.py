alpha = ' abcdefghijklmnopqrstuvwxyz'
c1, st1, st2= '', '',''
for c2 in s + ' ':
    if c1 == '':
        c1, st1 = c2, c2
    elif alpha.index(c2) >= alpha.index(c1):
        st1 += c2
        c1 = c2
    elif alpha.index(c2) < alpha.index(c1):
        if len(st1)>len(st2):
            st2 = st1
        st1, c1 = c2, c2
print ('Longest substring in alphabetical order is: '+st2)
