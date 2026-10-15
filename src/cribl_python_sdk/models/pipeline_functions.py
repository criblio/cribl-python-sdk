"""Auto-generated pipeline_function models from OpenAPI spec. DO NOT EDIT MANUALLY."""
from __future__ import annotations

from typing import Any, Literal, Optional

from pydantic import Field

from ._core import CriblModel
from .nested import (
    FunctionConfSchemaAggregateMetrics,
    FunctionConfSchemaAggregation,
    FunctionConfSchemaAutoTimestamp,
    FunctionConfSchemaCef,
    FunctionConfSchemaChain,
    FunctionConfSchemaClone,
    FunctionConfSchemaCode,
    FunctionConfSchemaComment,
    FunctionConfSchemaDetectionRules,
    FunctionConfSchemaDistinct,
    FunctionConfSchemaDnsLookup,
    FunctionConfSchemaDropDimensions,
    FunctionConfSchemaDynamicSampling,
    FunctionConfSchemaEval,
    FunctionConfSchemaEventBreaker,
    FunctionConfSchemaEventstats,
    FunctionConfSchemaFlatten,
    FunctionConfSchemaFoldkeys,
    FunctionConfSchemaGenStats,
    FunctionConfSchemaGeoip,
    FunctionConfSchemaGrok,
    FunctionConfSchemaHandlebars,
    FunctionConfSchemaJoin,
    FunctionConfSchemaJsonUnroll,
    FunctionConfSchemaLakeExport,
    FunctionConfSchemaLimit,
    FunctionConfSchemaLocalSearchRulesetRunner,
    FunctionConfSchemaLookup,
    FunctionConfSchemaMask,
    FunctionConfSchemaMetricsExport,
    FunctionConfSchemaMvExpand,
    FunctionConfSchemaMvPull,
    FunctionConfSchemaNotificationPolicies,
    FunctionConfSchemaNotifications,
    FunctionConfSchemaNotify,
    FunctionConfSchemaNumerify,
    FunctionConfSchemaOtlpLogs,
    FunctionConfSchemaOtlpMetrics,
    FunctionConfSchemaOtlpTraces,
    FunctionConfSchemaPack,
    FunctionConfSchemaPivot,
    FunctionConfSchemaPublishMetrics,
    FunctionConfSchemaRedis,
    FunctionConfSchemaRegexExtract,
    FunctionConfSchemaRegexFilter,
    FunctionConfSchemaRename,
    FunctionConfSchemaRollupMetrics,
    FunctionConfSchemaSampling,
    FunctionConfSchemaSearchEngineExport,
    FunctionConfSchemaSend,
    FunctionConfSchemaSensitiveDataScanner,
    FunctionConfSchemaSerde,
    FunctionConfSchemaSerialize,
    FunctionConfSchemaSidlookup,
    FunctionConfSchemaSnmpTrapSerialize,
    FunctionConfSchemaSort,
    FunctionConfSchemaStore,
    FunctionConfSchemaSuppress,
    FunctionConfSchemaTee,
    FunctionConfSchemaTrimTimestamp,
    FunctionConfSchemaUnion,
    FunctionConfSchemaUnroll,
    FunctionConfSchemaWindow,
    FunctionConfSchemaXmlUnroll,
)

