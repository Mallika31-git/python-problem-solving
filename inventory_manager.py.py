inventory={
    "Pen": 50,
    "Book": 20,
    "Pencil": 100
}
options=f"""
1.Add item
2.Update quantity
3.Remove item
4.Display inventory
"""
print(options)
choice=int(input("enter your choice:"))
if choice==1:
    item=input("enter your item:").capitalize()
    quantity=int(input("enter quantity of the item:"))
    if  item not  in inventory:
        inventory[item]=quantity
        print(inventory)
    else:
        print("entered item is already in dictionary")
elif choice==2:
    item=input("enter item:").capitalize()
    quantity=int(input("enter quantity:"))
    if item in inventory:
        inventory.update({item:quantity})
        print(inventory)
    else:
        print("sorry! entered item is not available")
elif choice==3:
    item=input("enter item:").capitalize()
    if item in inventory:
        del inventory[item]
        print(inventory)
    else:
        print("sorry! entered item is not available")
elif choice==4:
    for i in inventory:
        print(i,":",inventory[i])
else:
    print("sorry! entered choice is wrong")

     