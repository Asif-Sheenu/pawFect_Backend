from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from Accounts.models import User

# Create your tests here.


class AdminUserTests(APITestCase):
    def setUp(self):
        self.admin= User.objects.create_superuser(email="admintest@gmail.com",password = "admin123",name="admin")
        self.user = User.objects.create_user(email ="user1@gmail.com", password = "user123",name="user1")
        self.client.force_authenticate(user=self.admin)


    def test_get_users_list(self):
        url = reverse("admin-users")
        response= self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["email"],self.user.email)
    
    
    def test_block_user(self):
        url = reverse("admin-userblock", args=[self.user.id])
        response= self.client.patch(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)

