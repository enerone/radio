# Generated by Django 3.1.3 on 2020-11-09 19:33

import colorfield.fields
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=120, verbose_name='tipo')),
            ],
        ),
        migrations.RemoveField(
            model_name='station',
            name='grupo',
        ),
        migrations.AddField(
            model_name='station',
            name='group',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Grupo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='station',
            name='HTML_color_code',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
        migrations.AlterField(
            model_name='station',
            name='Instagram_profile_image',
            field=models.ImageField(default='station_images/default.png', upload_to='station_images', verbose_name='Imagen de perfil para Instagram'),
        ),
        migrations.AlterField(
            model_name='station',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Localidad'),
        ),
        migrations.AlterField(
            model_name='station',
            name='country',
            field=models.CharField(max_length=50, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='station',
            name='facebook_invite_text',
            field=models.TextField(max_length=4086, verbose_name='Texto de invitación para facebook'),
        ),
        migrations.AlterField(
            model_name='station',
            name='facebook_link',
            field=models.CharField(max_length=120, verbose_name='Enlace a facebook'),
        ),
        migrations.AlterField(
            model_name='station',
            name='facebook_profile_image',
            field=models.ImageField(default='station_images/default.png', upload_to='station_images', verbose_name='Imagen de Perfil para Facebook'),
        ),
        migrations.AlterField(
            model_name='station',
            name='frequency',
            field=models.CharField(max_length=120, verbose_name='Frecuencia'),
        ),
        migrations.AlterField(
            model_name='station',
            name='instagram_link',
            field=models.CharField(max_length=120, verbose_name='Enlace a instagram'),
        ),
        migrations.AlterField(
            model_name='station',
            name='is_HD',
            field=models.BooleanField(default=True, verbose_name='Es HD?'),
        ),
        migrations.AlterField(
            model_name='station',
            name='is_repeater',
            field=models.BooleanField(default=False, verbose_name='Es repetidora?'),
        ),
        migrations.AlterField(
            model_name='station',
            name='live_stream_AAC_url',
            field=models.CharField(max_length=120, verbose_name='Url de template live stream en AAC'),
        ),
        migrations.AlterField(
            model_name='station',
            name='live_stream_mp3_url',
            field=models.CharField(max_length=120, verbose_name='Url de template live stream en Mp3'),
        ),
        migrations.AlterField(
            model_name='station',
            name='main_image',
            field=models.ImageField(default='station_images/default.png', upload_to='station_images', verbose_name='Imagen Principal'),
        ),
        migrations.AlterField(
            model_name='station',
            name='province',
            field=models.CharField(max_length=50, verbose_name='Provincia'),
        ),
        migrations.AlterField(
            model_name='station',
            name='repeated',
            field=models.CharField(max_length=50, verbose_name='A quién repite?'),
        ),
        migrations.AlterField(
            model_name='station',
            name='secondary_image',
            field=models.ImageField(default='station_images/default.png', upload_to='station_images', verbose_name='Imagen secundaria'),
        ),
        migrations.AlterField(
            model_name='station',
            name='seo_labels',
            field=models.CharField(max_length=256, verbose_name='Etiquetas para seo'),
        ),
        migrations.AlterField(
            model_name='station',
            name='seo_meta',
            field=models.TextField(max_length=4086, verbose_name='Metadescripción para seo'),
        ),
        migrations.AlterField(
            model_name='station',
            name='seo_title',
            field=models.CharField(max_length=256, verbose_name='Titulo para seo'),
        ),
        migrations.AlterField(
            model_name='station',
            name='shown_repeaters_map',
            field=models.BooleanField(default=False, verbose_name='Aparece en mapa de repetidoras?'),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_poster',
            field=models.ImageField(default='station_images/default.png', upload_to='station_images', verbose_name='Poster de la radio'),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_site',
            field=models.CharField(max_length=50, verbose_name='Sitio al que pertenece la emisora'),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_type',
            field=models.CharField(max_length=120, verbose_name='Tipo de estacion'),
        ),
        migrations.AlterField(
            model_name='station',
            name='transmission_end_time',
            field=models.TimeField(verbose_name='Hora de fin de transmisión'),
        ),
        migrations.AlterField(
            model_name='station',
            name='transmission_start_time',
            field=models.TimeField(verbose_name='Hora de inicio de transmisión'),
        ),
        migrations.AlterField(
            model_name='station',
            name='twitter_cover_image',
            field=models.ImageField(default='station_images/default.png', upload_to='station_images', verbose_name='Imagen de portada para Twitter'),
        ),
        migrations.AlterField(
            model_name='station',
            name='twitter_invite_text',
            field=models.TextField(max_length=4086, verbose_name='Texto de invitación para twitter'),
        ),
        migrations.AlterField(
            model_name='station',
            name='twitter_link',
            field=models.CharField(max_length=120, verbose_name='Enlace a Twitter'),
        ),
        migrations.AlterField(
            model_name='station',
            name='twitter_profile_image',
            field=models.ImageField(default='station_images/default.png', upload_to='station_images', verbose_name='Imagen de perfil para Twitter'),
        ),
        migrations.AlterField(
            model_name='station',
            name='url_base',
            field=models.CharField(max_length=120, verbose_name='Base url'),
        ),
        migrations.AlterField(
            model_name='station',
            name='url_name',
            field=models.CharField(max_length=120, verbose_name='Nombre url'),
        ),
        migrations.AlterField(
            model_name='station',
            name='url_player_sufix',
            field=models.CharField(max_length=120, verbose_name='Sufijo url player'),
        ),
        migrations.AlterField(
            model_name='station',
            name='use_external_stream',
            field=models.BooleanField(default=False, verbose_name='Usa stream externo?'),
        ),
    ]