import hashlib  # Для хэширования паролей
import time  # Для симуляции воспроизведения видео


class User:
    """
    Класс User представляет пользователя платформы UrTube.
    """

    def __init__(self, nickname, password, age):
        """
        Инициализация пользователя.

        :param nickname: Имя пользователя (строка)
        :param password: Пароль пользователя (строка, будет хэширован)
        :param age: Возраст пользователя (число)
        """
        self.nickname = nickname
        self.password = self.hash_password(password)  # Хэшируем пароль при создании
        self.age = age

    def hash_password(self, password):
        """
        Хэширование пароля с использованием алгоритма SHA-256.

        :param password: Пароль в виде строки
        :return: Хэшированный пароль в виде целого числа
        """
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __eq__(self, other):
        """
        Метод сравнения двух пользователей по nickname и password.

        :param other: Другой объект User для сравнения
        :return: True, если nickname и password совпадают, иначе False
        """
        return self.nickname == other.nickname and self.password == other.password

    def __str__(self):
        """
        Возвращает строковое представление пользователя (его nickname).

        :return: nickname пользователя
        """
        return self.nickname

    def __repr__(self):
        """
        Возвращает официальное строковое представление пользователя.

        :return: Строка вида User(nickname, age)
        """
        return f"User(nickname='{self.nickname}', age={self.age})"


class Video:
    """
    Класс Video представляет видео на платформе UrTube.
    """

    def __init__(self, title, duration, adult_mode=False):
        """
        Инициализация видео.

        :param title: Заголовок видео (строка)
        :param duration: Продолжительность видео в секундах (число)
        :param adult_mode: Ограничение по возрасту (bool, по умолчанию False)
        """
        self.title = title
        self.duration = duration
        self.time_now = 0  # Время остановки просмотра, изначально 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        """
        Метод сравнения двух видео по заголовку.

        :param other: Другой объект Video для сравнения
        :return: True, если заголовки совпадают, иначе False
        """
        return self.title == other.title

    def __str__(self):
        """
        Возвращает строковое представление видео (его title).

        :return: title видео
        """
        return self.title

    def __repr__(self):
        """
        Возвращает официальное строковое представление видео.

        :return: Строка вида Video(title, duration, adult_mode)
        """
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"


class UrTube:
    """
    Класс UrTube представляет саму платформу, управляет пользователями и видео.
    """

    def __init__(self):
        """
        Инициализация платформы UrTube.
        """
        self.users = []  # Список объектов User
        self.videos = []  # Список объектов Video
        self.current_user = None  # Текущий авторизованный пользователь

    def log_in(self, nickname, password):
        """
        Метод авторизации пользователя.

        :param nickname: Имя пользователя (строка)
        :param password: Пароль пользователя (строка)
        """
        hashed_password = self.hash_password(password)  # Хэшируем введённый пароль для сравнения
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user  # Устанавливаем текущего пользователя
                return
        # Если пользователь не найден или пароль неверен
        print("Неправильный логин или пароль.")

    def register(self, nickname, password, age):
        """
        Метод регистрации нового пользователя.

        :param nickname: Имя пользователя (строка)
        :param password: Пароль пользователя (строка)
        :param age: Возраст пользователя (число)
        """
        # Проверяем, существует ли уже пользователь с таким nickname
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        # Создаём нового пользователя и добавляем в список
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user  # Автоматически авторизуем после регистрации

    def log_out(self):
        """
        Метод для выхода из аккаунта.
        """
        self.current_user = None

    def add(self, *videos):
        """
        Метод добавления видео на платформу.

        :param videos: Неограниченное количество объектов Video
        """
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)  # Добавляем видео, если его ещё нет
            # Если видео с таким названием уже существует, ничего не делаем

    def get_videos(self, search_word):
        """
        Метод поиска видео по ключевому слову.

        :param search_word: Поисковое слово (строка)
        :return: Список названий видео, содержащих поисковое слово (без учёта регистра)
        """
        search_word_lower = search_word.lower()
        return [video.title for video in self.videos if search_word_lower in video.title.lower()]

    def watch_video(self, title):
        """
        Метод воспроизведения видео.

        :param title: Название видео (строка)
        """
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # Ищем видео с точным совпадением названия (учитывая пробелы и регистр)
        video = next((v for v in self.videos if v.title == title), None)

        if video is None:
            # Если видео не найдено, ничего не делаем (по заданию)
            return

        # Проверяем возрастное ограничение
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        # Симулируем просмотр видео по секундам
        for second in range(1, video.duration + 1):
            print(second, end=' ')
            time.sleep(0.1)  # Уменьшил время сна для ускорения тестирования
        print("Конец видео")
        video.time_now = 0  # Сбрасываем время просмотра

    def hash_password(self, password):
        """
        Вспомогательный метод для хэширования пароля.

        :param password: Пароль в виде строки
        :return: Хэшированный пароль в виде целого числа
        """
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __str__(self):
        """
        Возвращает строковое представление текущего пользователя.

        :return: nickname текущего пользователя или "None"
        """
        return str(self.current_user) if self.current_user else "None"

    def __repr__(self):
        """
        Возвращает официальное строковое представление UrTube.

        :return: Строка вида UrTube(users, videos, current_user)
        """
        return f"UrTube(users={self.users}, videos={self.videos}, current_user={self.current_user})"


# Тестирование кода

if __name__ == "__main__":
    # Создаём экземпляр платформы UrTube
    ur = UrTube()

    # Создаём два видео
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео на платформу
    ur.add(v1, v2)

    # Проверка поиска видео
    print(ur.get_videos('лучший'))  # Ожидается: ['Лучший язык программирования 2024 года']
    print(ur.get_videos(
        'ПРОГ'))  # Ожидается: ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

    # Попытка просмотра видео без входа в аккаунт
    ur.watch_video('Для чего девушкам парень программист?')  # Ожидается: Войдите в аккаунт, чтобы смотреть видео

    # Регистрация пользователя 'vasya_pupkin' с возрастом 13
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)

    # Попытка просмотра взрослого видео пользователем младше 18 лет
    ur.watch_video('Для чего девушкам парень программист?')  # Ожидается: Вам нет 18 лет, пожалуйста покиньте страницу

    # Регистрация пользователя 'urban_pythonist' с возрастом 25
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

    # Воспроизведение взрослого видео пользователем старше 18 лет
    ur.watch_video('Для чего девушкам парень программист?')  # Ожидается: 1 2 3 4 5 6 7 8 9 10 Конец видео

    # Попытка повторной регистрации существующего пользователя 'vasya_pupkin'
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Ожидается: Пользователь vasya_pupkin уже существует

    # Проверка текущего авторизованного пользователя
    print(ur.current_user)  # Ожидается: urban_pythonist

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')  # Ожидается: (ничего)
