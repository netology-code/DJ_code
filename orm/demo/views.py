import random

from django.http import HttpResponse

from demo.models import Car, Person


def create_car(request):
    car = Car(
        brand=random.choice(['B1', 'B2', 'B3']),
        model=random.choice(['M1', 'M2', 'M3']),
        color=random.choice(['C1', 'C2', 'C3']),
    )
    car.save()
    return HttpResponse(f'Все получилось! Новая машина: {car.brand}, {car.model}')


def list_car(request):
    car_objects = Car.objects.all()
    cars = [f'{c.id}: {c.brand}, {c.model}: {c.color} | {c.owners.count()}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))


def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        Person.objects.create(name='P', car=car)
    return HttpResponse('Все получилось!')


def list_person(request):
    person_objects = Person.objects.all()
    people = [f'{p.name}: {p.car}' for p in person_objects]
    return HttpResponse('<br>'.join(people))
