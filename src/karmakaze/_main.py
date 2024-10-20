from types import SimpleNamespace
from typing import Union, List, Dict

from ._utils import timestamp_to_readable, TIME_FORMAT

__all__ = ["SanitiseAndParse"]


class SanitiseAndParse:

    def __init__(self, time_format: TIME_FORMAT = "locale"):

        self._time_format = time_format

    def _to_namespace_object(
        self, obj: Union[List[Dict], Dict]
    ) -> Union[List[SimpleNamespace], SimpleNamespace, Union[List[Dict], Dict]]:

        if isinstance(obj, Dict):
            # Recursively convert any dictionaries within the current dict
            return SimpleNamespace(
                **{
                    key: (
                        timestamp_to_readable(value, self._time_format)
                        if key in {"created", "created_utc", "edited", "revision_date"}
                        else self._to_namespace_object(obj=value)
                    )
                    for key, value in obj.items()
                }
            )
        elif isinstance(obj, List):
            # If it's a list, check if any of the items are dicts and convert them too
            return [self._to_namespace_object(obj=item) for item in obj]
        else:
            return obj

    def comment(self, response: Dict) -> SimpleNamespace:

        if isinstance(response, Dict):
            return self._to_namespace_object(obj=response)

    def comments(
        self, response: Union[List[Dict], Dict]
    ) -> Union[List[SimpleNamespace], SimpleNamespace]:

        if isinstance(response, List) and all(
            isinstance(comment, Dict) for comment in response
        ):
            return [self.comment(response=raw_comment) for raw_comment in response]
        elif isinstance(response, Dict):
            return self._to_namespace_object(obj=response.get("data", {}))

    def post(self, response: List[Dict]) -> SimpleNamespace:

        if isinstance(response, List) and len(response) == 2:
            children = response[0].get("data", {}).get("children")
            return self._to_namespace_object(obj=children[0])

    def posts(
        self,
        response: Dict,
    ) -> Union[List[SimpleNamespace], SimpleNamespace]:

        data: Dict = response.get("data", {})
        if isinstance(data, Dict):
            return self._to_namespace_object(obj=data)

    def subreddit(self, response: Dict) -> SimpleNamespace:

        if "data" in response:
            return self._to_namespace_object(obj=response)

    def subreddits(
        self, response: Dict
    ) -> Union[List[SimpleNamespace], SimpleNamespace]:

        if "data" in response:
            return self._to_namespace_object(obj=response.get("data", {}))

    def user(self, response: Dict) -> SimpleNamespace:

        if "data" in response:
            return self._to_namespace_object(obj=response)

    def users(self, response: Dict) -> Union[List[SimpleNamespace], SimpleNamespace]:
        if "data" in response:
            return self._to_namespace_object(obj=response.get("data", {}))

    def wiki_page(self, response: Dict) -> SimpleNamespace:

        if "data" in response:
            return self._to_namespace_object(obj=response)


# -------------------------------- END ----------------------------------------- #
