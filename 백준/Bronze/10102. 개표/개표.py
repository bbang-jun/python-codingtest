V = int(input())
vote = input()
voteA = 0
voteB = 0

for i in range(len(vote)):
    if vote[i] == "A":
        voteA += 1
    else:
        voteB += 1

if voteA > voteB:
    print("A")
elif voteA == voteB:
    print("Tie")
else:
    print("B")