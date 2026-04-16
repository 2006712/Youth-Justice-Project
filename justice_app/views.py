from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Youth, Offence, SupportProgram
from .forms import YouthForm, OffenceForm, SupportProgramForm


# -------------------------------
# HOME VIEW
# -------------------------------
def home(request):
    # Show all youths ordered by latest
    youths = Youth.objects.all().order_by('-created_at')

    # Simple search functionality
    search_query = request.GET.get('search')
    if search_query:
        youths = youths.filter(
            Q(name__icontains=search_query) |
            Q(school_status__icontains=search_query)
        )

    context = {
        'youths': youths,
        'search_query': search_query
    }

    return render(request, 'home.html', context)


# -------------------------------
# YOUTH LIST VIEW
# -------------------------------
def youth_list(request):
    youths = Youth.objects.all().order_by('name')

    # Filter by gender
    gender = request.GET.get('gender')
    if gender:
        youths = youths.filter(gender=gender)

    return render(request, 'youth_list.html', {
        'youths': youths
    })


# -------------------------------
# OFFENCE LIST VIEW
# -------------------------------
def offence_list(request):
    offences = Offence.objects.select_related('youth').all().order_by('-date_reported')

    # Filter by severity
    severity = request.GET.get('severity')
    if severity:
        offences = offences.filter(severity=severity)

    return render(request, 'offence_list.html', {
        'offences': offences
    })


# -------------------------------
# SUPPORT PROGRAM LIST
# -------------------------------
def support_program_list(request):
    programs = SupportProgram.objects.all()

    return render(request, 'program_list.html', {
        'programs': programs
    })


# -------------------------------
# RECOMMENDATION VIEW
# -------------------------------
def recommendations(request, youth_id):
    youth = get_object_or_404(Youth, id=youth_id)

    # Core logic delegated to model (HD design)
    programs = youth.recommend_programs()

    return render(request, 'recommendations.html', {
        'youth': youth,
        'programs': programs
    })


# -------------------------------
# ADD YOUTH
# -------------------------------
def add_youth(request):
    if request.method == 'POST':
        form = YouthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('youth_list')
    else:
        form = YouthForm()

    return render(request, 'add_youth.html', {
        'form': form
    })


# -------------------------------
# ADD OFFENCE
# -------------------------------
def add_offence(request):
    if request.method == 'POST':
        form = OffenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('offence_list')
    else:
        form = OffenceForm()

    return render(request, 'add_offence.html', {
        'form': form
    })


# -------------------------------
# ADD SUPPORT PROGRAM
# -------------------------------
def add_support_program(request):
    if request.method == 'POST':
        form = SupportProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('support_program_list')
    else:
        form = SupportProgramForm()

    return render(request, 'add_program.html', {
        'form': form
    })