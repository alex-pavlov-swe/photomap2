from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

# Create your views here.

from .models import Photo


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def photo_detail_view(request, photo_id, *args, **kwargs):
    """
    REST API VIEW
    return json data to be consumed by Javascript/Swift/Java/iOS/Android
    """
    data = {
        "id": photo_id
    }
    status = 200
    try:
        obj = Photo.objects.get(id=photo_id)
        data['title'] = obj.title
    except:
        data['message'] = "Not found"
        status = 404

    return JsonResponse(data, status=status)
    # return HttpResponse(f"<h1>Hello {photo_id} - {obj.content} </h1>")
