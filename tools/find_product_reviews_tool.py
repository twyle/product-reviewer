from langchain.tools import tool
from .helpers import list_video_comments
from youtube.models import Comment


class FindProductReviewTools():
    @tool
    def find_product_reviews(video_id: str) -> str:
        """Useful when you need to find a product reviews from youtube video comments."""
        comments: list[Comment] = list_video_comments(video_id)
        comments: list[str] = [comment.snippet.text_display for comment in comments]
        return ' '.join(comments)