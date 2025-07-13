import pytest


class TestBooksCollector:

#Проверка попытки добавить книгу
    @pytest.mark.parametrize('book', ['Лолита', 'Азазель'])
    def test_add_new_book_positive(self, books_collector, book):
        books_collector.add_new_book(book)
        assert len(books_collector.get_books_genre()) == 2

#Проверка, что метод возвращает правильный жанр, если книга найдена
    def test_set_book_genre_valid_name(self, books_collector):
        books_collector.add_new_book('Крепкий орешек')
        books_collector.set_book_genre('Крепкий орешек', 'Детективы')
        assert books_collector.books_genre['Крепкий орешек'] == 'Детективы'

#Проверка успешного возврата жанра книг
    def test_get_book_genre_existing(self, books_collector):
        books_collector.add_new_book('Мастер и Маргарита')
        books_collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert books_collector.get_book_genre('Мастер и Маргарита') == 'Фантастика'

#Проверка получения книг жанра 'Фантастика
    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):
        books_collector.add_new_book('Дюна')
        books_collector.set_book_genre('Дюна', 'Фантастика')
        assert books_collector.get_books_with_specific_genre('Фантастика')  \
               and type(books_collector.get_books_with_specific_genre('Фантастика')) == list

#Проверяет, что метод get_books_genre возвращает пустой словарь books_genre    
    def test_get_books_genre_empty_dict(self, books_collector):
        assert not books_collector.get_books_genre()

#Проверка позитивного сценария — отбор детских книг    
    def test_get_books_for_children_correct_genre(self, books_collector):
        books = ['Золотой ключик', 'Русалочка', 'Малыш и Карлсон']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre[x])
            x += 1

        for rating in books_collector.genre_age_rating:
            assert rating not in books_collector.get_books_for_children()

#Проверка положительного сценария добавления книги в избранные
    def test_add_book_in_favorites_success(self, books_collector):
        books_collector.add_new_book('Сонная лощина')
        books_collector.add_book_in_favorites('Сонная лощина')
        assert 'Сонная лощина' in books_collector.favorites

#проверка успешного удаления книги из избранного
    def test_delete_book_from_favorites_deletion_completed(self, books_collector):
        books_collector.add_new_book('Такси')
        books_collector.delete_book_from_favorites("Такси")
        assert "Вино из одуванчиков" not in books_collector.favorites

#Проверка возвращения списка избранных книг
    def test_get_list_of_favorites_books_not_empty(self, books_collector):
        books = ['1984', 'Заводной апельсин', 'Мы']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)
        assert books_collector.get_list_of_favorites_books()