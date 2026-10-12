"""Auto-generated function_response models from OpenAPI spec. DO NOT EDIT MANUALLY."""
from __future__ import annotations

from typing import Any, Literal, Optional

from pydantic import Field

from ._core import CriblModel

class FunctionAggregateMetrics(CriblModel):

    id: Literal["aggregate_metrics"] = "aggregate_metrics"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionAggregation(CriblModel):

    id: Literal["aggregation"] = "aggregation"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionAutoTimestamp(CriblModel):

    id: Literal["auto_timestamp"] = "auto_timestamp"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionCef(CriblModel):

    id: Literal["cef"] = "cef"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionChain(CriblModel):

    id: Literal["chain"] = "chain"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionClone(CriblModel):

    id: Literal["clone"] = "clone"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionCloudChangeEnricher(CriblModel):

    id: Literal["cloudChangeEnricher"] = "cloudChangeEnricher"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionCode(CriblModel):

    id: Literal["code"] = "code"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionComment(CriblModel):

    id: Literal["comment"] = "comment"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionDetectionRules(CriblModel):

    id: Literal["detection_rules"] = "detection_rules"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionDistinct(CriblModel):

    id: Literal["distinct"] = "distinct"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionDnsLookup(CriblModel):

    id: Literal["dns_lookup"] = "dns_lookup"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionDrop(CriblModel):

    id: Literal["drop"] = "drop"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionDropDimensions(CriblModel):

    id: Literal["drop_dimensions"] = "drop_dimensions"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionDynamicSampling(CriblModel):

    id: Literal["dynamic_sampling"] = "dynamic_sampling"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionEval(CriblModel):

    id: Literal["eval"] = "eval"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionEventBreaker(CriblModel):

    id: Literal["event_breaker"] = "event_breaker"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionEventstats(CriblModel):

    id: Literal["eventstats"] = "eventstats"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionExternaldata(CriblModel):

    id: Literal["externaldata"] = "externaldata"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionFlatten(CriblModel):

    id: Literal["flatten"] = "flatten"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionFoldkeys(CriblModel):

    id: Literal["foldkeys"] = "foldkeys"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionGenStats(CriblModel):

    id: Literal["gen_stats"] = "gen_stats"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionGeoip(CriblModel):

    id: Literal["geoip"] = "geoip"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionGrok(CriblModel):

    id: Literal["grok"] = "grok"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionHandlebars(CriblModel):

    id: Literal["handlebars"] = "handlebars"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionJoin(CriblModel):

    id: Literal["join"] = "join"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionJsonUnroll(CriblModel):

    id: Literal["json_unroll"] = "json_unroll"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionLakeExport(CriblModel):

    id: Literal["lake_export"] = "lake_export"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionLakehouseEngineMetricsNormalizer(CriblModel):

    id: Literal["lakehouse_engine_metrics_normalizer"] = "lakehouse_engine_metrics_normalizer"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionLimit(CriblModel):

    id: Literal["limit"] = "limit"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionLocalSearchDatatypeParser(CriblModel):

    id: Literal["local_search_datatype_parser"] = "local_search_datatype_parser"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionLocalSearchDatatypeSchemaMapper(CriblModel):

    id: Literal["local_search_datatype_schema_mapper"] = "local_search_datatype_schema_mapper"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionLocalSearchRulesetRunner(CriblModel):

    id: Literal["local_search_ruleset_runner"] = "local_search_ruleset_runner"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionLocalSearchSchemaMapper(CriblModel):

    id: Literal["local_search_schema_mapper"] = "local_search_schema_mapper"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionLocalSearchTimeRangeNormalizer(CriblModel):

    id: Literal["local_search_time_range_normalizer"] = "local_search_time_range_normalizer"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionLocalSearchTransformer(CriblModel):

    id: Literal["local_search_transformer"] = "local_search_transformer"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionLookup(CriblModel):

    id: Literal["lookup"] = "lookup"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionMask(CriblModel):

    id: Literal["mask"] = "mask"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionMetricsExport(CriblModel):

    id: Literal["metrics_export"] = "metrics_export"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionMetricsTimeRangeGate(CriblModel):

    id: Literal["metrics_time_range_gate"] = "metrics_time_range_gate"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionMvExpand(CriblModel):

    id: Literal["mv_expand"] = "mv_expand"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionMvPull(CriblModel):

    id: Literal["mv_pull"] = "mv_pull"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionNotificationPolicies(CriblModel):

    id: Literal["notification_policies"] = "notification_policies"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionNotifications(CriblModel):

    id: Literal["notifications"] = "notifications"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionNotify(CriblModel):

    id: Literal["notify"] = "notify"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionNumerify(CriblModel):

    id: Literal["numerify"] = "numerify"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionOtlpLogs(CriblModel):

    id: Literal["otlp_logs"] = "otlp_logs"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionOtlpMetrics(CriblModel):

    id: Literal["otlp_metrics"] = "otlp_metrics"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionOtlpTraces(CriblModel):

    id: Literal["otlp_traces"] = "otlp_traces"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionPack(CriblModel):

    id: Literal["pack"] = "pack"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionPivot(CriblModel):

    id: Literal["pivot"] = "pivot"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionPublishMetrics(CriblModel):

    id: Literal["publish_metrics"] = "publish_metrics"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionRedis(CriblModel):

    id: Literal["redis"] = "redis"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionRegexExtract(CriblModel):

    id: Literal["regex_extract"] = "regex_extract"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionRegexFilter(CriblModel):

    id: Literal["regex_filter"] = "regex_filter"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionRename(CriblModel):

    id: Literal["rename"] = "rename"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionRollupMetrics(CriblModel):

    id: Literal["rollup_metrics"] = "rollup_metrics"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionSampling(CriblModel):

    id: Literal["sampling"] = "sampling"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionSearchEngineExport(CriblModel):

    id: Literal["search_engine_export"] = "search_engine_export"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionSend(CriblModel):

    id: Literal["send"] = "send"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionSensitiveDataScanner(CriblModel):

    id: Literal["sensitive_data_scanner"] = "sensitive_data_scanner"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionSerde(CriblModel):

    id: Literal["serde"] = "serde"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionSerialize(CriblModel):

    id: Literal["serialize"] = "serialize"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionSidlookup(CriblModel):

    id: Literal["sidlookup"] = "sidlookup"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionSnmpTrapSerialize(CriblModel):

    id: Literal["snmp_trap_serialize"] = "snmp_trap_serialize"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionSort(CriblModel):

    id: Literal["sort"] = "sort"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionStore(CriblModel):

    id: Literal["store"] = "store"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionSuppress(CriblModel):

    id: Literal["suppress"] = "suppress"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionTee(CriblModel):

    id: Literal["tee"] = "tee"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionTrimTimestamp(CriblModel):

    id: Literal["trim_timestamp"] = "trim_timestamp"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionUnion(CriblModel):

    id: Literal["union"] = "union"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionUnroll(CriblModel):

    id: Literal["unroll"] = "unroll"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionWindow(CriblModel):

    id: Literal["window"] = "window"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")


