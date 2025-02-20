big={}
totscore=int(input("Wwhat the perfect score?"))

for i in range(20):
    name=input("Whats their name?")
    score=int(input("Whats their score?"))
    if score>totscore:
        score=("Are you sure? Whats the actual score?")
    big[name]=score

Lists=[[],[]]
passing=totscore/2

for i,j in big.items():
    if j<passing:
        Lists[0].append(i)
    else:
        Lists[1].append(i)

Lists[0].sort()
Lists[1].sort()

print("The people that failed are ",Lists[0])
print("And the people that passed are",Lists[1])