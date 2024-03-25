class Movie:
    def __init__(self, name, director, logo=None):
        self.name = name
        self.director = director
        self.logo = logo

    def get_title(self):
        return self.name

    def get_director(self):
        return self.director

    def get_logo(self):
        return self.logo
