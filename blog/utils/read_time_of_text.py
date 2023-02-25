import math


def read_time(content: str) -> int:
    result = len(content.split()) / 200
    return math.ceil(result)