class PipelineFunctionAggregateMetrics(CriblModel):

    id: Literal["aggregate_metrics"] = "aggregate_metrics"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaAggregateMetrics = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionAggregation(CriblModel):

    id: Literal["aggregation"] = "aggregation"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaAggregation = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionAutoTimestamp(CriblModel):

    id: Literal["auto_timestamp"] = "auto_timestamp"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaAutoTimestamp = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionCef(CriblModel):

    id: Literal["cef"] = "cef"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaCef = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionChain(CriblModel):

    id: Literal["chain"] = "chain"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaChain = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionClone(CriblModel):

    id: Literal["clone"] = "clone"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaClone = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionCloudChangeEnricher(CriblModel):

    id: Literal["cloudChangeEnricher"] = "cloudChangeEnricher"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: Any = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionCode(CriblModel):

    id: Literal["code"] = "code"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaCode = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionComment(CriblModel):

    id: Literal["comment"] = "comment"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaComment = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionDetectionRules(CriblModel):

    id: Literal["detection_rules"] = "detection_rules"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaDetectionRules = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionDistinct(CriblModel):

    id: Literal["distinct"] = "distinct"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaDistinct = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionDnsLookup(CriblModel):

    id: Literal["dns_lookup"] = "dns_lookup"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaDnsLookup = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionDrop(CriblModel):

    id: Literal["drop"] = "drop"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: Any = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionDropDimensions(CriblModel):

    id: Literal["drop_dimensions"] = "drop_dimensions"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaDropDimensions = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionDynamicSampling(CriblModel):

    id: Literal["dynamic_sampling"] = "dynamic_sampling"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaDynamicSampling = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionEval(CriblModel):

    id: Literal["eval"] = "eval"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaEval = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionEventBreaker(CriblModel):

    id: Literal["event_breaker"] = "event_breaker"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaEventBreaker = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionEventstats(CriblModel):

    id: Literal["eventstats"] = "eventstats"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaEventstats = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionExternaldata(CriblModel):

    id: Literal["externaldata"] = "externaldata"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: Any = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionFlatten(CriblModel):

    id: Literal["flatten"] = "flatten"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaFlatten = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionFoldkeys(CriblModel):

    id: Literal["foldkeys"] = "foldkeys"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaFoldkeys = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionGenStats(CriblModel):

    id: Literal["gen_stats"] = "gen_stats"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaGenStats = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionGeoip(CriblModel):

    id: Literal["geoip"] = "geoip"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaGeoip = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionGrok(CriblModel):

    id: Literal["grok"] = "grok"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaGrok = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionHandlebars(CriblModel):

    id: Literal["handlebars"] = "handlebars"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaHandlebars = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionJoin(CriblModel):

    id: Literal["join"] = "join"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaJoin = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionJsonUnroll(CriblModel):

    id: Literal["json_unroll"] = "json_unroll"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaJsonUnroll = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionLakeExport(CriblModel):

    id: Literal["lake_export"] = "lake_export"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaLakeExport = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionLakehouseEngineMetricsNormalizer(CriblModel):

    id: Literal["lakehouse_engine_metrics_normalizer"] = "lakehouse_engine_metrics_normalizer"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: Any = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionLimit(CriblModel):

    id: Literal["limit"] = "limit"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaLimit = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionLocalSearchDatatypeParser(CriblModel):

    id: Literal["local_search_datatype_parser"] = "local_search_datatype_parser"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: Any = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionLocalSearchDatatypeSchemaMapper(CriblModel):

    id: Literal["local_search_datatype_schema_mapper"] = "local_search_datatype_schema_mapper"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: Any = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionLocalSearchRulesetRunner(CriblModel):

    id: Literal["local_search_ruleset_runner"] = "local_search_ruleset_runner"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaLocalSearchRulesetRunner = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionLocalSearchSchemaMapper(CriblModel):

    id: Literal["local_search_schema_mapper"] = "local_search_schema_mapper"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: Any = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionLocalSearchTimeRangeNormalizer(CriblModel):

    id: Literal["local_search_time_range_normalizer"] = "local_search_time_range_normalizer"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: Any = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionLocalSearchTransformer(CriblModel):

    id: Literal["local_search_transformer"] = "local_search_transformer"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: Any = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionLookup(CriblModel):

    id: Literal["lookup"] = "lookup"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaLookup = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionMask(CriblModel):

    id: Literal["mask"] = "mask"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaMask = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionMetricsExport(CriblModel):

    id: Literal["metrics_export"] = "metrics_export"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaMetricsExport = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionMetricsTimeRangeGate(CriblModel):

    id: Literal["metrics_time_range_gate"] = "metrics_time_range_gate"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: Any = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionMvExpand(CriblModel):

    id: Literal["mv_expand"] = "mv_expand"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaMvExpand = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionMvPull(CriblModel):

    id: Literal["mv_pull"] = "mv_pull"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaMvPull = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionNotificationPolicies(CriblModel):

    id: Literal["notification_policies"] = "notification_policies"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaNotificationPolicies = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionNotifications(CriblModel):

    id: Literal["notifications"] = "notifications"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaNotifications = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionNotify(CriblModel):

    id: Literal["notify"] = "notify"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaNotify = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionNumerify(CriblModel):

    id: Literal["numerify"] = "numerify"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaNumerify = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionOtlpLogs(CriblModel):

    id: Literal["otlp_logs"] = "otlp_logs"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaOtlpLogs = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionOtlpMetrics(CriblModel):

    id: Literal["otlp_metrics"] = "otlp_metrics"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaOtlpMetrics = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionOtlpTraces(CriblModel):

    id: Literal["otlp_traces"] = "otlp_traces"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaOtlpTraces = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionPack(CriblModel):

    id: Literal["pack"] = "pack"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaPack = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionPivot(CriblModel):

    id: Literal["pivot"] = "pivot"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaPivot = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionPublishMetrics(CriblModel):

    id: Literal["publish_metrics"] = "publish_metrics"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaPublishMetrics = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionRedis(CriblModel):

    id: Literal["redis"] = "redis"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaRedis = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionRegexExtract(CriblModel):

    id: Literal["regex_extract"] = "regex_extract"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaRegexExtract = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionRegexFilter(CriblModel):

    id: Literal["regex_filter"] = "regex_filter"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaRegexFilter = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionRename(CriblModel):

    id: Literal["rename"] = "rename"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaRename = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionRollupMetrics(CriblModel):

    id: Literal["rollup_metrics"] = "rollup_metrics"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaRollupMetrics = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionSampling(CriblModel):

    id: Literal["sampling"] = "sampling"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaSampling = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionSearchEngineExport(CriblModel):

    id: Literal["search_engine_export"] = "search_engine_export"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaSearchEngineExport = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionSend(CriblModel):

    id: Literal["send"] = "send"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaSend = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionSensitiveDataScanner(CriblModel):

    id: Literal["sensitive_data_scanner"] = "sensitive_data_scanner"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaSensitiveDataScanner = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionSerde(CriblModel):

    id: Literal["serde"] = "serde"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaSerde = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionSerialize(CriblModel):

    id: Literal["serialize"] = "serialize"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaSerialize = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionSidlookup(CriblModel):

    id: Literal["sidlookup"] = "sidlookup"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaSidlookup = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionSnmpTrapSerialize(CriblModel):

    id: Literal["snmp_trap_serialize"] = "snmp_trap_serialize"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaSnmpTrapSerialize = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionSort(CriblModel):

    id: Literal["sort"] = "sort"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaSort = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionStore(CriblModel):

    id: Literal["store"] = "store"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaStore = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionSuppress(CriblModel):

    id: Literal["suppress"] = "suppress"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaSuppress = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionTee(CriblModel):

    id: Literal["tee"] = "tee"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaTee = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionTrimTimestamp(CriblModel):

    id: Literal["trim_timestamp"] = "trim_timestamp"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaTrimTimestamp = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionUnion(CriblModel):

    id: Literal["union"] = "union"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaUnion = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionUnroll(CriblModel):

    id: Literal["unroll"] = "unroll"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaUnroll = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionWindow(CriblModel):

    id: Literal["window"] = "window"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaWindow = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")


