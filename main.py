import random

# converts the number into a list of digits
def str_to_int(num):
    list_of_digits=[]
    for x in str(num):
        list_of_digits.append(x)

    # delete the code below after done checking
    return list_of_digits


# checks if the number has duplicate digits or not
def no_repeated_numbers(number):
    temp=str(number)
    if len(temp)==len(set(temp)):#set helps in checking if the digits are repeating or not
        return True
    else:
        return False
    
# generates 4 digit random number
def generate_4_digits():
    while True:
        n=random.randint(1000,9999)
        if no_repeated_numbers(n):
            return n

#now i need to build a function which gives the number of bulls(correct pos and correct number) and cows(wrong position correct number)
def bulls_and_cows(guess,number):
    num_list=str_to_int(number)
    guess_list=str_to_int(guess)

    bull_and_cow=[0,0]

    for i in range(4):
        

        if guess_list[i] in num_list:#checks if the guess number's digit is in number , if yes then it confirms bull or cow for sure

            if guess_list.index(guess_list[i])==num_list.index(guess_list[i]):
                bull_and_cow[0]+=1
            else:
                bull_and_cow[1]+=1
        else:
            continue
        
    print(f"Bulls {bull_and_cow[0]} and Cows {bull_and_cow[1]}")
                     

# now i need to build a function which takes the guess of the user

number_of_tries=int(input("Enter The Number Of Tries: "))
print("\n")
# number=generate_4_digits()
number=1234

# 1.The user can enter numbers which are not btw 1000 and 9999 
# 2.The user guesses a 4 digit number:
#       now i need to run the bull_and_cows function and give the output to the user

while number_of_tries>0:
    guess=int(input("Enter Your Guess Please: "))

    #  i need to consider a case where the user guesses perfectly:
    if guess==number:
        print(f"Congratulations! You Guessed Correctly, The Number was {number}!")
        break

    if guess<1000 or guess>9999:#Clears invalid inputs
        print("Please Enter A Valid Number Between 1000 and 9999.")
        print('\n')
        continue
    else:
        bulls_and_cows(guess,number)
        number_of_tries-=1
        print(f"Number of Tries Remaining: {number_of_tries}")
        print('\n')

if number_of_tries==0:
    print(f"Sorry, Your Are Out OF Tries, The Number Was: {number}")