from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def family(request,id):
    with open('Animal.json','r') as f:
        data = json.load(f)
        animals_list = []
        animals_in_family = []
        for ani in data['animals']:
            animals_list.append(ani)
        for anim in animals_list:
            if anim['family'] == int(id):
                animals_in_family.append(anim)
    return HttpResponse(animals_in_family)

def animal(request,id):
    with open('Animal.json', 'r') as f:
        data = json.load(f)
        animals_list = []
        for ani in data['animals']:
            animals_list.append(ani)
        for anim in animals_list:
            if anim['id'] == int(id):
                return HttpResponse(anim.items())
    return HttpResponse("Not found")


def people(request):
    with open('People.json','r') as f:
        data = json.load(f)
        peoples_list = []
        for people in data['people']:
            peoples_list.append(people)
        sorted(peoples_list, key=lambda i: i['age'])
    return HttpResponse(peoples_list)


def people_id(request,id):
    with open('People.json', 'r') as f:
        data = json.load(f)
        peoples_list = []
        for people in data['people']:
            peoples_list.append(people)
        for people in peoples_list:
            if people['id'] == int(id):
                return HttpResponse(people.items())
    return HttpResponse('not found')