from django.shortcuts import render
from .models import Youth

def home(request):
    youths = Youth.objects.all()
    return render(request, 'home.html', {'youths': youths})

def recommendations(request, youth_id):
    youth = Youth.objects.get(id=youth_id)
    programs = youth.recommend_programs()
    return render(request, 'recommendations.html', {
        'youth': youth,
        'programs': programs
    })
