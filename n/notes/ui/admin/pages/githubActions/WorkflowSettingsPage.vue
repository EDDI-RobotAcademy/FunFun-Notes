<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-select
                    v-model="selectedRepo"
                    :items="repositories"
                    label="저장소 선택"
                />
            </v-col>

            <v-col cols="12">
                <v-checkbox
                    v-for="workflow in workflowOptions"
                    :key="workflow.value"
                    v-model="selectedWorkflows"
                    :label="workflow.label"
                    :value="workflow.value"
                />
            </v-col>

            <v-col cols="12">
                <v-btn
                    color="primary"
                    @click="triggerWorkflows"
                    :disabled="!canTrigger"
                >
                    선택된 워크플로우 실행
                </v-btn>
            </v-col>

            <v-col cols="12">
                <v-alert v-if="message" :type="messageType" class="mt-4">
                    {{ message }}
                </v-alert>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useAdminStore } from '@/stores/adminStore'

const adminStore = useAdminStore()

const repositories = [
    'silenc3502/SK-Networks-8-Notes',
]

const workflowOptions = [
    { label: 'Deploy Test', value: 'deploy-test.yml' },
    { label: 'Integration Test', value: 'integration_test.yml' },
    { label: 'Deploy', value: 'deploy.yml' },
]

const selectedRepo = ref(repositories[0])
const selectedWorkflows = ref<string[]>([])

const message = ref('')
const messageType = ref<'success' | 'error'>('success')

const canTrigger = computed(() => selectedWorkflows.value.length > 0)

const triggerWorkflows = async () => {
    message.value = ''
    try {
        const userToken = localStorage.getItem("userToken")

        if (!userToken) {
            throw new Error('사용자 토큰이 존재하지 않습니다.')
        }

        for (const workflow of selectedWorkflows.value) {
            await adminStore.triggerGithubWorkflow({
                userToken,
                repoUrl: selectedRepo.value,
                workflowName: workflow,
            })
        }

        message.value = '워크플로우 실행 성공!'
        messageType.value = 'success'
    } catch (err: any) {
        message.value = `실행 실패: ${err.message}`
        messageType.value = 'error'
    }
}
</script>
