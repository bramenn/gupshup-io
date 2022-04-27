from ..util import ExtensibleEnum, Obj, Serializable, SerializableAttrs, deserializer, field

TEXT_MESSAGE_TYPES = "text"
MEDIA_MESSAGE_TYPES = ("Image", "video", "audio", "file")


class MessageType(ExtensibleEnum):
    """A message type."""

    TEXT: "MessageType" = "text"
    IMAGE: "MessageType" = "Image"
    CONTACT: "MessageType" = "m.contact"
    VIDEO: "MessageType" = "video"
    AUDIO: "MessageType" = "audio"
    FILE: "MessageType" = "file"
    LOCATION: "MessageType" = "m.location"
    BUTTON_REPLY: "MessageType" = "m.button_reply"
    LIST_REPLY: "MessageType" = "m.list_reply"

    @property
    def is_text(self) -> bool:
        return self.value in TEXT_MESSAGE_TYPES

    @property
    def is_media(self) -> bool:
        return self.value in MEDIA_MESSAGE_TYPES
