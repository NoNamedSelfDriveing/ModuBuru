1.	**부동산 판매 창** 밑 쪽 "TOTAL : " 이 표시된 텍스트 상자에 계속 나타나는 선택된 토지들의 총 가격을 변수에 실시간으로 저장하고 있는다.<br><br>
2.	판매 버튼이 눌리면 각종 데이터를 삭제하는 과정이 끝난 후 벌금만큼의 돈을 현찰로 인출한다.

	-	벌금만큼의 돈을 현찰로 인출한다.
	-	현재 플레이어가 걸렸던 **토지의 소유자** 는 인출된 돈을 받는다.
	-	이 **토지의 소유자** 의 데이터 베이스의 현금 소유액은 벌금만큼 증가한다.<br><br>

3.	일정 시간 대기 후 선택된 토지들의 총 가격을 저장한 변수 값에서 벌금을 뺀 만큼의 돈(잔돈)을 인출한다.

	-	현재 플레이어(걸린 플레이어)는 이 돈(잔돈)을 받는다.
	-	현재 플레이어의 데이터 베이스의 현금 소유액은 받은 잔돈만큼 증가한다.<br><br>

4.	**부동산 판매 창** 에 **완료** 버튼을 누르면 창은 사라지고 홈 화면으로 돌아간다.