
import django_heroku
from split_settings.tools import include

include(
    'local_settings/*.py'
)

django_heroku.settings(locals())
