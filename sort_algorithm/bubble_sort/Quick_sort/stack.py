from typing import Any
from collections import deque

class Stack:
    """고정 길이 스택 클래스(collections.deque 사용)"""

    def __init__(self, capacity:int = 20) -> None:
        self.capacity = capacity # 스택 최대값
        self.stk = deque([],capacity)
    
    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터 개수를 반환"""
        return len(self.stk)
    
    def is_empty(self) -> bool:
        """스택이 비어있는지 판단"""
        return not self.stk

    def is_full(self) -> bool:
        """스택이 가득차 있는지 판단"""
        return len(self.stk) == self.stk.maxlen
    
    def push(self, value:int) ->int:
        """스택에 value푸쉬"""
        self.stk.append(value)

    def pop(self) -> int:
        """스택에 값을 반환"""
        return self.stk.pop()

    def peek(self) -> Any:
        """스택에 마지막 값을 봄"""
        return self.stk[-1]
    
    def clear(self) -> Any:
        """모든 값을 삭제"""
        return self.stk.clear()

    def find(self, value:Any) -> Any:
        """찾고자하는 값의 인덱스를 반환"""
        try:
            return self.stk.index(value)
        except ValueError:
            return -1
    
    def count(self, value:Any) -> Any:
        """value의 갯수를 반환"""
        return self.stk.count(value)
    
    def __contains__(self, value:Any) -> Any:
        """스택에 value가 포함되어 있는지 판단"""
        return self.count(value)

    def dump(self) ->int:
        """스택 안에 있는 모든 데이터를 나열"""
        print(list(self.stk))