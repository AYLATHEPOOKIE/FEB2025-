"""#recap
lists=[32,5,3,7,True,"asfdsf"]
print(lists.index(True))
lists[-2]
lists[4]

for i in lists:
    print(i)

#double list
listmega=[[0,1,2,2.5],[3,4,5,5.5],[6,7,8,8.5]]
print(len(listmega[2]))
print(listmega[0][1])

for i in range (len(listmega)):
    for j in range(len(listmega [2])):
        print(listmega[i][j],end=" ")
    print("")

"""
"""#custom
list=[]
row=int(input("num of rows/coloums "))
for i in range(row):
  temp=[]
  for j in range(row):
    inr=input("Name a value ")
    temp.append(inr)
  list.append(temp)

for i in range (len(list)):
    for j in range(len(list[i])):
        print(list[i][j],end=" ")
    print("")
"""
# adding lists
A=[[1,1],[1,1],[1,1]]
B=[[43,34],[235,63],[321,3]]
AB=[[0,0],[0,0],[0,0]]
for i in range (len(A)):
    for j in range(len(A[2])):
        AB[i][j]=A[i][j]+B[i][j]

print(AB)