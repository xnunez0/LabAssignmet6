



"""
To statr, we will generate a random interger between 1 and 20, and 
based on the result of the number, we check to see if it falls under certain range
if the number is greater than 15, then the result will be "Cherries"
otherwise if the number is > 10, then the result wil be "Orange"
otherwise if the number is > 10, then the result wil be "Plum"
otherwise if the number is > 10, then the result wil be "Melon"
otherwise if the number is > 10, then the result wil be "Bell"
if the number is not any of the above, then the reult will be "Bar"

we iterate over using a loop three times ab=nd print the reults to the user. An example "Plum Cherries"

"""

"""
import random 
num = generate random number

if num is greater than 15,
    then the result will be "Cherries"
otherwise if num is > 10,
    then the result will be "Orange"
otherwise if num is > 5, 
    then the result will be "Plum"
otherwise if num is > 2, 
    then the result will be "Melon"
otherwise if num is > 1, 
    then the reult will be "Bell"
otherwise 
    the result will be "Bar"

loop three times 
    print the output (fruit) to the user 

"""
import random

def main():
    for i in range (0, 3):
        spin()
        
def spin():
    rand_num = random.randint(1, 20)
    output = ""
    if(rand_num > 15):
        output = "Cherries" 
    elif(rand_num > 10):
        output = "Orange"
    elif(rand_num > 5):
        output = "Plum"
    elif(rand_num > 2):
        output = "Bell"
    elif(rand_num > 1):
        output = "Melon"
    else:
        output = "Bar"

print(output, end="")

main()














