# 원형 이중 연결 리스트

from __future__ import annotations
from typing import Any,Type

class Node:
    def __init__(self, data:Any =None, next:Node =None, prev:Node = None) -> None:
        """초기화"""
        self.data = data                # 데이터
        self.next = next or self        # 앞쪽 포인터
        self.prev = prev or self        # 뒤쪽 포인터

class DubleLinkedList:
    """원형 이중 연결 리스트 클래스"""
    def __init__(self) -> None:
        self.head = self.current = Node()
        self.no = 0

    def __len__(self) -> int:
        """연결리스트의 노드 수를 반환"""
        return self.no
    
    def is_empty(self) -> bool:
        '''노드가 비어있는지 확인'''
        return self.head.next is self.head

    def search(self, data:Any) -> Any:
        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self,data:Any) -> Any:
        return self.search(data) >= 0

    def print_current_node(self) -> None:
        if self.is_empty():
            print('주목 노드가 없습니다.')
        else:
            print(self.current.data)

    def print(self) -> None:
        ptr = self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        ptr = self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.is_empty() or self.current.next is self.head:
            return False
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        if self.is_empty() or self.current.prev is self.head:
            return False
        self.current = self.current.prev
        return True
        
    def add(self, data:Any) -> Any:
        node = Node(data, self.current, self.current.next)
        self.current.next.prev =  self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data:Any) -> Any:
        '''맨앞에 노드에 삽입'''
        self.current = self.head
        self.add(data)
    
    def add_last(self, data:Any) -> Any:
        '''맨 뒤에 노드에 삽입'''
        self.current = self.head.prev
        self.add(data)

    def remove_current_node(self) -> None:
        '''주목노드삭제'''
        self.current.prev.next = self.current.next
        self.current.next.prev = self.current.prev
        self.current = self.current.next
        if self.current is self.head:
            self.current = self.current.next
    
    def remove(self, p:Node) -> None:
        '''노드 p를 삭제'''
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.current_remove_node()
                break
            ptr = ptr.next
    
    def remove_first(self) -> None:
        self.current = self.head.next
        self.remove_current_node()

    def remove_last(self) -> None:
        self.current = self.head.prev
        self.remove_current_node()

    def clear(self) -> None:
        while not self.is_empty():
            self.remove_first()
        self.no = 0

    def __iter__(self)->DubleLinkedListIterator:
        '''이터레이터를 반환'''
        return DubleLinkedListIterator(self.head)

    def __reversed__(self) -> DubleLinkedListReverseIterator:
        return DubleLinkedListReverseIterator(self.head)

class DubleLinkedListIterator:
    '''DoubleLinkedList의 이터레이터용 클래스'''
    def __init__(self, head:Node):
        self.head = head
        self.current = head.next

    def __iter__(self) ->DubleLinkedListIterator:
        return self

    def __next(self) -> Any:
        if self.curretn is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
    
class DubleLinkedListReverseIterator:
    def __init__(self, head:Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data

