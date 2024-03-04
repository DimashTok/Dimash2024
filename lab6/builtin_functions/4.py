from time import sleep
number = int(input())
miliseconds = int(input())
seconds = float(miliseconds/1000)
root = number ** (1/2)
sleep(seconds)
print(f"Square root of {number} after {miliseconds} miliseconds is {root}")
