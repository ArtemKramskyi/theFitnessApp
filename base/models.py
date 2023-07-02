from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class ExercisesCatalog(models.Model):
    CHEST = 'CHST'
    BACK = 'BCK'
    BICEPS = 'BCPS'
    TRICEPS = 'TRPS'
    ABDOMINALS = 'ABS'
    LEGS = 'LEG'
    SHOULDERS = 'SHLD'
    OTHER = 'OTH'
    EXERCISES_CATEGORIES = [
        (None, '---'),
        (CHEST, 'Chest'),
        (BACK, 'Back'),
        (BICEPS, 'Biceps'),
        (TRICEPS, 'Triceps'),
        (ABDOMINALS, 'Abdominals'),
        (LEGS, 'Legs'),
        (SHOULDERS, 'Shoulders'),
        (OTHER, 'Other')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exerciseName = models.CharField(max_length=80)
    exerciseDescription = models.CharField(max_length=450)
    exerciseImg = models.CharField(max_length=250, null=True, blank=True)
    category = models.CharField(
        max_length=15, choices=EXERCISES_CATEGORIES, default=EXERCISES_CATEGORIES[0][0])
    sets = models.PositiveIntegerField(default=3)
    reps = models.PositiveIntegerField(default=12)

    def __str__(self):
        return self.exerciseName


class Program(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    programName = models.CharField(max_length=150)

    def __str__(self):
        return self.programName


class Plan(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    exercise = models.ForeignKey(ExercisesCatalog, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('program', 'exercise')

    def __str__(self):
        return f"{self.program.user}: Program {self.program} -> Exercise {self.exercise}"
