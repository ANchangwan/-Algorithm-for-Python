from __future__ import annotations
from typing import Any,Type

class Node:
    def __init__(self, data:int, next:Node) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.current = None
        self.no = 0     # 노드의 갯수

    def __len__(self) ->None:
        return self.no

    def search(self, data:int) -> None:
        cnt =0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                print("데이터를 찾아습니다.")
                print(f'{cnt}번째 위치에 있습니다.')
                self.current = ptr
                return cnt
                
            ptr = ptr.next
            cnt+=1
        return -1


    def add_first(self, data:int) -> None:
        if self.head is None:
            ptr = self.head
            self.ptr.data = data

