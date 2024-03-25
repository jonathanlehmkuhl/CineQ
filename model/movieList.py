from model.movie import Movie


class MovieList:
    def __init__(self):
        self.movies = []

    def __getitem__(self, index):
        return self.movies[index]

    def __len__(self):
        return len(self.movies)

    def add_movie(self, movie):
        if isinstance(movie, Movie):
            self.movies.append(movie)
        else:
            print("Invalid object. It should be an instance of Movie class.")
