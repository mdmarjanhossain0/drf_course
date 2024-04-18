from django.shortcuts import render


def upload_base64_image_view(request):
    return render(request, "base64_image_upload.html", {})


def upload_image_view(request):
    return render(request, "upload_image.html", {})
