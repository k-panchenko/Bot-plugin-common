from dataclasses import dataclass

from bot_plugin.domain.base.serializable import JsonSerializable


@dataclass
class UnplugRequest(JsonSerializable):
    url: str

