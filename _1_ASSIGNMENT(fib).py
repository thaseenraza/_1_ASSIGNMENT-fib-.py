# Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

nth_term =int(input("Enter the terms : "))
first_number = 1                                         
second_number =1                                       
if nth_term <=9:
    print("The requested series is" ,first_number,second_number,end=" ")
    for i in range(2,nth_term):
        next=first_number+second_number                           
        print(next,end=" ")
        first_number=second_number
        second_number=next
else:
    print("The fibonacci series is out of range for above assignment" ,)
    



        