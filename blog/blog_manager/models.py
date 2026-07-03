from django.db import models

# Create your models here.
# blog:names,articles,chronological
# article: Heading,body,colums,comment_section,page_number,creator(user)
# user:roles,username,password,year

class User(models.Model):
    roles=models.CharField()
    year=models.IntegerField()
    password=models.CharField()
    username=models.CharField()

class Blog(models.Model):
    names=models.CharField(default='',unique=True, max_length=7)
    age=models.IntegerField()
    onetoone=models.OneToOneField(User)
    owner=models.ForeignKey(User)


class articles(models.Models):
    Heading=models.CharField()
    body=models.CharField()
    column=models.IntegerField()
    comment_section=models.CharField()
    page_number=models.IntegerField()
    creator=models.CharField()

# user=User.objects.create(roles='admin',year=2089,password='ekMEDu3',username='askO')
user=User.objects.get(username='ask',year=2000)
user.roles
user=User.objects.filter(username='jsdn',).order_by('year').all()

User.objects.filter(year=2000).update(year=2001)
# Tmw prebuilt project to analyze and reconstruct
# object. and filter. pick 5 and ask questions Assignment//////// get or create to tell him what that means

user=User.objects.only
user=User.objects.values_list
user=User.objects.__len__
user=User.objects.use_in_migrations
user=User.objects.none

User.objects.filter.__annotations__
User.objects.filter.__closure__
User.objects.filter.__str__
User.objects.filter.__annotations__
User.objects.filter.__defaults__