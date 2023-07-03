word = input()
length = len(word)
if length % 2 == 1:
    length -= 1

palindrome = 1
for i in range(length):
    if word[i] != word[-i-1]:
        palindrome = 0

print(palindrome)