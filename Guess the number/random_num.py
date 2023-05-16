import random
import sys , subprocess

def clear_screen():

    operating_system = sys.platform
    if operating_system == 'win32':
        subprocess.run('cls' , shell = True)

    

print("\t\tWELCOME TO THE WORLD OF GAMBBLING\t\t")
print("\n")
print("\t\tLet's TRY YOUR LUCK\t\t")

ans = input("press Enter to continue : ")
clear_screen()
file = open("random_num.txt" , 'a')
name = input(f"Please Enter your name : ")
file.write(f"{name}\n")
amount = int(input("Enter the amount you want to put on bet in INR : "))
file.write(f"Amount : {amount}\n")
clear_screen()
print(f"Rules of the Game :\n1.You have to choose the range of number in which you want to guess")
print(f"2.After selecting the range you have to guess the number")
print(f"3.After each fail guess  your money will get halved")
print(f"4.After each successfull guess your money get doubled")
print("5.Range of number should be atleast 20")
print(f"6..Anywhere in the game if you want to quit then write 'exit'")
ans = input("\nPress enter to Continue and you want to exit then write exit : ")
if ans == 'exit':
    print(f"Dear {name} Please visit again :)")
    quit()

else :
    pass

    num_range = input("Enter the range of number in which you want to guess : ")
    if num_range.isdigit():
        num_range = int(num_range)
        if num_range>= 20 :
            top_range = random.randint(0 , num_range)
        else :
            print("Invalid Range!")
            quit()


    elif num_range == 'exit':
        print("Thank you for visiting please visit again :)")
        quit()
    else:
        print("Please enter a valid input")
        quit()
while True :
   
    num = input("Enter the Guess : ")

    if num.isdigit():
        num = int(num)
        if num == top_range :
            print("Yeah! you made the correct guess, Keep playing")
            amount += amount
            top_range = random.randint(0 , num_range)

        elif num > 20 :
            print("Please Enter a valid number")
            continue

        
        else :
            print("Ohh!You missed,make another guess")
            amount = int(amount) - int(amount/2)
        

    elif(num == 'exit'):
        print("Thank you for playing , Hope you enjoyed.Please visit again :)")
        break
    else :
        print("Please enter the valid value")
        continue
    
             
print(f"Dear {name} your Amount after Playing is {amount}")
file.write(f"Amout left : {amount}\n")
     







