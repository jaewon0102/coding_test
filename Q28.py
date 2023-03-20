'''
## 해시 테이블

해시 함수란 임의 크기 데이터를 고정 크기 값으로 매핑하는 데 사용할 수 있는 함수다.

해시 테이블(맵)은 키를 값에 매핑할 수 있는 구조인, 연관 배열 추상 자료형을 구현하는 자료구조다.
= (key, value)로 데이터를 저장하는 자료구조 중 하나로 빠르게 데이터를 검색할 수 있는 자료구조다.

ABC -> A1
132BC -> CB
AF32B -> D5
--> 이렇게 각각의 문자길이가 다르지만 화살표(->)로 표시한 특정 함수를 통과하면 고정 크기 값으로 매핑된다. 여기서 화살표 역할을 하는 함수가 '해시 함수'다.

해싱은 정보를 가능한 한 빠르게 저장하고 검색하기 위해 사용하는 중요한 기법 중 하나다.

'''

# put(key, value): 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.
# get(key): 키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1을 리턴한다.
# remove(key): 키에 해당하는 키, 값을 해시맵에서 삭제한다.

import collections # 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성해준다.

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000 # 기본 사이즈는 1000개로 설정, 각 리스트노드를 담게 될 기본 자료형을 선언
        self.table = collections.defaultdict(ListNode) # 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성해주는 collectios.defaultdict를 사용

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 키,값을 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)
        # 해당 인덱스에 노드가 존재하는 경우, 개별 체이닝 방식으로 충돌을 해결한다. p는 인덱스의 첫번째 값이며 p.next를 계속 탐색한다.
        # 종료조건: 1. 이미 키가 존재할 경우 값을 업데이트하고 빠져나가는 경우 / 2. p.next가 None이라면 아무것도 하지 않고 루프를 빠져나가는 경우

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        # 연산으로 인덱스를 결정하고 해당 인덱스에 아무것도 없다면 -1을 리턴한다.
        
        # 노드가 조재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1
    # 해싱 결과에 하나 이상의 노드가 존재하는 것으로 p.next로 탐색하면서 일치하는 키를 찾는다.
    # 찾게 되면 값을 리턴하고, 찾지 못하면 루프를 빠져 나오면서 -1을 리턴한다.
    
    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        # 인덱스를 구한 다음 아무것도 없다면 잘못된 키를 삭제하는 시도인 것이므로 그냥 리턴한다.

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        # 첫번째 노드일 때 p.next is None이라면 유일한 노드를 삭제하는 경우이므로 모두 없애야 한다.
        
        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
        # prev는 이전노드, p는 현재 노드로 p.next로 탐색하다가 일치하는 노드를 찾게 되면 이전 노드의 다음을 현재 노드의 다음으로 연결한다.
        # 즉, 현재 노드를 연결고리가 없도록 끊어 버린다.
