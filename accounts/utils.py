def user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


def is_admin_user(user):
    return user.is_superuser or user_in_group(user, "Admin")


def is_case_worker(user):
    return user_in_group(user, "Case Worker")


def is_volunteer(user):
    return user_in_group(user, "Volunteer")