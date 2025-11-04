from django.shortcuts import render
from .models import LearningJourney, AboutMe, AdminScreenshot

def index(request):
    journey_items = LearningJourney.objects.all().order_by('-date_learned')
    admin_screenshots = AdminScreenshot.objects.all()
    
    context = {
        'journey_items': journey_items,
        'admin_screenshots': admin_screenshots,
    }
    return render(request, 'index.html', context)

def about_me(request):
    about_info = AboutMe.objects.first()
    
    context = {
        'about_info': about_info,
    }
    return render(request, 'aboutMe.html', context)