from django.shortcuts import render


def upload_image_view(request):
    return render(request, "upload_image.html", {})
