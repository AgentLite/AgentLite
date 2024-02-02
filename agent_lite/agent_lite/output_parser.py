import json

class OutputParserError(Exception):
    pass

def parse_json(text):
    text = text.strip()

    left_square = text.find("[")
    left_brace = text.find("{")

    if left_square < left_brace and left_square != -1:
        left = left_square
        right = text.rfind("]")
    else:
        left = left_brace
        right = text.rfind("}")

    json_text = text[left:right + 1]
    try:
        # Single JSON object case
        if left_square == -1:
            return [json.loads(json_text)]
        # Multiple JSON object case
        return json.loads(json_text)
    except json.JSONDecodeError:
        raise OutputParserError("Not a json markdown", {'output': text})
