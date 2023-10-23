from django.db import models


#


class Country(models.Model):
    code = models.CharField(verbose_name="Код страны", max_length=2, unique=True)
    name = models.CharField(verbose_name="Название страны", max_length=100)

    def __str__(self):
        return "{} ({})".format(self.name, self.code)


class Language(models.Model):
    code = models.CharField(verbose_name="Код языка", max_length=2, unique=True)
    name = models.CharField(verbose_name="Название языка", max_length=100)

    def __str__(self):
        return "{} ({})".format(self.name, self.code)
