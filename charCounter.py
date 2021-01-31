received = "no"

enteredstring = ""

while received == "no":
    enteredstring = input("please input string to be counted: ")
    received = "yes"

    while received == "yes":
        print([x for x in enteredstring])
        print("Lowercase Count =",sum(1 for i in enteredstring if i.islower()))
        print("Uppercase Count =",sum(1 for i in enteredstring if i.isupper()))
        print("Special Character Count =",sum(1 for i in enteredstring if not i.isalnum()))
        received = "no"