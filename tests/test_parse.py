from types import SimpleNamespace
from typing import List, Dict

from conftest import (
    RAW_COMMENTS,
    RAW_POST,
    RAW_POSTS,
    RAW_SUBREDDIT,
    RAW_USER,
    RAW_SUBREDDITS,
    RAW_USERS,
    RAW_WIKI_PAGE,
)
from karmakaze.parse import Parse
from karmakaze.sanitise import Sanitise


def test_comments_parsing():
    sanitised_comments = Sanitise.comments(RAW_COMMENTS)
    parsed_comments = Parse().comments(sanitised_comments)
    assert isinstance(parsed_comments, List)

    for comment in parsed_comments:
        assert isinstance(comment, SimpleNamespace)
        assert isinstance(comment.subreddit, str)
        assert isinstance(comment.replies, (Dict, str))
        assert hasattr(comment, "upvotes")


def test_post_parsing():
    sanitised_post = Sanitise.post(RAW_POST)
    parsed_post = Parse().post(sanitised_post)
    assert isinstance(parsed_post, SimpleNamespace)
    assert isinstance(parsed_post.upvotes, int)
    assert isinstance(parsed_post.upvote_ratio, (float, int))
    assert isinstance(parsed_post.is_robot_indexable, bool)


def test_posts_parsing():
    sanitised_posts = Sanitise.posts(RAW_POSTS)
    parsed_posts = Parse().posts(sanitised_posts)
    assert isinstance(parsed_posts, List)
    for post in parsed_posts:
        assert isinstance(post, SimpleNamespace)
        assert isinstance(post.comments, int)
        assert hasattr(post, "url")


def test_subreddit_parsing():
    sanitised_subreddit = Sanitise.subreddit_or_user(RAW_SUBREDDIT)
    parsed_subreddit = Parse().subreddit(sanitised_subreddit)
    assert isinstance(parsed_subreddit, SimpleNamespace)
    assert isinstance(parsed_subreddit.current_active_users, int)
    assert hasattr(parsed_subreddit, "display_name")


def test_subreddits_parsing():
    sanitised_subreddits = Sanitise.subreddits_or_users(RAW_SUBREDDITS)
    parsed_subreddits = Parse().subreddits(sanitised_subreddits)
    assert isinstance(parsed_subreddits, List)
    for subreddit in parsed_subreddits:
        assert isinstance(subreddit, SimpleNamespace)
        assert isinstance(subreddit.subscribers, int)
        assert hasattr(subreddit, "description")


def test_user_parsing():
    sanitised_user = Sanitise.subreddit_or_user(RAW_USER)
    parsed_user = Parse().user(sanitised_user)
    assert isinstance(parsed_user, SimpleNamespace)
    assert isinstance(parsed_user.created, str)
    assert hasattr(parsed_user, "comment_karma")


def test_users_parsing():
    sanitised_users = Sanitise.subreddits_or_users(RAW_USERS)
    parsed_users = Parse().users(sanitised_users)
    assert isinstance(parsed_users, List)
    for user in parsed_users:
        assert isinstance(user, SimpleNamespace)
        assert isinstance(user.accepts_followers, bool)
        assert hasattr(user, "name")


def test_wiki_page_parsing():
    sanitised_wiki_page = Sanitise.wiki_page(RAW_WIKI_PAGE)
    parsed_wiki_page = Parse().wiki_page(sanitised_wiki_page)
    assert isinstance(parsed_wiki_page, SimpleNamespace)
    assert isinstance(parsed_wiki_page.revision_date, str)
    assert hasattr(parsed_wiki_page, "revision_id")
