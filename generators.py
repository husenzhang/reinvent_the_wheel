# creating pipelines with generators

#!/usr/bin/env python3

print('test python3 print function.')

# test chain
from itertools import chain

for i in chain(range(6), ['a', 'b', 'c']):
    print(i)
