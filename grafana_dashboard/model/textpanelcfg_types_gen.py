# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND


from enum import Enum
from typing import Optional

from grafana_dashboard.utils import MyBaseModel


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


class CodeOptions(MyBaseModel):
    language: CodeLanguage
    showLineNumbers: Optional[bool] = False
    showMiniMap: Optional[bool] = False


class TextMode(Enum):
    html = 'html'
    markdown = 'markdown'
    code = 'code'


class PanelOptions(MyBaseModel):
    mode: TextMode
    code: Optional[CodeOptions] = None
    content: Optional[
        str
    ] = '# Title\n\nFor markdown syntax help: [commonmark.org/help](https://commonmark.org/help/)'


class TextPanelCfg(MyBaseModel):
    TextMode: TextMode
    CodeLanguage: Optional[CodeLanguage] = 'plaintext'
    CodeOptions: CodeOptions
    PanelOptions: PanelOptions
