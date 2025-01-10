import os
import sys
import random
import pandas as pd
from decimal import Decimal
from django.db import models
from django.utils import timezone
import django
from datetime import datetime, timedelta

# Django settings 모듈 설정
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db_automation.settings")
django.setup()

from account.entity.account import Account
from orders.entity.orders import Orders
from orders.entity.orders_items import OrdersItems


# 가짜 나이 값 생성 함수
def generate_fake_age():
    # 30대가 상대적으로 많이 생성되도록 가중치를 조정
    age_group = [random.randint(20, 29) for _ in range(30)] + \
                [random.randint(30, 39) for _ in range(50)] + \
                [random.randint(40, 59) for _ in range(20)]
    return random.choice(age_group)


# 가짜 주문 날짜 생성 함수 (최근 1년 내 날짜)
def generate_fake_date():
    days_ago = random.randint(0, 365)
    fake_date = datetime.now() - timedelta(days=days_ago)
    # 시간도 랜덤으로 설정
    fake_time = timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    return fake_date - fake_time


# 게임별 인기와 가격을 다르게 설정하는 함수
def game_price_adjustment(game_title):
    popular_keywords = ["유니콘 오버로드", "test", "포켓몬스터"]  # Popular 게임 제목 예시

    # 인기 있는 게임은 가격이 더 높고, 판매량도 많음
    if any(keyword in game_title for keyword in popular_keywords):
        price_factor = random.uniform(1.0, 1.3)  # 가격 범위 확장 (3.0 ~ 5.0배)
        quantity_factor = random.randint(300, 1000)  # 수량 범위 확장 (200 ~ 500)
    else:
        price_factor = random.uniform(0.3, 0.8)  # 가격 범위 축소 (0.1 ~ 0.3배)
        quantity_factor = random.randint(300, 1000)  # 수량 범위 축소 (5 ~ 15)
    return price_factor, quantity_factor


# 주문 항목 가져오기
orders_items = OrdersItems.objects.all()

# 결과 저장할 리스트
data = []

# 각 주문 항목에 대해 데이터를 처리
for item in orders_items:
    # 주문 정보 가져오기
    order = item.orders

    # 계정의 나이 생성 (가짜 나이 추가)
    age = generate_fake_age()

    # 게임별 가격 조정 및 수량 설정
    price_factor, quantity_factor = game_price_adjustment(item.game_software.title)

    # 가격과 수량 조정
    price = round(item.price * Decimal(price_factor), 2)  # 가격 변동
    quantity = max(item.quantity + random.randint(0, quantity_factor), 1)  # 수량 변동
    total_price = round(price * quantity, 2)

    # 데이터 추가
    data.append({
        "order_id": order.id,  # 주문 ID
        "game_software_title": item.game_software.title,  # 게임 소프트웨어
        "quantity": quantity,  # 수량
        "price": price,  # 가격
        "total_price": total_price,  # 총액
        "account_id": order.account.id,  # 계정 ID
        "age": age,  # 가짜 나이
        "order_date": generate_fake_date()  # 주문 날짜
    })

# Pandas DataFrame 생성
df = pd.DataFrame(data)

# 엑셀로 내보내기
output_file = "orders_items_with_age5.xlsx"
df.to_excel(output_file, index=False)

print(f"엑셀 파일로 내보내기 완료: {output_file}")
