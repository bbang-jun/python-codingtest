s = ['(', '(', ')', ')']

def solution(s):
    stack = []
    for element in s:
        if element == '(':
            stack.append(element)
        elif element == ')':
            stack.pop()
    if not stack:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    solution(s)