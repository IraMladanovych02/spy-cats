from django.db import models


class SpyCat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    current_mission = models.OneToOneField(
        'Mission',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='spy_cat_mission'
    )

    def __str__(self):
        return self.name


class Mission(models.Model):
    name = models.CharField(max_length=100)
    assigned_cat = models.OneToOneField(
        SpyCat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='mission_assigned_cat'
    )
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='targets')
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

