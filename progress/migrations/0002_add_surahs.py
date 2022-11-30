# Generated by Django 4.1.3 on 2022-11-29 23:52
import json

from django.conf import settings
from django.db import migrations


def add_surahs(apps, schema_editor):
    """
    Will add the name of the juz to Juz model.
    """
    Surah = apps.get_model("progress", "Surah")

    with open(settings.BASE_DIR / "preflight" / "surahs.json", "r") as f:
        surahs = json.load(f)

    for number, data in surahs.items():
        Surah.objects.create(
            number=int(number),
            ayas=data['count'],
            name_en=data['name_en'],
            name_ar=data['name_ar'],
        )


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_surahs),
    ]