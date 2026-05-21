from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from .models import Youth
from .services import get_all_youth_records, generate_support_recommendations
from accounts.decorators import volunteer_or_above_required, case_worker_required


@login_required
@permission_required("justice_app.view_youth", raise_exception=True)
@volunteer_or_above_required
def home(request):
    """
    Display all registered youths on the home page.
    Only authenticated users with view_youth permission can access this page.
    """
    youths = get_all_youth_records()

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

    recommendation_data = generate_support_recommendations(youth)

    context = {
        "youth": youth,
        "programs": recommendation_data["programs"],
        "reasons": recommendation_data["reasons"],
        "latest_offence": recommendation_data["latest_offence"],
    }

    return render(request, "recommendations.html", context)