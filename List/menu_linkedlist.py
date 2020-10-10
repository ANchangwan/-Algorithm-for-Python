from enum import Enum
from Linked_List import LinkedList

Menu = Enum('Menu',['머리노드삽입','꼬리노드삽입','머리노드삭제',
                    '꼬리노드삭제','주목노드출력','주목노드이동',
                    '주목노드삭제','모든노드삭제','검색','멤버십판단',
                    '모든노드출력','스캔','종료'])

def select_menu() -> Menu:

    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s,sep=' ',end='')
        n = int(input( ' : '))
        if 1<= n <=len(Menu):
            return Menu(n)

lst = LinkedList()

while True:
    menu = select_menu()

    if menu == Menu.머리노드삽입:
        lst.add_first(int(input('머리노드를 넣을 값을 입력하세요 : ')))

    elif menu == Menu.꼬리노드삽입:
        lst.add_last(int(input('꼬리노드를 넣을 값을 입력하세요 : ')))

    elif menu == Menu.머리노드삭제:
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:
        lst.remove_last()

    elif menu == Menu.주목노드출력:
        lst.print_current_node()
    
    elif menu == Menu.주목노드이동:
        lst.next()

    elif menu == Menu.주목노드삭제:
        lst.remove_current_node()
    
    elif menu == Menu.모든노드삭제:
        lst.clear()

    elif menu == Menu.검색:
        find = lst.search(int(input('검색할 노드를 입력해주세요 : ')))
        if find >= 0:
            print(f"노드는 {find + 1}번째에 있습니다.")
        else:
            print('찾고자하는 노드가 없습니다')
    
    elif mnue == Menu.모든노드출력:
        lst.print()
    
    elif menu == Menu.스캔 :
        for m in lst:
            print(m)
    else:
        break
