from django.test import TestCase
from ..models import TeamMember, Roles
from ..views.add import AddView
from unittest.mock import Mock, mock_open, call, patch

class AddViewTestCase(TestCase):
    def create_member(self, first_name, last_name, phone_number, email_address, role):
        member = TeamMember.objects.create()
        member.first_name=first_name
        member.last_name=last_name
        member.phone_number=phone_number
        member.email_address=email_address
        member.role=role
        member.save()
        return member

    def setUp(self):
        self.create_member("first_name1", "last_name1", "12345678", "number_one@gmail.com", Roles.REGULAR)
        self.create_member("first_name2", "last_name2", "87654321", "number_two@gmail.com", Roles.ADMIN)

    def tearDown(self):
        TeamMember.objects.all().delete()

    def test_create(self):
        self.assertEqual(TeamMember.objects.count(), 2)
        TeamMember.objects.create()
        self.assertEqual(TeamMember.objects.count(), 3)
    
    def test_delete(self):
        TeamMember.objects.get(id=1).delete()
        self.assertEqual(TeamMember.objects.count(), 1)
    
    def test_update(self):
        member = TeamMember.objects.get(id=1)
        self.assertEqual(member.first_name, "first_name1")
        self.assertEqual(member.last_name, "last_name1")

        member.first_name="updated_first_name"
        member.last_name="updated_last_name"
        member.save()

        member = TeamMember.objects.get(id=1)
        self.assertEqual(member.first_name, "updated_first_name")
        self.assertEqual(member.last_name, "updated_last_name")