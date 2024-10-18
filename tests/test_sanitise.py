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


def test_comments_sanitisation():
    sanitised_comments = Sanitise.comments(RAW_COMMENTS)
    assert isinstance(sanitised_comments, List)
    assert [Sanitise.kind(raw_comment) == "t3" for raw_comment in RAW_COMMENTS]
    for comment in sanitised_comments:
        assert isinstance(comment, Dict)
        assert "link_id" in comment


def test_post_sanitisation():
    sanitised_post = Sanitise.post(RAW_POST)
    assert isinstance(sanitised_post, Dict)
    assert isinstance(sanitised_post.get("ups"), int)
    assert Sanitise.kind(RAW_POST[1]) == "Listing"


def test_posts_sanitisation():
    sanitised_posts = Sanitise.posts(RAW_POSTS)
    assert isinstance(sanitised_posts, List)
    assert [Sanitise.kind(response=raw_post) == "Listing" for raw_post in RAW_POSTS]
    for post in sanitised_posts:
        assert isinstance(post, Dict)
        assert "title" or "selftext" in post


def test_subreddit_sanitisation():
    sanitised_subreddit = Sanitise.subreddit_or_user(RAW_SUBREDDIT)
    assert isinstance(sanitised_subreddit, Dict)
    assert isinstance(sanitised_subreddit.get("accounts_active"), int)
    assert "display_name" in sanitised_subreddit
    assert Sanitise.kind(RAW_SUBREDDIT) == "t5"


def test_subreddits_sanitisation():
    sanitised_subreddits = Sanitise.subreddits_or_users(RAW_SUBREDDITS)
    assert isinstance(sanitised_subreddits, List)
    assert [
        Sanitise.kind(response=raw_subreddit) == "t5"
        for raw_subreddit in RAW_SUBREDDITS
    ]
    for subreddit in sanitised_subreddits:
        assert isinstance(subreddit, Dict)
        assert isinstance(subreddit.get("subscribers"), int)
        assert "display_name" in subreddit


def test_user_sanitisation():
    sanitised_user = Sanitise.subreddit_or_user(RAW_USER)
    assert isinstance(sanitised_user, Dict)
    assert isinstance(sanitised_user.get("created"), (float, int))
    assert "comment_karma" in sanitised_user
    assert Sanitise.kind(RAW_USER) == "t2"


def test_users_sanitisation():
    sanitised_users = Sanitise.subreddits_or_users(RAW_USERS)
    assert isinstance(sanitised_users, List)
    assert [Sanitise.kind(response=raw_user) == "t2" for raw_user in RAW_USERS]
    for user in sanitised_users:
        assert isinstance(user, Dict)
        assert isinstance(user.get("accept_followers"), bool)
        assert "name" in user


def test_wiki_page_sanitisation():
    sanitised_wiki_page = Sanitise.wiki_page(RAW_WIKI_PAGE)
    assert isinstance(sanitised_wiki_page, Dict)
    assert isinstance(sanitised_wiki_page.get("revision_date"), (float, int))
    assert "link_karma" in sanitised_wiki_page.get("revision_by")
    assert Sanitise.kind(RAW_WIKI_PAGE) == "wikipage"
