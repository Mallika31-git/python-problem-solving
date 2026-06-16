options=f"""
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
"""
choice=''
while choice!=5 :
    print(options)
    choice=int(input("enter your choice:"))
    if choice==1:
        no1=int(input("enetr no.1:"))
        no2=int(input("enter no.2:"))
        result=no1+no2
        print("addition of two numbers:",result)
    elif choice==2:
         no1=int(input("enetr number :"))
         no2=int(input("enter  number that you want to subtract:"))
         result=no1-no2
         print( "subtraction of two numbers:",result)
    elif choice==3:
         no1=int(input("enetr no.1:"))
         no2=int(input("enter no.2:"))
         result=no1*no2
         print("multiplication of two numbers:",result)
    elif choice==4:
         no1=int(input("enetr dividend:"))
         no2=int(input("enter divisor:"))
         if no2==0:
             print("sorry! division is not possible")
         else:
          result=no1/no2
          print("division of two numbers:",result)
         
    
    elif choice ==5:
        print("singing out")
    else:
        print("sorry! entered choice is wrong")
         
        
       
        
     
 
    
     
      