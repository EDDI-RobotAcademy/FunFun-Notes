<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card>
                    <v-card-title>Shopping Cart</v-card-title>
                    <v-card-text>
                        <v-table>
                            <thead>
                            <tr>
                                <th>Select</th>
                                <th>Product</th>
                                <th>Price</th>
                                <th>Quantity</th>
                                <th>Total</th>
                                <th>Actions</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr v-for="item in cartItems" :key="item.cartItemId">
                                <td>
                                    <v-checkbox v-model="selectedItems" :value="item"></v-checkbox>
                                </td>
                                <td>{{ item.productName }}</td>
                                <td>{{ item.productPrice }}</td>
                                <td>
                                    <v-text-field
                                        v-model="item.quantity"
                                        type="number"
                                        min="1"
                                        @change="updateQuantity(item)"
                                    ></v-text-field>
                                </td>
                                <td>{{ item.productPrice * item.quantity }}</td>
                                <td>
                                    <v-btn color="red" @click="removeItem(item)">Remove</v-btn>
                                </td>
                            </tr>
                            </tbody>
                        </v-table>
                        <v-divider></v-divider>
                        <v-row>
                            <v-col>
                                <v-btn color="blue" @click="confirmCheckout">Checkout</v-btn>
                            </v-col>
                            <v-col class="text-right">
                                <strong>Total: {{ selectedItemsTotal }}</strong>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <!-- Confirmation Dialog -->
        <v-dialog v-model="isCheckoutDialogVisible" max-width="500">
            <v-card>
                <v-card-title>Confirm Checkout</v-card-title>
                <v-card-text>
                    Are you sure you want to order the selected items?
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text 
                            @click="isCheckoutDialogVisible = false">Cancel</v-btn>
                    <v-btn color="blue darken-1" text 
                            @click="proceedToOrder">Confirm</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { useCartStore } from "~/cart/stores/cartStore"

const selectedItems = ref([]);
const isCheckoutDialogVisible = ref(false);

const cartStore = useCartStore();
const router = useRouter();


// 계산 속성
const cartItems = computed(() => cartStore.cartList);
const cartTotal = computed(() =>
    cartStore.cartList.reduce(
        (total, item) => total + item.productPrice * item.quantity,
        0
    )
);

const selectedItemsTotal = computed(() =>
    selectedItems.value.reduce(
        (total, item) => total + item.productPrice * item.quantity,
        0
    )
);

// 메서드
const updateQuantity = (item) => {
    // 수량 업데이트 로직
};

const removeItem = (item) => {
    cartItems.value = cartItems.value.filter(
        (cartItem) => cartItem.cartItemId !== item.cartItemId
    );
    selectedItems.value = selectedItems.value.filter(
        (selectedItem) => selectedItem.cartItemId !== item.cartItemId
    );
};

const confirmCheckout = () => {
    isCheckoutDialogVisible.value = true;
};

const proceedToOrder = async () => {
    isCheckoutDialogVisible.value = false;

    try {
        const selectedCartItems = cartItems.value.filter((item) =>
            selectedItems.value.includes(item)
        );
        const orderItems = selectedCartItems.map((item) => ({
            cartItemId: item.cartItemId,
            orderPrice: item.productPrice,
            quantity: item.quantity,
        }));

/*
        const orderId = await store.dispatch("orderModule/requestCreateOrderToDjango", {
            items: orderItems,
        });
        */

        router.push({
            name: "OrderReadPage",
            params: { orderId: orderId.toString() },
        });
    } catch (error) {
        console.error("Order creation failed:", error);
    }
};

const fetchCartList = async () => {
    try {
        const response = await store.dispatch(
            "cartModule/requestCartListToDjango"
        );
        cartItems.value = response;
    } catch (error) {
        console.error("Error fetching cart list:", error);
    }
};

// 컴포넌트 초기화 시 데이터 로드
fetchCartList();
</script>

<style scoped>
/* 필요한 스타일을 여기에 추가합니다. */
</style>
