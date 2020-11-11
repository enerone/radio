from colorfield.fields import ColorField
from django.db import models
from django.utils.html import mark_safe
import uuid
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html


class Station_type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=120, verbose_name="tipo")
    
    def __str__(self):
        return self.type
    
class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, verbose_name="Nombre del grupo")
    
    def __str__(self):
        return self.name

class Station(models.Model):
    # STATION
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name="Nombre")
    short_description = models.CharField(max_length=250, verbose_name="Copete")
    large_description = models.TextField(max_length=4086, verbose_name="Descripcion")
    url_name = models.CharField(max_length=120, verbose_name="Nombre url")
    url_base = models.CharField(max_length=120, verbose_name="Base url")
    url_player_sufix = models.CharField(max_length=120, verbose_name="Sufijo url player")
    station_type = models.ManyToManyField(Station_type,blank=True, verbose_name="Tipo de estacion")
    transmission_start_time = models.TimeField(verbose_name="Hora de inicio de transmisión")
    transmission_end_time = models.TimeField(verbose_name="Hora de fin de transmisión")
    live_stream_mp3_url = models.CharField(max_length=120, verbose_name="Url de template live stream en Mp3")
    live_stream_AAC_url = models.CharField(max_length=120, verbose_name="Url de template live stream en AAC")
    use_external_stream = models.BooleanField(default=False, verbose_name="Usa stream externo?")
    external_stream_url = models.CharField(max_length=120, verbose_name="external_stream_url")
    is_HD = models.BooleanField(default=True,verbose_name='Es HD?')
    frequency = models.CharField(max_length=120,verbose_name='Frecuencia')
    country = models.CharField(max_length=50,verbose_name='País')
    province = models.CharField(max_length=50,verbose_name='Provincia')
    city = models.CharField(max_length=50,verbose_name='Localidad')
    station_site = models.CharField(max_length=50,verbose_name='Sitio al que pertenece la emisora') #cargador de sitios?
    is_repeater = models.BooleanField(default=False,verbose_name='Es repetidora?') 
    repeated = models.CharField(max_length=50,verbose_name='A quién repite?') #traigo lista de emisoras?
    shown_repeaters_map = models.BooleanField(default=False,verbose_name='Aparece en mapa de repetidoras?')
    group = models.ManyToManyField(Group,blank=True, verbose_name="Tipo de estacion")
    # IMAGENES
    main_image =  models.ImageField(upload_to="station_images", default="station_images/default.png", verbose_name='Imagen Principal')
    secondary_image = models.ImageField(upload_to="station_images", default="station_images/default.png" ,verbose_name='Imagen secundaria')
    station_poster = models.ImageField(upload_to="station_images", default="station_images/default.png" ,verbose_name='Poster de la radio')
    facebook_profile_image = models.ImageField(upload_to="station_images", default="station_images/default.png" ,verbose_name='Imagen de Perfil para Facebook')
    twitter_profile_image = models.ImageField(upload_to="station_images", default="station_images/default.png" ,verbose_name='Imagen de perfil para Twitter')
    twitter_cover_image = models.ImageField(upload_to="station_images", default="station_images/default.png" ,verbose_name='Imagen de portada para Twitter')
    Instagram_profile_image = models.ImageField(upload_to="station_images", default="station_images/default.png",verbose_name='Imagen de perfil para Instagram')
    # galeria de imagenes? es un url?
    HTML_color_code = ColorField(default='#FF0000')
    # LINKS
    facebook_link = models.CharField(max_length=120, verbose_name="Enlace a facebook")
    instagram_link = models.CharField(max_length=120, verbose_name="Enlace a instagram")
    twitter_link = models.CharField(max_length=120, verbose_name="Enlace a Twitter")
    facebook_invite_text = models.TextField(max_length=4086, verbose_name="Texto de invitación para facebook")
    twitter_invite_text = models.TextField(max_length=4086, verbose_name="Texto de invitación para twitter")
    # SEO
    seo_labels = models.CharField(max_length=256, verbose_name="Etiquetas para seo")
    seo_title = models.CharField(max_length=256, verbose_name="Titulo para seo" )
    seo_meta = models.TextField(max_length=4086, verbose_name="Metadescripción para seo")
    
    def __str__(self):
        return self.name

    @property
    def main_image_preview(self):
        if self.main_image:
            _thumbnail = get_thumbnail(self.main_image,'300x300',upscale=False,crop=False,quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

