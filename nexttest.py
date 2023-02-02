from itertools import cycle
from time import sleep

l = [1,2,3,4,5,6,7,8,9,0]

lcycle = cycle(l)

while True:
    print(next(lcycle))
    sleep(0.1)