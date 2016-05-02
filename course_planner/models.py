from django.db import models
from django.db.models import Count, Sum
from django.contrib import admin

class Quarter(models.Model):
    AUTUMN = 0
    WINTER = 1
    SPRING = 2
    SUMMER = 3

    SEASON_CHOICES = (
        (AUTUMN, "Autumn"),
        (WINTER, "Winter"),
        (SPRING, "Spring"),
        (SUMMER, "Summer")
    )
    year = models.CharField(max_length=20)
    season = models.IntegerField(default=0, choices=SEASON_CHOICES)
    unit_cap = models.IntegerField(default=10)

    def __str__(self):
        return "{} {}".format(self.year, self.get_season_display())

    def within_unit_cap(self):
        course_units = self.course_set.all().aggregate(total=Sum('units'))
        return course_units['total'] <= self.unit_cap

    class Meta:
        ordering = ('year', 'season')

class Course(models.Model):
    department = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    grade = models.CharField(max_length=10, blank=True)
    units = models.IntegerField(default=3)
    quarter = models.ForeignKey(Quarter)

    def __str__(self):
        return "{} {}: {} ({} units; {})".format(self.department, self.number, self.name, self.units, self.quarter)

    def short_str(self):
        return "{} {}: {}".format(self.department, self.number, self.short_name)

    class Meta:
        ordering = ('quarter__year', 'quarter__season', 'department', 'number')

class RequirementSource(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('weight',)

class Requirement(models.Model):
    COUNT_BY_COURSES = 0
    COUNT_BY_UNITS = 1
    COUNTING_METHODS = (
        (COUNT_BY_COURSES, 'courses'),
        (COUNT_BY_UNITS, 'units')
    )
    name = models.CharField(max_length=100)
    source = models.ForeignKey(RequirementSource)
    counting_method = models.IntegerField(default=COUNT_BY_COURSES, choices=COUNTING_METHODS)
    count_required = models.IntegerField(default=1)
    courses = models.ManyToManyField(Course, related_name="requirements")

    @property
    def progress(self):
        if self.counting_method == self.COUNT_BY_COURSES:
            return self.courses.count()
        else:
            total = self.courses.aggregate(units=Sum('units'))
            return total['units']

    def progress_display(self):
        return "{} of {} {}".format(self.progress, self.count_required, self.get_counting_method_display())

    @property
    def satisfied(self):
        return self.progress >= self.count_required
            
    def __str__(self):
        return "{}: {} ({})".format(self.source, self.name, self.progress_display())

admin.site.register(Course)
admin.site.register(RequirementSource)
admin.site.register(Requirement)
admin.site.register(Quarter)
