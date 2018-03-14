option='y'
while option=='y':
    print("Enter the limit till you want to print the sum")
    num=int(input())
    summ=(num*(num+1))/2
    print('Sum of first '+str(num)+' natural number is '+str(summ))
    print("Do you want to continue?(y/n)")
    option=input()
print('Thank you for using this programme')
