from rest_framework import status
from elearning.fixtures.user import user
from elearning.fixtures.post import post

class TestUserViewSet :
    endpoint = '/api/user/'
    
    def test_list(self, client, user):
        client.force_authenticate(user=user)
        responce = client.get(self.endpoint)
        assert responce.status_code == status.HTTP_200_OK
        assert responce.data["count"] == 1
    
    def test_retrieve(self, client, user):
        client.force_authenticate(user=user)
        responce = client.get(self.endpoint + str(user.public_id)+ "/")
        assert responce.status_code == status.HTTP_200_OK
        
    def test_create(self, client, user):
        data = {
            "user_name" : "other_test_user",
            "email" : "other_test@gmail.com",
            "password": "other_test_user_pass"
        }
        
        client.force_authenticate(user=user)
        responce = client.post(self.endpoint, data)
        
        assert responce.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_update(self, client, user):
        data = {
            "username" : "other_test_user",
            "email" : "other_test@gmail.com",
            "password": "other_test_user_pass"
        }
        client.force_authenticate(user=user)
        response = client.patch(self.endpoint + str(user.public_id) + "/", data)
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == data["username"]
        assert response.data["email"] == data["email"]
        
