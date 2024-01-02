from typing import Optional
from youtube.schemas import (
    SearchPart, SearchOptionalParameters, YouTubeResponse, YouTubeRequest
)
from youtube.schemas import (
    CommentThreadFilter, CommentThreadOptionalParameters, CommentThreadPart
)
from youtube.models import Search, Comment
from .extensions import youtube_client
from collections.abc import Iterator


def advanced_video_search( 
    query: str,
    channel_id: Optional[str] = None,
    max_results: Optional[int] = 10,
    order: Optional[str] = None,
    published_after: Optional[str] = None,
    published_before: Optional[str] = None,
    region_code: Optional[str] = None,
    relevance_language: Optional[str] = 'en',
    video_caption: Optional[str] = None,
    video_category_id: Optional[str] = None,
    video_definition: Optional[str] = None,
    video_dimension: Optional[str] = None,
    video_duration: Optional[str] = None,
    video_paid_product_placement: Optional[str] = None,
    video_syndicated: Optional[str] = None,
    video_type: Optional[str] = 'any'
    ) -> list[Search]:
    """Search the given channel for the given videos."""
    search_part: SearchPart = SearchPart()
    optional_params: SearchOptionalParameters = SearchOptionalParameters(
        channelId=channel_id,
        q=query,
        maxResults=max_results,
        order=order,
        publishedAfter=published_after,
        publishedBefore=published_before,
        regionCode=region_code,
        relevanceLanguage=relevance_language,
        type=['video'],
        videoCaption=video_caption,
        videoCategoryId=video_category_id,
        videoDefinition=video_definition,
        videoDimension=video_dimension,
        videoDuration=video_duration,
        videoPaidProductPlacement=video_paid_product_placement,
        videoSyndicated=video_syndicated,
        videoType=video_type
    )
    search_schema: YouTubeRequest = YouTubeRequest(
        part=search_part, optional_parameters=optional_params
    )
    response: YouTubeResponse = youtube_client.search(search_schema)
    items: list[Search] = response.items
    return items


def list_video_comments(video_id: str) -> list[Comment]:
    """List a given videos comments"""
    part: CommentThreadPart = CommentThreadPart()
    filter: CommentThreadFilter = CommentThreadFilter(
        videoId=video_id
    )
    optional: CommentThreadOptionalParameters = CommentThreadOptionalParameters(
        maxResults=30
    )
    request:YouTubeRequest = YouTubeRequest(
        part=part,
        filter=filter,
        optional_parameters=optional
    )
    comment_iterator: Iterator = youtube_client.get_comments_iterator(request)
    video_comments: list[Comment] = list()
    done: bool = False
    comment_count: int = 0
    for comment_threads in comment_iterator:
        if done:
            break
        for comment_thread in comment_threads:
            comment: Comment = comment_thread.snippet.top_level_comment
            video_comments.append(comment)
            comment_count += 1
            if comment_count > 30:
                done = True
                break
    return video_comments