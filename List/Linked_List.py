# 링크드 리스트 구현
from __future__ import annotations
from typing import Any, Type

class Node:
    """연결리스트 노드 생성"""
    def __init__(self, data:Any = None, next:Node = None):
        """초기화"""
        self.data = data # 데이타
        self.next = next # 뒤쪽 노드

class LinkedList:
    def __init__(self) -> int:
        """초기화"""
        self.no = 0            # 현재 노드의 갯수
        self.head = None        # 머리노드
        self.current = None  # 주목 포인트

    def __len__(self):
        """연결리스트의 노드의 개수를 반환"""
        return self.no
        
    def search(self, data:Any) ->int:
        cnt =0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                ptr.current = ptr
                return cnt
            cnt+=1
            ptr = ptr.next
        return -1
    
    def __contains__(self, data:Any) ->bool:
        """연결리스트에 데이터가 포함 되어 있는 판단"""
        return self.search(data)>=0

    def add_first(self, data:Any) -> int:
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data:Any) ->int:
        """맨 끝에 노드를 삽입"""
        if self.head is None:           # 리스트가 비어있다면 
            self.add_first(data)        # 맨 앞에 노드를 삽입
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1

    def remove_first(self) -> int:
        """맨 앞 노드 삭제"""
        while self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self) -> int:
        """꼬리 노드 삭제"""
        if self.head is not None:
            if self.head.next is None:  # 노드가 1개 뿐이라면
                self.remove_first() # 머리 노드를 삭제  
            else:
                ptr = self.head
                pre = self.head
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no-=1

    def remove(self,p:Node) -> None:
        """노드 p를 삭제"""
        if self.head is not None:
            if p is self.head:          # p가 머리 노드라면
                self.remove_first()          # 첫번째 노드 삭제

            else:
                ptr = self.head
                while ptr.next is not p:
                        ptr = ptr.next
                        if ptr is None:
                            return
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) ->None:
        """주목노드를삭제"""
        self.remove(self.current)

    def clear(self) -> None:
        """주목노드를 한 칸 뒤로 이동"""
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0

    def next(self) -> bool:
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True 

    def print_current_node(self) -> None:
        if self.current is None:
            print('데이터가 없습니다')
        else:
            print(self.current.data)

    def print(self) -> None:
        ptr = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next