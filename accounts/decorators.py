from django.contrib.auth.decorators import user_passes_test


def admin_required(view_func):
    return user_passes_test(
        lambda user: user.is_authenticated and (
            user.is_superuser or user.groups.filter(name="Admin").exists()
        )
    )(view_func)


def case_worker_required(view_func):
    return user_passes_test(
        lambda user: user.is_authenticated and (
            user.is_superuser
            or user.groups.filter(name="Admin").exists()
            or user.groups.filter(name="Case Worker").exists()
        )
    )(view_func)


def volunteer_or_above_required(view_func):
    return user_passes_test(
        lambda user: user.is_authenticated and (
            user.is_superuser
            or user.groups.filter(name="Admin").exists()
            or user.groups.filter(name="Case Worker").exists()
            or user.groups.filter(name="Volunteer").exists()
        )
    )(view_func)