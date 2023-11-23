from rest_framework import generics, status
from .models import Quote
from .serializers import QuoteSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.http import Http404

class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

# class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Quote.objects.all()
#     serializer_class = QuoteSerializer
class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Http404:
            return Response({
  "error": {
    "code": 404,
    "message": "Not Found",
    "details": "The requested resource was not found."
  }
}, status=status.HTTP_404_NOT_FOUND)




from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_quotes(request):
    members = Quote.objects.all()
    serialized_members = QuoteSerializer(members, many=True).data
    data = {'Quotes': [serialized_members]}
    return Response(data)

import random

import random
from django.http import JsonResponse

def random_quote_json(request):
    quote_count = Quote.objects.count()
    random_index = random.randint(0, quote_count - 1)
    random_quote = Quote.objects.all()[random_index]

    data = {
        "quote": random_quote.quote,
        "author": random_quote.author
    }
    data_1 = {'Quotes': [data]}
    return JsonResponse(data_1)

def contribute(request):
    quote = request.POST.get("quote")
    if quote:
        movie_title  = request.POST.get("movie_title",'Null')        
        actor_name   = request.POST.get("actor_name",'Null')        
        category     = request.POST.get("category",'Null')        
        publish_date = request.POST.get("publish_date",'Null')            
        source       = request.POST.get("source",'Null')    
        context      = request.POST.get("context",'Null')    
        rating       = request.POST.get("rating",'Null')    
        language     = request.POST.get("language",'Null')        
        author       = request.POST.get("author",'Null')    
        author_bio   = request.POST.get("author_bio",'Null')        
        adding = Quote(quote=quote,movie_title = movie_title , actor_name = actor_name , 
                    category=category,publish_date = publish_date , source=source
                    ,context=context,rating=rating,language=language,
                    author=author,author_bio=author_bio)
        adding.save()
    
    return render(request,"contribute.html")


def index(request):
    return render(request,'index.html')


from datetime import datetime
from django.db.models import Max

def latest_quote(request):
    newest_quote = Quote.objects.filter(publish_date__isnull=False).exclude(publish_date__exact='').order_by('-publish_date').first()

    if newest_quote:
        newest_quote_data = {
            'quote': newest_quote.quote,
            'publish_date': newest_quote.publish_date,
            # Include other fields you need here
        }
        return JsonResponse({'NewestQuote': newest_quote_data})
    else:
        return JsonResponse({'NewestQuote': 'No quotes found'})
