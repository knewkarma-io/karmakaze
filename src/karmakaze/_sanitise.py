from typing import List, Dict, Union

__all__ = ["Sanitise"]


class Sanitise:
    """
    Provides static methods to sanitise various types of data
    from Reddit API responses.
    """

    @staticmethod
    def comments(response: List[Dict]) -> Union[List[Dict], None]:
        """
        Sanitises a Reddit API response to extract and return a list of comment data.
        :param response: A list containing the Reddit API response data.
        :type response: List[Dict]
        :return: A list of dictionaries, each representing a comment's data.
        :rtype: List[Dict]
        """

        children: List[Dict] = []
        if isinstance(response, List):
            response = response[1]
            children = response.get("data").get("children")

        return (
            [child.get("data") for child in children]
            if isinstance(children, List)
            else None
        )

    @staticmethod
    def post(response: List[Dict]) -> Union[Dict, None]:
        """
        Sanitises a Reddit API response to extract and return the data of a single post.

        :param response: A list containing the Reddit API response data.
        :type response: List[Dict]
        :return: A dictionary representing the post's data.
        :rtype: Dict
        """

        children: List[Dict] = []
        if isinstance(response, List):
            response = response[0]
            children = response.get("data").get("children")

        return children[0].get("data") if isinstance(children, List) else None

    @staticmethod
    def posts(response: Dict) -> Union[List[Dict], None]:
        """
        Sanitises a Reddit API response to extract and return a list of post data.

        :param response: A dictionary containing the Reddit API response data.
        :type response: Dict
        :return: A list of dictionaries, each representing a post's data.
        :rtype: List[Dict]
        """

        children: Dict = response.get("data").get("children")
        return (
            [child.get("data") for child in children]
            if isinstance(children, List)
            else None
        )

    @staticmethod
    def subreddit_or_user(response: Dict) -> Union[Dict, None]:
        """
        Sanitises a Reddit API response to extract and return the data of a subreddit or user.

        :param response: A dictionary containing the Reddit API response data.
        :type response: Dict
        :return: A dictionary representing the subreddit or user's data, or None if not applicable.
        :rtype: Dict
        """

        data: Dict = response.get("data")
        return data if isinstance(data, Dict) else None

    @staticmethod
    def subreddits_or_users(response: Dict) -> Union[List[Dict], None]:
        """
        Sanitises a Reddit API response to extract and return a list of subreddit or user data.

        :param response: A dictionary containing the Reddit API response data.
        :type response: Dict
        :return: A list of dictionaries representing subreddit or user data, or None if not applicable.
        :rtype: Union[List[Dict], None]
        """

        children: List = response.get("data").get("children")
        return (
            [Sanitise.subreddit_or_user(response=data) for data in children]
            if isinstance(children, List)
            else None
        )

    @staticmethod
    def wiki_page(response: Dict) -> Union[Dict, None]:
        """
        Sanitises a Reddit API response to extract and return the data of a wiki page,
        including revision information.

        :param response: A dictionary containing the Reddit API response data.
        :type response: Dict
        :return: A dictionary representing the wiki page data, including revision information.
        :rtype: Dict
        """
        data: Dict = response.get("data")
        if data:
            revision_by = data.get("revision_by")
            if revision_by and isinstance(revision_by, Dict):
                sanitized_revision_by = Sanitise.subreddit_or_user(response=revision_by)
                data["revision_by"] = (
                    sanitized_revision_by if sanitized_revision_by else revision_by
                )

            return data


# -------------------------------- END ----------------------------------------- #
