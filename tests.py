import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("book_name", [
        "Маленький принц",
        "Война и мир",
        "А" * 40  
    ])
    def test_add_new_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        assert collector.get_book_genre(book_name) == ''

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Тестовая книга")
        
        for genre in ['Фантастика', 'Ужасы', 'Мультфильмы']:
            collector.set_book_genre("Тестовая книга", genre)
            assert collector.get_book_genre("Тестовая книга") == genre

    def test_get_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Комедия 1")
        collector.set_book_genre("Комедия 1", "Комедии")
        collector.add_new_book("Комедия 2")
        collector.set_book_genre("Комедия 2", "Комедии")
        
        books = collector.get_books_with_specific_genre("Комедии")
        assert sorted(books) == ["Комедия 1", "Комедия 2"]

    def test_get_books_genre(self):
        collector = BooksCollector()
        names = ["Книга1", "Книга2"]
        for name in names:
            collector.add_new_book(name)
        genres = collector.get_books_genre()
        for name in names:
            assert name in genres
            assert genres[name] == ''

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.add_new_book('Страшилка')
        collector.set_book_genre('Страшилка', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert 'Детская книга' in books_for_children
        assert 'Страшилка' not in books_for_children

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Фаворит')
        collector.add_book_in_favorites('Фаворит')
        collector.add_book_in_favorites('Фаворит') 
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count('Фаворит') == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Удаляемая книга')
        collector.add_book_in_favorites('Удаляемая книга')
        collector.delete_book_from_favorites('Удаляемая книга')
        assert 'Удаляемая книга' not in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites('Удаляемая книга')

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга2')
        favorites = collector.get_list_of_favorites_books()
        assert sorted(favorites) == ['Книга1', 'Книга2']
