
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',



        'USER': 'ftsteavhddpkdm',

        'PASSWORD': 'ee12a3bfd61946cf1625cd69af9f24be1840896faae4ebe235ab589d9031ed1c',

        'HOST': 'ec2-34-202-54-225.compute-1.amazonaws.com',

        'PORT': '5432',

    }
}
