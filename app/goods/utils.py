from . models import Product
from django.db.models import Q


def q_search(query: str):
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))
    
    keyword = [word for word in query.split() if len(word) > 2]
    q_objects = Q()
    
    for token in keyword:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Product.objects.filter(q_objects)