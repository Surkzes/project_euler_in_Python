# Problem Number 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
sum_ = 0
exponent = str(2**1000)
for i in range(0, len(exponent)):
    sum_ += int(exponent[i])
print(sum_)