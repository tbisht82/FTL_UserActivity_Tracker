# User Activity Tracker

Django rest framework project to get the activity time of users.

# Setup Steps:
1. clone the repository
1. Create a virtual environment
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py populate_db --users 6
5. python manage.py runserver

# Custom management command:
"python manage.py populate_db --users 6" or "python manage.py populate_db" is a custom command to generate dummy users and their activity start time and end time.
This command will insert dynamically generated data into User and ActivityPeriods table in database.

# API endpoints:
1. http://127.0.0.1:8000/api/activity/all/
This endpoint will provide the list of all the users and their activity timings
2. http://127.0.0.1:8000/api/activity/all/<user_id>
This endpoint will provide the activity timings and user data for a specific user

format of API response for end point:
{
    "ok": true/flase, -->>> ok will be true if there is members otherwise false
    "members": [
        {
            "id": "",
            "real_name": "",
            "tz": "",
            "activity_periods": [
                {
                    "start_time": "",
                    "end_time": ""
                },
                {
                    "start_time": "",
                    "end_time": ""
                }
            ]
        },
        {
            "id": "",
            "real_name": "",
            "tz": "",
            "activity_periods": [
                {
                    "start_time": "",
                    "end_time": ""
                },
                {
                    "start_time": "",
                    "end_time": ""
                }
            ]
        }
   ]
}
