from django.test import TestCase
from ..models import TeamMember, Roles
from unittest.mock import Mock, mock_open, call, patch

class ViewTestCase(TestCase):
    def setUp(self):
        TeamMember.objects.create()
        TeamMember.objects.create()

    def tearDown(self):
        TeamMember.objects.all().delete()

    def test_member_list_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_view_url(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 301)
        
    def test_edit_view_url(self):
        response = self.client.get('/edit/1/')
        self.assertEqual(response.status_code, 200)

    def test_delete_view_url(self):
        response = self.client.get('/delete/1/')
        self.assertEqual(response.status_code, 302)

    def test_delete_view(self):
        response = self.client.get('/delete/1/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/delete/2/')
        self.assertEqual(response.status_code, 302)

        num_objects = len(TeamMember.objects.all())
        self.assertEqual(num_objects, 0)
