from time import sleep
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password) # преобразует строку в хеш- значение
        self.age = age

    def __str__(self):
        return f"{self.nickname}"

    def __repr__(self):
        return f"{self.nickname}"

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title


class UrTube:
    users = []
    videos = []
    current_user = None

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __str__(self):
        return f"{self.users}, {self.videos}, {self.current_user}"

    # вход пользователя
    def log_in(self, nickname, password):
        if nickname in self.users:
            index = self.users[nickname]
            if hash(password) in self.users[index]:
                self.current_user = self.users[index]
                print("пользователь авторизован")
            else:
                print("Неверный пароль")
        else:
            print("Такого пользователя не существует")

    # регистрация нового пользователя
    def register(self, nickname, password, age):
        # функция any ищет хотя бы 1 элемент в итерируемом объекте
        # ищет совпадение в каждом объекте отдельно
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            a = User(nickname, password, age)
            self.users.append(a)
            self.current_user = a

    def log_out(self):
        self.current_user = None
        print("пользователь вышел")

    def add(self, *videos_):
        for video in videos_:
            if video not in self.videos:
                self.videos.append(video)
            else:
                pass

    def get_videos(self, string):
        st = []
        for video in self.videos:
            if string.upper() in video.title.upper():
                st.append(video.title)
        return st

    def watch_video(self, string):
        video_ = None
        user = self.current_user
        for video in self.videos:
            if video.title.find(string) > -1:
                video_ = video
        if video_ is None:
            print("Видео не найдено")
        elif self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            for i in range(1, int(video_.duration)+1):
                video_.time_now = i
                print(video_.time_now, end=" ")
                sleep(0.5)
            video_.time_now = 0
            print("Конец видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')