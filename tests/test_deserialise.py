from typing import List, Dict

from conftest import (
    RAW_COMMENTS,
    RAW_POST,
    RAW_POSTS,
    RAW_SUBREDDIT,
    RAW_USER,
    RAW_SUBREDDITS,
    RAW_USERS,
)
from conftest import RAW_WIKI_PAGE
from karmakaze.deserialise import Deserialise


def test_comments_deserialisation():
    deserialised_response = Deserialise.comments(RAW_COMMENTS)
    assert isinstance(deserialised_response, List)

    for comment in deserialised_response:
        assert isinstance(comment, Dict)
        assert "link_id" in comment


def test_post_deserialisation():
    deserialised_response = Deserialise.post(RAW_POST)
    assert isinstance(deserialised_response, Dict)
    assert isinstance(deserialised_response.get("ups"), int)


def test_posts_deserialisation():
    deserialised_response = Deserialise.posts(RAW_POSTS)
    assert isinstance(deserialised_response, List)
    for post in deserialised_response:
        assert isinstance(post, Dict)
        assert "title" or "selftext" in post


def test_subreddit_deserialisation():
    deserialised_response = Deserialise.subreddit_or_user(RAW_SUBREDDIT)
    assert isinstance(deserialised_response, Dict)
    assert isinstance(deserialised_response.get("accounts_active"), int)
    assert "display_name" in deserialised_response


def test_subreddits_deserialisation():
    deserialised_response = Deserialise.subreddits_or_users(RAW_SUBREDDITS)
    assert isinstance(deserialised_response, List)
    for subreddit in deserialised_response:
        assert isinstance(subreddit, Dict)
        assert isinstance(subreddit.get("subscribers"), int)
        assert "display_name" in subreddit


def test_user_deserialisation():
    deserialised_response = Deserialise.subreddit_or_user(RAW_USER)
    assert isinstance(deserialised_response, Dict)
    assert isinstance(deserialised_response.get("created"), (float, int))
    assert "comment_karma" in deserialised_response


def test_users_deserialisation():
    deserialised_response = Deserialise.subreddits_or_users(RAW_USERS)
    assert isinstance(deserialised_response, List)
    for user in deserialised_response:
        assert isinstance(user, Dict)
        assert isinstance(user.get("accept_followers"), bool)
        assert "name" in user


def test_wiki_page_deserialisation():
    deserialised_response = Deserialise.wiki_page(RAW_WIKI_PAGE)
    assert isinstance(deserialised_response, Dict)
    assert isinstance(deserialised_response.get("revision_date"), (float, int))
    assert "link_karma" in deserialised_response.get("revision_by")
