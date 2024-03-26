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


def tag_for_list(request):
    countries = ["Россия", "Австралия", "Египет", "США", "Великобритания"]
    length_countries = len(countries)
    return render(request, "tagforlist.html", context={"countries": countries, "length": length_countries})


def tag_for_dict(request):
    countries = {"Россия": "Москва", "Австралия": "Канберра", "Египет": "Каир", "США": "Вашингтон", "Великобритания": "Лондон"}
    return render(request, "tagfordict.html", context={"countries": countries})


def stat_files(request):
    return render(request, "statfiles.html")
