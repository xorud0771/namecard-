import sys  # 프로그램 종료를 위해 sys 모듈 사용

# 메뉴 화면 출력
display = ('''
-----------------------------------------------------------
1. 명함입력, 2. 명함수정, 3. 명함삭제, 4. 명함목록보기, 5. 종료
-----------------------------------------------------------
메뉴를 선택하세요 >>> ''')

# 명함 정보를 저장할 리스트 (각 명함은 리스트 형태로 저장됨: [이름, 이메일, 전화번호, 소속])
business_card = []

# 프로그램 무한 반복 실행 (사용자가 종료할 때까지 계속 실행됨)
while True:
    menu = input(display)  # 사용자에게 메뉴 선택 입력받기

    # 1번 선택: 명함 입력
    if menu == '1':
        print("1. 명함입력")  
        
        # 사용자로부터 명함 정보를 입력받기
        name = input("이름: ")  
        while True:
            email = input("이메일: ") # 이메일이 중복되는지 확인한다. 
            check = 0
            for index in range(len(business_card)):
                if business_card[index][1] == email :
                    check = 1 
                    print("중복된 이메일이 있습니다. 다시 입력해주세요.")
                    break
            if check == 0 :
                break # 동일한 내용을 찾지 못했다면 이메일 입력 받은 걸로 끝내면 된다.
        phone = input("전화번호: ")
        belong = input("소속: ")

        # 입력받은 정보를 리스트 형태로 저장
        card = [name, email, phone, belong]  # 명함 정보 리스트
        business_card.append(card)  # 명함 목록(business_card)에 추가

        # 입력된 명함 정보 출력
        print(f"\n{name}님의 명함이 입력되었습니다.")
        print("현재 명함 목록:", business_card)  # 전체 명함 리스트 출력

    # 2번 선택: 명함 수정
    elif menu == '2':
        print('명함 수정')
        name_to_edit = input("수정할 명함의 이름을 입력하세요: ")  # 수정할 명함의 이름 입력받기

        index = 0  # 리스트 탐색을 위한 인덱스 변수 (명함 찾기)
        found = False  # 명함을 찾았는지 여부 확인 변수

        for index in range(len(business_card)):
            if business_card[index][1] == name_to_edit :
                found = True
                while True:
                    item = input("수정할 항목을 선택하세요(1.이름 2. 전화번호 3. 이메일 4. 소속 5. 종료)")
                    if item == '5':
                        print("수정을 종료하겠습니다.")
                        break
                    item = int(item)
                    if item in (1,2,3,4):
                        business_card[index][item-1] = input("수정할 값을 입력 >>> ")

    # 3번 선택: 명함 삭제
    elif menu == '3':
        print('명함 삭제')
        remove = input('삭제할 명함의 이름을 입력하세요: ')  # 삭제할 명함 이름 입력받기

        index = 0  # 리스트 탐색을 위한 인덱스 변수
        found = False  # 명함 찾았는지 여부

        # 명함 목록을 탐색하며 입력한 이름과 일치하는 명함 찾기
        while index < len(business_card):
            if business_card[index][0] == remove:  # 이름이 일치하면 삭제
                del business_card[index]  # 해당 명함을 리스트에서 삭제
                found = True  # 명함을 찾았음을 표시
                print(f"\n'{remove}'님의 명함이 삭제되었습니다.")
                break  # 삭제 완료 후 반복 종료
            index += 1  # 다음 명함으로 이동

        # 리스트를 끝까지 탐색했지만 명함을 찾지 못한 경우 메시지 출력
        if not found:
            print("\n해당 이름의 명함을 찾을 수 없습니다.")

    # 4번 선택: 명함 목록 보기
    elif menu == '4':
        print('\n[ 명함 목록 ]')  # 명함 목록 출력

        if len(business_card) == 0:  # 명함이 하나도 없는 경우
            print("저장된 명함이 없습니다.")
        else:
            index = 0  # 리스트 탐색을 위한 인덱스 변수
            while index < len(business_card):  # 명함 목록이 있을 경우 반복 실행
                print(f"{index + 1}. {business_card[index]}")  # 각 명함 출력
                index += 1  # 다음 명함으로 이동

    # 5번 선택: 프로그램 종료
    elif menu == '5':
        print('\n프로그램 종료')
        sys.exit()  # 프로그램 종료 (sys.exit() 사용)

    # 잘못된 입력 처리
    else:
        print("\n메뉴 선택을 잘못하셨습니다. 다시 입력해주세요.")
