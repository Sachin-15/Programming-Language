# wap to accept marks of 6 students and display them in a sorted manner

m1 = int(input("Enter Marks for Student 1 : "))
m2 = int(input("Enter Marks for Student 2 : "))
m3 = int(input("Enter Marks for Student 3 : "))
m4 = int(input("Enter Marks for Student 4 : "))
m5 = int(input("Enter Marks for Student 5 : "))
m6 = int(input("Enter Marks for Student 6 : "))

mylist = [m1,m2,m3,m4,m5,m6]
mylist.sort()
print(mylist)