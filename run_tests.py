#!/usr/bin/env python
# coding: utf-8

import sys

from django.conf import settings


def main():
    settings.configure(
        INSTALLED_APPS=(
            'django_barricade',
        ),
        MIDDLEWARE_CLASSES = (
            'django_barricade.middleware.BarricadeMiddleware',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        ROOT_URLCONF='django_barricade.tests.urls',
        DEBUG=True,
    )

    from django.test.utils import get_runner

    test_runner = get_runner(settings)(verbosity=2, interactive=True)
    failures = test_runner.run_tests(['django_barricade'])
    sys.exit(failures)


if __name__ == '__main__':
    main()
