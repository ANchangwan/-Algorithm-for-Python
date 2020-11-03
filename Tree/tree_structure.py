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
        p = self.root               # 루트에 주목
        while True:
            if p is None:           # 더이상 진행 할 수 없으면
                return None         # 검색 실패
            if key == p.key:        # key와 노드p의 키가 같으면
                return p.value      # 검색 성공
            elif key < p.key:       # key쪽이 작으면 
                p = p.left          # 왼쪽 서브트리에서 검색
            else:                   # key 쪽이 크면
                p = p.right         # 오른쪽 서브트리에서 검색

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
        if self.root is None:
            self.root = Node(key,value,None,None)
            return True
        else:
            return add_node(self.root,key,value)

    def remove(self, key:Any) -> bool:
        """키가 key인 노드를 삭제"""
        p = self.root
        parent = None
        is_left_child = True
        while  True:
            if p is None:                   # 더 이상 진행할 수 없으면
                return False                # 그 키는 존재하지 않음
            
            if key == p.key:                # key와 노드 p의 키가 같으면
                break                       # 검색성공
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right
        
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.left = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True

    def dump(self)-> None:
        """덤프(모든 노드를 키의 오름차순으로 출력)"""
        def print_subtree(node:Node):
            """node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력"""
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key}  {node.value}')
                print_subtree(node.right)
            
        print_subtree(self.root)

    def min_key(self) -> Any:
        if self.root is None:
            return
        
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        if self.root is None:
            return None
        
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key