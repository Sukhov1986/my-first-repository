class Film:
    def __init__(self, name, genre, director, year, duration, studio, actors):
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.name} ({self.year})'


class FilmModel:
    def __init__(self):
        self.films = {}

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.name] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_film):
        film = self.films[user_film]
        dict_film = {
            'название фильма': film.name,
            'жанр': film.genre,
            'режиссер': film.director,
            'год выпуска': film.year,
            'длительность': film.duration,
            'студия': film.studio,
            'актеры': film.actors
        }
        return dict_film

    def remove_film(self, user_film):
        return self.films.pop(user_film)


