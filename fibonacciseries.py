#Fibonacci
a=int(input("Enter the number of terms: "))
first=0                                         #first element of series
second=1                                         #second element of series
if a<=0:
    print("The requested series is",f)
else:
    print(first,second, end=" ")
    for x in range(2,a):
        next=first+second                          
        print(next, end=" ")
        first=second
        second=next
