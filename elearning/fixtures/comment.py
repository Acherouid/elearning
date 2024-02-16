import pytest

from elearning.fixtures.user import user
from elearning.fixtures.post import post

from elearning.comment.models import Comment

@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(author=user, post=post, body="Test Comment Body")