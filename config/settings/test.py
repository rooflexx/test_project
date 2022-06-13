"""
With these settings, tests run faster.
"""

from .base import *  # noqa

# GENERAL
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    default="!!!SET DJANGO_SECRET_KEY!!!",
)
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

