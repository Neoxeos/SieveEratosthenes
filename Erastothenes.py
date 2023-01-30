'''
author : Christian Coirin
class : MATH 496
promgram using Erastosthenes Sieve to find prime numbers (trivial primes numbers) below a certain number
'''

import time


def PrimeCalculator(number):
  '''
  require : number of type int
  
  number: upper bound for which we wish to calculate primes such that
  #primes <= number

  returns : # primes of type int
  '''

  #edge cases
  if number == 2:
    return []
  elif number == 3:
    return [2]
  elif number == 4 or number == 5:
    return [2, 3]

  # first we can eliminate all even numbers and all numbers divisable by 5 and build a list with the rest of the numbers
  numberList = [2, 3, 5]
  i = 5
  while (i < number):
    if (i % 5 == 0):
      i += 2
      continue
    else:
      numberList.append(i)
    i += 2

  # now we divide every entry by the beginning number until we exhaust all numbers
  check = True
  divisorIndex = 1

  while (check):
    divisor = numberList[divisorIndex]  #we start at 3 since no even numbers

    max = len(
      numberList) - 4  # we don't need to check 2,3,5,7 so we start at 4
    count = 0
    while count < max:
      if numberList[count + 4] % divisor == 0 and numberList[count +
                                                             4] != divisor:
        numberList.pop(count + 4)
        max -= 1
      count += 1

    if divisorIndex == 1:
      divisorIndex += 2
      # we skip 5 since no multiples of 5
    else:
      divisorIndex += 1

    #condition to exit loop
    if divisorIndex == len(numberList) - 1:
      check = False

  return numberList


if __name__ == "__main__":
  timeStart = time.time()
  number = input("Enter a positive integer: \n")
  primeNumberList = PrimeCalculator(int(number))
  # print(primeNumberList)
  print(len(primeNumberList))
  print("--- %s seconds ---" % (time.time() - timeStart))
