from rest_framework import status
from rest_framework.response  import Response
from rest_framework.views import APIView
from .models import Mymodel
from .serializers import Myserializer


# Create your views here.
class Myview(APIView):
 def get_object(self, id):
        try:
            return Mymodel.objects.get(id=id)
        except Mymodel.DoesNotExist:
            raise HTTP404
        
 def post(self,request):
        serializer=Myserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

 def put(self,request,id):
        instance=self.get_object(id)
        serializer=Myserializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

 def delete(self,request,id):
        instance=self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


