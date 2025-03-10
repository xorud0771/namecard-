cards = []  # 명함 저장 리스트

while True:
    print("\n-------------------------------------------------------------------")
    print("1. 명함 입력  2. 명함 수정  3. 명함 삭제  4. 명함 목록 보기  5. 종료")
    print("-------------------------------------------------------------------")

    choice = input("메뉴를 선택하세요 >>> ")

    if choice == '1':  # 명함 입력
        print("\n[ 명함 입력 ]")
        name = input("이름을 입력해주세요: ")
        email = input("이메일을 입력해주세요: ")
        phone = input("전화번호를 입력해주세요: ")
        affiliation = input("소속(학교/직장)을 입력해주세요: ")
        cards.append([name, email, phone, affiliation])
        print("\n명함이 저장되었습니다.\n")

    elif choice == '2':  # 명함 수정
        if len(cards) == 0:
            print("\n저장된 명함이 없습니다.\n")
            continue

        print("\n[ 명함 수정 ]")
        for i in range(len(cards)):
            print(str(i + 1) + ". " + cards[i][0] + " / " + cards[i][1] + " / " + cards[i][2] + " / " + cards[i][3])
        
        index = input("수정할 명함 번호를 입력해주세요 (0: 취소): ")
        if index == '0':
            continue

        index = int(index) - 1
        if 0 <= index < len(cards):
            print("1. 이름 2. 이메일 3. 전화번호 4. 소속")
            field = input("수정할 항목을 선택해주세요: ")

            if field == '1':
                cards[index][0] = input("새로운 이름을 입력해주세요: ")
            elif field == '2':
                cards[index][1] = input("새로운 이메일을 입력해주세요: ")
            elif field == '3':
                cards[index][2] = input("새로운 전화번호를 입력해주세요: ")
            elif field == '4':
                cards[index][3] = input("새로운 소속을 입력해주세요: ")
            else:
                print("잘못된 입력입니다.")
            
            print("\n명함이 수정되었습니다.\n")
        else:
            print("잘못된 번호입니다.")

    elif choice == '3':  # 명함 삭제
        if len(cards) == 0:
            print("\n저장된 명함이 없습니다.\n")
            continue

        print("\n[ 명함 삭제 ]")
        for i in range(len(cards)):
            print(str(i + 1) + ". " + cards[i][0] + " / " + cards[i][1] + " / " + cards[i][2] + " / " + cards[i][3])
        
        index = input("삭제할 명함 번호를 입력해주세요 (0: 취소, 99: 전체 삭제): ")

        if index == '0':
            continue
        elif index == '99':
            cards = []
            print("\n모든 명함이 삭제되었습니다.\n")
        else:
            index = int(index) - 1
            if 0 <= index < len(cards):
                del cards[index]
                print("\n명함이 삭제되었습니다.\n")
            else:
                print("잘못된 번호입니다.")

    elif choice == '4':  # 명함 목록 보기
        if len(cards) == 0:
            print("\n저장된 명함이 없습니다.\n")
        else:
            print("\n[ 명함 목록 ]")
            for i in range(len(cards)):
                print(str(i + 1) + ". " + cards[i][0] + " / " + cards[i][1] + " / " + cards[i][2] + " / " + cards[i][3])
            print()

    elif choice == '5':  # 프로그램 종료
        print("\n프로그램을 종료합니다.\n")
        break

    else:
        print("\n잘못된 입력입니다. 다시 선택해주세요.\n")