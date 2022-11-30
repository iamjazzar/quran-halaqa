from django.shortcuts import render


def my_view(request):
    context = {
        "author": "Gaurav Singhal",
        "website": {
            "domain": "https://pluralsight.com",
            "views": 200
        },
        "odds": [1, 3, 5]
    }

    return render(request, "index.html", context)


def profile_view(request):
    return render(request, "profile.html", {})


def record_view(request):
    return render(request, "record.html", {})
