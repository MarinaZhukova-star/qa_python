class TestBooksCollector:

#Проверка попытки добавить книгу с длинным названием (>40 символов)
    def test_add_new_book_no_more_than_40(self, books_collector):
        books_collector.add_new_book('Прежде, чем я упаду')
        assert len(self.name) > 40

#Проверка, что метод возвращает правильный жанр, если книга найдена
    def test_set_book_genre_is_selected_from_list(self, books_collector):
        assert books_collector.books_genre['Крепкий орешек'] == 'Детектив'

#Проверка метода get_books_with_specific_genre на получение правильных результатов.
    def test_get_book_genre_found(self, books_collector):
        genre = books_collector.get_book_genre("Дюна")
        assert genre == "Фантастика"

#Проверка получения книг жанра 'Фантастика
    def test_get_books_with_specific_genre_fantasy(self, books_collector):
        fantasy_books = books_collector.get_books_with_specific_genre("Фантастика")
        assert fantasy_books == ["Дюна", "Пятый элемент"]

#Проверяет, что метод get_books_genre возвращает точный словарь books_genre    
    def test_get_books_genre_current_list(self, books_genre):
        expected_books_genre = kb.books_genre
        actual_books_genre = books_genre.get_books_genre()
        assert actual_books_genre == expected_books_genre

#Проверка позитивного сценария — отбор детских книг    
    def test_get_books_for_children_only_children_books(self, kids_book):
        expected_books = kb.books_genre
        children_books = kids_book.get_books_for_children()       
        assert children_books == expected_books

#Проверка положительного сценария добавления книги в избранные
    def test_add_book_in_favorites_success(self, books_genre):
        books_genre.add_book_in_favorites("Война миров")
        assert "Война миров" in books_genre.favorites

#проверка успешного удаления книги из избранного
    def test_delete_book_from_favorites_deletion_completed(self, favorites_books):
        favorites_books.delete_book_from_favorites("Такси")
        assert "Вино из одуванчиков" not in favorites_books.favorites

#Проверка возвращения списка избранных книг, когда список не пуст.
    def test_get_list_of_favorites_books_return_favorites(self, favorites_books):
        favorite_book = favorites_books.get_list_of_favorites_books()
        assert favorite_book == ["Вино из одуванчиков", "Такси"]

@pytest.mark.parametrize('fav_books', books_genre)
def test_check_fav_books(books_genre):
    assert check_fav_books(books_genre)