from django.db import models

# Create your models here.
class Dice(models.Model):
    # 이 모델은 데이터베이스에서 주사위 테이블로 변환되며, 각 필드는 테이블의 열(column)이 됩니다.
    # Django의 모델 클래스를 상속받아 Dice라는 데이터 모델을 정의
    # 데이터베이스 테이블 구조 정의

    id = models.AutoField(primary_key=True)
    # id :  주사위의 고유 식별자/ AutoField: 데이터베이스에서 자동 증가(AUTO_INCREMENT)필드, primary_key(기본키)로 사용.
    number = models.IntegerField()   # create()에 dice = Dice(number=randomNumber)가 있음.
    # number: 주사위의 눈금 값/ .IntegerField(): 정수(int) 타입과 매핑되며, 정수를 저장하는 데 사용

    def __str__(self):
        # Python의 특수 메서드, 객체를 문자열로 표현할 때 호출
        return f"주사위 id: {self.id}, 눈금: {self.number}"
        # Dice 객체가 출력될 때, 위의 형태로 (무조건) 출력 ㅋ


    def detId(self):
        # Dice 객체의 id값을 반환하는 Getter 메서드. dice.getId()를 호출하면 주사위의 고유 ID가 반환됨.
        return self.id


    def getNumber(self):
        return self.number

    class Meta:
        # Django의 메타 클레스로, 모델의 동작 방식을 추가로 설정함
        db_table = "dice"
        # db에서 사용될 table 이름을 명시적으로 지정시킴.
        # 이 모델은 dice table에 매핑됨

