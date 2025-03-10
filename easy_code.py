# 배운 코드로만 정리해봤습니다

display = ('''
-----------------------------------------------------------
1. 명함입력, 2. 명함수정, 3. 명함삭제 4. 명함목록보기, 5.종료
-----------------------------------------------------------
메뉴를 선택하세요 >>> ''')


business_card = []
menu = ''


while True :
    menu = input(display)
    if menu == '1':
        print('(명함입력)')
        print("명함 정보를 입력하세요:")
        name = input("이름: ")
        email = input("이메일: ")
        phone = input("전화번호: ")
        belong = input("소속 : ")


        card = [name, phone, email, belong]
        business_card.append(card)
        print(f"{name}님의 명함이 입력되었습니다.")
        print(business_card)
    elif menu == '2':
        print('명함수정')
        Q1 = input('수정할 명함이 있습니까? (Y / N)')
        if Q1 == 'Y' :
            name = input("수정할 사람의 이름을 입력하시오.")
            if name in business_card :
                business_card[1] = input('새 이메일 :')
                business_card[2] = input('새 전화번호 :')
                business_card[3] = input('새 소속 :')
                print(f"'{name}'님의 명함이 수정되었습니다.")
            else : print("해당 이름의 명함을 찾을 수 없습니다.")
    elif menu == '3':
        print('명함삭제')
        remove = input('삭제할 명함 이름을 입력하시오')
        if remove in business_card :
            business_card.remove({remove})
            print(f"'{name}'님의 명함이 삭제되었습니다.")
        else : print("해당 이름의 명함을 찾을 수 없습니다.")
    elif menu == '4':
        print('명함목록')
    elif menu == '5':
        print('프로그램 종료')
        sys.exit()
    else :
        print('메뉴선택을 잘못함.')
