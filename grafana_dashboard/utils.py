from dataclasses import dataclass
from enum import Enum

from pydantic import BaseModel, Extra


class MyBaseModel(BaseModel):
    def __repr_args__(self):
        return [
            (k, _repr_transform_arg_value(v))
            for k, v in super().__repr_args__()
            if _repr_should_keep_arg(self.__class__, k, v)
        ]

    class Config:
        extra = Extra.forbid


def _repr_transform_arg_value(v):
    # #10118
    if isinstance(v, Enum):
        return _Reprable(str(v))

    return v


def _repr_should_keep_arg(cls, k: str, v):
    # https://github.com/fzyzcjy/yplusplus/issues/10117#issuecomment-1630217216
    if v is None:
        return False

    info = cls.schema()['properties'].get(k)
    # print(f'hi cls={cls} k={k} v={v} info={info}')

    if info is None or 'default' not in info:
        return True

    return v != info['default']


@dataclass
class _Reprable:
    content: str

    def __repr__(self):
        return self.content
