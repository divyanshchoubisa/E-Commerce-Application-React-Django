from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="Divyansh",
                          email="divyansh@dc.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="9191919191",
                          gender="Male"
                          )
        user.set_password("1234567")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
