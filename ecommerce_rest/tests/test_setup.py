from faker import Faker

from rest_framework.test import APITestCase
from rest_framework import status

class TestSetUp(APITestCase):
    
    def setup(self):
        from apps.users.models import User
        
        faker = Faker()
        
        self.login_url = '/login/'
        self.user = User.objects.create_superuser(
            name = 'OscarJ',
            last_name = 'Jesus',
            username = faker.name(),
            password = 'maiki02',
            email = faker.email()    
        )
        
        response = self.client.post(
            self.login_url,
            {
                'username':self.user.username,
                'password': 'maiki02'
            },
            format = 'json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION= 'Bearer' + self.token)
        return super().setUP()
    
