from django.db import models
# Create your models here.
class Blog(models.Model):
    id                  =   models.AutoField(primary_key=True)
    TopicName           =   models.CharField(unique=True,null=False,max_length=100)
    Image               =   models.CharField(unique=True,null=False,max_length=100)
    TopicDescription    =   models.CharField(unique=True,null=False,max_length=2000)
    SubTopic            =   models.CharField(null=False,default='all',max_length=50)
    CreationTime        =   models.DateField()

    class Meta:
        db_table="blog"

