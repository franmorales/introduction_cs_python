c1 = ''
c2 = ''
c3 = ''
bob_count = 0
for char in s:
    c3,c2,c1 = c2, c1, char
    if c3+c2+c1 == 'bob':
        bob_count += 1
print ('Number of times bob occurs is: ' + str(bob_count))
