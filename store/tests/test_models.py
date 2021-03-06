from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Testeo del modelo de categoria para los atributos de inserción de datos/tipos/campos
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
    
    def test_category_model_entry(self):
        """
        Testeo del modelo de categoria para el "return name"
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProducsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='10.00', image='django')

    def test_products_model_entry(self):
        """
        Testeo del modelo de producto para los atributos de inserción de datos/tipos/campos
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')