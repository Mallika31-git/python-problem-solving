details={"mallika":99, "rinky":87 , "rebca":75 }
options=f"""
1 Add Student
2 Search Student
3 Update Marks
4 Delete Student
5 Display All Students
6 Exit
"""
print(options)
choice=int(input("enter your choice:"))
if choice== 1 :
    key=input("entr key:")
    value=int(input("enetr value:"))
    details[key]= value
    print(details)
elif choice==2:
    key=input("enter key:")
     
    if key in details:
        print("found:",details[key])
             
    else:
        print("not found")
         
elif choice==3:
     key=input("enter key :")
     if key in details:
      value=int(input(" enter value:"))
     
      details.update({key:value})
      print(details)
     else:
         print("key is not available")
     
elif choice==4:
    key=input("enter key :")
    if key in details:
     del details[key]
     print(details)
    else:
        print("sorry! entred key is not available")
elif choice==5:
    for i in details:
     print(i,":",details[i])
elif choice==6:
    print("signed out")
else:
    print("sorry! your choice is wrong")
    
                   
