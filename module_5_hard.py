import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'Ник: {self.nickname}, пароль: {self.password}, возраст: {self.age}'

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Название видео: {self.title}, длительность: {self.duration} минут'

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        if len(self.users) == 0:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = nickname
            return new_user

        if len(self.users) > 0:
            for user in self.users:
                if nickname == user.nickname:
                    print(f'Пользователь {nickname} уже существует!')
                    break
                else:
                    new_user = User(nickname, password, age)
                    self.users.append(new_user)
                    self.current_user = nickname
                return new_user

    def log_in(self, nickname, password):
        if len(self.users) == 0:
            print('Список пользователей пуст!')

        if len(self.users) > 0:
            for user in self.users:
                if nickname == user.nickname and hash(password) == user.password:
                    self.current_user = user
                    print(f'Пользователь {nickname} авторизован!')

    def log_out(self):
        self.current_user = None

    def add(self, *video_file):
        for video in video_file:
            if not (video.title in self.videos):
                self.videos.append(video)

    def get_videos(self, keyword):
        search = []
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                search.append(video.title)
        return search


    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео!')

        if self.current_user is not None:
            for video in self.videos:
                if video.title == title:
                    for user in self.users:
                        if self.current_user == user.nickname:
                            us = user

                    if video.adult_mode and us.age < 18:
                        print('\033[1;31m' + 'Вам нет 18 лет, пожалуйста покиньте страницу!' + '\033[0;30m')
                        break

                    while video.time_now < video.duration:
                        video.time_now += 1
                        time.sleep(1)
                        print(video.time_now, end=' ')

                    print('\033[1;30m' + 'Конец видео!' + '\033[0;30m')



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
