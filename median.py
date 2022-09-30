"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

if len(numbers)%2 == 0:
    mid = int(len(numbers)/2)
    median = ((numbers[mid] + numbers[mid-1])/2)
else:
    mid = len(numbers) // 2
    median = numbers[mid]

    # test push
print(median)
