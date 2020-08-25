from typing import Any

class FixedQueue:

    class Empty(Exception):
        """비어있는 fixedQueue에서 디큐 또는 피크 할때 내보내느 예외 처리"""
        pass

    class Full(Exception):
        """가득 차 있는 FixedQueue에서 인큐할 때 내보내는 예외처리"""
        pass

    def __init__(self, capacity:int) ->None:
        """큐 초기화"""
        self.no = 0                 # 현재 데이터 개수
        self.front = 0              # 맨 앞 데이터 커서
        self.rear                   # 뒤 쪽 데이터 커서
        self.capacity = capacity    # 큐의 크기
        self.que = [None]*capacity  # 큐의 본체

    def __len__(self) -> int:
        """큐에 있는 모든 데이터 개수를 반환"""
        return self.no

    def is_empty(self) -> bool:
        """큐의 데이터가 비어 있는지 확인"""
        return self.no <= 0

    def is_full(self) -> bool:
        """큐의 데이터가 가득 차 있는지 확인"""
        return self.no>=self.capacity

        