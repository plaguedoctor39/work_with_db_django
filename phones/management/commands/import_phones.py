import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                cur_phone = Phone()
                cur_phone.name = line[1]
                cur_phone.image = line[2]
                cur_phone.price = line[3]
                cur_phone.release_date = line[4]
                cur_phone.lte_exists = line[5]
                cur_phone.slug = slugify(cur_phone.name)
                cur_phone.save(cur_phone)
