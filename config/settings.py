
import django_heroku
from split_settings.tools import include

include(
    'components/*.py'
)

django_heroku.settings(locals())

