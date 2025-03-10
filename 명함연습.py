import sys

business_cards = []  # 명함 저장 리스트

while True:
    menu = input("\n📌 1. 입력 | 2. 수정 | 3. 삭제 | 4. 목록 | 5. 종료 → 선택: ")

    if menu == '1':  # 명함 입력
        business_cards.append([
            input("이름: ").strip(), input("이메일: ").strip(), 
            input("전화번호: ").strip(), input("소속: ").strip()
        ])
        print("✅ 명함이 저장되었습니다.")

    elif menu == '2':  # 명함 수정 (이름 포함)
        old_name = input("수정할 사람의 이름: ").strip()
        for card in business_cards:
            if card[0] == old_name:
                print(f"\n현재 정보 → 이름: {card[0]}, 이메일: {card[1]}, 전화번호: {card[2]}, 소속: {card[3]}")
                
                new_name = input("새 이름 (Enter: 변경 없음): ").strip() or card[0]
                card[0] = new_name  # 이름 변경 가능
                card[1] = input("새 이메일 (Enter: 변경 없음): ").strip() or card[1]
                card[2] = input("새 전화번호 (Enter: 변경 없음): ").strip() or card[2]
                card[3] = input("새 소속 (Enter: 변경 없음): ").strip() or card[3]

                print(f"✅ '{old_name}' → '{new_name}'님의 명함이 수정되었습니다.")
                break
        else:
            print("❌ 해당 이름의 명함을 찾을 수 없습니다.")

    elif menu == '3':  # 명함 삭제
        name = input("삭제할 이름: ").strip()
        business_cards = [card for card in business_cards if card[0] != name]
        print("✅ 삭제 완료!")

    elif menu == '4':  # 명함 목록
        print("\n📜 [ 명함 목록 ]")
        if business_cards:
            for card in business_cards:
                print(f"🔹 {card[0]} | {card[1]} | {card[2]} | {card[3]}")
        else:
            print("🚫 저장된 명함 없음")

    elif menu == '5':  # 프로그램 종료
        print("👋 종료합니다!")
        sys.exit()

    else:
        print("⚠️ 올바른 번호 입력!")