from app.core.qdrant import qdrant_client
from qdrant_client.http.exceptions import UnexpectedResponse
from qdrant_client.models import(
    VectorParams,
    Distance
)

try:
    qdrant_client.create_collection(
        collection_name="user_facts",
        vectors_config=VectorParams(
            size=768,
            distance=Distance.COSINE
        )
    )
    print("Collections Created Sucessfully")
except UnexpectedResponse:
    print("Collection already exists")