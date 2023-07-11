# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND
from grafana_dashboard.extracted_generated_common_models import *

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional

from grafana_dashboard.utils import MyBaseModel
from pydantic import Field, conint


class ControlsOptions(MyBaseModel):
    showZoom: Optional[bool] = Field(None, description='Zoom (upper left)')
    mouseWheelZoom: Optional[bool] = Field(None, description='let the mouse wheel zoom')
    showAttribution: Optional[bool] = Field(None, description='Lower right')
    showScale: Optional[bool] = Field(None, description='Scale options')
    showDebug: Optional[bool] = Field(None, description='Show debug')
    showMeasure: Optional[bool] = Field(None, description='Show measure')


class FrameGeometrySourceMode(Enum):
    auto = 'auto'
    geohash = 'geohash'
    coords = 'coords'
    lookup = 'lookup'


class MapViewConfig(MyBaseModel):
    id: Optional[str] = 'zero'
    lat: Optional[conint(ge=-9223372036854775808, le=9223372036854775807)] = 0
    lon: Optional[conint(ge=-9223372036854775808, le=9223372036854775807)] = 0
    zoom: Optional[conint(ge=-9223372036854775808, le=9223372036854775807)] = 1
    minZoom: Optional[int] = None
    maxZoom: Optional[int] = None
    padding: Optional[int] = None
    allLayers: Optional[bool] = True
    lastOnly: Optional[bool] = None
    layer: Optional[str] = None
    shared: Optional[bool] = None


class TooltipMode(Enum):
    none = 'none'
    details = 'details'


class MapCenterID(Enum):
    zero = 'zero'
    coords = 'coords'
    fit = 'fit'


class TooltipOptions(MyBaseModel):
    mode: TooltipMode


class FrameGeometrySource(MyBaseModel):
    mode: FrameGeometrySourceMode
    geohash: Optional[str] = Field(None, description='Field mappings')
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    wkt: Optional[str] = None
    lookup: Optional[str] = None
    gazetteer: Optional[str] = Field(None, description='Path to Gazetteer')


class MapLayerOptions(MyBaseModel):
    type: str
    name: str = Field(..., description='configured unique display name')
    config: Optional[Any] = Field(
        None, description='Custom options depending on the type'
    )
    location: Optional[FrameGeometrySource] = None
    filterData: Optional[Any] = Field(
        None,
        description='Defines a frame MatcherConfig that may filter data for the given layer',
    )
    opacity: Optional[int] = Field(
        None,
        description='Common properties:\nhttps://openlayers.org/en/latest/apidoc/module-ol_layer_Base-BaseLayer.html\nLayer opacity (0-1)',
    )
    tooltip: Optional[bool] = Field(
        None, description='Check tooltip (defaults to true)'
    )


class PanelOptions(MyBaseModel):
    view: MapViewConfig
    controls: ControlsOptions
    basemap: MapLayerOptions
    layers: List[MapLayerOptions]
    tooltip: TooltipOptions


class GeomapPanelCfg(MyBaseModel):
    PanelOptions: PanelOptions
    MapViewConfig: MapViewConfig
    ControlsOptions: ControlsOptions
    TooltipOptions: TooltipOptions
    TooltipMode: TooltipMode
    MapCenterID: MapCenterID
