from django.test import TestCase
from core.models import Profile

class ProfileModelTest(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            name='John Doe',
            profile_picture='profile/picture.jpg',
            about_me='Lorem ipsum dolor sit amet.',
            linkedin='https://www.linkedin.com/johndoe',
            github='https://github.com/johndoe',
            instagram='https://www.instagram.com/johndoe',
            twitter='https://twitter.com/johndoe',
            blog_name='My Blog',
            blog_description='Lorem ipsum dolor sit amet.',
            blog_theme='theme-1',
        )

    def test_profile_fields(self):
        self.assertEqual(self.profile.name, 'John Doe')
        self.assertEqual(self.profile.profile_picture, 'profile/picture.jpg')
        self.assertEqual(self.profile.about_me, 'Lorem ipsum dolor sit amet.')
        self.assertEqual(self.profile.linkedin, 'https://www.linkedin.com/johndoe')
        self.assertEqual(self.profile.github, 'https://github.com/johndoe')
        self.assertEqual(self.profile.instagram, 'https://www.instagram.com/johndoe')
        self.assertEqual(self.profile.twitter, 'https://twitter.com/johndoe')
        self.assertEqual(self.profile.blog_name, 'My Blog')
        self.assertEqual(self.profile.blog_description, 'Lorem ipsum dolor sit amet.')
        self.assertEqual(self.profile.blog_theme, 'theme-1')