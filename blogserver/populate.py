import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogserver.settings")
import django
django.setup()
import datetime
from BlogDetails.models import Blog

def populate():
    blog = Blog.objects.get_or_create(
        TopicName="What is Docker?",
        Image='test1', 
        TopicDescription="lorem ipsum1", 
        SubTopic="Web Development",
        CreationTime=datetime.datetime.now()
        )

if __name__=='__main__':
    print("Populating Database")
    populate()
    print("Databse populated")