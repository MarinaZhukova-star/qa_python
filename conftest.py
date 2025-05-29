@pytest.fixture(scope='session')
def books_collector():
    collector = BooksCollector()
    collector.add_new_book("Дюна", "Фантастика")
    collector.add_new_book("Прежде, чем я упаду", "Ужасы")
    collector.add_new_book("Крепкий орешек", "Детективы")
    collector.add_new_book("Любовь и голуби", "Комедии")
    collector.add_new_book("Пятый элемент", "Фантастика")
    return collector

@pytest.fixture(scope='session')
def books_genre():
    bc = BooksCollector()
    bc.books_genre = {
        "Война миров": "Фантастика",
        "12 стульев": "Комедии",
        "17 мгновений весны": "Детектив"
    }
    return bc

@pytest.fixture(scope='session')
def kids_book():
    kb = BooksCollector()
    kb.books_genre = {
        "Щелкунчик": "Мультфильмы",
        "Русалочка": "Мультфильмы",
        "Золушка": "Мультфильмы"
    }
    return kb

@pytest.fixture(scope='session')
def favorites_booksfavorites_books():
    fb = BooksCollector()
    fb.books_genre = {
        "Дюна", "Фантастика",
        "Прежде, чем я упаду", "Ужасы",
        "Крепкий орешек", "Детективы",
        "Пятый элемент", "Фантастика"
    }
    fb.favorites = ["Прежде, чем я упаду", "Пятый элемент"]
    return fb