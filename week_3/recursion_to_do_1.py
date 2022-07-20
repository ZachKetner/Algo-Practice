#Write a recursive function that given a number returns the sum of integers from
#1 to that number. Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2);
#rSigma(-1) = 0.

def rSigma(int):
    if int <= 0:
        return 0
    return round(int) + rSigma(round(int) - 1)

print(rSigma(5))

# Given num, return the product of ints from 1 up to num. If less than zero,
# treat as zero. If not an integer, truncate. Experts tell us 0! is 1. rFact(3)
# = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).

def rFact(valueInput):
    if valueInput < 1:
        return 1
    return int(valueInput) * rFact(valueInput - 1)

print(rFact(4.8))