# Generated by Django 3.2.7 on 2021-09-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygovernmentjobs', '0032_admitcarddata_admit_card_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admitcarddata',
            name='admit_card_date',
            field=models.CharField(default='', max_length=30),
        ),
    ]
