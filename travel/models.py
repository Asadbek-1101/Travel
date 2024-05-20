from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="category_image", null=True)

    def __str__(self):
        return f"{self.name}"

class Davlatlar(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True, related_name="davlat")
    image = models.ImageField(upload_to="davlat_image", null=True)

    def __str__(self):
        return f"{self.name}"

class Reys(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="reys", null=True)

    def __str__(self):
        return f"{self.name}"

class Country(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    reys = models.ForeignKey(Reys, on_delete=models.CASCADE, related_name="country")
    destination = models.CharField(max_length=100)
    image = models.ImageField(upload_to="reys_image", null=True)

    def __str__(self):
        return f"{self.name}"





