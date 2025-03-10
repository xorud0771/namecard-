# 명함 정보를 저장할 리스트
cards = []

# 프로그램 실행 (무한 반복)
while True:
    print("\n-------------------------------------------------------------------")
    print("1. 명함 입력  2. 명함 수정  3. 명함 삭제  4. 명함 목록 보기  5. 종료")
    print("-------------------------------------------------------------------")

    # 사용자 입력 받기
    choice = input("메뉴를 선택하세요 >>> ")

    # 1번 선택: 명함 입력
    if choice == '1':
        print("\n[ 명함 입력 ]")
        name = input("이름을 입력해주세요: ")
        email = input("이메일을 입력해주세요: ")
        phone = input("전화번호를 입력해주세요: ")
        affiliation = input("소속(학교/직장)을 입력해주세요: ")

        # 입력받은 정보를 리스트에 추가
        card = [name, email, phone, affiliation]
        cards.append(card)
        print("\n명함이 저장되었습니다.\n")

    # 2번 선택: 명함 수정
    elif choice == '2':
        if len(cards) == 0:
            print("\n저장된 명함이 없습니다.\n")
            continue  # 다시 메뉴로 돌아감

        print("\n[ 명함 수정 ]")
        
        name1 = input("수정할 명함 이름을 입력해주세요 (0: 취소): ")
        if name1 == '0':
            continue  # 메뉴로 돌아감

        name1 = index - 1
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

    # 3번 선택: 명함 삭제
    elif choice == '3':
        if len(cards) == 0:
            print("\n저장된 명함이 없습니다.\n")
            continue

        print("\n[ 명함 삭제 ]")
        i = 0
        while i < len(cards):
            card = cards[i]
            print(str(i + 1) + ". " + card[0] + " / " + card[1] + " / " + card[2] + " / " + card[3])
            i += 1

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

    # 4번 선택: 명함 목록 보기
    elif choice == '4':
        if len(cards) == 0:
            print("\n저장된 명함이 없습니다.\n")
        else:
            print("\n[ 명함 목록 ]")
            i = 0
            while i < len(cards):
                card = cards[i]
                print(str(i + 1) + ". " + card[0] + " / " + card[1] + " / " + card[2] + " / " + card[3])
                i += 1
            print()

    # 5번 선택: 프로그램 종료
    elif choice == '5':
        print("\n프로그램을 종료합니다.\n")
        break  # 프로그램 종료

    # 잘못된 입력 처리
    else:
        print("\n잘못된 입력입니다. 다시 선택해주세요.\n")
# 명함 정보를 저장할 리스트
cards = []

# 프로그램 실행 (무한 반복)
while True:
    print("\n-------------------------------------------------------------------")
    print("1. 명함 입력  2. 명함 수정  3. 명함 삭제  4. 명함 목록 보기  5. 종료")
    print("-------------------------------------------------------------------")

    # 사용자 입력 받기
    choice = input("메뉴를 선택하세요 >>> ")

    # 1번 선택: 명함 입력
    if choice == '1':
        print("\n[ 명함 입력 ]")
        name = input("이름을 입력해주세요: ")
        email = input("이메일을 입력해주세요: ")
        phone = input("전화번호를 입력해주세요: ")
        affiliation = input("소속(학교/직장)을 입력해주세요: ")

        # 입력받은 정보를 리스트에 추가
        card = [name, email, phone, affiliation]
        cards.append(card)
        print("\n명함이 저장되었습니다.\n")

    # 2번 선택: 명함 수정
    elif choice == '2':
        if len(cards) == 0:
            print("\n저장된 명함이 없습니다.\n")
            continue  # 다시 메뉴로 돌아감

        print("\n[ 명함 목록 ]")
        print(cards)  # 전체 목록 출력

        name1 = input("수정할 명함의 이름을 입력해주세요 (0: 취소): ")
        if name1 == '0':
            continue  # 메뉴로 돌아감

        # 입력한 이름과 같은 명함 찾기
        index = 0
        selected_card = None

        while index < len(cards):
            if cards[index][0] == name1:
                selected_card = cards[index]
                break  # 찾으면 종료
            index += 1

        if selected_card:  # 명함을 찾았을 경우
            print("\n현재 명함 정보:", selected_card)
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
            print("\n해당 이름의 명함이 없습니다.\n")

    # 3번 선택: 명함 삭제
    elif choice == '3':
        if len(cards) == 0:
            print("\n저장된 명함이 없습니다.\n")
            continue

        print("\n[ 명함 삭제 ]")
        print(cards)  # 전체 목록 출력

        name1 = input("삭제할 명함의 이름을 입력해주세요 (0: 취소, 99: 전체 삭제): ")

        if name1 == '0':
            continue
        elif name1 == '99':
            cards = []
            print("\n모든 명함이 삭제되었습니다.\n")
        else:
            index = 0
            found = False
            while index < len(cards):
                if cards[index][0] == name1:
                    del cards[index]
                    found = True
                    print("\n명함이 삭제되었습니다.\n")
                    break
                index += 1
            
            if not found:
                print("\n해당 이름의 명함이 없습니다.\n")

    # 4번 선택: 명함 목록 보기
    elif choice == '4':
        if len(cards) == 0:
            print("\n저장된 명함이 없습니다.\n")
        else:
            print("\n[ 명함 목록 ]")
            print(cards)  # 전체 목록 출력
            print()

    # 5번 선택: 프로그램 종료
    elif choice == '5':
        print("\n프로그램을 종료합니다.\n")
        break  # 프로그램 종료

    # 잘못된 입력 처리
    else:
        print("\n잘못된 입력입니다. 다시 선택해주세요.\n")
