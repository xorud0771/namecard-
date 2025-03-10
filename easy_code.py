import sys

# 메뉴 화면 출력
display = ('''
-----------------------------------------------------------
1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료
-----------------------------------------------------------
메뉴를 선택하세요 >>> ''')

# 명함 정보를 저장할 리스트
business_card = []

# 프로그램 무한 반복 실행
while True:
    menu = input(display)  # 메뉴 화면
    if menu == '1':
        print("1. 명함입력")
        name = input("이름: ")
        email = input("이메일: ")
        phone = input("전화번호: ")
        belong = input("소속: ")

        card = [name, email, phone, belong]  # 순서 오류 수정 (이메일이 두 번째)
        business_card.append(card)
        print(f"\n{name}님의 명함이 입력되었습니다.")
        print("현재 명함 목록:", business_card)

    elif menu == '2':
        print('명함 수정')
        name_to_edit = input("수정할 명함의 이름을 입력하세요: ")

        index = 0  # 리스트 탐색을 위한 인덱스 변수 생성
        found = False  # 명함을 찾았는지 여부 확인 변수

        while index < len(business_card):  # 명함 목록이 있을 때 반복
            if business_card[index][0] == name_to_edit:  # 이름이 일치하는 명함 찾기
                found = True
                print("\n현재 명함 정보:", business_card[index])  # 기존 명함 출력

                # 새 정보 입력 받아 기존 데이터 대체
                business_card[index][0] = input("새 이름: ")
                business_card[index][1] = input("새 이메일: ")
                business_card[index][2] = input("새 전화번호: ")
                business_card[index][3] = input("새 소속(학교/직장): ")

                print("\n수정된 명함 정보:", business_card[index])
                print(f"\n'{name_to_edit}'님의 명함이 수정되었습니다.")
                break  # 명함을 찾고 수정한 후 종료
            index += 1  # 다음 명함으로 이동

        if not found:  # 리스트를 끝까지 돌았어도 못 찾았다면
            print("\n수정할 명함을 찾지 못했습니다. 다시 입력해주세요.")

    elif menu == '3':
        print('명함 삭제')
        remove = input('삭제할 명함의 이름을 입력하세요: ')

        index = 0
        found = False  # 명함 찾았는지 여부

        while index < len(business_card):
            if business_card[index][0] == remove:  # 이름이 일치하면 삭제
                del business_card[index]
                found = True
                print(f"\n'{remove}'님의 명함이 삭제되었습니다.")
                break  # 삭제 완료 후 종료
            index += 1

        if not found:
            print("\n해당 이름의 명함을 찾을 수 없습니다.")

    elif menu == '4':
        print('\n[ 명함 목록 ]')
        if len(business_card) == 0:
            print("저장된 명함이 없습니다.")
        else:
            index = 0
            while index < len(business_card):
                print(f"{index + 1}. {business_card[index]}")
                index += 1

    elif menu == '5':
        print('\n프로그램 종료')
        sys.exit()

    else:
        print("\n메뉴 선택을 잘못하셨습니다. 다시 입력해주세요.")
