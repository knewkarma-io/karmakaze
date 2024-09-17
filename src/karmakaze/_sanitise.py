from typing import List, Dict, Union

__all__ = ["Sanitise"]


class Sanitise:
    """
    Provides static methods to sanitize various types of data
    from Reddit API responses.
    """

    @staticmethod
    def comments(response: List[Dict]) -> Union[List[Dict], None]:
        """
        Sanitizes a Reddit API response to extract and return a list of comment data.

        :param response: A list containing the Reddit API response data. The response
                         is expected to contain multiple elements, where the second element
                         (index 1) holds the relevant data.
        :type response: List[Dict]
        :return: A list of dictionaries, each representing a comment's data.
           Returns None if the response is invalid.
        :rtype: Union[List[Dict], None]
        """

        if isinstance(response, List):
            response = response[1]  # Extract the second element where data resides.
            data: Dict = response.get("data")
            children = data.get("children")

            return (
                [child.get("data") for child in children]
                if isinstance(children, List)
                else None
            )

    @staticmethod
    def pagination_id(response: Dict) -> Union[str, None]:
        """
        Sanitises a Reddit API response to extract and return a pagination ID.

        :param response: A dictionary containing Reddit API response data.
        :type response: Dict
        :return: A pagination ID from the response, if response is valid.
                Returns None if the response is invalid.
        :rtype: Union[str, None]
        """

        return response.get("after")

    @staticmethod
    def post(response: List[Dict]) -> Union[Dict, None]:
        """
        Sanitizes a Reddit API response to extract and return the data of a single post.

        :param response: A list containing the Reddit API response data. The response
                         is expected to contain multiple elements, where the first element
                         (index 0) holds the relevant data.
        :type response: List[Dict]
        :return: A dictionary representing the post's data, or None if the response is invalid.
        :rtype: Union[Dict, None]
        """

        children: List[Dict] = []
        if isinstance(response, List):
            response = response[0]  # Extract the first element where data resides.
            children = response.get("data").get("children")

        return children[0].get("data") if isinstance(children, List) else None

    @staticmethod
    def posts(response: Dict) -> Union[List[Dict], None]:
        """
        Sanitizes a Reddit API response to extract and return a list of post data.

        :param response: A dictionary containing the Reddit API response data.
        :type response: Dict
        :return: A list of dictionaries, each representing a post's data.
                 Returns None if the response is invalid.
        :rtype: Union[List[Dict], None]
        """

        data: Dict = response.get("data")
        children: List = data.get("children")
        return (
            [child.get("data") for child in children]
            if isinstance(children, List)
            else None
        )

    @staticmethod
    def subreddit_or_user(response: Dict) -> Union[Dict, None]:
        """
        Sanitizes a Reddit API response to extract and return the data of a subreddit or user.

        :param response: A dictionary containing the Reddit API response data.
        :type response: Dict
        :return: A dictionary representing the subreddit or user's data, or None if the response is invalid.
        :rtype: Union[Dict, None]
        """

        data: Dict = response.get("data")
        return data if isinstance(data, Dict) else None

    @staticmethod
    def subreddits_or_users(response: Dict) -> Union[List[Dict], None]:
        """
        Sanitizes a Reddit API response to extract and return a list of subreddit or user data.

        :param response: A dictionary containing the Reddit API response data.
        :type response: Dict
        :return: A list of dictionaries representing subreddit or user data.
                 Returns None if the response is invalid.
        :rtype: Union[List[Dict], None]
        """

        data: Dict = response.get("data")
        children: List = data.get("children")
        return (
            [Sanitise.subreddit_or_user(response=child) for child in children]
            if isinstance(children, List)
            else None
        )

    @staticmethod
    def wiki_page(response: Dict) -> Union[Dict, None]:
        """
        Sanitizes a Reddit API response to extract and return the data of a wiki page,
        including revision information.

        :param response: A dictionary containing the Reddit API response data.
        :type response: Dict
        :return: A dictionary representing the wiki page data, including revision information.
                 Returns None if the response is invalid.
        :rtype: Union[Dict, None]
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
