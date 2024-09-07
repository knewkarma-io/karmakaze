from types import SimpleNamespace
from typing import Dict, Union, List

from .tools import timestamp_to_readable, TIME_FORMAT

__all__ = ["Strukt"]


class Strukt:
    def __init__(self, time_format: TIME_FORMAT = "locale"):
        self._time_format = time_format

    def comments(
        self, raw_comments: Union[List[Dict], Dict]
    ) -> Union[List[SimpleNamespace], SimpleNamespace]:
        """
        Restructures raw Reddit comments and parses them into a list of SimpleNamespace objects.

        :param raw_comments: A list of dictionaries, each representing raw comment data,
                             or a single dictionary.
        :type raw_comments: Union[List[Dict], Dict]
        :return: Parsed comments data as a list of SimpleNamespace objects if the input is a list,
                 or a single SimpleNamespace object if the input is a dictionary.
        :rtype: Union[List[SimpleNamespace], SimpleNamespace]
        """

        def comment(raw_comment: Dict) -> SimpleNamespace:
            """
            Restructures a single raw comment and parses it into a SimpleNamespace object.

            :param raw_comment: A dictionary containing raw data for a single Reddit raw_comment.
            :type raw_comment: Dict
            :return: A SimpleNamespace object containing the parsed comment data.
            :rtype: SimpleNamespace
            """

            return SimpleNamespace(
                **{
                    "body": raw_comment.get("body"),
                    "id": raw_comment.get("id"),
                    "author": raw_comment.get("author"),
                    "author_is_premium": raw_comment.get("author_premium"),
                    "upvotes": raw_comment.get("ups"),
                    "downvotes": raw_comment.get("downs"),
                    "subreddit": raw_comment.get("subreddit_name_prefixed"),
                    "subreddit_type": raw_comment.get("subreddit_type"),
                    "post_id": raw_comment.get("link_id"),
                    "post_title": raw_comment.get("link_title"),
                    "is_nsfw": raw_comment.get("over_18"),
                    "is_edited": raw_comment.get("edited"),
                    "score": raw_comment.get("score"),
                    "hidden_score": raw_comment.get("score_hidden"),
                    "gilded": raw_comment.get("gilded"),
                    "is_stickied": raw_comment.get("stickied"),
                    "is_locked": raw_comment.get("locked"),
                    "is_archived": raw_comment.get("archived"),
                    "subreddit_id": raw_comment.get("subreddit_id"),
                    "author_is_blocked": raw_comment.get("author_is_blocked"),
                    "link_author": raw_comment.get("link_author"),
                    "replies": raw_comment.get("replies"),
                    "saved": raw_comment.get("saved"),
                    "can_mod_post": raw_comment.get("can_mod_post"),
                    "send_replies": raw_comment.get("send_replies"),
                    "parent_id": raw_comment.get("parent_id"),
                    "author_fullname": raw_comment.get("author_fullname"),
                    "controversiality": raw_comment.get("controversiality"),
                    "body_html": raw_comment.get("body_html"),
                    "link_permalink": raw_comment.get("link_permalink"),
                    "name": raw_comment.get("name"),
                    "treatment_tags": raw_comment.get("treatment_tags"),
                    "awarders": raw_comment.get("awarders"),
                    "all_awardings": raw_comment.get("all_awardings"),
                    "quarantine": raw_comment.get("quarantine"),
                    "link_url": raw_comment.get("link_url"),
                    "created": timestamp_to_readable(
                        timestamp=raw_comment.get("created"),
                        time_format=self._time_format,
                    ),
                }
            )

        if isinstance(raw_comments, List) and all(
            isinstance(comment) for comment in raw_comments
        ):
            return [comment(raw_comment=raw_comment) for raw_comment in raw_comments]
        elif isinstance(raw_comments, Dict):
            return comment(raw_comment=raw_comments)

    def posts(
        self, raw_posts: Union[Dict, List]
    ) -> Union[List[SimpleNamespace], SimpleNamespace]:
        """
        Restructures raw Reddit posts and parses them into a list of SimpleNamespace objects.

        :param raw_posts: A list of dictionaries, each representing raw post data,
                          or a single dictionary.
        :type raw_posts: Union[List[Dict], Dict]
        :return: Parsed post data as a list of SimpleNamespace objects if the input is a list,
                 or a single SimpleNamespace object if the input is a dictionary.
        :rtype: Union[List[SimpleNamespace], SimpleNamespace]
        """

        def post(raw_post: Dict) -> SimpleNamespace:
            """
            Restructures a single raw post and parses it into a SimpleNamespace object.

            :param raw_post: A dictionary containing raw data for a single Reddit post.
            :type raw_post: Dict
            :return: A SimpleNamespace object containing parsed post data.
            :rtype: SimpleNamespace
            """

            return SimpleNamespace(
                **{
                    "author": raw_post.get("author"),
                    "title": raw_post.get("title"),
                    "body": raw_post.get("selftext"),
                    "id": raw_post.get("id"),
                    "subreddit": raw_post.get("subreddit"),
                    "subreddit_id": raw_post.get("subreddit_id"),
                    "subreddit_type": raw_post.get("subreddit_type"),
                    "subreddit_subscribers": raw_post.get("subreddit_subscribers"),
                    "upvotes": raw_post.get("ups"),
                    "upvote_ratio": raw_post.get("upvote_ratio"),
                    "downvotes": raw_post.get("downs"),
                    "thumbnail": raw_post.get("thumbnail"),
                    "gilded": raw_post.get("gilded"),
                    "is_video": raw_post.get("is_video"),
                    "is_nsfw": raw_post.get("over_18"),
                    "is_shareable": raw_post.get("is_reddit_media_domain"),
                    "is_robot_indexable": raw_post.get("is_robot_indexable"),
                    "permalink": raw_post.get("permalink"),
                    "is_locked": raw_post.get("locked"),
                    "is_archived": raw_post.get("archived"),
                    "domain": raw_post.get("domain"),
                    "score": raw_post.get("score"),
                    "comments": raw_post.get("num_comments"),
                    "saved": raw_post.get("saved"),
                    "clicked": raw_post.get("clicked"),
                    "hidden": raw_post.get("hidden"),
                    "pwls": raw_post.get("pwls"),
                    "hide_score": raw_post.get("hide_score"),
                    "num_crossposts": raw_post.get("num_crossposts"),
                    "parent_whitelist_status": raw_post.get("parent_whitelist_status"),
                    "name": raw_post.get("name"),
                    "quarantine": raw_post.get("quarantine"),
                    "link_flair_text_color": raw_post.get("link_flair_text_color"),
                    "is_original_content": raw_post.get("is_original_content"),
                    "can_mod_post": raw_post.get("can_mod_post"),
                    "is_created_from_ads_ui": raw_post.get("is_created_from_ads_ui"),
                    "author_premium": raw_post.get("author_premium"),
                    "is_self": raw_post.get("is_self"),
                    "link_flair_type": raw_post.get("link_flair_type"),
                    "wls": raw_post.get("wls"),
                    "author_flair_type": raw_post.get("author_flair_type"),
                    "allow_live_comments": raw_post.get("allow_live_comments"),
                    "no_follow": raw_post.get("no_follow"),
                    "is_crosspostable": raw_post.get("is_crosspostable"),
                    "pinned": raw_post.get("pinned"),
                    "author_is_blocked": raw_post.get("author_is_blocked"),
                    "link_flair_background_color": raw_post.get(
                        "link_flair_background_color"
                    ),
                    "author_fullname": raw_post.get("author_fullname"),
                    "whitelist_status": raw_post.get("whitelist_status"),
                    "edited": timestamp_to_readable(
                        timestamp=raw_post.get("edited"), time_format=self._time_format
                    ),
                    "url": raw_post.get("url"),
                    "created": timestamp_to_readable(
                        timestamp=raw_post.get("created"), time_format=self._time_format
                    ),
                }
            )

        if isinstance(raw_posts, List) and all(isinstance(post) for post in raw_posts):
            return [post(raw_post=raw_post) for raw_post in raw_posts]
        elif isinstance(raw_posts, Dict):
            return post(raw_post=raw_posts)

    def subreddits(
        self, raw_subreddits: Union[List[Dict], Dict]
    ) -> Union[List[SimpleNamespace], SimpleNamespace]:
        """
        Restructures raw Reddit subreddits and parses them into a list of SimpleNamespace objects.

        :param raw_subreddits: A list of dictionaries, each representing raw subreddit data, or a single dictionary.
        :type raw_subreddits: Union[List[Dict], Dict]
        :return: Parsed subreddit data as a list of SimpleNamespace objects if the input is a list, or a single SimpleNamespace object if the input is a Dictionary.
        :rtype: Union[List[SimpleNamespace], SimpleNamespace]
        """

        def subreddit(raw_subreddit: dict) -> SimpleNamespace:
            """
            Restructures a single raw subreddit and parses it into a SimpleNamespace object.

            :param raw_subreddit: A dictionary containing raw data for a single subreddit.
            :type raw_subreddit: Dict
            :return: A SimpleNamespace object containing parsed subreddit data.
            :rtype: SimpleNamespace
            """

            return SimpleNamespace(
                **{
                    "title": raw_subreddit.get("title"),
                    "display_name": raw_subreddit.get("display_name"),
                    "id": raw_subreddit.get("id"),
                    "description": raw_subreddit.get("public_description"),
                    "submit_text": raw_subreddit.get("submit_text"),
                    "submit_text_html": raw_subreddit.get("submit_text_html"),
                    "icon": (
                        raw_subreddit.get("icon_img").split("?")[0]
                        if raw_subreddit.get("icon_img")
                        else ""
                    ),
                    "type": raw_subreddit.get("subreddit_type"),
                    "subscribers": raw_subreddit.get("subscribers"),
                    "current_active_users": raw_subreddit.get("accounts_active"),
                    "is_nsfw": raw_subreddit.get("over18"),
                    "language": raw_subreddit.get("lang"),
                    "whitelist_status": raw_subreddit.get("whitelist_status"),
                    "url": raw_subreddit.get("url"),
                    "user_flair_position": raw_subreddit.get("user_flair_position"),
                    "spoilers_enabled": raw_subreddit.get("spoilers_enabled"),
                    "allow_galleries": raw_subreddit.get("allow_galleries"),
                    "show_media_preview": raw_subreddit.get("show_media_preview"),
                    "allow_videogifs": raw_subreddit.get("allow_videogifs"),
                    "allow_videos": raw_subreddit.get("allow_videos"),
                    "allow_images": raw_subreddit.get("allow_images"),
                    "allow_polls": raw_subreddit.get("allow_polls"),
                    "public_traffic": raw_subreddit.get("public_traffic"),
                    "description_html": raw_subreddit.get("description_html"),
                    "emojis_enabled": raw_subreddit.get("emojis_enabled"),
                    "primary_color": raw_subreddit.get("primary_color"),
                    "key_color": raw_subreddit.get("key_color"),
                    "banner_background_color": raw_subreddit.get(
                        "banner_background_color"
                    ),
                    "icon_size": raw_subreddit.get("icon_size"),
                    "header_size": raw_subreddit.get("header_size"),
                    "banner_size": raw_subreddit.get("banner_size"),
                    "link_flair_enabled": raw_subreddit.get("link_flair_enabled"),
                    "restrict_posting": raw_subreddit.get("restrict_posting"),
                    "restrict_commenting": raw_subreddit.get("restrict_commenting"),
                    "submission_type": raw_subreddit.get("submission_type"),
                    "free_form_reports": raw_subreddit.get("free_form_reports"),
                    "wiki_enabled": raw_subreddit.get("wiki_enabled"),
                    "community_icon": (
                        raw_subreddit.get("community_icon").split("?")[0]
                        if raw_subreddit.get("community_icon")
                        else ""
                    ),
                    "banner_background_image": raw_subreddit.get(
                        "banner_background_image"
                    ),
                    "mobile_banner_image": raw_subreddit.get("mobile_banner_image"),
                    "allow_discovery": raw_subreddit.get("allow_discovery"),
                    "is_crosspostable_subreddit": raw_subreddit.get(
                        "is_crosspostable_subreddit"
                    ),
                    "notification_level": raw_subreddit.get("notification_level"),
                    "suggested_comment_sort": raw_subreddit.get(
                        "suggested_comment_sort"
                    ),
                    "disable_contributor_requests": raw_subreddit.get(
                        "disable_contributor_requests"
                    ),
                    "community_reviewed": raw_subreddit.get("community_reviewed"),
                    "original_content_tag_enabled": raw_subreddit.get(
                        "original_content_tag_enabled"
                    ),
                    "has_menu_widget": raw_subreddit.get("has_menu_widget"),
                    "videostream_links_count": raw_subreddit.get(
                        "videostream_links_count"
                    ),
                    "created": timestamp_to_readable(
                        timestamp=raw_subreddit.get("created"),
                        time_format=self._time_format,
                    ),
                }
            )

        if isinstance(raw_subreddits, List) and all(
            isinstance(subreddit) for subreddit in raw_subreddits
        ):
            return [
                subreddit(raw_subreddit=raw_subreddit)
                for raw_subreddit in raw_subreddits
            ]
        elif isinstance(raw_subreddits, Dict):
            return subreddit(raw_subreddit=raw_subreddits)

    def users(
        self, raw_users: Union[List[Dict], Dict]
    ) -> Union[List[SimpleNamespace], SimpleNamespace]:
        """
        Restructures raw Reddit users and parses them into a list of SimpleNamespace objects.

        :param raw_users: A list of dictionaries, each containing raw user data, or a single dictionary.
        :type raw_users: Union[List[Dict], Dict]
        :return: Parsed user data as a list of SimpleNamespace objects if the input is a list, or a single SimpleNamespace object if the input is a dictionary.
        :rtype: Union[List[SimpleNamespace], SimpleNamespace]
        """

        def user(raw_user: Dict) -> SimpleNamespace:
            """
            Restructures a single raw user and parses it into a SimpleNamespace object.

            :param raw_user: A dictionary containing raw data for a single Reddit user.
            :type raw_user: Dict
            :return: A SimpleNamespace object containing parsed user data.
            :rtype: SimpleNamespace
            """

            return SimpleNamespace(
                **{
                    "name": raw_user.get("name"),
                    "id": raw_user.get("id"),
                    "avatar_url": raw_user.get("icon_img"),
                    "is_verified": raw_user.get("verified"),
                    "has_verified_email": raw_user.get("has_verified_email"),
                    "is_gold": raw_user.get("is_gold"),
                    "is_mod": raw_user.get("is_mod"),
                    "is_blocked": raw_user.get("is_blocked"),
                    "is_employee": raw_user.get("is_employee"),
                    "hidden_from_bots": raw_user.get("hide_from_robots"),
                    "accepts_followers": raw_user.get("accept_followers"),
                    "comment_karma": raw_user.get("comment_karma"),
                    "link_karma": raw_user.get("link_karma"),
                    "awardee_karma": raw_user.get("awardee_karma"),
                    "total_karma": raw_user.get("total_karma"),
                    "subreddit": raw_user.get("subreddit"),
                    "is_friend": raw_user.get("is_friend"),
                    "snoovatar_img": raw_user.get("snoovatar_img"),
                    "awarder_karma": raw_user.get("awarder_karma"),
                    "pref_show_snoovatar": raw_user.get("pref_show_snoovatar"),
                    "has_subscribed": raw_user.get("has_subscribed"),
                    "created": timestamp_to_readable(
                        timestamp=raw_user.get("created"), time_format=self._time_format
                    ),
                }
            )

        if isinstance(raw_users, List) and all(isinstance(user) for user in raw_users):
            return [user(raw_user=raw_user) for raw_user in raw_users]

        elif isinstance(raw_users, Dict) and "is_employee" in raw_users:
            return user(raw_user=raw_users)

    def wiki_page(self, raw_wiki_page: Dict) -> SimpleNamespace:
        """
        Restructures raw Reddit wiki page and parses it into a SimpleNamespace object.

        :param raw_wiki_page: A dictionary representing raw wiki page data.
        :type raw_wiki_page: Dict
        :return: Parsed wiki page data as a SimpleNamespace object.
        :rtype: SimpleNamespace
        """

        if isinstance(raw_wiki_page, Dict):
            return SimpleNamespace(
                **{
                    "revision_id": raw_wiki_page.get("revision_id"),
                    "revision_date": timestamp_to_readable(
                        timestamp=raw_wiki_page.get("revision_date"),
                        time_format=self._time_format,
                    ),
                    "content_markdown": raw_wiki_page.get("content_md"),
                    "revised_by": self.users(
                        raw_users=raw_wiki_page.get("revision_by")
                    ),
                    "kind": raw_wiki_page.get("kind"),
                    "may_revise": raw_wiki_page.get("may_revise"),
                    "reason": raw_wiki_page.get("reason"),
                    "content_html": raw_wiki_page.get("content_html"),
                }
            )


# -------------------------------- END ----------------------------------------- #
