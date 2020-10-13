# 커서로 연결리스트 구현
from __future__ import annotations
from typing import Any,Type

Null = -1

class Node:
    """연결리스트용 노듵클래스(배열 커서버전)"""
    def __init__(self, data:Null,next:Null,dnext:Null):
        self.data = data    #데이터
        self.next = next    # 리스트의 뒤쪽 포인터
        self.dnext = dnext  # 프리리스트의 뒤쪽 포인터

class ArrayLinkedList:
    def __init__(self, capacity:Null):
        self.head = Null                     # 머리노드
        self.current = Null                  # 주목 노드
        self.max = Null                      # 사용중인 꼬리 레코드
        self.delected = Null                 # 프리 리스트의 머리 노드
        self.capacity = capacity             # 리스트의 크기
        self.n = [Null()] * self.capacity    # 리스트 본체
        self.no = 0

    def __len__(self) ->int:
        """연결리스트의 노드 수를 반환"""
        return self.no

    def get_insert_index(self):
        """다음에 삽입할 레코드의 인덱스를 구함"""
        if self.deleted == Null:                    # 삭제 레코드는 존재하지 않음ㄴㅇㄹ
            if self.max < self.capacity:
                self.max += 1
                return self.max                     # 새 레코드를 사용
            else:
                return Null                         # 크기 초과

        else:
            rec = self.delected
            self.deleted = self.n[rec].dnext        # 프리 리스트에서 맨 앞 rec를 꺼내기
            return rec

    def delete_index(self, idx:int) ->None:
        '''레코드 idx를 프리 리스트에 등록'''
        if self.deleted == Null:            # 삭제 레코드는 존재하지 않음
            self.deleted = idx
            self.n[idx].dnext = Null        # idx를 프리 리스트의 맨앞에 등록
        else:
            rec = self.deleted
            self.deleted = idx              # idx를 프리 리스트의 맨 앞에 삽입
            self.n[rec].dnext =rec