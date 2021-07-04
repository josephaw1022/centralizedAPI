
import os
from dotenv import load_dotenv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': str(os.getenv('ENGINE')),

        'USER': str(os.getenv('USER')),

        'PASSWORD': str(os.getenv('PASSWORD')),

        'HOST': str(os.getenv('HOST')),

        'PORT': str(os.getenv('PORT'))

    }
}
