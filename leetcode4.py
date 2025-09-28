#Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.

def isHappy(n):
    while(len(str(n)) > 1):
        summa = 0
        for i in str(n):
            summa += int(i) ** 2
        n = summa

    if n == 1 or n == 7:
        return True
    else:
        return False  
print(isHappy(2))