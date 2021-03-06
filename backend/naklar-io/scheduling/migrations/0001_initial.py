# Generated by Django 3.1.4 on 2020-12-16 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import scheduling.validators
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roulette', '0020_auto_20201028_1411_squashed_0026_auto_20201117_1643'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20201212_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(validators=[scheduling.validators.validate_start_time])),
                ('duration', models.DurationField(validators=[scheduling.validators.validate_duration])),
                ('weekly', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='uuid')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalAppointment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('start_time', models.DateTimeField(validators=[scheduling.validators.validate_start_time])),
                ('duration', models.DurationField(validators=[scheduling.validators.validate_duration])),
                ('topic', models.CharField(blank=True, max_length=255)),
                ('confirmation_request_time', models.DateTimeField(blank=True, editable=False)),
                ('status', models.TextField(choices=[('REQUESTED', 'Requested'), ('CONFIRMED', 'Confirmed'), ('OWNER_REJECTED', 'Owner Rejected'), ('INVITEE_REJECTED', 'Invitee Rejected'), ('OWNER_STARTED', 'Owner Started'), ('INVITEE_STARTED', 'Invitee Started'), ('BOTH_STARTED', 'Both Started')], default='REQUESTED')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='roulette.meeting')),
                ('owner', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, to_field='uuid')),
                ('subject', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='account.subject')),
                ('timeslot', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='scheduling.timeslot')),
            ],
            options={
                'verbose_name': 'historical appointment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(validators=[scheduling.validators.validate_start_time])),
                ('duration', models.DurationField(validators=[scheduling.validators.validate_duration])),
                ('topic', models.CharField(blank=True, max_length=255)),
                ('confirmation_request_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.TextField(choices=[('REQUESTED', 'Requested'), ('CONFIRMED', 'Confirmed'), ('OWNER_REJECTED', 'Owner Rejected'), ('INVITEE_REJECTED', 'Invitee Rejected'), ('OWNER_STARTED', 'Owner Started'), ('INVITEE_STARTED', 'Invitee Started'), ('BOTH_STARTED', 'Both Started')], default='REQUESTED')),
                ('invitee_rejects', models.ManyToManyField(blank=True, related_name='rejected_appointments', to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='roulette.meeting')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='uuid')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.subject')),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.timeslot')),
            ],
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='appointment',
            constraint=models.UniqueConstraint(condition=models.Q(models.Q(('status', 'OWNER_REJECTED'), ('status', 'INVITEE_REJECTED'), _connector='OR'), _negated=True), fields=('timeslot', 'start_time'), name='unique_appointment_timeslot_start_time'),
        ),
    ]
