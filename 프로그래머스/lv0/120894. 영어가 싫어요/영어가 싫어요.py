def solution(numbers):
    ns = ["zero", "one", "two", "three", "four", "five", 
          "six", "seven", "eight", "nine"]
    for i,n in enumerate(ns):
        numbers = numbers.replace(n,str(i))
    return int(numbers)