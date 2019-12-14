from django.db import models


# Create your models here.
# creating table in database(travello) directly
# from the destination class using concept of ORM(Object Relation Mapper)
class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

# NORMAL CLASS BASE FOR CREATE DYNAMIC PAGE
# class Destination:
#     id: int
#     name: str
#     desc: str
#     price: int
#     img: str
#     offer: bool
#

    # def __init__(self, id, name, desc, price, image, offer):
    #     self.id = id
    #     self.name = name
    #     self.desc = desc
    #     self.price = price
    #     self.img = image
    #     self.offer = offer
