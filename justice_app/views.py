from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from .models import Youth
from accounts.decorators import volunteer_or_above_required, case_worker_required


@login_required
@permission_required("justice_app.view_youth", raise_exception=True)
@volunteer_or_above_required
def home(request):
    """
    Display all registered youths on the home page.
    Only authenticated users with view_youth permission can access this page.
    """
    youths = Youth.objects.all().order_by("-id")

    context = {
        "youths": youths
    }

    return render(request, "home.html", context)


@login_required
@permission_required("justice_app.view_youth", raise_exception=True)
@permission_required("justice_app.view_supportprogram", raise_exception=True)
@case_worker_required
def recommendations(request, youth_id):
    """
    Show recommended support programs for a selected youth.
    Only Admin and Case Worker users can access recommendations.
    """
    youth = get_object_or_404(Youth, id=youth_id)

    # Use "offences" because your Offence model uses related_name="offences"
    latest_offence = youth.offences.order_by("-date_reported").first()

    # Use recommend_programs() because this is the method in your current Youth model
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
        "youth": youth,
        "programs": programs,
        "reasons": reasons,
        "latest_offence": latest_offence,
    }

    return render(request, "recommendations.html", context)