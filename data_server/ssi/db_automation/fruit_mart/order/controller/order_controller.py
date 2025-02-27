
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from fruit_mart.order.service.service_impl import OrderServiceImpl
from fruit_mart.order.repository.order_repository_impl import OrderRepositoryImpl
class OrderController(viewsets.ViewSet):
    orderService = OrderServiceImpl.getInstance()
    orderRepository = OrderRepositoryImpl.getInstance()

    def sell_item(self, request):
        print(f"Reached sell_item: {request.method}")
        print(f"Received data: {request.data}")
        customer = request.data.get('customer_id')
        fruit = request.data.get('fruit')
        number = request.data.get('number')

        try:
            order = self.orderService.buyFruit(customer, fruit, number)
            order_data = {
                'id': order.id,
                'customer': order.customerNickName,
                'fruit': order.fruitType,
                'number': order.buyNumber
            }
            return Response(order_data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            print(f"Error: {e}")
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_customer_orders(self, request):
        customer_name = request.query_params.get('customer-name')

        if not customer_name:
            return Response({"error": "Customer name is required"}, status=status.HTTP_400_BAD_REQUEST)

        orders = self.orderRepository.findByCustomer(customer_name)
        if not orders.exists():
            return Response({"message": "No orders found for this customer"}, status=status.HTTP_404_NOT_FOUND)

        order_data = [
            {
                "id": order.id,
                "customer": order.customerNickName,
                "fruit": order.fruitType,
                "number": order.buyNumber
            }
            for order in orders
        ]
        return Response(order_data, status=status.HTTP_200_OK)
    
    def refund_order(self, request):
        try:
            customer_name = request.data.get('customer_name')
            order_id = request.data.get('order_id')
            refund_item = request.data.get('refund_item')
            refund_quantity = request.data.get('refund_quantity')

            print(f"Received data: customer_name={customer_name}, order_id={order_id}, refund_item={refund_item}, refund_quantity={refund_quantity}")

            if not all([customer_name, order_id, refund_item, refund_quantity]):
                return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

            refund_quantity = int(refund_quantity)
            updated_order = self.orderService.refundOrder(order_id, refund_quantity, refund_item)

            return Response({
                "message": "Refund processed successfully",
                "order_id": updated_order.id,
                "remaining_quantity": updated_order.buyNumber
            }, status=status.HTTP_200_OK)
        except ValueError as e:
            print(f"ValueError: {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Exception: {e}")
            return Response({"error": "Internal server error", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        