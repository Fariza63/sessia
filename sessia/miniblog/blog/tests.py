from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTest(TestCase):

    def setUp(self):
        # Тест үшін қолданушы жасау
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_post(self):
        # Пост жасау
        post = Post.objects.create(title='Test Post', content='This is a test post', author=self.user)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post')
        self.assertEqual(post.author, self.user)

class CommentModelTest(TestCase):

    def setUp(self):
        # Тест үшін қолданушы және пост жасау
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', content='This is a test post', author=self.user)

    def test_create_comment(self):
        # Комментарий жасау
        comment = Comment.objects.create(post=self.post, text='This is a test comment', author=self.user)
        self.assertEqual(comment.text, 'This is a test comment')
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.author, self.user)
