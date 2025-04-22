# search/documents.py
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from board.models import Post

post_index = Index('posts')
post_index.settings(
    number_of_shards=1,
    number_of_replicas=0,
    analysis={
        'analyzer': {
            'korean': {
                'type': 'custom',
                'tokenizer': 'nori_tokenizer',
                'filter': ['lowercase']
            }
        }
    }
)

@registry.register_document
class PostDocument(Document):
    # keyword 필드만 색인
    keyword = fields.TextField(analyzer='korean')  

    class Index:
        name = 'posts'

    class Django:
        model = Post
        fields = ['keyword'] 
