from django.db import models
from rest_framework.exceptions import ValidationError


class SpyCat(models.Model):
    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=100, decimal_places=2)
    current_mission = models.OneToOneField(
        'Mission',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='spy_cats'
    )

    def __str__(self):
        return self.name


class Mission(models.Model):
    name = models.CharField(max_length=100)
    assigned_cat = models.ForeignKey(
        SpyCat,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='missions'
    )
    is_complete = models.BooleanField(default=False)
    targets = models.ManyToManyField("Target", related_name='missions')

    def __str__(self):
        return self.name

    def validate_mission(self):
        if not (1 <= self.targets.count() <= 3):
            raise ValidationError(
                {"targets": "There must be between 1 and 3 "
                            "targets assigned to the mission."}
            )

    def check_completion(self):
        if all(target.is_complete for target in self.targets.all()):
            self.is_complete = True
            self.save()


class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)
    mission = models.ForeignKey(
        "Mission",
        on_delete=models.CASCADE,
        related_name="target_missions"
    )

    class Meta:
        unique_together = ("name", "mission")
        ordering = ("name",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_complete:
            self.notes = self.notes
        super(Target, self).save(*args, **kwargs)
