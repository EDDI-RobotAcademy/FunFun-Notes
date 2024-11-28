#도서관에 책별로 카테고리가 있다
#카테고리별 책 권수가 있다
#빌린 카테고리와 권수가 보인다
import random
bookList=[]
numberList=[]
allList={}
backList={}

categ=int(input("몇개의 카테고리가 있나요?"))
for i in range(categ):
    book=input("어떤 카테고리가 있나요?")
    bookList.append(book)
print(bookList)

for  i in range(len(bookList)):
    bookNumber=random.randint(2,10)
    numberList.append(bookNumber)
print(numberList)
allList={book:number for book,number in zip(bookList,numberList)}
print("현재 재고는",allList,"있습니다.")

lendBook = input("무엇을 빌리시겠습니까?")
if lendBook in bookList:
    for i in range(len(bookList)):
        if lendBook==bookList[i]:
            how=int(input("몇권 빌리시겠습니까?"))
            lust=numberList[i]-how
            numberList[i]=lust
else:
    print("그런건 없습니다")



backList={book:number for book,number in zip(bookList,numberList)}
print("남은 책들은",backList,"입니다.")

