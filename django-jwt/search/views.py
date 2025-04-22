# search/views.py
from django.shortcuts import render
from search.documents import PostDocument

def search_posts(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = PostDocument.search().query(
            "match", keyword=query
        )

    return render(request, 'search/results.html', {'results': results, 'query': query})
