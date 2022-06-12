python manage.py makemigrations
python manage.py migrate
python manage.py sampledata && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell
