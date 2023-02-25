import readtime


def read_time(content: str):
    result = readtime.of_markdown(content)
    return result
