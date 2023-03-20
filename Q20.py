'''

괄호로 된 입력 값이 올바른지 판별하라

입력 ()[]{}
출력 true

마지막에 오는 여는 괄호의 닫힌 괄호가 먼저 나와야 한다.
(){} / {()} --> 가능
{(}) --> 불가능

모든 괄호들이 닫혀야지만 true, {() 이렇게 닫힌게 없으면 false

stack = 리스트의 한쪽 끝으로는 자료의 삽입, 한쪽은 자료의 삭제가 이루어지는 자료구조

매핑 테이블을 만들어놓고, 매핑 테이블에 존재하지 않으면 푸시하고, 팝했을 때 결과가 일치하지 않으면 False를 리턴한다.
또한, 스택이 비어있는 상태에서 pop연산을 시도할 경우 오류가 발생하기 때문에 이에 대한 예외처리도 구현한다.

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

            # 닫는 괄호를 만날때 stack에서 pop된 원소와 매칭되는지 확인한다.
        elif not stack or table[char] != stack.pop():
            return False
        # s의 마지막 값까지 탐색했을때, 남는 괄호가 하나도 없으면 True, 아니면 False
    return len(stack) == 0

print(isValid(s='{')) # FALSE
print(isValid(s='{}')) # TRUE
print(isValid(s='{()}')) # TRUE
print(isValid(s='()]')) # FALSE
