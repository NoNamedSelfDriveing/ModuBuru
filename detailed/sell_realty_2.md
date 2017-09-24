1.	걸린 토지의 토지 카드를 바코드로 찍는 순간 바로 그 토지 카드의 벌금과 현재 플레이어의 현금 소유액을 비교하는 함수 로 점프한다(파산 여부를 떠나 이 과정은 벌금 납부 과정에 매번 시행된다).
2.	벌금과 현재 플레이어의 현금 소유액 비교를 통해 나오는 결과는 다음과 같다.

	-	2-1. 벌금이 현금 소유액보다 같거나 낮은 경우

		-	현금 소유액을 벌금만큼 차감하는 함수로 점프한다.
		-	차감 후 현재 플레이어의 현금 잔액을 표시해준다.

	-	2-2. 벌금이 현재 소유액보다 높은 경우

		-	현재 플레이어가 부동산 판매로 벌금을 납부할 수 있는지 검사한다.
			-	부동산 판매로 벌금을 납부할 수 없다면 바로 파산 신청 버튼을 누른 결과로 이동한다.
		-	부동산 판매 버튼과 파산 신청 버튼 중 하나를 선택한다.
		-	부동산 판매 버튼을 눌렀다면 부동산 판매 창을 띄워준다.
		-	부동산 판매 창에는 현재 플레이어가 소유한 부동산들이 리스트로 보여진다.