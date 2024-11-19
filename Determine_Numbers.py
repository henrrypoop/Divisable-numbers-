#This is a test project to demonstrate how to determine odd/even numbers
def Determine_Numbers():
    try:
        if int(input("Enter a number here: ")) % 2 == 0: #Takes the user input number and see if it's divisable by 2 > odd numbers
            print("This is an even number")
        else:
            print("This is an odd number")
    except ValueError as V:
        print("You have not entered a number :(",V)
Determine_Numbers()
