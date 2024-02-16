from django.db import models
from elearning.abstract.models import AbstractModel, AbstractManager

# Create your models here.

class CommentManager(AbstractManager):
    pass
class Comment(AbstractModel):
    post = models.ForeignKey(to="elearning_post.Post", on_delete=models.CASCADE)
    author = models.ForeignKey(to="elearning_user.User", on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    
    objects = CommentManager()
    
    def __str__(self):
        return self.author.name