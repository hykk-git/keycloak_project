from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from board.models import Post

# posts 인덱스 테이블에 저장
post_index = Index('posts')

post_index.settings(
    number_of_shards=1,
    number_of_replicas=0,
    analysis={
        'analyzer': {
            'korean': {
                'type': 'custom',
                'tokenizer': 'nori_tokenizer',
                "filter": [
                    "lowercase",
                    "nori_readingform",
                    "nori_part_of_speech"
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