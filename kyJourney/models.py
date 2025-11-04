from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_learned = models.DateField()
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    student_id = models.CharField(max_length=20)
    interests = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class AdminScreenshot(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='admin_screenshots/')
    display_order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.title