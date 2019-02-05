import os
import sys
import django

sys.path.append('.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()

from slack.utils import log_channels, listen

log_channels()
#listen()