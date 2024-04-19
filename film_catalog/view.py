def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f' {title} '.center(50, '='))
            output = func(*args, **kwargs)
            print('=' * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title('Редактирование данных каталога фильмов')
    def wait_user_answer(self):
        print('1 - добавление фильма'
              '\n2 - каталог фильмов'
              '\n3 - просмотр определенного фильма'
              '\n4 - удаление фильма'
              '\nq - выход из программы')
        user_answer = input('Действия с фильмами: ')
        return user_answer

    @add_title('Запись данных о фильме')
    def add_user_film(self):
        dict_film = {
            'название фильма': None,
            'жанр': None,
            'режиссер': None,
            'год выпуска': None,
            'длительность': None,
            'студия': None,
            'актеры': []
        }
        for key in dict_film:
            if key == 'актеры':
                dict_film[key] = input('Введите список актеров через пробел:').split()
            else:
                dict_film[key] = input(f'Введите {key}: ')
        return dict_film

    @add_title('Каталог фильмов')
    def show_all_films(self, films):
        for ind, film in enumerate(films, start=1):
            print(f'{ind}. {film}')

    @add_title('Ввод названия фильма')
    def get_user_film(self):
        user_film = input('Введите название фильма: ')
        return user_film

    @add_title('Просмотр данных о фильме')
    def show_single_film(self, film):
        for key in film:
            print(f"{key} {film[key]}")

    @add_title('Сообщение об ошибке')
    def show_incorrect_title_error(self, user_film):
        print(f'Фильма с названием {user_film} не существует')

    @add_title('Удаление фильма')
    def remove_single_film(self, film):
        print(f'Фильм {film} был удален')

    @add_title('Сообщение об ошибке')
    def show_incorrect_answer_error(self, answer):
        print(f'Варианта {answer} не существует')
