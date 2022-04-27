from attr import dataclass

from ..primitive import AppName
from ..util import Obj
from .type import EventType


@dataclass
class BaseEvent:
    """Base event class. The only things an event **must** have are content and event type."""

    app: AppName
    timestamp: int
    version: int
    type: EventType
    payload: Obj
