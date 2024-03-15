from django.db import models

# Create your models here.
class ArticleData(models.Model):
    """Initial inventory items"""
  
    title = models.CharField(max_length=200 , blank=True, null=True)
    image = models.URLField(max_length=200,null=True,blank=True)
    date = models.DateTimeField(blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    article_source = models.CharField(max_length=100 , blank=True, null=True)
   
    def __str__(self):
        return self.title
