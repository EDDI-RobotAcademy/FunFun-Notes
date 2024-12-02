

class Market:
    def __init__(self):
        self.appleCount=100
        self.orangeCount=100
        self.applePrice=1000
        self.orangePrice=152000
        self.Coins=200000
        #int(input("How many oranges do you want to buy? "))
        #int(input("How many oranges do you want to buy? "))
        self.getApple =  int(input("How many appples do you want to buy? "))
        self.getOrange = int(input("How many oranges do you want to buy? "))
        self.getCoins = int(input("How many coins do you want to spend? "))
        result1 = int(self.appleCount)-self.getApple
        result2 = int(self.orangeCount)-self.getOrange
        result3 = int(self.Coins)-self.getCoins

        print("마트에남아있는 사과와 오렌지의 개수는 각각 " + str(result1),str(result2))
        print("받을수있는 잔돈" + str(result3))
        print("Thank you for shopping with us")


market = Market()



