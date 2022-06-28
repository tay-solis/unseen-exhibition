import os

from django.contrib.auth.models import User
from django.db import migrations
from django.db.backends.postgresql.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps

import google.auth
from google.cloud import secretmanager


def createsuperuser(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    """
    Dynamically create an admin user as part of a migration
    Password is pulled from Secret Manger (previously created as part of tutorial)
    """
    if os.getenv("TRAMPOLINE_CI", None):
        # We are in CI, so just create a placeholder user for unit testing.
        admin_password = "test"
    else:
        client = secretmanager.SecretManagerServiceClient()

        # Get project value for identifying current context
        _, project = google.auth.default()

        # Retrieve the previously stored admin password
        DJANGO_SUPERUSER_PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "superuser_password")
        name = f"projects/{project}/secrets/{DJANGO_SUPERUSER_PASSWORD}/versions/latest"
        admin_password = client.access_secret_version(name=name).payload.data.decode(
            "UTF-8"
        )

    # Create a new user using acquired password, stripping any accidentally stored newline characters
    User.objects.create_superuser("admin", password=admin_password.strip())


class Migration(migrations.Migration):

    initial = True
    dependencies = []
    operations = [migrations.RunPython(createsuperuser)]

