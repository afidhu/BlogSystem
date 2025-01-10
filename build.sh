set -o errexist

pip install -r requirements.txt

python manage.py collectstatic --np-input

python manage.py migrate