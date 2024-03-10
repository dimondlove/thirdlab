from django.shortcuts import render


def index(request):
    header = "Данные пользователя"
    langs = ["Python", "Java", "C#"]
    user = {"name": "Tom", "age": 23}
    address = ("Абрикосовая", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": address}
    return render(request, "index.html", context=data)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
