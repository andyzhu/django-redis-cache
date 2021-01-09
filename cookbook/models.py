from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)
    ingredients = models.ManyToManyField(
        'cookbook.Food',
        through='cookbook.Ingredient',
        through_fields=('recipe', 'food')
    )
    instructions = models.TextField(null=True, blank=True)

    class Meta(object):
        app_label = 'cookbook'
        default_related_name = 'recipes'

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'cookbook'
        default_related_name = 'foods'
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)

    unit_of_measure = models.CharField(max_length=255)

    desc = models.TextField()
    
    class Meta:
        app_label = 'cookbook'
    
    def __str__(self):
        return f'{self.recipe}: {self.amount} {self.unit_of_measure} {self.food}'
