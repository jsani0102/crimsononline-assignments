x = 1
while x <= 100:
    mod3 = x % 3 == 0
    mod5 = x % 5 == 0
    if (mod3 and mod5): print "FizzBuzz"
    elif (mod5): print "Buzz"
    elif (mod3): print "Fizz"
    else: print x
    x += 1
