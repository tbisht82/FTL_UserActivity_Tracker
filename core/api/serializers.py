from rest_framework import serializers
from rest_framework.fields import Field

from core.models import User, ActivityPeriod


class TimezoneField(Field):
    """Take the timezone object and make it JSON serializable"""

    def to_representation(self, obj):
        return obj.zone

    def to_internal_value(self, data):
        return data


class ActivityPeriodSerializer(serializers.ModelSerializer):
    """
    Model Serializer for Activity Period model
    """
    def to_representation(self, instance):
        """
        Converting Timezone.now() format to desired format (Mmm dd yyyy hh:mmAM/PM)
        """
        representation = super(ActivityPeriodSerializer, self).to_representation(instance)
        representation['start_time'] = instance.start_time.strftime("%b %d %Y %I:%M%p")
        representation['end_time'] = instance.end_time.strftime("%b %d %Y %I:%M%p")
        return representation

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserSerializer(serializers.ModelSerializer):
    """
    Model Serializer for User model and using ActivityPeriodSerializer to get activity times for each user
    """
    id = serializers.CharField(source='user_id')
    real_name = serializers.CharField(source='name')
    tz = TimezoneField(source='timezone')
    activity_periods = ActivityPeriodSerializer(source='user', many=True)

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')
