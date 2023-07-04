n = int(input())
people = []

for i in range(n):
  name, dd, mm, yyyy = map(str, input().split())
  dd, mm, yyyy = map(int, (dd, mm, yyyy))
  people.append((yyyy, mm, dd, name))
people.sort()

print(people[-1][3])
print(people[0][3])