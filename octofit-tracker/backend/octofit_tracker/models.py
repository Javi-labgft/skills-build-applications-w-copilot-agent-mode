from djongo import models


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)  # nombre del equipo
    is_superhero = models.BooleanField(default=False)
    def __str__(self):
        return self.email


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name


class Activity(models.Model):
    user_email = models.EmailField()  # referencia por email
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutos
    date = models.DateField()
    def __str__(self):
        return f"{self.user_email} - {self.type}"


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    team_name = models.CharField(max_length=50)  # referencia por nombre
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.team_name} - {self.points}"
