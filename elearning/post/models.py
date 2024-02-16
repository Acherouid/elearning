from django.db import models
from elearning.abstract.models import AbstractModel, AbstractManager

# Create your models here.

class PostManager(AbstractManager):
    pass

class Post(AbstractModel):
    author = models.ForeignKey(to="elearning_user.User", on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    
    objects = PostManager()
    
    def __str__(self):
        # return f"{self.author.name}"
        return f"{self.body}"
    
    # class Meta:
    #     # db_table = "'elearning.post'"
    #     db_table = 'elearning_post'