from types import SimpleNamespace
from typing import Dict, List

from ._tools import timestamp_to_readable, TIME_FORMAT

__all__ = ["Parse"]


class Parse:
    """
    Provides methods for parsing sanitized data into SimpleNamespace objects.
    """

    def __init__(self, time_format: TIME_FORMAT = "locale"):
        """
        Initializes the Parse instance with the specified time format.

        :param time_format: Specifies the format of time-related fields.
                            Use 'concise' for a human-readable time difference,
                            or 'locale' for a localized datetime string.
                            Defaults to 'locale'.
        :type time_format: Literal["concise", "locale"]
        """

        self._time_format = time_format

    def comment(self, data: Dict) -> SimpleNamespace:
        """
        Parses a Reddit comment into a SimpleNamespace object.

        :param data: A dictionary containing raw data for a single Reddit comment.
        :type data: Dict
        :return: A SimpleNamespace object with parsed comment data.
        :rtype: SimpleNamespace
        """

        return (
            SimpleNamespace(
                **{
                    "body": data.get("body"),
                    "id": data.get("id"),
                    "author": data.get("author"),
                    "author_is_premium": data.get("author_premium"),
                    "upvotes": data.get("ups"),
                    "downvotes": data.get("downs"),
                    "subreddit": data.get("subreddit_name_prefixed"),
                    "subreddit_type": data.get("subreddit_type"),
                    "post_id": data.get("link_id"),
                    "post_title": data.get("link_title"),
                    "is_nsfw": data.get("over_18"),
                    "is_edited": data.get("edited"),
                    "score": data.get("score"),
                    "hidden_score": data.get("score_hidden"),
                    "gilded": data.get("gilded"),
                    "is_stickied": data.get("stickied"),
                    "is_locked": data.get("locked"),
                    "is_archived": data.get("archived"),
                    "subreddit_id": data.get("subreddit_id"),
                    "author_is_blocked": data.get("author_is_blocked"),
                    "link_author": data.get("link_author"),
                    "replies": data.get("replies"),
                    "saved": data.get("saved"),
                    "can_mod_post": data.get("can_mod_post"),
                    "send_replies": data.get("send_replies"),
                    "parent_id": data.get("parent_id"),
                    "author_fullname": data.get("author_fullname"),
                    "controversiality": data.get("controversiality"),
                    "body_html": data.get("body_html"),
                    "link_permalink": data.get("link_permalink"),
                    "name": data.get("name"),
                    "treatment_tags": data.get("treatment_tags"),
                    "awarders": data.get("awarders"),
                    "all_awardings": data.get("all_awardings"),
                    "quarantine": data.get("quarantine"),
                    "link_url": data.get("link_url"),
                    "created": timestamp_to_readable(
                        timestamp=data.get("created"),
                        time_format=self._time_format,
                    ),
                }
            )
            if isinstance(data, Dict)
            else SimpleNamespace
        )

    def comments(self, data: List[Dict]) -> List[SimpleNamespace]:
        """
        Parses a list of Reddit comments into a list of SimpleNamespace objects.

        :param data: A list of dictionaries representing raw comment data.
        :type data: List[Dict]
        :return: A list of SimpleNamespace objects with parsed comment data.
        :rtype: List[SimpleNamespace]
        """

        if isinstance(data, List) and all(
            isinstance(comment, Dict) for comment in data
        ):
            return [self.comment(data=raw_comment) for raw_comment in data]

    def post(self, data: Dict) -> SimpleNamespace:
        """
        Parses a subreddit into a SimpleNamespace object.

        :param data: A dictionary containing raw data for a single subreddit.
        :type data: Dict
        :return: A SimpleNamespace object with parsed subreddit data.
        :rtype: SimpleNamespace
        """

        return (
            SimpleNamespace(
                **{
                    "author": data.get("author"),
                    "title": data.get("title"),
                    "body": data.get("selftext"),
                    "id": data.get("id"),
                    "subreddit": data.get("subreddit"),
                    "subreddit_id": data.get("subreddit_id"),
                    "subreddit_type": data.get("subreddit_type"),
                    "subreddit_subscribers": data.get("subreddit_subscribers"),
                    "upvotes": data.get("ups"),
                    "upvote_ratio": data.get("upvote_ratio"),
                    "downvotes": data.get("downs"),
                    "thumbnail": data.get("thumbnail"),
                    "gilded": data.get("gilded"),
                    "is_video": data.get("is_video"),
                    "is_nsfw": data.get("over_18"),
                    "is_shareable": data.get("is_reddit_media_domain"),
                    "is_robot_indexable": data.get("is_robot_indexable"),
                    "permalink": data.get("permalink"),
                    "is_locked": data.get("locked"),
                    "is_archived": data.get("archived"),
                    "domain": data.get("domain"),
                    "score": data.get("score"),
                    "comments": data.get("num_comments"),
                    "saved": data.get("saved"),
                    "clicked": data.get("clicked"),
                    "hidden": data.get("hidden"),
                    "pwls": data.get("pwls"),
                    "hide_score": data.get("hide_score"),
                    "num_crossposts": data.get("num_crossposts"),
                    "parent_whitelist_status": data.get("parent_whitelist_status"),
                    "name": data.get("name"),
                    "quarantine": data.get("quarantine"),
                    "link_flair_text_color": data.get("link_flair_text_color"),
                    "is_original_content": data.get("is_original_content"),
                    "can_mod_post": data.get("can_mod_post"),
                    "is_created_from_ads_ui": data.get("is_created_from_ads_ui"),
                    "author_premium": data.get("author_premium"),
                    "is_self": data.get("is_self"),
                    "link_flair_type": data.get("link_flair_type"),
                    "wls": data.get("wls"),
                    "author_flair_type": data.get("author_flair_type"),
                    "allow_live_comments": data.get("allow_live_comments"),
                    "no_follow": data.get("no_follow"),
                    "is_crosspostable": data.get("is_crosspostable"),
                    "pinned": data.get("pinned"),
                    "author_is_blocked": data.get("author_is_blocked"),
                    "link_flair_background_color": data.get(
                        "link_flair_background_color"
                    ),
                    "author_fullname": data.get("author_fullname"),
                    "whitelist_status": data.get("whitelist_status"),
                    "edited": timestamp_to_readable(
                        timestamp=data.get("edited"), time_format=self._time_format
                    ),
                    "url": data.get("url"),
                    "created": timestamp_to_readable(
                        timestamp=data.get("created"), time_format=self._time_format
                    ),
                }
            )
            if isinstance(data, Dict)
            else SimpleNamespace
        )

    def posts(
        self,
        data: List[Dict],
    ) -> List[SimpleNamespace]:
        """
        Parses a list of Reddit posts into a list of SimpleNamespace objects.

        :param data: A list of dictionaries representing raw post data.
        :type data: List[Dict]
        :return: A list of SimpleNamespace objects with parsed post data.
        :rtype: List[SimpleNamespace]
        """

        if isinstance(data, List) and all(isinstance(post, Dict) for post in data):
            return [self.post(data=raw_post) for raw_post in data]

    def subreddit(self, data: Dict) -> SimpleNamespace:
        """
        Parses a single raw subreddit into a SimpleNamespace object.

        :param data: A dictionary containing raw data for a single subreddit.
        :type data: Dict
        :return: A SimpleNamespace object containing parsed subreddit data.
        :rtype: SimpleNamespace
        """

        return (
            SimpleNamespace(
                **{
                    "title": data.get("title"),
                    "display_name": data.get("display_name"),
                    "id": data.get("id"),
                    "description": data.get("public_description"),
                    "submit_text": data.get("submit_text"),
                    "submit_text_html": data.get("submit_text_html"),
                    "icon": (
                        data.get("icon_img").split("?")[0]
                        if data.get("icon_img")
                        else ""
                    ),
                    "type": data.get("subreddit_type"),
                    "subscribers": data.get("subscribers"),
                    "current_active_users": data.get("accounts_active"),
                    "is_nsfw": data.get("over18"),
                    "language": data.get("lang"),
                    "whitelist_status": data.get("whitelist_status"),
                    "url": data.get("url"),
                    "user_flair_position": data.get("user_flair_position"),
                    "spoilers_enabled": data.get("spoilers_enabled"),
                    "allow_galleries": data.get("allow_galleries"),
                    "show_media_preview": data.get("show_media_preview"),
                    "allow_videogifs": data.get("allow_videogifs"),
                    "allow_videos": data.get("allow_videos"),
                    "allow_images": data.get("allow_images"),
                    "allow_polls": data.get("allow_polls"),
                    "public_traffic": data.get("public_traffic"),
                    "description_html": data.get("description_html"),
                    "emojis_enabled": data.get("emojis_enabled"),
                    "primary_color": data.get("primary_color"),
                    "key_color": data.get("key_color"),
                    "banner_background_color": data.get("banner_background_color"),
                    "icon_size": data.get("icon_size"),
                    "header_size": data.get("header_size"),
                    "banner_size": data.get("banner_size"),
                    "link_flair_enabled": data.get("link_flair_enabled"),
                    "restrict_posting": data.get("restrict_posting"),
                    "restrict_commenting": data.get("restrict_commenting"),
                    "submission_type": data.get("submission_type"),
                    "free_form_reports": data.get("free_form_reports"),
                    "wiki_enabled": data.get("wiki_enabled"),
                    "community_icon": (
                        data.get("community_icon").split("?")[0]
                        if data.get("community_icon")
                        else ""
                    ),
                    "banner_background_image": data.get("banner_background_image"),
                    "mobile_banner_image": data.get("mobile_banner_image"),
                    "allow_discovery": data.get("allow_discovery"),
                    "is_crosspostable_subreddit": data.get(
                        "is_crosspostable_subreddit"
                    ),
                    "notification_level": data.get("notification_level"),
                    "suggested_comment_sort": data.get("suggested_comment_sort"),
                    "disable_contributor_requests": data.get(
                        "disable_contributor_requests"
                    ),
                    "community_reviewed": data.get("community_reviewed"),
                    "original_content_tag_enabled": data.get(
                        "original_content_tag_enabled"
                    ),
                    "has_menu_widget": data.get("has_menu_widget"),
                    "videostream_links_count": data.get("videostream_links_count"),
                    "created": timestamp_to_readable(
                        timestamp=data.get("created"),
                        time_format=self._time_format,
                    ),
                }
            )
            if isinstance(data, Dict)
            else SimpleNamespace
        )

    def subreddits(self, data: List[Dict]) -> List[SimpleNamespace]:
        """
        Parses a list of subreddits into a list of SimpleNamespace objects.

        :param data: A list of dictionaries representing raw subreddit data.
        :type data: List[Dict]
        :return: A list of SimpleNamespace objects with parsed subreddit data.
        :rtype: List[SimpleNamespace]
        """

        if isinstance(data, List) and all(
            isinstance(subreddit, Dict) for subreddit in data
        ):
            return [self.subreddit(data=raw_subreddit) for raw_subreddit in data]

    def user(self, data: Dict) -> SimpleNamespace:
        """
        Parses a Reddit user into a SimpleNamespace object.

        :param data: A dictionary containing raw data for a single Reddit user.
        :type data: Dict
        :return: A SimpleNamespace object with parsed user data.
        :rtype: SimpleNamespace
        """

        return (
            SimpleNamespace(
                **{
                    "name": data.get("name"),
                    "id": data.get("id"),
                    "avatar_url": data.get("icon_img"),
                    "is_verified": data.get("verified"),
                    "has_verified_email": data.get("has_verified_email"),
                    "is_gold": data.get("is_gold"),
                    "is_mod": data.get("is_mod"),
                    "is_blocked": data.get("is_blocked"),
                    "is_employee": data.get("is_employee"),
                    "hidden_from_bots": data.get("hide_from_robots"),
                    "accepts_followers": data.get("accept_followers"),
                    "comment_karma": data.get("comment_karma"),
                    "link_karma": data.get("link_karma"),
                    "awardee_karma": data.get("awardee_karma"),
                    "total_karma": data.get("total_karma"),
                    "subreddit": data.get("subreddit"),
                    "is_friend": data.get("is_friend"),
                    "snoovatar_img": data.get("snoovatar_img"),
                    "awarder_karma": data.get("awarder_karma"),
                    "pref_show_snoovatar": data.get("pref_show_snoovatar"),
                    "has_subscribed": data.get("has_subscribed"),
                    "created": timestamp_to_readable(
                        timestamp=data.get("created"), time_format=self._time_format
                    ),
                }
            )
            if isinstance(data, Dict)
            else SimpleNamespace
        )

    def users(self, data: List[Dict]) -> List[SimpleNamespace]:
        """
        Parses a list of Reddit users into a list of SimpleNamespace objects.

        :param data: A list of dictionaries representing raw user data.
        :type data: List[Dict]
        :return: A list of SimpleNamespace objects with parsed user data.
        :rtype: List[SimpleNamespace]
        """

        if isinstance(data, List) and all(isinstance(user, Dict) for user in data):
            return [self.user(data=raw_user) for raw_user in data]

    def wiki_page(self, data: Dict) -> SimpleNamespace:
        """
        Parses a Reddit wiki page into a SimpleNamespace object.

        :param data: A dictionary containing raw data for a Reddit wiki page.
        :type data: Dict
        :return: A SimpleNamespace object with parsed wiki page data.
        :rtype: SimpleNamespace
        """

        if isinstance(data, Dict):
            return SimpleNamespace(
                **{
                    "revision_id": data.get("revision_id"),
                    "revision_date": timestamp_to_readable(
                        timestamp=data.get("revision_date"),
                        time_format=self._time_format,
                    ),
                    "content_markdown": data.get("content_md"),
                    "revised_by": self.user(data=data.get("revised_by")),
                    "kind": data.get("kind"),
                    "may_revise": data.get("may_revise"),
                    "reason": data.get("reason"),
                    "content_html": data.get("content_html"),
                }
            )


# -------------------------------- END ----------------------------------------- #
