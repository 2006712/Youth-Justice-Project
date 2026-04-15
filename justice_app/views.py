from django.shortcuts import render, redirect
from .models import Youth, Offence, SupportProgram
from .forms import YouthForm, OffenceForm, SupportProgramForm


def home(request):
    return render(request, 'justice_app/home.html')


def youth_list(request):
    youths = Youth.objects.all()
    return render(request, 'justice_app/youth_list.html', {'youths': youths})


def offence_list(request):
    offences = Offence.objects.all()
    return render(request, 'justice_app/offence_list.html', {'offences': offences})


def support_program_list(request):
    programs = SupportProgram.objects.all()
    return render(request, 'justice_app/program_list.html', {'programs': programs})


def add_youth(request):
    if request.method == 'POST':
        form = YouthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('youth_list')
    else:
        form = YouthForm()
    return render(request, 'justice_app/form.html', {'form': form, 'title': 'Add Youth'})


def add_offence(request):
    if request.method == 'POST':
        form = OffenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('offence_list')
    else:
        form = OffenceForm()
    return render(request, 'justice_app/form.html', {'form': form, 'title': 'Add Offence'})


def add_support_program(request):
    if request.method == 'POST':
        form = SupportProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('support_program_list')
    else:
        form = SupportProgramForm()
    return render(request, 'justice_app/form.html', {'form': form, 'title': 'Add Support Program'})