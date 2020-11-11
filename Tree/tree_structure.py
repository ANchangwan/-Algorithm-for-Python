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

     def remove(self,key:Any) -> bool:
        p = self.root                        # 스캔 중인 노드
        parent = None                        # 스캔 중인 노드의 부모노드
        is_left_child = True                 # p는 parent의 외쪽 자식 노드인지 확인

        while True:
            if p is None:
                return None
            if key == p.key:
                break
            else:
                p = parent
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right
        
        if p.left is None:                # p에 왼쪽 자식이 없으면
            if p is self.root:
                p.left = self.root        
            elif is_left_child:
                parent.left = p.right     # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.left     # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif p.right is None:              # p에 오른쪽 자식이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left        # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.right      # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
        else:
            parent = p                          
            left = p.left                       # 서브트리 안에서 가장 큰 노드
            is_left_child = True                
            while left.right is not None:       # 가장 큰 노드 left를 검색
                parent = p.left
                left.right = p.right
                is_left_child = False
            
            p.key = left.key                    # left의 키를 p로 이동
            p.value = left.value                # left의 데티러르 p로 이동
            if is_left_child:
                parent.left = left.left         # left를 삭제
            else:
                parent.right = left.left        # left를 삭제

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
