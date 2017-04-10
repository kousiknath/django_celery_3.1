from __future__ import absolute_import

import celery


@celery.task(name="sum_two_numbers")
def add(x, y):
    return x + y

@celery.task()
def kousik_test():
    pass