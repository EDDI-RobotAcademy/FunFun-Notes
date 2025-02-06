<template>
    <v-container fluid class="pa-4">
        <!-- 배경 이미지와 텍스트를 포함한 Hero 섹션 -->
        <v-row>
            <v-col cols="12">
                <v-img
                        src="https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg"
                        height="400"
                        class="rounded-xl"
                >
                    <v-row class="fill-height ma-0" align="center" justify="center">
                        <v-col class="text-center">
                            <v-btn color="primary" large class="mb-4">
                                Get Started
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-img>
            </v-col>
        </v-row>

        <!-- 기능 카드 섹션 -->
        <v-row class="mt-6" align="start">
            <v-col v-for="n in 4" :key="n" cols="12" sm="6" md="3">
                <v-card>
                    <v-img
                            src="https://picsum.photos/1600/900"
                            height="200"
                    ></v-img>
                    <v-card-title class="text-h6">특징 {{ n }}</v-card-title>
                    <v-card-subtitle>
                        가즈아~ 지브로
                    </v-card-subtitle>
                    <v-card-actions>
                        <v-btn text>Learn More</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>

        <!-- Footer 섹션 -->
        <v-row>
            <v-col cols="12" class="text-center">
                <v-divider></v-divider>
                <p>&copy; 2024 지브로. All rights reserved.</p>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    name: "HomePage"
}
</script>

<style scoped>

</style>