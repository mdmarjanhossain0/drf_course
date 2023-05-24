from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.api.serializers import ArticleSerializer


@api_view(["POST"])
def upload_article_api_view(request):
    if request.method == "POST":
        data = request.data
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            article = serializer.save()
            data = serializer.data
            return Response(data=data)
        return Response(serializer.errors, status=400)


# Base64 Encoding:

# Base64 encoding allows you to represent binary data, such as an image, as ASCII text.
# With this approach, the image file is converted into a Base64-encoded string on the client side before sending it to the server.
# The client typically includes the Base64-encoded image data as a field in the request payload, often as a JSON object.
# On the server side, you can decode the Base64-encoded image data back into binary form and save it as a file or process it further as needed.
# In DRF, you can create a custom serializer field to handle Base64-encoded image data and decode it during deserialization.
# Here's an example of a custom serializer field for handling Base64-encoded images: