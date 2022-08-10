from django.db import models

# TODO: need second model to store docs content

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=50)
    content = models.TextField()
    revision = models.DateTimeField(auto_now_add=True)
