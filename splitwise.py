def addition():
    g=[] #it is used to calcuate the total amount paid by one person
    m = int(input("How many places did u pay:"))
    for i in range(1,m+1):
        d = int(input(f"Enter the {i} place where you paid:"))
        g.append(d)
    Sum = sum(g)
    return Sum

n = int(input("Enter the number of people:"))
a= [] #it holds the names of people
b = [] #it holds the total expenses made by each person
for i in range(0,n):
    nam = input(f"Enter the {i+1} th person name:")
    a.append(nam)
    print(f"{a[i]} enter the expenses you made:")
    s = addition()
    b.append(s)
    print(f"The total expenses made by {a[i]} is",s)
total = sum(b)
avg = (total/(n+1))
# print("the avg amount each person should pay is",avg)
#now b contains the individual payments done by different people
Max = (max(b))
Index = b.index(Max)
name = a[Index]
z = [] #list to store the amount paid by people who paid more than average
f = [] #list to store people namewho paid more than average
for i in range(len(b)):
    if b[i] > avg:
        c=b.index(b[i])
        f.append(a[i])
        z.append(b[i])
# print(f)
for i in range(len(f)):       
    pass 
    # print(f"the people who paid more than average is {z[i]} and their name is {f[i]}")
    # print(f"the amount {f[i]} should receive from others is {z[i]-avg}")
l = [] #list of persons whose amount is lesser than average
o = [] #the amount they paid 
for i in range(len(b)):
    if b[i] < avg:
        c=b.index(b[i])
        l.append(a[i])
        o.append(b[i])

tlo =[]
for i in range(len(l)):        
    # print(f"the people who paid more than average is {o[i]} and their name is {l[i]}")
    # print(f"The total amount that {l[i]} to others is {avg - o[i]}")
    total_l = avg-o[i]
    tlo.append(total_l)

for i in range(len(z)):
    for j in range(len(o)):
        if z[i] > tlo[j] :
            if (tlo[j]-(z[i]-avg)==0):
                print(f"{l[j]} should pay {abs(z[i]-avg)}rs to {f[i]}")
            else:
                print(f"{l[j]} pay {abs(tlo[j]-(z[i]-avg))} rs to {f[i]}")

# for i in range(0,n+1):
#     if b[i] > avg:
#         print(f"{a[i]} is settled")
#         name = a[i]
#     else:
#         if avg-b[i] == 0:
#             print(f"{a[i]} is settled")
#         else:
#             kk = b[i]-(avg-b[i])
            
#             # if kk == avg:
#             # print(f"{a[i]} has to pay {avg-b[i]} rs to {name}")
#             # else:
#             #     kk
#             #     print(f"{a[i]} has to pay {kk} rs to {name} and {avg-kk} to other")
