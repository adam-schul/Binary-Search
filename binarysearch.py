
import random, sys, time

try:
    while True:
        print('Name a number between 0 and 50000: ', end='')
        num = int(input())
        start_time = time.time()
        randomlist = random.sample(range(0, 50000), 25000)
       
        randomlist.sort()

        def find(green):
            blue = True
            fred = True
            while blue:
                for i in range(len(randomlist)):
                    while fred:
                        mid = (randomlist[len(randomlist) // 2])
                        if len(randomlist) == 1:
                            if randomlist[0] == green:
                                print('Number is in the list.')
                                blue = False
                                fred = False
                            elif randomlist[0] != green:
                                print('Number is not in the list.')
                                blue = False
                                fred = False
                        elif green == mid:
                           print('Number is in the list.')
                           blue = False
                           fred = False
                        elif green >= mid:
                            del randomlist[0:(len(randomlist) // 2)]
                        elif green <= mid:
                            del randomlist[(len(randomlist) // 2):len(randomlist)]

        find(num)
        print(str(time.time() - start_time) + ' seconds.')

except KeyboardInterrupt:
    sys.exit()

