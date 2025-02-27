from django.urls import path
from . import controller
from fruit_mart.mart.controller.mart_controller import MartController
from fruit_mart.order.controller.order_controller import OrderController

urlpatterns = [
    path('', controller.index, name='index'),  # 기본 경로에 대해 index 뷰로 매핑
    path('create_or_update_fruit/', MartController.as_view({'post': 'create_or_update_fruit'}), name='create_or_update_fruit'),
    path('get_all_fruits/', MartController.as_view({'get': 'get_all_fruits'}), name='get_all_fruits'),
    path('get_fruit_by_name/', MartController.as_view({'get': 'get_fruit_by_name'}), name='get_fruit_by_name'),
    path('order/sell/', OrderController.as_view({'post': 'sell_item'}), name='sell_item'),
    path('order/customer-orders/', OrderController.as_view({'get': 'get_customer_orders'}), name='customer-orders'),
    path('order/refund/', OrderController.as_view({'post': 'refund_order'}), name='refund_order'),
]
    # 다른 URL 경로들 추가

