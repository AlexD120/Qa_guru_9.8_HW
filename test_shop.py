"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500) is True

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(500)  # Покупаем 500 продуктов
        assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
            # TODO напишите проверки на метод buy,
            #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
            with pytest.raises(ValueError):
                product.buy(1500) # Пытаемся купить больше, чем есть в наличии, ожидаем ошибку ValueError


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product):
        cart = Cart()
        cart.add_product(product, 3)
        assert cart.products == {product: 3}  # Проверяем, что продукт добавлен в корзину

    def test_remove_product(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        cart.remove_product(product, 2)
        assert cart.products == {product: 3}  # Проверяем, что количество продукта уменьшилось на 2

    def test_remove_product_entirely(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert cart.products == {}  # Проверяем, что весь продукт был удален из корзины

    def test_clear(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        cart.clear()
        assert cart.products == {}  # Проверяем, что корзина была очищена

    def test_get_total_price(self, product):
        cart = Cart()
        cart.add_product(product, 3)
        assert cart.get_total_price() == 300  # Проверяем, что общая стоимость рассчитана

    def test_buy(self, product):
        cart = Cart()
        cart.add_product(product, 3)
        cart.buy()  # Покупаем продукты из корзины
        assert product.quantity == 997  # Проверяем, что количество продуктов уменьшилось

    def test_remove_product_more_than_available(self, product):
        cart = Cart()
        product = Product("Test Product", 10.0, "Description", 5)

        # Добавляем продукт в корзину
        cart.add_product(product, 3)

        # Удаляем больше, чем есть в корзине
        cart.remove_product(product, 5)

        # Проверяем, что продукта больше нет в корзине
        assert product not in cart.products