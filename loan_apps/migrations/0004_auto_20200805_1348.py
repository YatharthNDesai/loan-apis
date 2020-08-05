# Generated by Django 3.0.3 on 2020-08-05 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan_apps', '0003_owner_loanapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanapplication',
            name='Business',
        ),
        migrations.RemoveField(
            model_name='loanapplication',
            name='CFApplicationData',
        ),
        migrations.RemoveField(
            model_name='loanapplication',
            name='RequestHeader',
        ),
        migrations.AddField(
            model_name='business',
            name='LoanApplication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loan_apps.LoanApplication'),
        ),
        migrations.AddField(
            model_name='cfapplicationdata',
            name='LoanApplication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loan_apps.LoanApplication'),
        ),
        migrations.AddField(
            model_name='requestheader',
            name='LoanApplication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='loan_apps.LoanApplication'),
        ),
    ]