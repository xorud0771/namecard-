import sys

display = '''
--------------------------------------------------------
1. 명함입력 2. 명함수정 3. 명함삭제 4. 명함목록보기 5. 종료
--------------------------------------------------------
메뉴를 선택하세요 >>> '''

# display 명함 메뉴 보여주고 입력 받기(int : 숫자로 입력)
menu = int(input(display))

# 메뉴 입력에 따라 다음 실행
# 1. 명함입력

card = [] # 입력 받을 명함을 넣을 빈 리스트
cards = [] # 입력 받은 명함 목록 -> 입력 받은 명함을 추가로 계속 넣어줄 거임.
if menu == '1':
    print("1. 명함입력")
    name = input("이름 >>> ")
    email = input("이메일 >>> ")
    phone = input("전화번호 >>> ")
    card = [name, email, phone]
    cards.append(card)
    print("명함이 저장되었습니다.")
    print(card)

elif menu == '2':
    print("2. 명함수정")

    # 수정 원하는 명함의 이메일을 입력 받는다. 
    # 입력 받은 이메일을 명함 목록에 있는 이메일과 비교하여 찾는다. 
    # 다시 재입력 받는다. 

    while True:
        email_to_edit = input("수정 원하는 명함의 이메일 입력 >>> ")
        check = 0 # 명함을 찾았는 지 확인하는 변수 

        for card in cards: # 명함 목록 탐색
            if card[1] == email_to_edit:
                check = 1
                print(f"수정할 명함을 찾았습니다.{card}")

                # 변경할 데이터 입력하고 대체
                card[0] = input("새로운 이름 입력 >>> ") 
                card[1] = input("새로운 이메일 입력 >>> ")
                card[2] = input("새로운 전화번호 입력 >>> ")
                print(f"명함 정보가 수정되었습니다.{card}")
            break
        else:
            print("해당 이메일을 가진 명함이 없습니다.")

elif menu == '3':
    print("명함삭제")

    while True:
        email_to_delete = input("삭제하기를 원하는 명함의 이메일 입력 >>> ")
        check = 0

        for card in cards :
            if card[1] == email_to_delete :
                check = 1
                print(f"삭제할 명함을 찾았습니다. {card}")
                card.pop()
                break
            else :
                print("삭제할 명함이 없습니다.")

elif menu == "4" :
    print("명함목록보기")
    for card in cards :
        print(f'{card[0]}{card[1]}{card[2]}')

elif menu == "5" :
    print("프로그램 종료")
    sys.exit()

else:
    print('메뉴 선택을 잘못했습니다. 다시 선택해주세요')        

