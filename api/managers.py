from django.db import models


class HouseQuerySet(models.QuerySet):
    def get_house_by_location(self, post_code):
        return self.filter(post_code__contains=post_code)

    def get_house_between_end_beginning_date(self, beginning_date, end_date):
        return self.filter(transaction_date__range=(beginning_date, end_date))


class HouseManager(models.Manager):
    def get_queryset(self):
        return HouseQuerySet(self.model, using=self._db)

    def get_house_by_location(self, post_code):
        return self.get_queryset().get_house_by_location(post_code)

    def get_house_between_end_beginning_date(self, beginning_date, end_date):
        return self.get_queryset().get_house_between_end_beginning_date(beginning_date, end_date)
