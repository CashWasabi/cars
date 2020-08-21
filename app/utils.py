from datetime import datetime
from typing import Any
import json
from uuid import UUID


# This serves as addon for unserializable classes
class CustomEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        if isinstance(obj, datetime):
            # if the obj is datetime, we simply return the value of isoformat
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def json_pretty_dump(parsed: dict) -> str:
    return json.dumps(parsed, indent=2, cls=CustomEncoder)
