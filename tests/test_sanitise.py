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
from karmakaze.sanitise import Sanitise

sanitise = Sanitise


def test_comments_sanitisation():
    sanitised_comments = sanitise.comments(RAW_COMMENTS)
    assert isinstance(sanitised_comments, List)

    for comment in sanitised_comments:
        assert isinstance(comment, Dict)
        assert "link_id" in comment


def test_post_sanitisation():
    sanitised_post = sanitise.post(RAW_POST)
    assert isinstance(sanitised_post, Dict)
    assert isinstance(sanitised_post.get("ups"), int)


def test_posts_sanitisation():
    sanitised_posts = sanitise.posts(RAW_POSTS)
    assert isinstance(sanitised_posts, List)
    for post in sanitised_posts:
        assert isinstance(post, Dict)
        assert "title" or "selftext" in post


def test_subreddit_sanitisation():
    sanitised_subreddit = sanitise.subreddit_or_user(RAW_SUBREDDIT)
    assert isinstance(sanitised_subreddit, Dict)
    assert isinstance(sanitised_subreddit.get("accounts_active"), int)
    assert "display_name" in sanitised_subreddit


def test_subreddits_sanitisation():
    sanitised_subreddits = sanitise.subreddits_or_users(RAW_SUBREDDITS)
    assert isinstance(sanitised_subreddits, List)
    for subreddit in sanitised_subreddits:
        assert isinstance(subreddit, Dict)
        assert isinstance(subreddit.get("subscribers"), int)
        assert "display_name" in subreddit


def test_user_sanitisation():
    sanitised_user = sanitise.subreddit_or_user(RAW_USER)
    assert isinstance(sanitised_user, Dict)
    assert isinstance(sanitised_user.get("created"), (float, int))
    assert "comment_karma" in sanitised_user


def test_users_sanitisation():
    sanitised_users = sanitise.subreddits_or_users(RAW_USERS)
    assert isinstance(sanitised_users, List)
    for user in sanitised_users:
        assert isinstance(user, Dict)
        assert isinstance(user.get("accept_followers"), bool)
        assert "name" in user


def test_wiki_page_sanitisation():
    sanitised_wiki_page = sanitise.wiki_page(RAW_WIKI_PAGE)
    assert isinstance(sanitised_wiki_page, Dict)
    assert isinstance(sanitised_wiki_page.get("revision_date"), (float, int))
    assert "link_karma" in sanitised_wiki_page.get("revision_by")
