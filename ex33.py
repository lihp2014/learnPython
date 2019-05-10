numbers = []
def myLoop(count):
    i = 0
    while i < count:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

myLoop(5)

print "The numbers: "

for num in numbers:
    print num
