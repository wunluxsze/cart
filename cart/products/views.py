from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializers import CartSerializer
from rest_framework.views import APIView


class CartView(APIView):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            queryset = Cart.objects.all()
            serializer = CartSerializer(queryset, many=True)
        else:
            queryset = Cart.objects.get(id=pk)
            serializer = CartSerializer(queryset)
        if not pk:
            return Response({"Cart": serializer.data})
        else:
            return Response({"Cart": serializer.data})

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"Product": serializer.data})

    def put(self, request, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "status PUT is not allowed"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = Cart.objects.get(id=pk)
        except Cart.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"product": serializer.data})

    def delete(self, request, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "status PUT is not allowed"})

        try:
            instance = Cart.objects.get(id=pk)
        except Cart.DoesNotExist:
            return Response({"error": "Object does not exist"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()

        return Response({"product": instance.id})
