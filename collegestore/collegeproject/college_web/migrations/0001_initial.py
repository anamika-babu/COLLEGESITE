# Generated by Django 4.2.3 on 2023-07-08 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField()),
                ('PhoneNo', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Address', models.TextField()),
                ('DebitNoteBook', models.BooleanField(default=False, verbose_name='DebitNoteBook')),
                ('Pen', models.BooleanField(default=False, verbose_name='Pen')),
                ('ExamPaper', models.BooleanField(default=False, verbose_name='Exampaper')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_web.course')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_web.department')),
                ('Gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_web.gender')),
                ('Purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_web.purpose')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_web.department'),
        ),
    ]
