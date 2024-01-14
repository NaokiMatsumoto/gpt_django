from django.db import models

# Model for Prefecture
class Prefecture(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for City
class City(models.Model):
    name = models.CharField(max_length=100)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Model for Restaurant
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
