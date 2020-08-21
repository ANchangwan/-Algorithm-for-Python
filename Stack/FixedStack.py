
from typing import Any

class FixedStack:
    """고정 길이 스택 클래스"""

    class Empty(Exception):
        """비어 있는 FixedStack에 팝 또는 피크할 때 내보내는 예외처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedStack에 푸시할 때 내보내는 예외처리"""
        pass

    def __init__(self, capacity:int = 256) ->None:
        self.stk = [None]*self.capacity # 스택 본체
        self.capacity = capacity        # 스택의 크기
        self.ptr = 0                    # 스택 포인터

    def __len__(self) ->int:
        """스택에 쌍여있는  데이터 개수를 반환"""
        return self.ptr

    def is_Empty(self)->bool:
        """스택이 비어있는지 판단"""
        return self.ptr<=0

    def is_full(self)->bool:
        """스택이 가득 차있는지 판단"""
        return self.ptr>=self.capacity

        