from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import News,Faq,Contact
from django.utils.translation import gettext_lazy as _

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class NewsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = News
        fields = ('title', 'author', 'date_created', 'date_modified',
                   'images',)
        read_only_fields = ('date_created', 'date_modified')
        extra_kwargs = {
            'body': {'help_text': 'body serializer help_text'},
            'author': {
                'default': serializers.CurrentUserDefault(),
                'help_text': _("The ID of the user that created this article; if none is provided, "
                               "defaults to the currently logged in user.")
            },
        }

class FaqSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Faq
        fields = ('question','answer')
        read_only_fields = ('date_created', 'date_modified')

class ContactSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Contact
        fields = ('name','surname','email','phone','subject','message')
        read_only_fields = ('date_created', 'date_modified')