class PipelineFunctionXmlUnroll(CriblModel):

    id: Literal["xml_unroll"] = "xml_unroll"
    filter: Optional[str] = Field(default=None, description="JavaScript expression that selects data to pass through the Function.")
    description: Optional[str] = Field(default=None, description="Brief description of the Pipeline function.")
    disabled: Optional[bool] = Field(default=None, description="If true, disable the Pipeline function so that events are not passed through it. Otherwise, false.")
    final: Optional[bool] = Field(default=None, description="If true, stop passing events to downstream Pipeline Functions after the Function executes. Otherwise, false.")
    conf: FunctionConfSchemaXmlUnroll = Field(..., description="Configuration specific to the Pipeline Function.")
    groupId: Optional[str] = Field(default=None, description="Unique identifier of the group that contains the Pipeline Function.")

# --- Discriminated Union ---

from typing import Annotated, Union
from pydantic import Discriminator, Tag

PipelineFunction = Annotated[
    Union[
        Annotated[PipelineFunctionAggregateMetrics, Tag("aggregate_metrics")],
        Annotated[PipelineFunctionAggregation, Tag("aggregation")],
        Annotated[PipelineFunctionAutoTimestamp, Tag("auto_timestamp")],
        Annotated[PipelineFunctionCef, Tag("cef")],
        Annotated[PipelineFunctionChain, Tag("chain")],
        Annotated[PipelineFunctionClone, Tag("clone")],
        Annotated[PipelineFunctionCloudChangeEnricher, Tag("cloudChangeEnricher")],
        Annotated[PipelineFunctionCode, Tag("code")],
        Annotated[PipelineFunctionComment, Tag("comment")],
        Annotated[PipelineFunctionDetectionRules, Tag("detection_rules")],
        Annotated[PipelineFunctionDistinct, Tag("distinct")],
        Annotated[PipelineFunctionDnsLookup, Tag("dns_lookup")],
        Annotated[PipelineFunctionDrop, Tag("drop")],
        Annotated[PipelineFunctionDropDimensions, Tag("drop_dimensions")],
        Annotated[PipelineFunctionDynamicSampling, Tag("dynamic_sampling")],
        Annotated[PipelineFunctionEval, Tag("eval")],
        Annotated[PipelineFunctionEventBreaker, Tag("event_breaker")],
        Annotated[PipelineFunctionEventstats, Tag("eventstats")],
        Annotated[PipelineFunctionExternaldata, Tag("externaldata")],
        Annotated[PipelineFunctionFlatten, Tag("flatten")],
        Annotated[PipelineFunctionFoldkeys, Tag("foldkeys")],
        Annotated[PipelineFunctionGenStats, Tag("gen_stats")],
        Annotated[PipelineFunctionGeoip, Tag("geoip")],
        Annotated[PipelineFunctionGrok, Tag("grok")],
        Annotated[PipelineFunctionHandlebars, Tag("handlebars")],
        Annotated[PipelineFunctionJoin, Tag("join")],
        Annotated[PipelineFunctionJsonUnroll, Tag("json_unroll")],
        Annotated[PipelineFunctionLakeExport, Tag("lake_export")],
        Annotated[PipelineFunctionLakehouseEngineMetricsNormalizer, Tag("lakehouse_engine_metrics_normalizer")],
        Annotated[PipelineFunctionLimit, Tag("limit")],
        Annotated[PipelineFunctionLocalSearchDatatypeParser, Tag("local_search_datatype_parser")],
        Annotated[PipelineFunctionLocalSearchDatatypeSchemaMapper, Tag("local_search_datatype_schema_mapper")],
        Annotated[PipelineFunctionLocalSearchRulesetRunner, Tag("local_search_ruleset_runner")],
        Annotated[PipelineFunctionLocalSearchSchemaMapper, Tag("local_search_schema_mapper")],
        Annotated[PipelineFunctionLocalSearchTimeRangeNormalizer, Tag("local_search_time_range_normalizer")],
        Annotated[PipelineFunctionLocalSearchTransformer, Tag("local_search_transformer")],
        Annotated[PipelineFunctionLookup, Tag("lookup")],
        Annotated[PipelineFunctionMask, Tag("mask")],
        Annotated[PipelineFunctionMetricsExport, Tag("metrics_export")],
        Annotated[PipelineFunctionMetricsTimeRangeGate, Tag("metrics_time_range_gate")],
        Annotated[PipelineFunctionMvExpand, Tag("mv_expand")],
        Annotated[PipelineFunctionMvPull, Tag("mv_pull")],
        Annotated[PipelineFunctionNotificationPolicies, Tag("notification_policies")],
        Annotated[PipelineFunctionNotifications, Tag("notifications")],
        Annotated[PipelineFunctionNotify, Tag("notify")],
        Annotated[PipelineFunctionNumerify, Tag("numerify")],
        Annotated[PipelineFunctionOtlpLogs, Tag("otlp_logs")],
        Annotated[PipelineFunctionOtlpMetrics, Tag("otlp_metrics")],
        Annotated[PipelineFunctionOtlpTraces, Tag("otlp_traces")],
        Annotated[PipelineFunctionPack, Tag("pack")],
        Annotated[PipelineFunctionPivot, Tag("pivot")],
        Annotated[PipelineFunctionPublishMetrics, Tag("publish_metrics")],
        Annotated[PipelineFunctionRedis, Tag("redis")],
        Annotated[PipelineFunctionRegexExtract, Tag("regex_extract")],
        Annotated[PipelineFunctionRegexFilter, Tag("regex_filter")],
        Annotated[PipelineFunctionRename, Tag("rename")],
        Annotated[PipelineFunctionRollupMetrics, Tag("rollup_metrics")],
        Annotated[PipelineFunctionSampling, Tag("sampling")],
        Annotated[PipelineFunctionSearchEngineExport, Tag("search_engine_export")],
        Annotated[PipelineFunctionSend, Tag("send")],
        Annotated[PipelineFunctionSensitiveDataScanner, Tag("sensitive_data_scanner")],
        Annotated[PipelineFunctionSerde, Tag("serde")],
        Annotated[PipelineFunctionSerialize, Tag("serialize")],
        Annotated[PipelineFunctionSidlookup, Tag("sidlookup")],
        Annotated[PipelineFunctionSnmpTrapSerialize, Tag("snmp_trap_serialize")],
        Annotated[PipelineFunctionSort, Tag("sort")],
        Annotated[PipelineFunctionStore, Tag("store")],
        Annotated[PipelineFunctionSuppress, Tag("suppress")],
        Annotated[PipelineFunctionTee, Tag("tee")],
        Annotated[PipelineFunctionTrimTimestamp, Tag("trim_timestamp")],
        Annotated[PipelineFunctionUnion, Tag("union")],
        Annotated[PipelineFunctionUnroll, Tag("unroll")],
        Annotated[PipelineFunctionWindow, Tag("window")],
        Annotated[PipelineFunctionXmlUnroll, Tag("xml_unroll")],
    ],
    Discriminator("id"),
]
