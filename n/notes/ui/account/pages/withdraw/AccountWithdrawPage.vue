<template>
    <v-container class="withdraw-container">
        <v-card class="pa-8" max-width="600">
            <v-card-title>회원 탈퇴</v-card-title>
            <v-card-text>
                <p>정말로 탈퇴하시겠습니까? 이 작업은 되돌릴 수 없습니다.</p>
            </v-card-text>
            <v-card-actions>
                <v-btn color="error" @click="handleWithdraw">회원 탈퇴</v-btn>
                <v-btn @click="cancelWithdraw">취소</v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script setup lang="ts">
import { useAccountStore } from '~/stores/accountStore';
import { useRouter } from 'vue-router';

const accountStore = useAccountStore();
const router = useRouter();

const handleWithdraw = async () => {
    if (confirm('정말로 탈퇴하시겠습니까?')) {
        try {
            await accountStore.withdraw();
            // 탈퇴 후 홈 페이지로 이동
            router.push('/');
        } catch (error) {
            alert('회원 탈퇴에 실패했습니다. 다시 시도해 주세요.');
        }
    }
};

const cancelWithdraw = () => {
    router.push('/');
};
</script>

<style scoped>
.withdraw-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
</style>
