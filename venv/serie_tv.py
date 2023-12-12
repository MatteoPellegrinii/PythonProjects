class SerieTV:
    def __init__(self, titolo, genere, stagioni, episodi, anno):
        self.titolo = titolo
        self.genere = genere
        self.stagioni = stagioni
        self.episodi = episodi
        self.anno = anno

    def __str__(self):
        return f"{self.titolo} ({self.anno}), Genere: {self.genere}, Stagioni: {self.stagioni}, Episodi: {self.episodi}"

# Creiamo una lista di istanze della classe SerieTV
serie_tv_list = [
    SerieTV("Breaking Bad", "Drama", 5, 62, 2008),
    SerieTV("Stranger Things", "Sci-Fi", 4, 34, 2016),
    SerieTV("Game of Thrones", "Fantasy", 8, 73, 2011),
    SerieTV("The Mandalorian", "Action", 2, 16, 2019),
    SerieTV("Friends", "Comedy", 10, 236, 1994),
    SerieTV("The Office", "Comedy", 9, 201, 2005),
    SerieTV("Black Mirror", "Sci-Fi", 6, 22, 2011),
    SerieTV("The Simpsons", "Animation", 33, 704, 1989),
    SerieTV("Sherlock", "Crime", 4, 13, 2010),
    SerieTV("Westworld", "Sci-Fi", 3, 28, 2016)
]


# Puoi aggiungere altri nomi di serie TV a questa lista


def aggiungi_serie(serie):
    serie_tv_list.append(serie)

def rimuovi_serie(titolo):
    global serie_tv_list
    serie_tv_list = [serie for serie in serie_tv_list if serie.titolo != titolo]



def trova_serie(titolo):
    for serie in serie_tv_list:
        if serie.titolo == titolo:
            return serie
    return None
