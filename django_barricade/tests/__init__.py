# coding: utf-8
import time

from django.test import TestCase
from django.test.utils import override_settings


@override_settings(
    BARRICADE_BOUND=(3, 3)
)
class BarricadeMiddlewareTest(TestCase):
    def test_response_delayed_by_middleware(self):
        start_time = time.time()
        self.client.get('/')
        end_time = time.time()

        spent_time = end_time - start_time
        self.assertGreater(spent_time, 3)