class FunctionXmlUnroll(CriblModel):

    id: Literal["xml_unroll"] = "xml_unroll"
    xfilename: str = Field(..., alias="__filename", description="Path to the JavaScript file that implements the Function.")
    asyncTimeout: Optional[float] = Field(None, description="Maximum time, in milliseconds, that the Function is allowed to run asynchronously before timing out.")
    cribl_version: Optional[str] = Field(None, description="Minimum Cribl version required by the Function, if applicable.")
    disabled: Optional[bool] = Field(None, description="If true, the Function is disabled and will not execute in a Pipeline. Otherwise, false.")
    group: str = Field(..., description="Category group the Function belongs to.")
    handleSignals: Optional[bool] = Field(None, description="If true, the Function handles stream signals such as flush and close. Otherwise, false.")
    loadTime: float = Field(..., description="Time the Function module was loaded, in milliseconds since the Unix epoch.")
    modTime: float = Field(..., description="Time the Function module was last modified, in milliseconds since the Unix epoch.")
    name: str = Field(..., description="Display name of the Function.")
    sync: Optional[bool] = Field(None, description="If true, the Function executes synchronously. Otherwise, false.")
    uischema: dict[str, Any] = Field(..., description="UI Schema that controls how the Function's configuration form is rendered.")
    version: str = Field(..., description="Version string of the Function.")
    schema_: Optional[dict[str, Any]] = Field(None, alias="schema", description="JSON Schema document that describes the Function configuration.")

# --- Discriminated Union ---

from typing import Annotated, Union
from pydantic import Discriminator, Tag

