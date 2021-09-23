class Client:
    def __init__(self, client, balance):
        self.client = client
        self.balance = balance

    def getClient(self):
            return self.client

    def getBalance(self):
            return self.balance

    def balance_info(self):
            return f'Клиент "{self.getClient()}". Баланс: {self.getBalance()} руб.'

client_1 = Client('Иван Петров', '50')
client_2 = Client('Пётр Иванов', '90')
client_3 = Client('Семён Сидиров', '800')
print(client_1.balance_info())
print(client_2.balance_info())
print(client_3.balance_info())