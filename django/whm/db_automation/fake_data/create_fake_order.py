import os
import sys

import django
import random
from django.db import transaction

# Django settings 모듈 설정
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db_automation.settings")
django.setup()

from decimal import Decimal
from django.utils import timezone

from account.entity.account import Account
from orders.entity.orders import Orders
from orders.entity.orders_items import OrdersItems
from game_software.entity.game_software import GameSoftware
from game_software.entity.game_software_price import GameSoftwarePrice


# 계정과 게임 소프트웨어 데이터에서 랜덤으로 선택하여 주문 생성
def generate_orders_data():
    accounts = Account.objects.all()
    game_software_list = list(GameSoftware.objects.all())  # 쿼리셋을 리스트로 변환
    prices = GameSoftwarePrice.objects.all()

    for _ in range(1000):
        # 랜덤으로 계정 선택
        account = random.choice(accounts)

        # 주문 총액 계산
        total_amount = Decimal(0)

        # 랜덤으로 1개 이상의 게임 소프트웨어 선택
        game_software_choices = random.sample(game_software_list, random.randint(1, 5))  # 최대 5개까지 선택

        # 주문 생성
        order = Orders(
            account=account,
            total_amount=total_amount,
            status="PENDING",  # 기본값
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        order.save()

        # 주문 항목 생성
        for game_software in game_software_choices:
            # 게임 소프트웨어 가격 찾기
            price = random.choice(prices)
            price_value = price.price  # 가격 가져오기

            # 주문 항목 생성
            order_item = OrdersItems(
                orders=order,
                game_software=game_software,
                quantity=random.randint(1, 3),  # 게임 수량은 1~3개
                price=price_value
            )
            order_item.save()

            # 총액 업데이트
            total_amount += price_value * order_item.quantity

        # 총액 업데이트
        order.total_amount = total_amount
        order.save()


generate_orders_data()