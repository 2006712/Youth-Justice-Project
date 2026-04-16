from django.shortcuts import render, get_object_or_404
from .models import Youth


def home(request):
    """
    Display all registered youths on the home page.
    Ordered by newest first.
    """
    youths = Youth.objects.all().order_by('-created_at')

    context = {
        'youths': youths
    }

    return render(request, 'home.html', context)


def recommendations(request, youth_id):
    """
    Show recommended support programs for a selected youth.
    Also explain why these recommendations were generated.
    """
    youth = get_object_or_404(Youth, id=youth_id)

    # Get latest offence for decision logic
    latest_offence = youth.offences.order_by('-date_reported').first()

    programs = youth.recommend_programs()
    reasons = []

    if latest_offence:
        reasons.append(f"Latest offence severity: {latest_offence.severity}")
        reasons.append(f"Latest offence type: {latest_offence.offence_type}")

    if youth.family_support_level == "Low":
        reasons.append("Low family support indicates need for extra guidance and mentoring.")

    elif youth.family_support_level == "Medium":
        reasons.append("Moderate family support suggests benefit from structured intervention.")

    if youth.school_status == "Dropped Out":
        reasons.append("Youth is currently out of school, so education-focused support is relevant.")

    elif youth.school_status == "Attending":
        reasons.append("Youth is still connected to school, which supports rehabilitation through structured programs.")

    if not latest_offence:
        reasons.append("No offence history found, so no specific recommendation could be generated.")

    if not programs:
        reasons.append("No exact program match was found based on the current rules.")

    context = {
        'youth': youth,
        'programs': programs,
        'reasons': reasons,
        'latest_offence': latest_offence,
    }

    return render(request, 'recommendations.html', context)