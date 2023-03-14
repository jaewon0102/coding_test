'''괄호로 된 입력 값이 올바른지 판별하라

입력 ()[]{}
출력 true

마지막에 오는 여는 괄호의 닫힌 괄호가 먼저 나와야 한다.
(){} / {()} --> 가능
{(}) --> 불가능

모든 괄호들이 닫혀야지만 true, {() 이렇게 닫힌게 없으면 false

'''
def isValid(s: str) -> bool:
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    
    for char in s:
        if char not in table:
            # 여는 괄호는 stack에서 push
            stack.append(char)

            # 닫는 괄호를 만날때 stack에서 pop 한다.
        elif not stack or table[char] != stack.pop():
            return False
        # s의 마지막 값까지 탐색했을때, 남는 괄호가 하나도 없으면 True, 아니면 False
    return len(stack) == 0

print(isValid(s='{')) # FALSE
print(isValid(s='{}')) # TRUE
print(isValid(s='{()}')) # TRUE
print(isValid(s='()]')) # FALSE