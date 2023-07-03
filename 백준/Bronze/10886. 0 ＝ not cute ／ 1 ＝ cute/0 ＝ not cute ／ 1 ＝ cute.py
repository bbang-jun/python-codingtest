N = int(input())
cute = 0
notCute = 0

for i in range(N):
    vote = int(input())
    if vote == 1:
        cute += 1
    else:
        notCute += 1

if cute > notCute:
    print("Junhee is cute!")
elif cute < notCute:
    print("Junhee is not cute!")