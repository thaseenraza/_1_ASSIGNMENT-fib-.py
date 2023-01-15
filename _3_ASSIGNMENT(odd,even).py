# Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 4
# Number of odd numbers : 5

even = 0
odd = 0
# start_range =int(input("Enter the start range : "))
End_range = int(input("Enter the End range :"))
for i in range(1,End_range): 

    if i % 2 == 0: 

        even += 1

    else: 

        odd+= 1          
print(range(1,End_range))

print("No of Even numbers in range : ", even) 

print("No of Odd Numbers in range : ", odd)

