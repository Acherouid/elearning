from rest_framework import serializers
from elearning.user.models import User
from elearning.abstract.serializers import AbstractSerializer
from django.conf import settings


class UserSerializer(AbstractSerializer):
    posts_count = serializers.SerializerMethodField()
    # id = serializers.UUIDField(source='public_id',read_only=True, format='hex')
    # created = serializers.DateTimeField(read_only=True)
    # updated = serializers.DateTimeField(read_only=True)
    
    def get_posts_count(self, instance):
        return instance.post_set.all().count()
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
        
    #     if not representation['avatar']:
    #         representation['avatar'] = settings.DEFAULT_AVATAR_URL
    #         return representation
        
    #     if settings.DEBUG :
    #         request = self.context.get('request')
    #         representation['avatar'] = request.build_absolute_uri(representation['avatar'])
            
    #     return representation
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if not representation['avatar']:
            representation['avatar'] = settings.DEFAULT_AVATAR_URL
            return representation
        
        request = self.context.get('request')
        
        if request is not None:
            representation['avatar'] = request.build_absolute_uri(representation['avatar'])
        else:
            # Handle the case where request is None
            # For example, set a default or provide an alternative behavior
            representation['avatar'] = settings.DEFAULT_AVATAR_URL
        
        return representation

    
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'first_name',
        'last_name', 'bio', 'avatar', 'email',
        'is_active', 'created', 'updated', 'posts_count']
        read_only_field = ['is_active']