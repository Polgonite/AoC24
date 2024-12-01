# part one

f = open("input", "r")

llist = []
rlist = []

num = 0

for line in f:
    lnum, rnum = line.split("   ")
    llist.append(int(lnum))
    rlist.append(int(rnum))

llist.sort()
rlist.sort()

ans1 = 0

for x in range(len(llist)):
    ans1 += max(llist[x], rlist[x]) - min(llist[x], rlist[x])

print("The distance between the lists is: " + str(ans1))

# part two

ans2 = 0

for x in range(len(llist)):
    
    matches = 0

    for y in range(len(rlist)):
        if llist[x] == rlist[y]:
            matches += 1
    
    ans2 += llist[x] * matches

print("The similarity score between the lists is: " + str(ans2))