from dataclasses import dataclass
from enum import Enum

from pydantic import BaseModel


class MyBaseModel(BaseModel):
    def __repr_args__(self):
        return [
            (k, _transform_repr_arg_value(v))
            for k, v in super().__repr_args__()
        ]


def _transform_repr_arg_value(v):
    # #10118
    if isinstance(v, Enum):
        return _Reprable(str(v))

    return v


@dataclass
class _Reprable:
    content: str

    def __repr__(self):
        return self.content
