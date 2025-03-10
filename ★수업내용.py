## 명함관리 프로그램 작성
# 1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료버튼

import sys

display = '''
--------------------------------------------------------------
1.명함입력  2.명함수정  3.명함삭제  4.명함목록보기  5.종료
--------------------------------------------------------------
메뉴를 선택하세요 >>> '''

menu = ''
cards = []
while True:
    menu = input(display)
    # 1번 선택: 명함 입력
    if menu == '1':
        print("\n[ 명함 입력 ]")
        name = input("이름: ")
        phone = input("전화번호: ")
        affiliation = input("소속(학교/직장): ")
        while True:
            email = input("이메일: ")
            check = 0
            for index in range(len(cards)):
                if cards[index][3] == email:
                    check = 1
                    print('다른 이메일을 입력하세요. ')
                    break
            if check == 0:
                break
            # 이메일 중복 금지를 위한 코드 

        # 입력받은 정보를 리스트에 추가
        card = [name, phone, affiliation, email]
        cards.append(card)
        print("\n명함이 저장되었습니다.\n")
        print(card)
        
    elif menu == '2':
        if len(cards) == 0:
            print('\n저장된 명함이 없습니다.\n')
            continue

        print("\n[ 명함 수정 ]")
        named = input("수정할 명함의 이메일을 입력해주세요: ")
        check = 0
        for index in range(len(cards)):
            if cards[index][3] == email:
                check = 1
                while True:
                    item = input('수정할 항목을 선택하세요. \n1.이름 2.번호 3.소속 4.종료 >>> ')
                    if item == '4':
                        break
                    item = int(item)
                    if item in (1,2,3):
                        cards[index][item-1] = input('수정할 내용 입력 >>> ')
                    if check == 0:
                        print('데이터가 없습니다.')
            if card[0] == named:
                print("\n1. 이름 2. 이메일 3. 전화번호 4. 소속")
                field = input("수정할 항목을 선택해주세요: ")

    elif menu == '3':
        print("\n[ 명함 삭제 ]")
        email = input('삭제할 명함의 이메일을 입력하세요. ')
        check = 0
        for index in range(len(cards)):
            if cards[index][3] == email:
                check = 1
                print('삭제 >>> ', cards.pop(index))
                break
            if check == 0:
                print('입력된 명함이 없습니다.')

    elif menu == '4':
        print("\n[ 명함 목록 보기 ]")
        for card in cards:
            print(f'{card[0]} {card[1]} {card[2]} {card[3]}')

    elif menu == '5':
        print("\n[ 프로그램 종료 ]")
        sys.exit()
    else:
        print('메뉴선택을 잘못하셨습니다.')
