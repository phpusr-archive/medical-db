from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=100)
    advices = models.ManyToManyField('Advice')

    def __str__(self):
        return self.name


class Advice(models.Model):
    recommendation = models.CharField(max_length=255)
    scientic_recommendation = models.TextField()

    class Type(models.IntegerChoices):
        ONE = 1,
        TWO = 2,
        THREE = 3

    type = models.PositiveIntegerField(choices=Type.choices)

    def __str__(self):
        return self.recommendation


class AdviceSource(models.Model):
    url = models.URLField()
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE, related_name='sources')

    def __str__(self):
        return self.url
