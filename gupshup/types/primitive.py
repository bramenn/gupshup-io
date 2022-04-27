from typing import Dict, List, NewType, Union

AppName = NewType("AppName", str)
AppName.__doc__ = "A Gupshup application name."

JSON = NewType("JSON", Union[str, int, float, bool, None, Dict[str, "JSON"], List["JSON"]])
JSON.__doc__ = "A union type that covers all JSON-serializable data."
