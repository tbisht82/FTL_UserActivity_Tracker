from django.urls import path
from core.api import views

urlpatterns = [
    # url to see all activity times for all the users
    path('all/', views.AllActivityListView.as_view(), name='all_activities'),

    # url to see all activity times for a specific user by using user_id
    path('all/<user_id>', views.UserActivityDetailedView.as_view(), name='user_activity')
]
