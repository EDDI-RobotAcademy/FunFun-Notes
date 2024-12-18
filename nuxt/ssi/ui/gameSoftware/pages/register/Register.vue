<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-text-field v-model="productName" label="상품명" />
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-text-field v-model="productPrice" label="가격" type="number" />
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-textarea v-model="productDescription" label="상품 세부 정보" auto-grow />
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-file-input v-model="productImage" label="이미지 파일" prepend-icon="mdi-camera" />
      </v-col>
    </v-row>

    <v-row v-if="uploadedFileName">
      <v-col cols="12">
        <p>업로드된 파일: {{ uploadedFileName }}</p>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" class="text-right">
        <v-btn color="primary" @click="onSubmit">작성 완료</v-btn>
        <v-btn color="error" @click="onCancel" class="ml-2">취소</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
definePageMeta({
  name: 'GameSoftwareRegisterPage'
})

import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useGameSoftwareStore } from '../../stores/gameSoftwareStore'

const router = useRouter()
const gameSoftwareStore = useGameSoftwareStore()

const gameSoftwareName = ref('')
const gameSoftwarePrice = ref(0)
const gameSoftwareDescription = ref('')
const gameSoftwareImage = ref(null)
const uploadedFileName = ref('')

const onSubmit = async () => {
  console.log('상품 등록 버튼 눌렀음')

  try {
    if (productImage.value) {
      const formData = new FormData()
      formData.append('productName', productName.value)
      formData.append('productPrice', productPrice.value.toString())
      formData.append('productDescription', productDescription.value)
      formData.append('productImage', productImage.value)

      await gameSoftwareStore.requestCreateGameSoftware(formData)

      uploadedFileName.value = gameSoftwareStore.uploadedFileName

      router.push({ name: 'ProductListPage' })
    } else {
      console.error('이미지 파일을 선택하세요!')
    }
  } catch (error) {
    console.error('상품 등록 실패:', error)
  }
}

const onCancel = () => {
  console.log('취소 버튼 눌렀음')
  router.back()
}
</script>