from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="person_photo")
    bio = models.TextField()
    dob = models.DateField()


    def __unicode__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=50)
    cover_photo = models.ImageField(upload_to="movie_cover")
    description = models.TextField()
    release_date = models.DateField(default=now)
    rating = models.IntegerField(default=1, validators=[
                MaxValueValidator(5),
                MinValueValidator(1)
            ])

    directors = models.ManyToManyField(Person, related_name='director')
    writers = models.ManyToManyField(Person, related_name='writer')
    actors = models.ManyToManyField(Person, related_name='actor')

    def add_staff(self, staff_type, person):
        if staff_type == 'director':
            self.directors.add(person)
        elif staff_type == 'writer':
            self.writers.add(person)
        elif staff_type == 'actor':
            self.actors.add(person)
        else:
            raise ValueError('Unknown staff_type: ' + str(staff_type))

    def __unicode__(self):
        return self.title