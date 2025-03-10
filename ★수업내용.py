## 명함관리 프로그램 작성
# 1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료버튼

import sys

display = '''
--------------------------------------------------------------
1.명함입력  2.명함수정  3.명함삭제  4.명함목록보기  5.종료
--------------------------------------------------------------
메뉴를 선택하세요 >>> '''

menu = ''
cards = [['하하', '010', '학교', 'gkssk'], ['파파', '098', '직장', 'qppq']]
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
        print('저장된 명함 목록: ', cards)
        
    elif menu == '2':
        if len(cards) == 0:
            print('\n저장된 명함이 없습니다.\n')
            continue

        print("\n[ 명함 수정 ]")
        email = input("수정할 명함의 이메일을 입력해주세요: ")
        check = 0
        for index in range(len(cards)):
        # for index, card in enumerate(cards): (이것도 가능/ 결과값: (인덱스값, 실제값))
            # if card[3] == email:
            if cards[index][3] == email:
                check = 1
                while True:
                    item = input('\n수정할 항목을 선택하세요. \n1.이름 2.번호 3.소속 4.종료 >>> ')
                    if item == '4':
                        break
                    item = int(item)
                    if item in (1,2,3):
                        cards[index][item-1] = input('\n수정할 내용 입력 >>> ')
                    if check == 0:
                        print('잘못된 입력입니다. 다시 선택해주세요.')

    elif menu == '3':
        print("\n[ 명함 삭제 ]")
        email = input('삭제할 명함의 이메일을 입력하세요 : ')
        check = 0
        for index in range(len(cards)):
            if cards[index][3] == email:
                check = 1
                print('삭제 >>> ', cards.pop(index))
                break # 찾았으면 삭제 후 반복문 종료
        if check == 0:
            print('입력된 명함이 없습니다.')

    elif menu == '4':
        print("\n[ 명함 목록 보기 ]")
        print("-" * 60)
        for card in cards:
            print(f'{card[0]} /  {card[1]} /  {card[2]} /  {card[3]}')
        print("-" * 60)

    elif menu == '5':
        print("\n[ 프로그램 종료 ]")
        sys.exit()
    else:
        print('메뉴선택을 잘못하셨습니다.')
