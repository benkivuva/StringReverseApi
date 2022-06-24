from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class ReversedStringsView(APIView):
    serializer_class = StringtoReverseSerializer

    def post(self, request):
        phrase= request.data.get("phrase")
        rvs = phrase.split(' ')
        reversed_phrase = ' '.join(reversed(rvs))
        
        return Response({"Reversed": reversed_phrase})