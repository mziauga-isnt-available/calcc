from math import prod

def calc():
    choice = input("you want to add(1) or times(2)? ")
    amount = int(input("how many numbers?? "))
    numbers = []
    for x in range(amount):
        y = float(input("soo what are these numbers? " + str(x + 1) + ": "))
        numbers.append(y)
    if choice == "1":
        answer = sum(numbers)
    else:
        answer = prod(numbers)
    
    print("your answer is:", answer)
    option = input("unless do you want the rounded ver? y/n: ")
    if option.lower() == "y":
        print("yay its:", round(answer , 2))
calc()