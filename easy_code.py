import sys

# 사용자에게 보여줄 메뉴 화면
# 숫자를 입력받아 해당 기능을 실행하도록 유도

display = '''
--------------------------------------------------------
1. 명함입력 2. 명함수정 3. 명함삭제 4. 명함목록보기 5. 종료
--------------------------------------------------------
메뉴를 선택하세요 >>> '''

cards = []  # 입력받은 명함 목록 (리스트 형태로 저장)

while True:
    menu = input(display)  # 사용자가 선택한 메뉴 입력받기
    
    if menu == '1':  # 1번 선택: 명함 입력
        print("1. 명함입력")
        name = input("이름 >>> ")  # 사용자 이름 입력
        email = input("이메일 >>> ")  # 이메일 입력
        phone = input("전화번호 >>> ")  # 전화번호 입력
        card = [name, email, phone]  # 입력받은 데이터를 리스트에 저장
        cards.append(card)  # 전체 명함 리스트에 추가
        print("명함이 저장되었습니다.")

    elif menu == '2':  # 2번 선택: 명함 수정
        print("2. 명함수정")
        email_to_edit = input("수정할 명함의 이메일 입력 >>> ")  # 수정할 명함 찾기 위해 이메일 입력
        found = False  # 명함 찾았는지 여부 확인용 변수

        for card in cards:  # 명함 목록 순회
            if card[1] == email_to_edit:  # 입력한 이메일과 일치하는 명함 찾기
                print(f"수정할 명함을 찾았습니다: {card}")
                card[0] = input("새로운 이름 입력 >>> ")  # 새 이름 입력
                card[1] = input("새로운 이메일 입력 >>> ")  # 새 이메일 입력
                card[2] = input("새로운 전화번호 입력 >>> ")  # 새 전화번호 입력
                print("명함 정보가 수정되었습니다.")
                found = True  # 명함을 찾았으므로 True 설정
                break  # 수정 후 종료
        if not found:
            print("해당 이메일을 가진 명함이 없습니다.")  # 찾지 못한 경우 메시지 출력

    elif menu == '3':  # 3번 선택: 명함 삭제
        print("3. 명함삭제")
        email_to_delete = input("삭제할 명함의 이메일 입력 >>> ")  # 삭제할 명함의 이메일 입력
        found = False  # 명함 찾았는지 여부 확인용 변수

        for card in cards:  # 명함 목록 탐색
            if card[1] == email_to_delete:  # 입력한 이메일과 일치하는 명함 찾기
                print(f"삭제할 명함을 찾았습니다: {card}")
                cards.remove(card)  # 해당 명함을 리스트에서 제거
                print("명함이 삭제되었습니다.")
                found = True  # 삭제 완료
                break  # 삭제 후 루프 종료
        if not found:
            print("삭제할 명함이 없습니다.")  # 찾지 못한 경우 메시지 출력

    elif menu == '4':  # 4번 선택: 명함 목록 출력
        print("4. 명함목록보기")
        if not cards:  # 저장된 명함이 없을 경우
            print("저장된 명함이 없습니다.")
        else:
            for card in cards:  # 저장된 명함 출력
                print(f"이름: {card[0]}, 이메일: {card[1]}, 전화번호: {card[2]}")

    elif menu == '5':  # 5번 선택: 프로그램 종료
        print("프로그램 종료")
        sys.exit()  # 프로그램 종료

    else:
        print("메뉴 선택을 잘못했습니다. 다시 선택해주세요.")  # 올바른 메뉴 입력 유도
