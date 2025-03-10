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
    elif choice == '2' :
        name_edit = input("수정할 명함의 이름을 입력하세요.") # 이름을 입력하세요
        index = cards[][0]
        print(cards[index][0)
        


        
        
