import locale
import time
from datetime import timezone, datetime
from typing import Literal, Union

TIME_FORMAT = Literal["locale", "concise"]

__all__ = [
    "timestamp_to_concise",
    "timestamp_to_locale",
    "timestamp_to_readable",
    "TIME_FORMAT",
]


def timestamp_to_locale(timestamp: float) -> str:
    """
    Converts a unix timestamp to a localized datetime string based on the system's locale.

    :param timestamp: Unix timestamp to convert.
    :type timestamp: float
    :return: A localized datetime string from the converted timestamp.
    :rtype: str
    """

    # Set the locale to the user's system default
    locale.setlocale(locale.LC_TIME, "")

    # Convert timestamp to a timezone-aware datetime object in UTC
    utc_object = datetime.fromtimestamp(timestamp, timezone.utc)

    local_object = utc_object.astimezone()

    # Format the datetime object according to the locale's conventions
    return local_object.strftime("%x, %X")


def timestamp_to_concise(timestamp: int) -> str:
    """
    Convert a Unix timestamp into a human-readable concise time difference.

    :param timestamp: A Unix timestamp.
    :type timestamp: int
    :return: A string representing the time difference from now.
    :rtype: str
    """

    # Convert the current time to a Unix timestamp
    now = int(time.time())

    # Calculate the difference in seconds
    diff = now - timestamp

    # Define the time thresholds in seconds
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    week = 7 * day
    month = 30 * day
    year = 12 * month

    # Determine the time unit and value
    if diff < minute:
        count = diff
        label = "seconds" if int(count) > 1 else "second"  # seconds
    elif diff < hour:
        count = diff // minute
        label = "minutes" if int(count) > 1 else "minute"  # minutes
    elif diff < day:
        count = diff // hour
        label = "hours" if int(count) > 1 else "hour"  # hours
    elif diff < week:
        count = diff // day
        label = "days" if int(count) > 1 else "day"
    elif diff < month:
        count = diff // week
        label = "weeks" if int(count) > 1 else "week"
    elif diff < year:
        count = diff // month
        label = "months" if int(count) > 1 else "month"
    else:
        count = diff // year
        label = "years" if int(count) > 1 else "year"

    return "just now" if int(count) == 0 else f"{int(count)} {label}"


def timestamp_to_readable(
    timestamp: Union[int, float], time_format: TIME_FORMAT = "locale"
) -> str:
    """
    Converts a Unix timestamp into a more readable format based on the specified `time_format`.
    The function supports converting the timestamp into either a localized datetime string or a concise
    human-readable time difference (e.g., "3 hours ago").

    :param timestamp: The Unix timestamp to be converted.
    :type timestamp: Union[int, float]
    :param time_format: Determines the format of the output time. Use "concise" for a human-readable
                        time difference, or "locale" for a localized datetime string. Defaults to "locale".
    :type time_format: Literal["concise", "locale"]
    :return: A string representing the formatted time. The format is determined by the `time_format` parameter.
    :rtype: str
    """

    if timestamp and isinstance(timestamp, (int, float)):
        if time_format == "concise":
            concise_time: str = timestamp_to_concise(timestamp=int(timestamp))
            return f"{concise_time} ago"
        elif time_format == "locale":
            return timestamp_to_locale(timestamp=timestamp)


# -------------------------------- END ----------------------------------------- #
