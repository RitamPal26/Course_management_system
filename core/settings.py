# core/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drf_yasg',

    'vendor',
    'product',
    'course',
    'certification',

    'vendor_product_mapping',
    'product_course_mapping',
    'course_certification_mapping',
]