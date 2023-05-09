# Generated by Django 4.0.4 on 2022-05-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamverwaltung_main', '0005_skill_rename_projectquestion_projectanswer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.CharField(choices=[('ia', 'Informatik'), ('iw', 'Wirtschaftsinformatik'), ('iv', 'Verwaltungsinformatik'), ('wi', 'Wirtschaftsingenieurswesen')], default=None, max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='vorname', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='title',
            field=models.CharField(choices=[('h', 'Herr'), ('f', 'Frau')], default='h', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=1023),
        ),
        migrations.AlterField(
            model_name='project',
            name='documentfile_url',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='responsible',
            field=models.CharField(max_length=255),
        ),
    ]