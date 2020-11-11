from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os

class StationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Station
        fields =['id','name','short_description','large_description','url_name',
                 'url_base','url_player_sufix','station_type','transmission_start_time',
                 'transmission_end_time','live_stream_mp3_url','live_stream_AAC_url',
                 'use_external_stream','external_stream_url','is_HD','frequency','country','province','city',
                 'station_site','is_repeater','repated','shown_repeaters_map','group','main_image','secondary_image',
                 'station_poster','facebook_profile_image','twitter_profile_image','twitter_cover_image',
                 'Instagram_profile_image','HTML_color_code','facebook_link','instagram_link','twitter_link',
                 'facebook_invite_text','twitter_invite_text','seo_labels','seo_title','seo_meta']