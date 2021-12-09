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
