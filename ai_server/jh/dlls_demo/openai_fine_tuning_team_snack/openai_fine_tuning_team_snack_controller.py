import os
import json
import openai
from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Reinforcement Learning from Human Feedback
openaiFineTuningTeamSnackRouter = APIRouter()

# 피드백 데이터 저장
feedbackData = []

# 이전 파인 튜닝 데이터 그대로 가져오면 됩니다
trainingData = [

    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "부산에서 밀면 맛집 어디가 좋아?"},
            {"role": "assistant", "content": "부산에서 밀면을 맛볼 수 있는 유명한 곳으로는 '부산밀면', '초량밀면', '가야밀면' 등이 있습니다. 특히 여름철 시원한 육수와 쫄깃한 면발이 인상적입니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "대구에서 납작만두 유명한 곳 알려줘."},
            {"role": "assistant", "content": "대구에서 납작만두를 맛볼 수 있는 곳으로는 '미성당 납작만두', '대구 할매납작만두' 등이 유명합니다. 대구만의 독특한 납작한 만두로, 매콤한 양념장과 함께 먹으면 더욱 맛있습니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "광주에서 떡갈비 맛집 추천해줘."},
            {"role": "assistant", "content": "광주에서 떡갈비를 맛볼 수 있는 곳으로는 '궁전제과 떡갈비', '송정 떡갈비', '양동시장 떡갈비' 등이 있습니다. 특히 담양식 떡갈비가 부드럽고 달짝지근한 양념이 특징입니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "수원에서 왕갈비 맛집 어디 있어?"},
            {"role": "assistant", "content": "수원에서는 '가보정', '본수원갈비', '화춘옥' 같은 곳이 유명합니다. 두툼한 고기와 달콤한 양념이 조화를 이루는 수원 왕갈비를 추천합니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "춘천에서 닭갈비 맛집 추천해줘."},
            {"role": "assistant", "content": "춘천에서 닭갈비를 맛볼 수 있는 대표적인 곳으로는 '명동 닭갈비', '춘천 1번가 닭갈비', '유포리막국수 닭갈비' 등이 있습니다. 숯불 닭갈비와 철판 닭갈비 중 취향에 맞게 선택하면 좋습니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "제주도에서 흑돼지 맛집 어디야?"},
            {"role": "assistant", "content": "제주도에서 흑돼지를 맛볼 수 있는 곳으로는 '돈사돈', '흑돈가', '제주마농 흑돼지' 등이 유명합니다. 참숯에 구운 흑돼지는 제주에서 꼭 맛봐야 할 음식 중 하나입니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "인천에서 짜장면 유명한 곳 추천해줘."},
            {"role": "assistant", "content": "인천 차이나타운에서 유명한 짜장면 맛집으로는 '신승반점', '공화춘', '자금성' 등이 있습니다. 인천은 짜장면의 발상지로 알려져 있어, 오리지널 스타일의 짜장면을 맛볼 수 있습니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "강릉에서 초당두부 맛집 어디야?"},
            {"role": "assistant", "content": "강릉에서 초당두부를 맛볼 수 있는 곳으로는 '초당할머니순두부', '동화가든', '원조초당순두부' 등이 있습니다. 고소하고 부드러운 순두부 요리가 일품입니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "여수에서 갓김치 맛있는 곳 알려줘."},
            {"role": "assistant", "content": "여수에서 갓김치를 구매하거나 맛볼 수 있는 곳으로는 '여수 수산시장', '돌산갓김치 전문점', '여수 갓김치 명가' 등이 있습니다. 갓김치는 매콤하고 아삭한 식감이 특징입니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "마산에서 아구찜 맛집 어디야?"},
            {"role": "assistant", "content": "마산에서 아구찜을 맛볼 수 있는 곳으로는 '마산 원조아구찜', '복성반점', '진아구찜' 등이 유명합니다. 얼큰하고 깊은 맛의 국물과 쫄깃한 아구 살이 특징입니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "속초에 있는 해산물 맛집 추천해줘."},
            {"role": "assistant", "content": "속초에서 해산물을 맛볼 수 있는 좋은 곳으로는 속초 대게, 홍성 한우 등이 있습니다. 대게는 특히 이 지역에서 매우 유명합니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "전주에서 비빔밥 맛집 어디가 좋아?"},
            {"role": "assistant",
             "content": "전주는 비빔밥으로 유명한 도시입니다. 전주 비빔밥을 맛볼 수 있는 곳으로는 전주 한옥 마을 내 여러 식당이 있으며, 그중에서도 특히 명성이 높은 곳을 추천드립니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 김치찌개 맛집 있어?"},
            {"role": "assistant",
             "content": "서울에는 김치찌개를 제공하는 수많은 맛집이 있습니다. 한일관, 이문설농탕 등이 특히 인기가 많으며, 깊고 풍부한 맛의 김치찌개를 제공합니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "인천에서 좋은 생선구이 맛집 알려줄 수 있어?"},
            {"role": "assistant",
             "content": "인천에서 생선구이를 즐길 수 있는 좋은 곳으로는 인천 생선구이가 있습니다. 신선한 해산물을 사용하여 다양한 생선구이를 맛볼 수 있는 이곳은 지역 주민들 사이에서도 인기가 높습니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "포항에서 김밥 맛있는 곳 어디야?"},
            {"role": "assistant",
             "content": "포항에서는 포항 김밥이 매우 유명합니다. 신선한 재료를 사용하고, 가성비가 좋기로 소문난 이곳은 방문객들에게 항상 만족을 제공합니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 평양냉면 맛있는 곳 추천해줘."},
            {"role": "assistant", "content": "서울에서 평양냉면을 맛볼 수 있는 곳으로는 '을밀대', '우래옥', '봉피양' 등이 있습니다. 슴슴하고 깊은 육수 맛이 특징입니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 떡볶이 맛집 알려줘."},
            {"role": "assistant", "content": "서울에서 떡볶이를 맛볼 수 있는 유명한 곳으로는 '마포 원조 조폭떡볶이', '신당동 할머니떡볶이', '모범떡볶이' 등이 있습니다. 매콤달콤한 소스와 쫄깃한 떡이 조화를 이룹니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 삼겹살 맛집 추천해줘."},
            {"role": "assistant", "content": "서울에서 삼겹살이 맛있는 곳으로는 '육전식당', '금돼지식당', '서래갈매기' 등이 있습니다. 신선한 고기와 적절한 숙성으로 풍미가 뛰어납니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 감자탕 맛집 어디야?"},
            {"role": "assistant", "content": "서울에서 감자탕을 맛볼 수 있는 곳으로는 '안양 감자탕', '마포 감자탕', '성수 감자탕' 등이 있습니다. 푹 끓여낸 국물과 부드러운 뼈고기가 일품입니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 닭한마리 맛집 알려줘."},
            {"role": "assistant", "content": "서울에서 닭한마리를 맛볼 수 있는 유명한 곳으로는 '진옥화 할매 닭한마리', '공릉동 닭한마리', '명동 닭한마리' 등이 있습니다. 부드러운 닭고기와 담백한 육수가 특징입니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 곱창 맛집 추천해줘."},
            {"role": "assistant", "content": "서울에서 곱창을 맛볼 수 있는 곳으로는 '마포 곱창', '부산양곱창', '청량리 곱창골목' 등이 유명합니다. 신선한 곱과 바삭한 식감이 조화를 이룹니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 돼지국밥 맛있는 곳 알려줘."},
            {"role": "assistant", "content": "서울에서 돼지국밥을 맛볼 수 있는 곳으로는 '합정옥', '영등포 복국', '남포 돼지국밥' 등이 있습니다. 부산 스타일의 진한 국물을 맛볼 수 있습니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 보쌈 맛집 어디야?"},
            {"role": "assistant", "content": "서울에서 보쌈을 맛볼 수 있는 곳으로는 '원할머니 보쌈', '청기와타운', '연희동 보쌈' 등이 있습니다. 부드러운 고기와 새콤한 김치가 조화를 이룹니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 전통 한정식 맛집 추천해줘."},
            {"role": "assistant", "content": "서울에서 전통 한정식을 맛볼 수 있는 곳으로는 '한성옥', '소반', '다래원' 등이 있습니다. 다양한 반찬과 정갈한 요리를 즐길 수 있습니다."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "순댕이네얼큰칼국수(수제비) 가게 정보를 알려줘."},
            {"role": "assistant", "content": "순댕이네얼큰칼국수(수제비) 가게 정보입니다.\n\n- **대표 메뉴**: 바지락 얼큰칼국수\n- **주소**: 서울특별시 금천구 시흥대로 136길 1, 1호선 독산역 도보 25분\n- **문의 및 안내**: 02-852-3670\n- **영업시간**: 10:00~16:00\n- **주차시설**: 연중무휴\n- **쉬는날**: 매주 일요일\n\n**메뉴**:\n- 바지락 얼큰 칼국수: 11,000원\n- 바지락 얼큰 칼제비: 11,000원\n- 바지락 칼국수: 9,000원\n- 바지락 칼제비: 9,000원\n- 곱빼기: 1,000원 추가\n- 공기밥: 무료 제공\n- 반찬: 셀프 제공"}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "순댕이네얼큰칼국수(수제비) 가게 리뷰를 알려줘."},
            {"role": "assistant", "content": "순댕이네얼큰칼국수(수제비) 가게 리뷰입니다.\n\n"
                "- **리뷰1**: 바지락 칼제비는 순댕이네의 대표 메뉴로, 바지락은 신선한 해산물 그 자체로도 깊은 맛을 느낄 수 있습니다.\n"
                "- **리뷰2**: 이곳의 바지락은 특히 신선하고 질 좋은 재료를 사용하여, 씹을 때마다 바다의 풍미가 느껴지는 것이 특징입니다.\n"
                "- **리뷰3**: 칼제비의 면발은 쫄깃하고 부드러우며 바지락과의 조화가 좋습니다. 면발이 국물에 잘 스며들어, 국물을 한 숟가락 떠 먹으면 그 맛이 입안 가득 퍼집니다.\n"
                "- **리뷰4**: 보통 칼국수와 수제비의 차이는 면발의 형태에 있습니다. 칼국수는 일반적으로 밀가루로 만든 면으로, 얇고 긴 형태를 띠고 있습니다.\n"
                "- **리뷰5**: 수제비는 조금 더 두껍고 쫄깃한 면발로, 국물과 함께 먹었을 때 그 식감이 더욱 두드러집니다. 바지락 칼제비는 매운 국물과 바지락의 조화가 특히 뛰어난데, 매운맛이 강하면서도 국물의 깊은 맛이 어우러져 매력적인 풍미를 제공합니다.\n"
                "- **리뷰6**: 칼국수 맛집의 기본은 김치에 있다고 할 수 있는데, 순댕이네의 김치는 매콤하고 아삭아삭하여 칼제비와 함께 먹으면 더욱 맛있습니다.\n"
                "- **리뷰7**: 매운 국물의 강렬한 맛과 부드러운 면발의 조화는 이 식당의 특징입니다. 매번 방문할 때마다 일관된 품질의 음식을 제공합니다.\n"
                "- **리뷰8**: 칼제비의 푸짐한 바지락은 정말 인상적입니다. 이곳에서 식사를 하면 바지락의 신선함을 직접 확인할 수 있습니다.\n"
                "- **리뷰9**: 이 식당의 분위기는 매우 친절하고 환영하는 느낌을 줍니다. 서비스가 빠르고 효율적이어서 자주 방문하게 됩니다.\n"
                "- **리뷰10**: 순댕이네는 가족 단위 손님에게도 적합합니다. 메뉴가 다양하고 아이들이 좋아하는 맛이 포함되어 있어 전체 가족이 즐길 수 있습니다."
            }
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "서울에서 매운 음식 맛집을 추천해줘."},
            {"role": "assistant", "content": "서울에서 매운 음식을 즐길 수 있는 유명한 맛집 리스트입니다:\n\n"
                "- **롸카두들내쉬빌핫치킨 성수점**\n"
                "- **소신이쏘**\n"
                "- **순댕이네얼큰수제비(독산)**\n"
                "- **옥천매운족발**\n"
                "- **화랑 불닭**\n"
                "- **봉천동 매운 떡볶이**\n"
                "- **꼬꼬닭**\n"
                "- **창동역 불닭꼬치**\n"
                "- **해주냉면**\n"
                "- **뱃고동**\n"
                "- **신토불이 떡볶이**\n"
                "- **경춘자의라면땡기는날**\n"
                "- **남박의 얼큰 한우 쌀국수**\n"
                "- **허브족발 (당산)**\n"
                "- **신림 코다리 (신림)**\n"
                "- **티엔호아 (강남)**\n"
                "- **열불날개 (홍대)**\n"
                "- **청양마루 (이태원)**\n"
                "- **매운맛집 도봉산**\n"
                "- **칠리차차 (명동)**\n"
                "- **홍콩반점(신촌)**\n"
                "- **불난떡볶이 (천호동)**\n"
                "- **매콤한 양념갈비 전문점 (청량리)**\n"
                "- **떡볶이 천국 (잠실)**\n"
                "- **매운갈비찜의 달인 (서초동)**\n"
                "- **흑돼지 불고기 전문점 (목동)**\n"
                "- **빨간오뎅 (동대문)**\n"
                "- **부탄츄 (서교동)**\n"
                "- **매운 라면의 천국 (건대)**\n\n"
                "이곳들은 매운맛을 좋아하는 사람들에게 인기가 많은 곳들입니다. 취향에 따라 다양한 매운 음식을 즐겨보세요!"
            }
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "넌 한국 맛집 정보를 제공하는 도우미야."},
            {"role": "user", "content": "지역별 맛집 리스트를 알려줘."},
            {"role": "assistant", "content":
                "**서울**\n"
                "- 미진\n"
                "- 경성면옥\n"
                "- 삼청동 수제비\n"
                "- 토속촌\n"
                "- 명동 칼국수\n"
                "- 무교동 북어국집\n"
                "- 남도 한식 곰탕\n"
                "- 진미평양냉면\n"
                "- 오장동 함흥냉면\n"
                "- 영양센터\n"
                "- 양재동 맷돌\n"
                "- 원조 순두부\n"
                "- 진옥화 할매 닭한마리\n"
                "- 가메골 손만두\n"
                "- 별미골\n"
                "- 대가방\n"
                "- 청평한우촌\n"
                "- 남문피자\n"
                "- 진주집\n"
                "- 황소고집\n"
                "- 이문설농탕\n"
                "- 망원시장 막걸리\n"
                "- 벽제갈비\n"
                "- 매운갈비찜\n"
                "- 순희네 빈대떡\n"
                "- 영등포 복국\n"
                "- 청량리 수제비\n"
                "- 성수동 만두\n"
                "- 이화수전통육개장\n"
                "- 장충동 족발\n"
                "- 김포 골드라면\n"
                "- 영동 특색 떡볶이\n"
                "- 논현동 백반\n"
                "- 사당동 냉면\n"
                "- 신사동 샐러드바\n"
                "- 여의도 족발\n"
                "- 한성옥\n"
                "- 소이연남\n"
                "- 을밀대\n"
                "- 산울림\n"
                "- 육전식당\n"
                "- 마장동 해장국\n"
                "- 금돼지식당\n"
                "- 봉피양\n"
                "- 우육면관\n"
                "- 연남서식당\n"
                "- 매화\n"
                "- 강남면옥\n"
                "- 삼성옥\n"
                "- 한일관\n"
                "- 느린마을 양조장\n"
                "- 청기와타운\n"
                "- 아현동김밥\n"
                "- 약수터갈비\n"
                "- 자매집\n"
                "- 낙원타코\n"
                "- 순댕이네얼큰칼국수(수제비)\n"
                "- 우래옥\n"
                "- 차돌박이\n"
                "- 서울밀면\n"
                "- 논현동태찜\n"
                "- 신촌설렁탕\n"
                "- 이코이\n"
                "- 부산양곱창\n\n"
    
                "**부산**\n"
                "- 동백양과점\n"
                "- 송정해수욕장 막국수\n"
                "- 원조국수집\n"
                "- 꼬막집\n"
                "- 민락동 전복죽\n"
                "- 밀면 대통령\n"
                "- 원조 간장게장\n"
                "- 부산밀면\n"
                "- 동래파전\n"
                "- 부산 닭갈비\n\n"
    
                "**전라도 (전주, 광주, 목포 등)**\n"
                "- 전주 비빔밥 (전주)\n"
                "- 광주 떡갈비 (광주)\n"
                "- 목포 서산동태찜 (목포)\n"
                "- 목포 피순대 (목포)\n"
                "- 목포 홍어삼합 (목포)\n"
                "- 여수 갓김치 (여수)\n\n"
    
                "**경상도 (대구, 부산, 경북 등)**\n"
                "- 근대골목닭발 (대구)\n"
                "- 구미 국밥 (구미)\n"
                "- 사천 낙지 (사천)\n"
                "- 진주 냉면 (진주)\n"
                "- 마산 회센터 (마산)\n\n"
    
                "**강원도**\n"
                "- 강릉 닭강정 (강릉)\n"
                "- 속초 대게 (속초)\n"
                "- 춘천 막국수 (춘천)\n"
                "- 원주 치즈닭갈비 (원주)\n"
                "- 삼척 해물파전 (삼척)\n"
                "- 태백 고원양식 (태백)\n\n"
    
                "**충청도**\n"
                "- 대전 육개장 (대전)\n"
                "- 청주 감자탕 (청주)\n"
                "- 당진 해물탕 (당진)\n"
                "- 보령 물회 (보령)\n"
                "- 태안 소금구이 (태안)\n"
                "- 서산 해미읍성 떡볶이 (서산)\n"
                "- 홍성 한우 (홍성)\n"
                "- 단양 소갈비살 (단양)\n"
                "- 영월 동동주 (영월)\n\n"
    
                "**제주도**\n"
                "- 제주 흑돼지구이 (제주)\n\n"
    
                "각 지역별 유명한 맛집들이며, 취향에 맞는 곳을 방문해 보세요!"
            }
        ]
    }
]


class Feedback(BaseModel):
    fineTuneId: str
    prompt: str
    response: str
    feedback: str  # 'positive' 또는 'negative'
    betterResponse: str = None


# 피드백을 수집하는 엔드포인트
@openaiFineTuningTeamSnackRouter.post("/give-feedback-snack")
def giveFeedback(feedback: Feedback):
    feedbackData.append(feedback.dict())
    return {"status": "Feedback received"}


# 피드백을 처리하여 새로운 훈련 데이터를 생성하는 함수
def processFeedback():
    for item in feedbackData:
        if item['feedback'] == 'negative':
            # 부정적인 피드백에 대한 개선된 응답을 수집
            betterResponse = item.get('betterResponse')
            if not betterResponse:
                betterResponse = f"이것은 잘못된 답변입니다: {item.get('response')}"

            newTrainingExample = {
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": item['prompt']},
                    {"role": "assistant", "content": betterResponse}
                ]
            }
            trainingData.append(newTrainingExample)

    # # 생성된 훈련 데이터를 파일로 저장
    if trainingData:
        saveTrainingData(trainingData)


# 새로운 훈련 데이터를 저장하는 함수
def saveTrainingData(trainingData, filename="training_data.jsonl"):
    with open(filename, "w") as file:
        for item in trainingData:
            file.write(json.dumps(item) + "\n")


# 파인 튜닝을 시작하는 함수
def startFineTuning():
    saveTrainingData(trainingData)

    filePath = "training_data.jsonl"
    with open(filePath, "rb") as file:
        response = openai.files.create(file=file, purpose='fine-tune')

    fileId = response.id
    fineTuneResponse = openai.fine_tuning.jobs.create(
        training_file=fileId,
        model="gpt-3.5-turbo",
        hyperparameters={
            "n_epochs": 20
        }
    )
    return fineTuneResponse.id


# 파인 튜닝을 피드백 기반으로 시작하는 엔드포인트
@openaiFineTuningTeamSnackRouter.post("/fine-tune-with-feedback-snack")
def fineTuneWithFeedback(backgroundTasks: BackgroundTasks):
    processFeedback()  # 피드백을 처리하여 새로운 훈련 데이터를 생성
    fineTuneId = startFineTuning()  # 새로운 데이터로 모델을 미세 조정
    backgroundTasks.add_task(checkFineTuneStatus, fineTuneId)
    return {"status": "Fine-tuning started with feedback", "fineTuneId": fineTuneId}


# 파인 튜닝 상태를 확인하는 함수
def checkFineTuneStatus(fineTuneId):
    statusResponse = openai.fine_tuning.jobs.retrieve(fineTuneId)
    status = statusResponse.status
    print(f"Fine-tuning status for {fineTuneId}: {status}")


# 파인 튜닝 상태를 확인하는 엔드포인트
@openaiFineTuningTeamSnackRouter.get("/fine-tune-status-snack/{fineTuneId}")
def getFineTuneStatus(fineTuneId: str):
    statusResponse = openai.fine_tuning.jobs.retrieve(fineTuneId)
    return {"status_response": statusResponse}

class Query(BaseModel):
    text: str

@openaiFineTuningTeamSnackRouter.post("/chat-snack")
def chat_with_model(query: Query):
    fine_tuned_model = "ft:gpt-3.5-turbo-0125:personal::B7eBosSD"
    response = openai.chat.completions.create(
        model=fine_tuned_model,
        messages=[{"role": "user", "content": query.text}]
    )
    return {"response": response.choices[0].message.content}
