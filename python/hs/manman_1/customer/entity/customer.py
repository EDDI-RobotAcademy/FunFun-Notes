# 고객 객체 생성
customer = Customer()

# 고객이 사과 5개와 배 3개 구매
customer.buy_fruits(mart, ["사과", "배"], [5, 3])

# 고객이 구매한 과일 목록 출력
customer.show_bought_fruits()