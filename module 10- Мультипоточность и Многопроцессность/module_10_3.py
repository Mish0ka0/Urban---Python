import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            a = randint(50, 500)
            self.balance += a
            print(f'Пополнение: {a}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked() == 1:
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            a = randint(50, 500)
            print(f'Запрос {i} на {a}.')
            if a <= self.balance:
                self.balance -= a
                print(f'Снятие {a}. Баланс: {self.balance}')
            elif a > self.balance:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

thread_1 = threading.Thread(target=Bank.deposit, args=(bk,))
thread_2 = threading.Thread(target=Bank.take, args=(bk,))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f'Итоговый баланс: {bk.balance}')
