#Loops
#iterate 0-10 using for loop&while loop
#1.for loop
for i in range(11):
    print(i)
print("________________________________________________")
#2.while loop
count=0
while count<=10:
    print(count)
    count+=1
print("_____________________________________________________")
#iterate 10-0 using for loop &while loop
#1.for loop
for i in range(10,-1,-1):
    print(i)
print("________________________________________________________")
#2.while loop
count=10
while count>=0:
    print(count)
    count-=1
print("________________________________________________________")
#loop that makes seven calls to print()   
for i in range(1,8):
    print('#'* i)
print("_____________________________________________________")

#nested loop
for row in range(7):          # 7 rows
    for col in range(8):      # 8 columns
        print("#", end=" ")   # print # without new line
    print()                   # move to next line after each row
print("________________________________________________________")
for i in range(11):   # from 0 to 10
    print(f"{i} x {i} = {i * i}")
#iterate through the list using for loops
lang_list=['Python','Numpy','Pandas','Django','Flask']
for item in lang_list:
    print(item)
print("________________________________________________________")    
#iterate from 0 to 100 using for loop and print only even numbers
print("EVEN NUMBERS")
for i in range(101):
    if i % 2==0:
        print(i)
print("__________________________________________________________")
#iterate from 0 to 100 using for loop and print only odd numbers
print("ODD NUMBERS")
for i in range(101):
  if i% 2 !=0:
      print(i)
