# Generated by Django 4.2.5 on 2023-11-08 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=255)),
                ('semestre', models.CharField(choices=[('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('S9', 'S9'), ('S10', 'S10')], default='S5', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(choices=[('Apprenti', 'Apprenti'), ('TuteurPedagogique', 'TuteurPedagogique'), ('Administrateur', 'Administrateur'), ('CoordinatriceAlternance', 'CoordinatriceAlternance'), ('MaitreAlternance', 'MaitreAlternance')], default='Apprenti', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('motDePasse', models.CharField(max_length=255)),
                ('roles', models.ManyToManyField(to='api.role')),
            ],
        ),
        migrations.CreateModel(
            name='TuteurPedagogique',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idUtilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='MaitreAlternance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idUtilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='CoordinatriceAlternance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idUtilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Apprenti',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('optionMajeure', models.CharField(max_length=255)),
                ('optionMineure', models.CharField(max_length=255)),
                ('idMaitreAlternance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.maitrealternance')),
                ('idTuteurPedagogique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tuteurpedagogique')),
                ('idUtilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Administrateur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idUtilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.utilisateur')),
            ],
        ),
    ]
