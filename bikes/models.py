from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Users


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Colors(models.Model):
    color_name = models.CharField(max_length=64)

    class Meta:
        db_table = 'colors'

    def __str__(self):
        return self.color_name


class Size(models.Model):
    sizetype = models.CharField(max_length=64)

    class Meta:
        db_table = 'size'

    def __str__(self):
        return self.sizetype


class Bike(models.Model):
    bikemodel = models.CharField(max_length=255, default='no bike model yet')
    image = models.ImageField(upload_to='bike_img/', default='default_img/')
    bikecolor = models.ForeignKey(Colors, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.IntegerField()
    miqdori = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'bike'

    def __str__(self):
        return self.bikemodel


class Review(models.Model):
    comment = models.CharField(max_length=255)
    star_given = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f'{self.star_given} - {self.bike.model} - {self.user.username}'


class PurchaseRequest(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchase_request'

    def __str__(self):
        return f'{self.name} - {self.phone}'