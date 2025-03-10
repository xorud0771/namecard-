cards = []  # 명함 저장 리스트

while True:
    print("\n-------------------------------------------------------------------")
    print("1. 명함 입력  2. 명함 수정  3. 명함 삭제  4. 명함 목록 보기  5. 종료")
    print("-------------------------------------------------------------------")

    choice = input("메뉴를 선택하세요 >>> ")

    if choice == '1':  # 명함 입력
        print("\n[ 명함 입력 ]")
        name = input("이름을 입력해주세요: ")
        email = input("이메일을 입력해주세요: ")
        phone = input("전화번호를 입력해주세요: ")
        affiliation = input("소속(학교/직장)을 입력해주세요: ")
        cards.append([name, email, phone, affiliation])
        print("\n명함이 저장되었습니다.\n")
        fgff