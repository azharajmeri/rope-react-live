# Generated by Django 3.2.3 on 2021-06-27 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_uploadeddocuments_workpackage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadeddocuments',
            name='workpackage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='documents', to='main.workpackage'),
        ),
    ]