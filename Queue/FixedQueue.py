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

    def enque(self, data:Any) ->int:
        """data를 인큐"""
        if self.is_full():
            return FixedQueue.Full
        self.que[self.rear] = data
        self.rear+=1
        self.no +=1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> int:
        """데이타를 디큐(데이터를 출력(꺼냄))"""
        if self.is_empty():
            return FixedQueue.Empty
        data = self.que[self.front]
        self.front += 1
        self.no -=1
        if self.front == self.capacity:
            self.front = 0
        return data
    
    def peek(self) -> Any:
        """큐에서  데이터를 피크(맨 앞 데이터를 들여다봄)"""
        if self.is_empty():
            return FixedQueue.Empty
        return self.que[self.front]

    def find(self, value:Any) ->Any:
        """큐에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
        if self.is_empty():
            return FixedQueue.Empty
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1
    
    def count(self,value:Any)->Any:
        """큐에 있는 value의 개수를 반환"""
        c=0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c
    
    def __contains__(self, value:Any) -> bool:
        """큐에 value가 있는지 판단"""
        return self.count(value)

    def clear(self) -> None:
        """큐에 데이터를 비움"""
        self.no = self.front = self.rear = 0


    def dump(self) -> None:
        """모든 데이터를 맨 앞부터 맨 긑 순으로 출력"""
        if self.is_empty():
            print("큐가 비어있습니다.")
        else:
            for i in range(self.no):
                print(self.que[(i + front) % self.capacity], end = " ")
        print()
        


        