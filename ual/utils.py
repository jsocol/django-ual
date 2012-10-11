from ual.models import UserAction


def log_user_action(user, action):
    return UserAction.objects.create(user=user, action=action)
