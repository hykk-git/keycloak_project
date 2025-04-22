from django.shortcuts import render
from search.documents import PostDocument

def search_posts(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = PostDocument.search().query(
            "multi_match",
            query=query,
            fields=['title', 'content']
        )

    return render(request, 'search/results.html', {'results': results, 'query': query})
