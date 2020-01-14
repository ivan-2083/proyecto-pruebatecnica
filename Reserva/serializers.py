from rest_framework import serializers
from .models import nub_arrendar,ref_comuna,ref_region,mae_sala

class Arrendarserialaizer(serializers.ModelSerializer):

    class Meta:
        model = nub_arrendar
        fields = ('nrr_id_sala','nrr_id_comuna', 'nrr_id_region', 'nrr_fecha', 'nrr_hora')


class Salaserialaizer(serializers.ModelSerializer):
 
    
    class Meta:
        model = mae_sala
        fields = ('msl_nombre','msl_numero')

class Comunaserialaizer(serializers.ModelSerializer):

    class Meta:
        model = ref_comuna
        fields = (' rcm_nombre')
        
class Regionserialaizer(serializers.ModelSerializer):

    class Meta:
        model = nub_arrendar
        fields = ('rrg_ordinal','rrg_id')