from random import randrange

print("INTEGER DIVISION")
print("Enter your answer for each problem.")
print("Type 'q' to quit.")

answer = ""
while (True):
    try:
        # Eliminate ivision by zero
        denom = 0
        while (denom == 0):
            denom = randrange(10)
        
        # Use denominator to determine numerator to insure that the answer is an integer
        num = denom * randrange(10)
            
        answer = input(str(num) + "/" + str(denom) + " = ")
        if (answer == "q"):
            print("Goodbye!!!")
            break
        else:
            if (int(answer) == num/denom):
                print("Correct!!!")
            else:
                print("Incorrect!!!")
    except ValueError:
         print("Please enter Integers only!")