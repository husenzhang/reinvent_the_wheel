# probability of sum of two dices <=9
from __future__ import division
import random

dice = range(1, 7)
s = []
for i in range(1000):
    add = random.choice(dice) + random.choice(dice)
    s.append(add)

n = [ i for i in s if i <= 9]
print 'sum of two dices <= 9: %d out of %d' %(len(n), len(s))
