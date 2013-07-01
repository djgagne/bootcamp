#Authors: David John and John David
# and Jing is trying to puch back

def add_four(a,b,c,d):
    return a+b+c+d

from adding import add_three

def mul_two(a,b):
    reture a*b

def add_two(a,b):
    return a+b

def main():
    print "Blah"
    print ("2 + 3 = ",add_two(2,3))
    print ("2 + 3 + 4 = ", add_three(2,3,4))
    print add_four(3,6,2,1)
if __name__ == "__main__":
    main()
