from langchain.tools import tool
from .helpers import advanced_video_search
from youtube.models import Search


class FindProductVideoTools():
    @tool
    def find_product_video_id(product: str) -> str:
        """Useful when you need to find a product review video from youtube."""
        query: str = f'reviews of the latest {product}'
        search_results: list[Search] = advanced_video_search(query)
        return search_results[0].resource_id
        
        