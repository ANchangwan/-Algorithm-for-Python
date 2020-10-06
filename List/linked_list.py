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

    def add(self, data:Any) -> int:
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1