FunctionResponse = Annotated[
    Union[
        Annotated[FunctionAggregateMetrics, Tag("aggregate_metrics")],
        Annotated[FunctionAggregation, Tag("aggregation")],
        Annotated[FunctionAutoTimestamp, Tag("auto_timestamp")],
        Annotated[FunctionCef, Tag("cef")],
        Annotated[FunctionChain, Tag("chain")],
        Annotated[FunctionClone, Tag("clone")],
        Annotated[FunctionCloudChangeEnricher, Tag("cloudChangeEnricher")],
        Annotated[FunctionCode, Tag("code")],
        Annotated[FunctionComment, Tag("comment")],
        Annotated[FunctionDetectionRules, Tag("detection_rules")],
        Annotated[FunctionDistinct, Tag("distinct")],
        Annotated[FunctionDnsLookup, Tag("dns_lookup")],
        Annotated[FunctionDrop, Tag("drop")],
        Annotated[FunctionDropDimensions, Tag("drop_dimensions")],
        Annotated[FunctionDynamicSampling, Tag("dynamic_sampling")],
        Annotated[FunctionEval, Tag("eval")],
        Annotated[FunctionEventBreaker, Tag("event_breaker")],
        Annotated[FunctionEventstats, Tag("eventstats")],
        Annotated[FunctionExternaldata, Tag("externaldata")],
        Annotated[FunctionFlatten, Tag("flatten")],
        Annotated[FunctionFoldkeys, Tag("foldkeys")],
        Annotated[FunctionGenStats, Tag("gen_stats")],
        Annotated[FunctionGeoip, Tag("geoip")],
        Annotated[FunctionGrok, Tag("grok")],
        Annotated[FunctionHandlebars, Tag("handlebars")],
        Annotated[FunctionJoin, Tag("join")],
        Annotated[FunctionJsonUnroll, Tag("json_unroll")],
        Annotated[FunctionLakeExport, Tag("lake_export")],
        Annotated[FunctionLakehouseEngineMetricsNormalizer, Tag("lakehouse_engine_metrics_normalizer")],
        Annotated[FunctionLimit, Tag("limit")],
        Annotated[FunctionLocalSearchDatatypeParser, Tag("local_search_datatype_parser")],
        Annotated[FunctionLocalSearchDatatypeSchemaMapper, Tag("local_search_datatype_schema_mapper")],
        Annotated[FunctionLocalSearchRulesetRunner, Tag("local_search_ruleset_runner")],
        Annotated[FunctionLocalSearchSchemaMapper, Tag("local_search_schema_mapper")],
        Annotated[FunctionLocalSearchTimeRangeNormalizer, Tag("local_search_time_range_normalizer")],
        Annotated[FunctionLocalSearchTransformer, Tag("local_search_transformer")],
        Annotated[FunctionLookup, Tag("lookup")],
        Annotated[FunctionMask, Tag("mask")],
        Annotated[FunctionMetricsExport, Tag("metrics_export")],
        Annotated[FunctionMetricsTimeRangeGate, Tag("metrics_time_range_gate")],
        Annotated[FunctionMvExpand, Tag("mv_expand")],
        Annotated[FunctionMvPull, Tag("mv_pull")],
        Annotated[FunctionNotificationPolicies, Tag("notification_policies")],
        Annotated[FunctionNotifications, Tag("notifications")],
        Annotated[FunctionNotify, Tag("notify")],
        Annotated[FunctionNumerify, Tag("numerify")],
        Annotated[FunctionOtlpLogs, Tag("otlp_logs")],
        Annotated[FunctionOtlpMetrics, Tag("otlp_metrics")],
        Annotated[FunctionOtlpTraces, Tag("otlp_traces")],
        Annotated[FunctionPack, Tag("pack")],
        Annotated[FunctionPivot, Tag("pivot")],
        Annotated[FunctionPublishMetrics, Tag("publish_metrics")],
        Annotated[FunctionRedis, Tag("redis")],
        Annotated[FunctionRegexExtract, Tag("regex_extract")],
        Annotated[FunctionRegexFilter, Tag("regex_filter")],
        Annotated[FunctionRename, Tag("rename")],
        Annotated[FunctionRollupMetrics, Tag("rollup_metrics")],
        Annotated[FunctionSampling, Tag("sampling")],
        Annotated[FunctionSearchEngineExport, Tag("search_engine_export")],
        Annotated[FunctionSend, Tag("send")],
        Annotated[FunctionSensitiveDataScanner, Tag("sensitive_data_scanner")],
        Annotated[FunctionSerde, Tag("serde")],
        Annotated[FunctionSerialize, Tag("serialize")],
        Annotated[FunctionSidlookup, Tag("sidlookup")],
        Annotated[FunctionSnmpTrapSerialize, Tag("snmp_trap_serialize")],
        Annotated[FunctionSort, Tag("sort")],
        Annotated[FunctionStore, Tag("store")],
        Annotated[FunctionSuppress, Tag("suppress")],
        Annotated[FunctionTee, Tag("tee")],
        Annotated[FunctionTrimTimestamp, Tag("trim_timestamp")],
        Annotated[FunctionUnion, Tag("union")],
        Annotated[FunctionUnroll, Tag("unroll")],
        Annotated[FunctionWindow, Tag("window")],
        Annotated[FunctionXmlUnroll, Tag("xml_unroll")],
    ],
    Discriminator("id"),
]
