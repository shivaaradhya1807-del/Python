classmates=["Aarav" ,"Myra" ,"Rahul" ,"Sneha" ,"Dev"]
print("Classlist :",classmates)

print(len(classmates))
print("first student is : ",classmates[0])
print("last student is : ",classmates[4])
print("first 3 students are",classmates[:3])

classmates.append("Mira")
print("after adding mira :",classmates)
classmates.remove("Dev")
print("after removing Dev",classmates)
classmates.sort()
print(classmates)
classmates.reverse()
print(classmates)


