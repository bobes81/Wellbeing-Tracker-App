from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_previous_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='type',
            field=models.CharField(max_length=100, default="Cardio"),  # Updated max_length to 100
        ),
    ]