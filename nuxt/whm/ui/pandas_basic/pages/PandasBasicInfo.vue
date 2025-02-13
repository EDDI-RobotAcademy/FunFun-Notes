<template>
  <v-container>
    <!-- v-container는 정리해주는 명령어-->
    <h2>Pandas Basic Info</h2>
    <!-- h2는 제목설정 명령어-->
    <v-list>
      <!-- v-list는 리스트 컴포넌트로 여러 항목을 세로로 나열함-->
      <v-list-item v-for="pandasInfo in pandasInfoList" :key="pandasInfo.id">
        <!-- v-for는 반복문으로 pandasInfoList 항목에 대해 v-list-item을 반복 랜더링-->
        <!-- pandasInfo는 pandasInfoList배열의 각 항목을 나타내며 name과 age를 출력-->
        <!-- :key="pandasInfo.id는 고유id값을 key로 사용-->
        <v-list-item-content>
          <v-list-item-title>{{ pandasInfo.name }}</v-list-item-title>
          <v-list-item-subtitle>{{ pandasInfo.age }}</v-list-item-subtitle>
        </v-list-item-content>
        <!-- name을 제목,age를 부제목으로 값을 출력한다-->
      </v-list-item>
    </v-list>
  </v-container>
</template>

<script>
import { defineComponent } from "@vue/composition-api";
// vue3의 composition API를 사용하기 위해 @vue/composition-api에서
// defineComponent를 가져온다다

export default defineComponent({
  setup() {
    // setup()은 ref, computed, 메서드 등을 사용하기 위해 쓰인다다
    const pandasInfoList = ref([]);
    // pandasInfoList는 정보 리스트를 저장하는 반응형 변수
    const loading = ref(false);
    // 데이터가 로딩주인지 여부를 나타내는 상태
    // 기본은 false이며, 데이터를 가져오는 동안 true로 설정
    const error = ref(null);
    // 데이터를 가져오는 동안 오류를 저장하는 상태
    // 기본은 null이며, 오류 발생 시 오류 메세지가 저장

    const fetchPandasInfo = async () => {
      // pandasInfo를 서버에서 가져오는 함수
      loading.value = true;
      // 데이터를 가져오는 모습습
      try {
        const response = await fetch(
          // fetch()는 HTTP 요청을 보냄냄
          "http://localhost:8000/pandas-basic/request-pandas-info"
        );

        if (!response.ok) {
          throw new Error(`Error: ${response.status}`);
        } // 응답이 성공적이지 않으면 오류메세지를 출력
        // 만약 서버가 404상태면 response.status는 404가 저장
        // throw new Error(`Error: 404`)가 실행 그 후 catch에서 해당 오류를 처리리

        const data = await response.json();
        pandasInfoList.value = data.serializedPandasInfoList;
        // 응답이 성공적이면 JSON 데이터(serializer정보)를 받아와 pandasInfoList에 저장
      } catch (err) {
        error.value = err.message; // 오류발생시 실행행
      } finally {
        loading.value = false;
      } // finally는 catch가 실행된 후 항상 실행되며 로딩상태를 false로 바꾼다
    };

    onMounted(fetchPandasInfo);

    return {
      pandasInfoList,
      loading,
      error,
    };
  },
});
</script>
