<template>
    <v-container>
        <v-card>
            <v-card-title>{{ post?.title || "제목 없음" }}</v-card-title>
            <v-card-subtitle>{{ post?.nickname }} | {{ formatDate(post?.createDate) }}</v-card-subtitle>
            <v-card-text>
                <div v-html="postContent"></div>
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" @click="goBack">목록으로</v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useBlogPostStore } from '~/stores/blogPostStore';
import { getSignedUrlFromS3 } from '~/utility/awsS3Instance'; // S3에서 가져오기

const route = useRoute();
const router = useRouter();
const blogPostStore = useBlogPostStore();
const post = ref(null);
const postContent = ref("");

const fetchPostDetail = async () => {
    const postId = route.params.id;
    if (!postId) return;

    try {
        const data = await blogPostStore.requestReadPost(postId);
        if (data) {
            post.value = data;

            // S3에서 HTML 파일 다운로드
            if (data.content) {
                const url = await getSignedUrlFromS3(`blog-post/${data.content}`);
                const response = await fetch(url);
                postContent.value = await response.text();
            }
        }
    } catch (error) {
        console.error("게시글을 불러오는 데 실패했습니다.", error);
    }
};

const goBack = () => {
    router.push("/blog-post/list");
};

const formatDate = (dateString) => {
    if (!dateString) return "";
    return new Date(dateString).toLocaleDateString("ko-KR");
};

onMounted(fetchPostDetail);
</script>
