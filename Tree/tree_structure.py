# 이진 검색 트리 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, key:Any, value:Any, left:Node, right:Node) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None    # 루트
    
    def search(self, key:Any) -> None:
        p = self.root       # 루트에 주목
        while True:
            if p is None:   # 더이상 진행 할 수 없으면
                return None # 검색 실패
            if key == p.key:        #key와 노드p의 키가 같으면
                return p.value  # 검색 성공
            elif key < p.key:   # key쪽이 작으면 
                p = p.left      # 왼쪽 서브트리에서 검색
            else:               # key 쪽이 크면
                p = p.right     # 오른쪽 서브트리에서 검색

    def add(self, key:Any,value:Any) -> bool:
        """키가 key이고 값이 value인 노드를 삽입"""
        def add_node(node:Node, key:Any, value:Any) -> None:
            """node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입"""
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key,value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right,key,value)
            return True





