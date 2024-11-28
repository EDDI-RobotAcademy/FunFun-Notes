class RegisterHandler:

    @classmethod
    def processUserInputOnRegister(self):
        userInputId = input("아이디: ")
        userInputPassword = input("비밀번호: ")

        return userInputId, userInputPassword
