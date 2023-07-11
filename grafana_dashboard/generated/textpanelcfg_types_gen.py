# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class CodeLanguage(Enum):
    plaintext = 'plaintext'
    yaml = 'yaml'
    xml = 'xml'
    typescript = 'typescript'
    sql = 'sql'
    go = 'go'
    markdown = 'markdown'
    html = 'html'
    json = 'json'


class CodeOptions(BaseModel):
    language: CodeLanguage
    showLineNumbers: bool
    showMiniMap: bool


class TextMode(Enum):
    html = 'html'
    markdown = 'markdown'
    code = 'code'


class PanelOptions(BaseModel):
    mode: TextMode
    code: Optional[CodeOptions] = None
    content: str


class TextPanelCfg(BaseModel):
    TextMode: TextMode
    CodeLanguage: CodeLanguage
    CodeOptions: CodeOptions
    PanelOptions: PanelOptions
