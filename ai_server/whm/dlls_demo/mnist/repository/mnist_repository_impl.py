#tensorflow 라이브러리 사용
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

from tensorflow.keras.datasets import mnist

from tensorflow.keras.utils import to_categorical

from mnist.repository.mnist_repository import MnistRepository


class MnistRepositoryImpl(MnistRepository):

    #데이터를 로드함
    #mnist를 로드하여 (X_train, y_train), (X_test, y_test)에 각각 배치


    def loadData(self):
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        return X_train, y_train, X_test, y_test

    #데이터 전처리
    # 기본적인 RGB는 0~255에 해당
    # 그래픽 카드는 이것을 0.0~1.0사이로 취급하여 보다 세밀하게 관찰 가능
    # 고로 위의 값들을 255로 나눠서 0.0~1.0사이로 스케일함(정규화라고도 함)
    # to_categorical이라는 것을 통해 one-Hot encoding아라는 것 진행
    # 예시로 숫자 3의 경우 : [0,0,0,1,0,0,0,0,0,0]
    # 예시로 숫자 5의 경우 : [0,0,0,0,0,1,0,0,0,0]
    def preprocessData(self, X_train, y_train, X_test, y_test):
        X_train, X_test = X_train / 255.0, X_test / 255.0
        y_train, y_test = to_categorical(y_train, num_classes=10), to_categorical(y_test, num_classes=10)
        return X_train, y_train, X_test, y_test


    # 딥러닝 모델 구축
    # 숫자는 input을 제외하고 마지막 softmax를 제외하고 전부 맘대로 넣어도 무방
    # 데이터 추이가 요동을 치거나 들쭉 날쭉하면 cosh ,sinh계열 사용하면 됨
    # 결국 직관력 및 구현력의 싸움, 실험을 위해 시간 필요
    def buildModel(self):
        model = Sequential([
            Flatten(input_shape=(28, 28)),
            Dense(128, activation='relu'),
            Dense(64, activation='relu'),
            #출력층을 10개의 노드를 가지고 e(익스포넨셜-오일러 상수) 계열로 값을 처리
            # 계산 결과는 0~1사이로 수렴
            # [0,0,0,0,0,1,0,0,0,0]<<<이게 숫자 5
            # 각 자리별로 계싹ㄴ된 수치값이 존재
            # 가장 높은 확률값이 나타나는 것을 선택
            # [0.01,0.01,0.01,0.01,0.01,0.91,0.01,0.01,0.01]
            Dense(10, activation='softmax'),
        ])
        return model

    def compileModel(self, buildModel):
        # adam 최적화 알고리즘을 사용
        # categorical_crossentropy는 분류문제를 계산할 떄 사용하는 손실 함수
        # metrics=['accuracy']의 경우 학습과정에서 정확도를 평가
        buildModel.compile(optimizer='adam',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])


        # 훈련 데이터를 가지고 모델을 학습시킴
        # y=ax+b를 찾는 것이라고 함
        # 이것을 만들기 위해 전체 데이터를 10번 반복학습(epochs=10)
        # batch_size=32는 한번에 데이터 32개를 처리

    def trainModel(self, buildModel, X_train, y_train):
        buildModel.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

    def evaluateModel(self, buildModel, X_test, y_test):
        _, accuracy = buildModel.evaluate(X_test, y_test)
        return accuracy