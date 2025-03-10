# 명함 정보를 저장할 리스트 (명함을 여러 개 저장할 수 있음)
cards = []

# 무한 반복하여 사용자가 종료(5번 선택)할 때까지 메뉴를 계속 출력
while True:
    print("\n-------------------------------------------------------------------")
    print("1. 명함 입력  2. 명함 수정  3. 명함 삭제  4. 명함 목록 보기  5. 종료")
    print("-------------------------------------------------------------------")

    # 사용자에게 메뉴 선택 입력 받기
    choice = input("메뉴를 선택하세요 >>> ")

    # 1번 선택: 명함 입력
    if choice == '1':  
        print("\n[ 명함 입력 ]")  # 명함 입력 화면 출력
        name = input("이름을 입력해주세요: ")  # 사용자에게 이름 입력받기
        email = input("이메일을 입력해주세요: ")  # 사용자에게 이메일 입력받기
        phone = input("전화번호를 입력해주세요: ")  # 사용자에게 전화번호 입력받기
        affiliation = input("소속(학교/직장)을 입력해주세요: ")  # 사용자에게 소속 입력받기
        
        # 입력받은 정보를 리스트 형태로 저장하여 cards 리스트에 추가
        cards.append([name, email, phone, affiliation])
        print("\n명함이 저장되었습니다.\n")  # 저장 완료 메시지 출력

    # 2번 선택: 명함 수정
    elif choice == '2':  
        if len(cards) == 0:  # 명함이 없을 경우
            print("\n저장된 명함이 없습니다.\n")
            continue  # 다시 메뉴로 돌아감

        print("\n[ 명함 수정 ]")  # 명함 수정 화면 출력
        
        # 저장된 명함 목록 출력 (번호를 붙여줌)
        for i in range(len(cards)):
            print(str(i + 1) + ". " + cards[i][0] + " / " + cards[i][1] + " / " + cards[i][2] + " / " + cards[i][3])
        
        # 수정할 명함 번호 입력받기
        index = input("수정할 명함 번호를 입력해주세요 (0: 취소): ")
        if index == '0':  # 취소 선택 시 메뉴로 돌아감
            continue

        index = int(index) - 1  # 사용자가 입력한 번호를 리스트 인덱스로 변환
        if 0 <= index < len(cards):  # 올바른 범위인지 확인
            print("1. 이름 2. 이메일 3. 전화번호 4. 소속")
            field = input("수정할 항목을 선택해주세요: ")  # 수정할 정보 선택

            # 선택한 항목에 따라 새 값 입력받아 수정
            if field == '1':
                cards[index][0] = input("새로운 이름을 입력해주세요: ")
            elif field == '2':
                cards[index][1] = input("새로운 이메일을 입력해주세요: ")
            elif field == '3':
                cards[index][2] = input("새로운 전화번호를 입력해주세요: ")
            elif field == '4':
                cards[index][3] = input("새로운 소속을 입력해주세요: ")
            else:
                print("잘못된 입력입니다.")  # 유효하지 않은 선택 처리
            
            print("\n명함이 수정되었습니다.\n")  # 수정 완료 메시지 출력
        else:
            print("잘못된 번호입니다.")  # 유효하지 않은 번호 처리

    # 3번 선택: 명함 삭제
    elif choice == '3':  
        if len(cards) == 0:  # 명함이 없을 경우
            print("\n저장된 명함이 없습니다.\n")
            continue

        print("\n[ 명함 삭제 ]")  # 명함 삭제 화면 출력

        # 저장된 명함 목록 출력
        for i in range(len(cards)):
            print(str(i + 1) + ". " + cards[i][0] + " / " + cards[i][1] + " / " + cards[i][2] + " / " + cards[i][3])
        
        # 삭제할 명함 번호 입력받기
        index = input("삭제할 명함 번호를 입력해주세요 (0: 취소, 99: 전체 삭제): ")

        if index == '0':  # 취소 선택 시 메뉴로 돌아감
            continue
        elif index == '99':  # 전체 삭제 선택
            cards = []  # 모든 명함 삭제 (리스트를 비움)
            print("\n모든 명함이 삭제되었습니다.\n")
        else:
            index = int(index) - 1  # 사용자가 입력한 번호를 리스트 인덱스로 변환
            if 0 <= index < len(cards):  # 올바른 범위인지 확인
                del cards[index]  # 선택한 명함 삭제
                print("\n명함이 삭제되었습니다.\n")  # 삭제 완료 메시지 출력
            else:
                print("잘못된 번호입니다.")  # 유효하지 않은 번호 처리

    # 4번 선택: 명함 목록 보기
    elif choice == '4':  
        if len(cards) == 0:  # 명함이 없을 경우
            print("\n저장된 명함이 없습니다.\n")
        else:
            print("\n[ 명함 목록 ]")  # 명함 목록 화면 출력

            # 저장된 명함 출력 (번호를 붙여줌)
            for i in range(len(cards)):
                print(str(i + 1) + ". " + cards[i][0] + " / " + cards[i][1] + " / " + cards[i][2] + " / " + cards[i][3])
            print()

    # 5번 선택: 프로그램 종료
    elif choice == '5':  
        print("\n프로그램을 종료합니다.\n")  # 종료 메시지 출력
        break  # while 문을 빠져나와 프로그램 종료

    # 올바르지 않은 입력 처리
    else:
        print("\n잘못된 입력입니다. 다시 선택해주세요.\n")
