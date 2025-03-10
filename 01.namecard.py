def input_card():
    """명함 입력 화면"""
    print("\n[ 명함 입력 ]")
    name = input("이름을 입력해주세요: ")
    email = input("이메일을 입력해주세요: ")
    phone = input("전화번호를 입력해주세요: ")
    affiliation = input("소속(학교/직장)을 입력해주세요: ")
    cards.append({"이름": name, "이메일": email, "전화번호": phone, "소속": affiliation})
    print("\n명함이 저장되었습니다.\n")

def edit_card():
    """명함 수정 화면"""
    if not cards:
        print("\n저장된 명함이 없습니다.\n")
        return

    print("\n[ 명함 수정 ]")
    list_cards()
    index = int(input("수정할 명함 번호를 입력해주세요 (0: 취소): ")) - 1
    if index == -1:
        return

    if 0 <= index < len(cards):
        print("1. 이름 2. 이메일 3. 전화번호 4. 소속")
        choice = input("수정할 항목을 선택해주세요: ")

        if choice == '1':
            cards[index]["이름"] = input("새로운 이름을 입력해주세요: ")
        elif choice == '2':
            cards[index]["이메일"] = input("새로운 이메일을 입력해주세요: ")
        elif choice == '3':
            cards[index]["전화번호"] = input("새로운 전화번호를 입력해주세요: ")
        elif choice == '4':
            cards[index]["소속"] = input("새로운 소속을 입력해주세요: ")
        else:
            print("잘못된 입력입니다.")
        
        print("\n명함이 수정되었습니다.\n")
    else:
        print("잘못된 번호입니다.")

def delete_card():
    """명함 삭제 화면"""
    if not cards:
        print("\n저장된 명함이 없습니다.\n")
        return

    print("\n[ 명함 삭제 ]")
    list_cards()
    index = input("삭제할 명함 번호를 입력해주세요 (0: 취소, 99: 전체 삭제): ")

    if index == '0':
        return
    elif index == '99':
        cards.clear()
        print("\n모든 명함이 삭제되었습니다.\n")
        return

    index = int(index) - 1
    if 0 <= index < len(cards):
        del cards[index]
        print("\n명함이 삭제되었습니다.\n")
    else:
        print("잘못된 번호입니다.")

def list_cards():
    """명함 목록 보기"""
    if not cards:
        print("\n저장된 명함이 없습니다.\n")
        return

    print("\n[ 명함 목록 ]")
    for i, card in enumerate(cards, 1):
        print(f"{i}. {card['이름']} / {card['이메일']} / {card['전화번호']} / {card['소속']}")
    print()

cards = []

while True:
    print("\n-------------------------------------------------------------------")
    print("1. 명함 입력  2. 명함 수정  3. 명함 삭제  4. 명함 목록 보기  5. 종료")
    print("-------------------------------------------------------------------")
    
    choice = input("메뉴를 선택하세요 >>> ")

    if choice == '1':
        input_card()
    elif choice == '2':
        edit_card()
    elif choice == '3':
        delete_card()
    elif choice == '4':
        list_cards()
    elif choice == '5':
        print("\n프로그램을 종료합니다.\n")
        break
    else:
        print("\n잘못된 입력입니다. 다시 선택해주세요.\n")