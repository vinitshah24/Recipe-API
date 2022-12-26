from django.test import TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch

from decimal import Decimal

from core import models


def create_user(email='test@gmail.com', password='some_pass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'test@gmail.com'
        password = 'some_pass'
        user = create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)

    def test_new_user_email_normalized(self):
        """Test that the email for new user is normalized"""
        sample_tests = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"]
        ]
        for email, expected_email in sample_tests:
            user = create_user(email=email, password='some_pass')
            self.assertEqual(user.email, expected_email)

    def test_new_user_invalid_email(self):
        """Test create new user without an email raises an error"""
        with self.assertRaises(ValueError):
            create_user(None, 'some_pass')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('test@gmail.com', 'some_pass')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        user = create_user(email='test@example.com', password='some_pass')
        recipe = models.Recipe.objects.create(user=user,
                                              title='Test Recipe',
                                              time_minutes=5,
                                              price=Decimal(5.50),
                                              description='Sample Description')
        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(user=create_user(), name='Tag1')
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(user=create_user(), name='Cucumber')
        self.assertEqual(str(ingredient), ingredient.name)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')
        expected_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, expected_path)
