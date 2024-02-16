import pytest

from elearning.fixtures.user import user
from elearning.post.models import Post


@pytest.fixture
def post(db, user):
    return Post.objects.create(author=user, body="Test Post Body")