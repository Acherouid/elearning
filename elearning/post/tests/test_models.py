import pytest

from elearning.fixtures.user import user
from elearning.post.models import Post

@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(author=user, body="Test Post Body")
    assert post.body == "Test Post Body"
    assert post.author == user