from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class UserAction(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(default=datetime.now, db_index=True)
    action = models.CharField(max_length=255, db_index=True)
