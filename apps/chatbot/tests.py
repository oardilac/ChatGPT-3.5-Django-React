from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from chatbot.models import AIPost

class AIPostTest(TestCase):
    """ Test module for AIPost model """

    def setUp(self):
        self.client = APIClient()
        self.aipost_data = {
            'title': 'Test AIPost',
            'content': 'This is a test AIPost'
        }
        self.response = self.client.post(
            reverse('aipost-list'),
            self.aipost_data,
            format='json')

    def test_create_aipost(self):
        """ Test the creation of a new AIPost """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AIPost.objects.count(), 1)
        self.assertEqual(AIPost.objects.get().title, self.aipost_data['title'])

    def test_get_aipost(self):
        """ Test retrieving a single AIPost """
        aipost = AIPost.objects.get()
        response = self.client.get(
            reverse('aipost-detail', kwargs={'pk': aipost.id}),
            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], aipost.title)

    def test_update_aipost(self):
        """ Test updating an existing AIPost """
        aipost = AIPost.objects.get()
        updated_aipost = {'title': 'Updated Test AIPost', 'content': 'This is an updated test AIPost'}
        response = self.client.put(
            reverse('aipost-detail', kwargs={'pk': aipost.id}),
            updated_aipost,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_aipost['title'])

    def test_delete_aipost(self):
        """ Test deleting an existing AIPost """
        aipost = AIPost.objects.get()
        response = self.client.delete(
            reverse('aipost-detail', kwargs={'pk': aipost.id}),
            format='json',
            follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
