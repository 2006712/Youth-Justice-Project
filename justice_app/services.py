from .models import Youth


def get_all_youth_records():
    """
    Return all youth records ordered by newest first.
    This keeps database query logic outside the view.
    """
    return Youth.objects.all().order_by("-id")


def generate_support_recommendations(youth):
    """
    Generate support program recommendations for a selected youth.

    This service handles:
    - latest offence lookup
    - support program recommendation logic
    - explanation reason generation
    - school status and family support checks
    """
    latest_offence = youth.offences.order_by("-date_reported").first()

    programs = youth.recommend_programs()

    reasons = []

    if latest_offence:
        reasons.append(f"Latest offence severity: {latest_offence.severity}")
        reasons.append(f"Latest offence type: {latest_offence.offence_type}")

    if youth.family_support_level == "Low":
        reasons.append(
            "Low family support indicates need for extra guidance and mentoring."
        )

    elif youth.family_support_level == "Medium":
        reasons.append(
            "Moderate family support suggests benefit from structured intervention."
        )

    if youth.school_status == "Dropped Out":
        reasons.append(
            "Youth is currently out of school, so education-focused support is relevant."
        )

    elif youth.school_status == "Attending":
        reasons.append(
            "Youth is still connected to school, which supports rehabilitation through structured programs."
        )

    if not latest_offence:
        reasons.append(
            "No offence history found, so no specific recommendation could be generated."
        )

    if not programs:
        reasons.append(
            "No exact program match was found based on the current rules."
        )

    return {
        "programs": programs,
        "reasons": reasons,
        "latest_offence": latest_offence,
    }