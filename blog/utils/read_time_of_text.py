import math

def read_time(content: str):
    result = len(content.split()) / 200
    return math.ceil(result)
