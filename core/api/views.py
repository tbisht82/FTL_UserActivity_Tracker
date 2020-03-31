from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from core.models import User


class AllActivityListView(ListAPIView):
    """
    This List View will provide a response of ok and members,
    ok --> true if there is any record in members else false,
    members --> user list with their activity times
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        res = super(AllActivityListView, self).list(request, *args, **kwargs)
        if len(res.data) > 0:
            check = True
        else:
            check = False
        res.data = {"ok": check, "members": res.data}
        return res


class UserActivityDetailedView(RetrieveAPIView):
    """
    This Retrieve View will provide a response with a specific user and its activity times.
    """
    lookup_field = 'user_id'
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
