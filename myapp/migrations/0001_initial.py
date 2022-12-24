# Generated by Django 2.2.2 on 2022-12-24 11:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('date_requested', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_code', models.CharField(max_length=200)),
                ('drug_name', models.CharField(max_length=500)),
                ('manufacturer', models.CharField(max_length=500)),
                ('supplied_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('supply_unit', models.CharField(max_length=300)),
                ('quantity', models.FloatField()),
                ('unit_price', models.FloatField()),
                ('date_recorded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('date_recorded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('position', models.CharField(choices=[('Nurse', 'Nurse'), ('Clinical Officer', 'Clinical Officer'), ('Public Health Officer', 'Public Health Officer'), ('Cleaner', 'Cleaner'), ('Security', 'Security'), ('Driver', 'Driver'), ('Counselor', 'Counselor'), ('Nutritionist', 'Nutritionist')], max_length=100)),
                ('employment_date', models.DateTimeField()),
                ('shift', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('supply_type', models.CharField(max_length=500)),
                ('contracted_on', models.DateTimeField()),
                ('contract_type', models.CharField(choices=[('Temporary', 'Temporary'), ('Permanent', 'Permanent')], max_length=50)),
                ('postal_code', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescribed_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('prescription_notes', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Patient')),
                ('prescribed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Staff')),
                ('prescribed_drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Drug')),
            ],
        ),
        migrations.CreateModel(
            name='PatientVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_commented', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.FloatField()),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='HealthHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='drug',
            name='supplied_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Supplier'),
        ),
    ]
