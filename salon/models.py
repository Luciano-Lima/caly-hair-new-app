from django.db import models


# # # Create your models here.

class Cutting(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Cutting & Styling'
        verbose_name_plural = 'Cutting & Styling'

        def __str__(self):
                return self.verbose_name

# class Styling(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     class Meta:
#         verbose_name = 'Up-Styling'
#         verbose_name_plural = 'Up-Styling'

#     def __str__(self):
#         return self.name

# class Colour(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     class Meta:
#         verbose_name_plural = "Colour"

#     def __str__(self):
#         return self.name   

# class Highlights(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     class Meta:
#         verbose_name_plural = 'highlight'

#     def __str__(self):
#         return self.name

# class Toners(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     class Meta:
#         verbose_name_plural = 'Toner'

#     def __str__(self):
#         return self.name

# class Treatment(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

#     class Meta:
#         verbose_name_plural = 'Treatment'

#     def __str__(self):
#         return self.name