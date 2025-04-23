from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from board.models import Post

# posts 인덱스 테이블에 저장
post_index = Index('posts')

post_index.settings(
    number_of_shards=1,
    number_of_replicas=0,
    analysis={
        'tokenizer': {
            'nori_custom_tokenizer': {
                'type': 'nori_tokenizer',
                'decompound_mode': 'mixed' 
            }
        },
        'analyzer': {
            'korean': {  
                'type': 'custom',
                'tokenizer': 'nori_custom_tokenizer',
                'filter': [
                    'lowercase',
                ]
            }
        }
    }
)

@registry.register_document
class PostDocument(Document):
    # keyword 필드만 색인
    keyword = fields.TextField(
        analyzer="korean",
        fields={
            "raw": fields.KeywordField()
        }
    )  

    class Index:
        name = 'posts'
        settings = post_index._settings

    class Django:
        model = Post
        fields = ['id']