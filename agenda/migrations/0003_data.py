from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_usuario'),
    ]

    planos = [
        ('UNIMED', 'Unimed'),
        ('BRADESCO', 'Bradesco'),
        ('VIDALEVE', 'VidaLeve'),
        ('PARTICULAR', 'Particular')
    ]
    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('plano', models.CharField(max_length=7, choices=planos)),
                ('medico', models.CharField(max_length=100)),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agenda.usuario')),
            ],
        ),
    ]
