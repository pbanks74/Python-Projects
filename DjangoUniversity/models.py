from django.db import models

# created a class and defined its attributes
class djangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=False, null=False)
    CourseNumber = models.IntegerField(default="", blank=False, null=False)
    InstructorName = models.CharField(max_length=60, default="", blank=False, null=False)
    Duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    # assigns a manager
    objects = models.Manager()

    # returns title of course
    def __str__(self):
        return self.Title