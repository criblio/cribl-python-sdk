"""Auto-generated nested object models from OpenAPI spec. DO NOT EDIT MANUALLY."""
from __future__ import annotations

from typing import Any, Literal, Optional

from pydantic import Field

from ._core import CriblModel
from ._core import (
    HecTokenMetadataParam,
    TlsSettingsClient,
)

class AuthTokenConfInputCriblTcp(CriblModel):

    tokenSecret: str = Field(..., description="Select or create a stored text secret")
    enabled: Optional[bool] = Field(None, description="Enable token")
    description: Optional[str] = Field(None, description="Optional token description")


class AuthTypeHttp(CriblModel):
    """Authentication settings for HTTP requests."""

    disabled: bool = Field(..., description="Whether authentication is disabled for HTTP requests.")
    username: Optional[str] = Field(None, description="Username")
    password: Optional[str] = Field(None, description="Password")
    authType: Optional[Literal['manual', 'secret', 'manualAPIKey', 'textSecret']] = Field(None, description="Enter credentials directly, or select a stored secret")
    credentialsSecret: Optional[str] = Field(None, description="Select or create a secret that references your credentials")
    manualAPIKey: Optional[str] = Field(None, description="Enter API key directly")
    textSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    xtemplate_manualAPIKey: Optional[str] = Field(None, alias="__template_manualAPIKey", description="Binds 'manualAPIKey' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'manualAPIKey' at runtime.")


class CertOptionsType(CriblModel):
    """Certificate credentials for Microsoft OAuth authentication."""

    certificateName: Optional[str] = Field(None, description="The name of the predefined certificate.")
    privKeyPath: str = Field(..., description="Path to the private key to use. Key should be in PEM format. Can reference $ENV_VARS.")
    passphrase: Optional[str] = Field(None, description="Passphrase to use to decrypt the private key.")
    certPath: str = Field(..., description="Path to the certificate to use. Certificate should be in PEM format. Can reference $ENV_VARS.")


class CertificateType(CriblModel):
    """Certificate credentials for the Azure service principal."""

    certificateName: str = Field(..., description="The certificate you registered as credentials for your app in the Azure portal")


class CheckpointingType(CriblModel):
    """Checkpoint settings used to resume processing after an interruption."""

    enabled: bool = Field(..., description="Resume processing files after an interruption")
    retries: Optional[float] = Field(None, description="The number of times to retry processing when a processing error occurs. If Skip file on error is enabled, this setting is ignored.")


class ColumnMappingConfOutputClickHouse(CriblModel):

    columnName: str = Field(..., description="Name of the column in ClickHouse that will store field value")
    columnType: Optional[str] = Field(None, description="Type of the column in the ClickHouse database")
    columnValueExpression: str = Field(..., description="JavaScript expression to compute value to be inserted into ClickHouse table")


class ConnectionConfInputCollection(CriblModel):

    pipeline: Optional[str] = Field(None, description="Pipeline or Pack to process data before sending to the Destination.")
    output: Optional[str] = Field(None, description="Destination to send data to when not using Routes.")


class DiskSpoolingType(CriblModel):
    """Disk Spooling"""

    enable: Optional[bool] = Field(None, description="Spool events on disk for Cribl Edge and Search. Default is disabled.")
    timeWindow: Optional[str] = Field(None, description="Time period for grouping spooled events. Default is 10m.")
    maxDataSize: Optional[str] = Field(None, description="Maximum disk space that can be consumed before older buckets are deleted. Examples: 420MB, 4GB. Default is 1GB.")
    maxDataTime: Optional[str] = Field(None, description="Maximum amount of time to retain data before older buckets are deleted. Examples: 2h, 4d. Default is 24h.")
    compress: Optional[Literal['none', 'gzip']] = Field(None, description="Data compression format. Default is gzip.")


class FunctionConfSchemaAggregateMetricsAddItem(CriblModel):

    name: Optional[str] = Field(None, description="Name of the field to set or add to the event.")
    value: str = Field(..., description="JavaScript expression to compute the value (can be constant)")


class FunctionConfSchemaAggregateMetricsAggregationsItem(CriblModel):

    metricType: str = Field(..., description="The output metric type")
    agg: str = Field(..., description="Aggregate function to perform on events. Example: sum(bytes).where(action=='REJECT').as(TotalBytes)")


class FunctionConfSchemaAggregationAddItem(CriblModel):

    name: Optional[str] = Field(None, description="Name of the field to set or add to the event.")
    value: str = Field(..., description="JavaScript expression to compute the value (can be constant)")


class FunctionConfSchemaAutoTimestampTimestampsItem(CriblModel):

    regex: str = Field(..., description="Regex with first capturing group matching the timestamp")
    strptime: str = Field(..., description="Select or enter strptime format for the captured timestamp")


class FunctionConfSchemaCefExtensionItem(CriblModel):

    name: str = Field(..., description="Name of the CEF extension field. Must contain only alphanumeric characters.")
    value: str = Field(..., description="JavaScript expression to compute the value (can be constant)")


class FunctionConfSchemaCefHeaderItem(CriblModel):

    name: Optional[str] = Field(None, description="Name of the CEF header field. Header names are predefined by the CEF standard.")
    value: str = Field(..., description="JavaScript expression to compute the value (can be constant)")


class FunctionConfSchemaChain(CriblModel):

    processor: Optional[str] = Field(None, description="The data processor (Pack/Pipeline) to send events through")


class FunctionConfSchemaClone(CriblModel):

    clones: Optional[list[dict[str, Any]]] = Field(None, description="Create clones with the following fields set")


class FunctionConfSchemaCode(CriblModel):

    code: Optional[str] = Field(None, description="Caution: This Function will be evaluated in an unprotected context. This means that you will be able to execute almost any JavaScript code.")
    maxNumOfIterations: Optional[float] = Field(None, description="The maximum number of allowed iterations within this Function. Defaults to 5,000.")
    activeLogSampleRate: Optional[float] = Field(None, description="Rate at which this Function logs errors. For example, a value of 1 logs every error, a value of 1000 (the default) logs every thousandth error, and so on.")
    useUniqueLogChannel: Optional[bool] = Field(None, description="Logs from this Function will be sent to a unique channel in the form `func:code:${pipelineName}:${functionIndex}`. Disable to use the generic `func:code` log channel instead.")


class FunctionConfSchemaComment(CriblModel):

    comment: Optional[str] = Field(None, description="Optional, short description of this Function's purpose in the Pipeline")


class FunctionConfSchemaDetectionRulesLocalOverridesConfFieldOverridesItem(CriblModel):

    id: str = Field(..., description="Unique identifier for the Detection Rule to override.")
    severityId: Optional[int] = Field(None, description="Severity level to assign to the Detection Rule.")
    confidenceId: Optional[int] = Field(None, description="Confidence level to assign to the Detection Rule.")
    impactId: Optional[int] = Field(None, description="Impact level to assign to the Detection Rule.")
    isAlert: Optional[bool] = Field(None, description="If true, the Detection Rule creates an alert. Otherwise, false.")
    message: Optional[str] = Field(None, description="Replacement alert message for the Detection Rule.")


class FunctionConfSchemaDetectionRulesLocalOverridesConfInlineRulesItem(CriblModel):

    id: str = Field(..., description="Unique identifier for the Detection Rule.")
    name: str = Field(..., description="Display name for the Detection Rule.")
    condition: str = Field(..., description="Expression that determines whether the Detection Rule matches an event.")
    severityId: Optional[int] = Field(None, description="Severity level for the Detection Rule.")
    confidenceId: Optional[int] = Field(None, description="Confidence level for the Detection Rule.")
    isAlert: Optional[bool] = Field(None, description="If true, the Detection Rule creates an alert. Otherwise, false.")
    message: Optional[str] = Field(None, description="Alert message emitted when the Detection Rule matches.")
    tags: Optional[list[str]] = Field(None, description="Tags for filtering and grouping detection rules.")


class FunctionConfSchemaDistinct(CriblModel):
    """distinct configuration"""

    groupBy: Optional[list[str]] = Field(None, description="Defines the properties that are concatenated to produce distinct key")
    maxCombinations: Optional[float] = Field(None, description="maximum number of tracked combinations")
    maxDepth: Optional[float] = Field(None, description="maximum number of groupBy properties")
    isFederated: Optional[bool] = Field(None, description="indicator that the operator runs on a federated executor")
    suppressPreviews: Optional[bool] = Field(None, description="Toggle this on to suppress generating previews of intermediate results")


class FunctionConfSchemaDnsLookupDnsLookupFieldsItem(CriblModel):

    inFieldName: Optional[str] = Field(None, description="Name of the field containing the hostname or IP address to look up.")
    resourceRecordType: Optional[str] = Field(None, description="The DNS record type (RR) to return. Defaults to 'A'.")
    outFieldName: Optional[str] = Field(None, description="Name of field to add lookup results to. Leave blank to overwrite the lookup field.")


class FunctionConfSchemaDnsLookupReverseLookupFieldsItem(CriblModel):

    inFieldName: Optional[str] = Field(None, description="Name of the field containing the IP to look up. If the field value is not in IPv4 or IPv6 format, the lookup is skipped.")
    outFieldName: Optional[str] = Field(None, description="Name of field to add the resolved domain to. Leave blank to overwrite the lookup field.")


class FunctionConfSchemaDropDimensions(CriblModel):

    timeWindow: Optional[str] = Field(None, description="The time span of the tumbling window for aggregating events. Must be a valid time string (such as 10s).")
    dropDimensions: Optional[list[str]] = Field(None, description="One or more dimensions to be dropped. Supports wildcard expressions. Warning: Using wildcard '*' causes all dimensions in the event to be dropped.")
    flushOnInputClose: Optional[bool] = Field(None, description="Flush aggregations when an input stream is closed. If disabled, aggregations are flushed based on Time Window Settings instead.")


class FunctionConfSchemaDynamicSampling(CriblModel):

    # values: log=Logarithmic, sqrt=Square Root
    mode: Optional[str] = Field(None, description="Defines how sample rate will be derived: log(previousPeriodCount) or sqrt(previousPeriodCount)")
    keyExpr: Optional[str] = Field(None, description="Expression used to derive sample group key. Example:`${domain}:${status}`. Each sample group will have its own derived sampling rate based on volume. Defaults to `${host}`.")
    samplePeriod: Optional[float] = Field(None, description="How often (in seconds) sample rates will be adjusted")
    minEvents: Optional[float] = Field(None, description="Minimum number of events that must be received in previous sample period for sampling mode to be applied to current period. If the number of events received for a sample group is less than this minimum, a sample rate of 1:1 is used.")
    maxSampleRate: Optional[float] = Field(None, description="Maximum sampling rate. If computed sampling rate is above this value, it will be limited to this value.")


class FunctionConfSchemaEvalAddItem(CriblModel):

    name: Optional[str] = Field(None, description="Name of the field to set or add to the event.")
    value: str = Field(..., description="JavaScript expression to compute the value (can be constant)")
    disabled: Optional[bool] = Field(None, description="Set to No to disable the evaluation of an individual expression")


class FunctionConfSchemaEventstats(CriblModel):
    """eventstats configuration"""

    aggregations: Optional[list[str]] = Field(None, description="Aggregate function(s) to perform on events. E.g., sum(bytes).where(action=='REJECT').as(TotalBytes)")
    groupBys: Optional[list[str]] = Field(None, description="Fields to group aggregates by, supports wildcard expressions.")
    maxEvents: Optional[float] = Field(None, description="Specifies how many events are at max kept in memory to be enriched with aggregations")
    flushOnInputClose: Optional[bool] = Field(None, description="Determines if aggregations should flush when an input stream is closed. If disabled, time window settings will control flush behavior.")


class FunctionConfSchemaFlatten(CriblModel):

    fields: Optional[list[str]] = Field(None, description="List of top-level fields to include for flattening. Supports * wildcards, except when used on internal fields. Defaults to empty array, which means all fields.")
    prefix: Optional[str] = Field(None, description="Prefix string for flattened field names. Defaults to empty.")
    depth: Optional[float] = Field(None, description="Number representing the nested levels to consider for flattening. Defaults to 5. Minimum should be 1.")
    delimiter: Optional[str] = Field(None, description="Delimiter to be used for flattening. Defaults to underscore.")


class FunctionConfSchemaFoldkeys(CriblModel):

    deleteOriginal: Optional[bool] = Field(None, description="When enabled (default), only the folded keys are kept. When disabled, the original entries are retained alongside the folded keys.")
    separator: Optional[str] = Field(None, description="Character or string used to separate key levels to be folded. Defaults to the dot (.) character.")
    selectionRegExp: Optional[str] = Field(None, description="Optional regular expression to select a subset of the keys to fold.")
    maxDepth: Optional[int] = Field(None, description="Maximum recursion depth when traversing nested objects. Prevents infinite loops caused by cyclic references. Defaults to 20.")


class FunctionConfSchemaGenStats(CriblModel):
    """Gen stats configuration"""

    fields: Optional[list[str]] = Field(None, description="List of field names from which to generate statistics.")


class FunctionConfSchemaGeoipAdditionalFieldsItem(CriblModel):

    extraInField: str = Field(..., description="Field name in which to find an IP to look up. Can be nested.")
    extraOutField: str = Field(..., description="Field name in which to store the GeoIP lookup results")


class FunctionConfSchemaHandlebarsTemplatesItem(CriblModel):
    """Template definition"""

    id: str = Field(..., description="Unique identifier for this template")
    content: str = Field(..., description="Handlebars template string")
    description: Optional[str] = Field(None, description="Optional description of what this template is used for")
    type: str = Field(..., description="Type categorization for the template (e.g., Universal, Email, Slack)")


class FunctionConfSchemaJoinFieldConditionsItem(CriblModel):

    leftFieldName: str = Field(..., description="The field name to join on, on the left side.")
    rightFieldName: str = Field(..., description="The field name on the right side of the data, i.e. the stage results, that we are joining with")


class FunctionConfSchemaJsonUnroll(CriblModel):

    path: Optional[str] = Field(None, description="Path to array to unroll, such as foo.0.bar")
    name: Optional[str] = Field(None, description="Name of each exploded array element in each new event. Leave empty to expand the array element with its original name.")


class FunctionConfSchemaLakeExport(CriblModel):
    """Lake export Configuration"""

    searchJobId: Optional[str] = Field(None, description="Id of the search job this function is running on.")
    dataset: Optional[str] = Field(None, description="Name of the dataset")
    lake: Optional[str] = Field(None, description="Name of the lake")
    tee: Optional[bool] = Field(None, description="Tee results to search. When set to true results will be shipped instead of stats")
    flushMs: Optional[float] = Field(None, description="How often are stats flushed in ms")
    suppressPreviews: Optional[bool] = Field(None, description="Disables generation of intermediate stats. When true stats will be emitted only on end")


class FunctionConfSchemaLimit(CriblModel):

    limit: Optional[int] = Field(None, description="Number of qualifying events to pass through")


class FunctionConfSchemaLocalSearchRulesetRunner(CriblModel):

    rulesetType: Optional[str] = Field(None, description="Type of ruleset to apply: dataset or datatype.")
    rulesetId: Optional[str] = Field(None, description="ID of the ruleset to apply.")
    ruleset: Optional[dict[str, Any]] = Field(None, description="Full ruleset definition, used with live data capture for draft or unsaved rulesets.")
    markAndIncludeDroppedEvents: Optional[bool] = Field(None, description="Only for use with live data capture. Mark events that were dropped by dataset rules and still include them for capture")


class FunctionConfSchemaLookupInFieldsItem(CriblModel):

    eventField: str = Field(..., description="Field name as it appears in events")
    lookupField: Optional[str] = Field(None, description="Optional: The field name as it appears in the lookup file. Defaults to event field name")


class FunctionConfSchemaLookupOutFieldsItem(CriblModel):

    lookupField: str = Field(..., description="The field name as it appears in the lookup file")
    eventField: Optional[str] = Field(None, description="Optional: Field name to add to event. Defaults to lookup field name.")
    defaultValue: Optional[str] = Field(None, description="Optional: Value to assign if lookup entry is not found")


class FunctionConfSchemaMaskFlagsItem(CriblModel):

    name: Optional[str] = Field(None, description="Name of the field to set when one or more masking rules match.")
    value: str = Field(..., description="JavaScript expression to compute the value (can be constant)")


class FunctionConfSchemaMaskRulesItem(CriblModel):

    matchRegex: str = Field(..., description="Pattern to replace. Use /g to replace all matches.")
    replaceExpr: str = Field(..., description="A JavaScript expression or literal to replace the matching content. Capturing groups can be referenced as g1, g2, and so on, and event fields as event..")
    disabled: Optional[bool] = Field(None, description="Set to No to disable the evaluation of an individual rule")


class FunctionConfSchemaMvExpand(CriblModel):

    sourceFields: Optional[list[str]] = Field(None, description="Array of property-/field-names to expand")
    targetNames: Optional[list[str]] = Field(None, description="stores the value as new target field name")
    rowLimit: Optional[float] = Field(None, description="max. number of rows generated out of every source events")
    itemIndexName: Optional[str] = Field(None, description="name of an optional index property generated into the output")
    # values: bag=Store as object, array=Store as array
    bagExpansionMode: Optional[str] = Field(None, description="decides if bag-values are expanded to bags or arrays")


class FunctionConfSchemaMvPull(CriblModel):

    arrayPath: Optional[str] = Field(None, description="Field name of the array within events that contains the data objects of interest. Can be a path.")
    relativeKeyPath: Optional[str] = Field(None, description="Extract the K-V pair's key from this field, relative to the data object.")
    relativeValuePath: Optional[str] = Field(None, description="Extract the K-V pair's value from this field, relative to the data object.")
    targetBagPath: Optional[str] = Field(None, description="Optionally, specify a bag as the target for K-V entries. If not specified, these entries are stored on each top-level event.")
    deleteOriginal: Optional[bool] = Field(None, description="Toggle this on to remove each original array of data objects after extraction. If toggled off, arrays are retained.")


class FunctionConfSchemaNotificationPoliciesPoliciesItemTemplateTargetPairsItem(CriblModel):

    templateId: str = Field(..., description="ID of the notification template to use")
    targetId: str = Field(..., description="ID of the notification target (output)")


class FunctionConfSchemaNotifications(CriblModel):

    id: Optional[str] = Field(None, description="Notification ID")
    field: Optional[str] = Field(None, description="Notification event state field name")
    deduplicate: Optional[bool] = Field(None, description="Toggle deduplication.")


class FunctionConfSchemaNotify(CriblModel):
    """Notify Configuration"""

    group: Optional[str] = Field(None, description="Group the notification belongs to")
    notificationId: Optional[str] = Field(None, description="Workspace within the deployment to send the search results to.")
    searchId: Optional[str] = Field(None, description="Id of the search this function is running on.")
    savedQueryId: Optional[str] = Field(None, description="Id of the saved query")
    trigger: Optional[str] = Field(None, description="Js expression that filters events, a greater than 'Trigger Count' events will trigger the notification")
    # values: custom=Where, resultsCount=Count of Results
    triggerType: Optional[str] = Field(None, description="Type of the trigger condition. custom applies a kusto expression over the results, and results count applies a comparison over results count")
    # values: >=greater than, <=less than, ====equals, !===not equal to, >==greater than or equal to, <==less than or equal to
    triggerComparator: Optional[str] = Field(None, description="Operation to be applied over the results count")
    triggerCount: Optional[float] = Field(None, description="How many results that match trigger the condition")
    resultsLimit: Optional[float] = Field(None, description="Number of results to include in the notification event")
    searchUrl: Optional[str] = Field(None, description="Url of the search results")
    message: Optional[str] = Field(None, description="Message content template, available fields: searchId, resultSet, savedQueryId, notificationId, searchResultsUrl")
    authToken: Optional[str] = Field(None, description="Auth token for sending notification messages")
    messagesEndpoint: Optional[str] = Field(None, description="System messages api endpoint")
    tenantId: Optional[str] = Field(None, description="Current tenant id")


class FunctionConfSchemaNumerify(CriblModel):

    depth: Optional[int] = Field(None, description="Depth to which the Numerify Function will search within a nested event. Depth greater than 5 (the default) could decrease performance.")
    ignoreFields: Optional[list[str]] = Field(None, description="Fields to NOT numerify. Takes precedence over 'Include expression' when set. Supports wildcards. A '!' before field name(s) means: numerify all fields EXCEPT these. For syntax details, see [Wildcard Lists](https://docs.cribl.io/stream/introduction-reference/#wildcard-lists).")
    filterExpr: Optional[str] = Field(None, description="Optional JavaScript expression to determine whether a field should be numerified. If left blank, all fields will be numerified. Use the 'name' and 'value' global variables to access fields' names/values. Examples: `value != null`, `name=='fieldname'`. You can access other fields' values via `__e.`.")
    format: Optional[str] = Field(None, description="Numeric format to apply after type conversion.")
    digits: Optional[float] = Field(None, description="Number of digits after the decimal point, between 0 and 20. If left blank, defaults to 2.")


class FunctionConfSchemaOtlpLogs(CriblModel):

    dropNonLogEvents: Optional[bool] = Field(None, description="Drop events that are not OTLP log records.")
    preserveNativeAnyValue: Optional[bool] = Field(None, description="Body and attribute values already in OTLP AnyValue form (e.g. {string_value: \"...\"}) are preserved rather than being re-wrapped")
    batchOTLPLogs: Optional[bool] = Field(None, description="Batch OTLP log records by shared top-level `resource` attributes")
    sendBatchSize: Optional[float] = Field(None, description="Number of log records after which a batch will be sent, regardless of the timeout")
    timeout: Optional[float] = Field(None, description="Time duration after which a batch will be sent, regardless of size")
    sendBatchMaxSize: Optional[float] = Field(None, description="Maximum batch size. Enter 0 for no maximum.")
    metadataKeys: Optional[list[str]] = Field(None, description="When set, this processor will create one batcher instance per distinct combination of values in the metadata")
    metadataCardinalityLimit: Optional[float] = Field(None, description="Limit the number of unique combinations of metadata key values that will be processed over the lifetime of the process. After the limit is reached, events with new metadata key value combinations will be dropped.")


class FunctionConfSchemaOtlpMetrics(CriblModel):

    resourceAttributes: Optional[list[str]] = Field(None, description="Top-level event fields to promote as OTLP resource attributes. Entries without `*` match the attribute name exactly (`cluster` matches only `cluster`). Append `*` for prefix matching (`cluster*` also matches `cluster_id` and `cluster.name`). Use `!` to exclude names; list exclusions before broader patterns (for example `!k8s.internal.*`, `k8s.*`). Matching is by whole top-level field name only; it does not walk nested objects. Use Eval to copy nested fields to the top level first.")
    resourceAttributePrefixes: Optional[list[str]] = Field(None, description="Deprecated. Prefer 'Resource attributes', which supports exact and wildcard matching. This field lists prefixes of top-level attributes to add as resource attributes. Every entry is treated as a prefix, so `cluster` also matches `cluster_foo`, with no way to match an attribute name exactly. This field applies only when 'Resource attributes' is empty. Use Eval to copy nested attributes to the top level for matching.")
    dropNonMetricEvents: Optional[bool] = Field(None, description="Drop events that are not OTLP metric data points.")
    otlpVersion: Optional[str] = Field(None, description="OpenTelemetry Protocol (OTLP) version to use for metric serialization.")
    batchOTLPMetrics: Optional[bool] = Field(None, description="Batch OTLP metrics by shared top-level `resource` attributes")
    sendBatchSize: Optional[float] = Field(None, description="Number of metric data points after which a batch will be sent, regardless of the timeout")
    timeout: Optional[float] = Field(None, description="Time duration after which a batch will be sent, regardless of size")
    sendBatchMaxSize: Optional[float] = Field(None, description="Maximum batch size. Enter 0 for no maximum.")
    metadataKeys: Optional[list[str]] = Field(None, description="When set, this processor will create one batcher instance per distinct combination of values in the metadata")
    metadataCardinalityLimit: Optional[float] = Field(None, description="Limit the number of unique combinations of metadata key values that will be processed over the lifetime of the process. After the limit is reached, events with new metadata key value combinations will be dropped.")


class FunctionConfSchemaOtlpTraces(CriblModel):

    dropNonTraceEvents: Optional[bool] = Field(None, description="Drop events that are not OTLP trace spans.")
    otlpVersion: Optional[str] = Field(None, description="OpenTelemetry Protocol (OTLP) version to use for trace serialization.")
    batchOTLPTraces: Optional[bool] = Field(None, description="Batch OTLP traces by shared top-level `resource` attributes")
    sendBatchSize: Optional[float] = Field(None, description="Number of spans after which a batch will be sent, regardless of the timeout")
    timeout: Optional[float] = Field(None, description="Time duration after which a batch will be sent, regardless of size")
    sendBatchMaxSize: Optional[float] = Field(None, description="Maximum batch size. Enter 0 for no maximum.")
    metadataKeys: Optional[list[str]] = Field(None, description="When set, this processor will create one batcher instance per distinct combination of values in the metadata")
    metadataCardinalityLimit: Optional[float] = Field(None, description="Limit the number of unique combinations of metadata key values that will be processed over the lifetime of the process. After the limit is reached, events with new metadata key value combinations will be dropped.")


class FunctionConfSchemaPack(CriblModel):

    unpackedFields: Optional[list[str]] = Field(None, description="List of fields to keep, everything else will be packed")
    target: Optional[str] = Field(None, description="Name of the (packed) target field")


class FunctionConfSchemaPivot(CriblModel):
    """Simple Pivot Configuration"""

    labelField: Optional[str] = Field(None, description="Fields to be used for the left-most column.")
    dataFields: Optional[list[str]] = Field(None, description="Fields with the cell values (i.e. aggregates)")
    qualifierFields: Optional[list[str]] = Field(None, description="Fields to qualify or group data fields")


class FunctionConfSchemaPublishMetricsFieldsItem(CriblModel):

    inFieldName: str = Field(..., description="The name of the field in the event that contains the metric value")
    outFieldExpr: Optional[str] = Field(None, description="JavaScript expression to evaluate the metric field name. Defaults to Event Field Name.")
    metricType: str = Field(..., description="The type of metric to publish (counter, timer, gauge, distribution, summary, or histogram).")


class FunctionConfSchemaRedisCommandsItem(CriblModel):

    outField: Optional[str] = Field(None, description="Name of the field in which to store the returned value. Leave blank to discard returned value.")
    command: str = Field(..., description="Redis command to perform. For a complete list visit: https://redis.io/commands")
    keyExpr: str = Field(..., description="A JavaScript expression to compute the value of the key to operate on. Can also be a constant such as 'username'.")
    argsExpr: Optional[str] = Field(None, description="A JavaScript expression to compute arguments to the operation. Can return an array.")


class FunctionConfSchemaRegexFilterRegexListItem(CriblModel):

    regex: str = Field(..., description="Regex to test against")


class FunctionConfSchemaRenameRenameItem(CriblModel):

    currentName: str = Field(..., description="Name of the field to rename. Literal identifiers must be quoted.")
    newName: str = Field(..., description="The name the field will be renamed to. Literal identifiers must be quoted.")


class FunctionConfSchemaRollupMetrics(CriblModel):

    dimensions: Optional[list[str]] = Field(None, description="List of dimensions across which to perform rollups. Supports wildcards. Defaults to all original dimensions.")
    timeWindow: Optional[str] = Field(None, description="The time span of the rollup window. Must be a valid time string (such as 10s).")
    # values: max=Maximum, min=Minimum, avg=Average
    gaugeRollup: Optional[str] = Field(None, description="The operation to use when rolling up gauge metrics. Defaults to last.")


class FunctionConfSchemaSamplingRulesItem(CriblModel):

    filter: str = Field(..., description="JavaScript filter expression matching events to be sampled. Use true to match all.")
    rate: int = Field(..., description="Sampling rate; picks one out of N matching events")


class FunctionConfSchemaSearchEngineExport(CriblModel):
    """Search engine export Configuration"""

    searchJobId: Optional[str] = Field(None, description="Id of the search job this function is running on.")
    dataset: Optional[str] = Field(None, description="Id of the dataset")
    tee: Optional[bool] = Field(None, description="Tee results to search. When set to true results will be shipped instead of stats")
    flushMs: Optional[float] = Field(None, description="How often are stats flushed in ms")
    suppressPreviews: Optional[bool] = Field(None, description="Disables generation of intermediate stats. When true stats will be emitted only on end")


class FunctionConfSchemaSend(CriblModel):
    """Send Configuration"""

    url: Optional[str] = Field(None, description="Full URL to send search to.")
    group: Optional[str] = Field(None, description="Group within the workspace we're sending to.")
    workspace: Optional[str] = Field(None, description="Workspace within the deployment to send the search results to.")
    sendUrlTemplate: Optional[str] = Field(None, description="Template to build the URL to send from.")
    searchId: Optional[str] = Field(None, description="Id of the search this function is running on.")
    tee: Optional[bool] = Field(None, description="Tee results to search. When set to true results will be shipped instead of stats")
    flushMs: Optional[float] = Field(None, description="How often are stats flushed in ms")
    suppressPreviews: Optional[bool] = Field(None, description="Disables generation of intermediate stats. When true stats will be emitted only on end")
    mode: Optional[str] = Field(None, description="In Sender mode, forwards search results directly to the destination. In Metrics mode, accumulates metrics from federated send operators, and forwards the aggregate metrics.")


class FunctionConfSchemaSensitiveDataScannerFlagsItem(CriblModel):

    name: Optional[str] = Field(None, description="Name of the field to set when one or more scanning rules match.")
    value: str = Field(..., description="JavaScript expression to compute the value to assign to this field.")


class FunctionConfSchemaSensitiveDataScannerRulesItem(CriblModel):

    rulesetId: str = Field(..., description="The ID of the ruleset to use for the scan")
    replaceExpr: str = Field(..., description="A JavaScript expression or literal to replace the matching content. Capturing groups can be referenced as g1, g2, and so on, and event fields as event..")
    disabled: Optional[bool] = Field(None, description="If true, disable this rule so that it is not applied during scanning.")


class FunctionConfSchemaSerialize(CriblModel):

    # values: elff=Extended Log File Format, clf=Common Log Format, kvp=Key=Value Pairs, json=JSON Object, delim=Delimited values
    type: Optional[str] = Field(None, description="Data output format.")
    fields: Optional[list[str]] = Field(None, description="Required for CSV, ELFF, CLF, and Delimited values. All other formats support wildcard field lists. Examples: host, array*, !host *")
    srcField: Optional[str] = Field(None, description="Field containing object to serialize. Leave blank to serialize top-level event fields.")
    dstField: Optional[str] = Field(None, description="Field to serialize data to")
    cleanFields: Optional[bool] = Field(None, description="Clean field names by replacing non-[a-zA-Z0-9] characters with _")
    pairDelimiter: Optional[str] = Field(None, description="Delimiter used to separate key=value pairs. Defaults to a single space character. Should not have common characters with key-value delimiter.")
    keyValueDelimiter: Optional[str] = Field(None, description="Delimiter used to separate key and value in pair. Defaults to a '='. Should not have common characters with pair delimiter.")


class FunctionConfSchemaSidlookupFieldsItem(CriblModel):

    name: Optional[str] = Field(None, description="Name of the field to set or add to the event.")
    expr: str = Field(..., description="JavaScript expression to compute the value (can be constant)")
    disabled: Optional[bool] = Field(None, description="Set to No to disable the evaluation of an individual expression")


class FunctionConfSchemaSnmpTrapSerializeV3UserConf(CriblModel):
    """SNMPv3 user configuration, including authentication and privacy protocol settings."""

    name: Optional[str] = Field(None, description="Username for the SNMPv3 user.")
    # values: sha=SHA1
    authProtocol: Optional[Literal['none', 'md5', 'sha', 'sha224', 'sha256', 'sha384', 'sha512']] = Field(None, description="Authentication protocol for the SNMPv3 user.")
    privProtocol: Optional[str] = Field(None, description="Privacy protocol for SNMPv3 encryption.")


class FunctionConfSchemaSort(CriblModel):
    """Sort Configuration"""

    sortId: Optional[str] = Field(None, description="Has to be unique if there are multiple sorts on the pipeline.")
    comparisonExpression: Optional[str] = Field(None, description="The expression can access the events via the 'left' and 'right' properties.")
    topN: Optional[float] = Field(None, description="Limits the output to N (highest/lowest) events")
    maxEvents: Optional[float] = Field(None, description="Specifies the number of events that can flow into this function")
    suppressPreviews: Optional[bool] = Field(None, description="Toggle this on to suppress generating previews of intermediate results")


class FunctionConfSchemaStore(CriblModel):
    """Store Function Configuration"""

    type: Optional[str] = Field(None, description="The type of knowledge object, generated by the function (i.e., 'lookup')")
    destination: Optional[str] = Field(None, description="Configures where and how the data should be stored")
    description: Optional[str] = Field(None, description="The knowledge object's description")
    fieldMapping: Optional[dict[str, Any]] = Field(None, description="Mapping event property names to output field names")
    separator: Optional[str] = Field(None, description="Character to be used as value delimiter in output")
    overwrite: Optional[bool] = Field(None, description="For existing files, an error is thrown if overwrite is false or the file is replaced if overwrite is true")
    compress: Optional[str] = Field(None, description="True will compress output, false leaves it as it is and auto decides based on size")
    tee: Optional[bool] = Field(None, description="Tee results to the next operator")
    maxEvents: Optional[float] = Field(None, description="Limits how many events can be stored")
    suppressPreviews: Optional[bool] = Field(None, description="Suppresses the timer-based export stats generating")


class FunctionConfSchemaSuppress(CriblModel):

    keyExpr: Optional[str] = Field(None, description="Suppression key expression used to uniquely identify events to suppress. For example, `${ip}:${port}` will use fields ip and port from each event to generate the key.")
    allow: Optional[float] = Field(None, description="The number of events to allow per time period")
    suppressPeriodSec: Optional[float] = Field(None, description="The number of seconds to suppress events after 'Number to allow' events are received")
    dropEventsMode: Optional[bool] = Field(None, description="If disabled, suppressed events will be tagged with suppress=1 but not dropped")
    maxCacheSize: Optional[float] = Field(None, description="The maximum number of keys that can be cached before idle entries are removed. Leave at default unless you understand the implications of changing.")
    cacheIdleTimeoutPeriods: Optional[float] = Field(None, description="The number of suppression periods 'Suppression Period' of inactivity before a cache entry is considered idle. Leave at default unless you understand the implications of changing.")
    numEventsIdleTimeoutTrigger: Optional[float] = Field(None, description="Check cache for idle sessions every N events when cache size is > 'Maximum Cache Size'. Leave at default unless you understand the implications of changing.")


class FunctionConfSchemaTee(CriblModel):

    command: Optional[str] = Field(None, description="Command to execute and feed events to, via stdin. One JSON-formatted event per line.")
    args: Optional[list[str]] = Field(None, description="Command-line arguments to pass to the command.")
    restartOnExit: Optional[bool] = Field(None, description="Restart the process if it exits and/or we fail to write to it")
    env: Optional[dict[str, Any]] = Field(None, description="Environment variables to overwrite or set")


class FunctionConfSchemaTrimTimestamp(CriblModel):

    field: Optional[str] = Field(None, description="Name of field in which to save the timestamp. (If empty, timestamp will not be saved to a field.)")


class FunctionConfSchemaUnion(CriblModel):
    """Union Configuration"""

    searchJobId: Optional[str] = Field(None, description="The id for this search job.")
    stageIds: Optional[list[str]] = Field(None, description="The stages we are unioning with.")


class FunctionConfSchemaUnroll(CriblModel):

    srcExpr: Optional[str] = Field(None, description="Field in which to find/calculate the array to unroll. Example: _raw, _raw.split(/\\n/)")
    dstField: Optional[str] = Field(None, description="Field in destination event in which to place the unrolled value")


class FunctionConfSchemaWindow(CriblModel):

    eventWindowId: Optional[float] = Field(None, description="Identifies the unique ID, used for a event window")
    registeredFunctions: Optional[list[str]] = Field(None, description="All window functions, tracked by this event window")
    tailEventCount: Optional[float] = Field(None, description="Number of events to keep before the current event in the window")
    headEventCount: Optional[float] = Field(None, description="Number of events to keep after the current event in the window")


class FunctionConfSchemaXmlUnroll(CriblModel):

    unroll: Optional[str] = Field(None, description="Path to array to unroll. Example: ^root\\.child\\.ElementToUnroll$")
    inherit: Optional[str] = Field(None, description="Regex matching elements to copy into each unrolled event. Example: ^root\\.(childA|childB|childC)$")
    unrollIdxField: Optional[str] = Field(None, description="Add a field with this name, containing the index at which the item was located, starting from 0")
    pretty: Optional[bool] = Field(None, description="Pretty print the output XML")


class GpuType(CriblModel):
    """Select the level of detail for GPU metrics"""

    mode: Optional[Literal['basic', 'all', 'custom', 'disabled']] = Field(None, description="Select the level of detail for GPU metrics")
    perGpu: Optional[bool] = Field(None, description="Generate metrics for each GPU")
    detail: Optional[bool] = Field(None, description="Generate full GPU metrics")


class HostConfOutputSyslog(CriblModel):

    host: str = Field(..., description="The hostname of the receiver")
    port: float = Field(..., description="The port to connect to on the provided host")
    tls: Optional[Literal['inherit', 'off']] = Field(None, description="Whether to inherit TLS configs from group setting or disable TLS")
    servername: Optional[str] = Field(None, description="Servername to use if establishing a TLS connection. If not specified, defaults to connection host (if not an IP); otherwise, uses the global TLS settings.")
    weight: Optional[float] = Field(None, description="Assign a weight (>0) to each endpoint to indicate its traffic-handling capability")
    xtemplate_host: Optional[str] = Field(None, alias="__template_host", description="Binds 'host' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'host' at runtime.")
    xtemplate_port: Optional[str] = Field(None, alias="__template_port", description="Binds 'port' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'port' at runtime.")


class InputAnthropicComplianceActivitiesConf(CriblModel):
    """Activities"""

    enabled: Optional[bool] = Field(None, description="Enabled")
    cronSchedule: Optional[str] = Field(None, description="Schedule on which to run this collection job")
    earliest: Optional[str] = Field(None, description="Earliest time for data collection, relative to now")
    latest: Optional[str] = Field(None, description="Latest time for data collection, relative to now")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")
    stateTracking: Optional[bool] = Field(None, description="Track collection progress between consecutive scheduled executions")
    stateUpdateExpression: Optional[str] = Field(None, description="JavaScript expression that defines how to update the state from an event. Use the event's data and the current state to compute the new state. See [Understanding State Expression Fields](https://docs.cribl.io/stream/collectors-rest#state-tracking-expression-fields) for more information.")
    stateMergeExpression: Optional[str] = Field(None, description="JavaScript expression that defines which state to keep when merging a task's newly reported state with previously saved state. Evaluates `prevState` and `newState` variables, resolving to the state to keep.")
    manageState: Optional[dict[str, Any]] = Field(None, description="Controls for viewing and managing the collector state.")


class InputAnthropicComplianceChatMessagesConf(CriblModel):
    """Chat Messages"""

    enabled: Optional[bool] = Field(None, description="Enabled")
    cronSchedule: Optional[str] = Field(None, description="Schedule on which to run this collection job")
    earliest: Optional[str] = Field(None, description="Earliest time for data collection, relative to now")
    latest: Optional[str] = Field(None, description="Latest time for data collection, relative to now")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")
    stateTracking: Optional[bool] = Field(None, description="Track collection progress between consecutive scheduled executions")
    stateUpdateExpression: Optional[str] = Field(None, description="JavaScript expression that defines how to update the state from an event. Use the event's data and the current state to compute the new state. See [Understanding State Expression Fields](https://docs.cribl.io/stream/collectors-rest#state-tracking-expression-fields) for more information.")
    stateMergeExpression: Optional[str] = Field(None, description="JavaScript expression that defines which state to keep when merging a task's newly reported state with previously saved state. Evaluates `prevState` and `newState` variables, resolving to the state to keep.")
    manageState: Optional[dict[str, Any]] = Field(None, description="Controls for viewing and managing the collector state.")


class InputAnthropicComplianceChatsConf(CriblModel):
    """Chats"""

    enabled: Optional[bool] = Field(None, description="Enabled")
    cronSchedule: Optional[str] = Field(None, description="Schedule on which to run this collection job")
    earliest: Optional[str] = Field(None, description="Earliest time for data collection, relative to now")
    latest: Optional[str] = Field(None, description="Latest time for data collection, relative to now")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")
    stateTracking: Optional[bool] = Field(None, description="Track collection progress between consecutive scheduled executions")
    stateUpdateExpression: Optional[str] = Field(None, description="JavaScript expression that defines how to update the state from an event. Use the event's data and the current state to compute the new state. See [Understanding State Expression Fields](https://docs.cribl.io/stream/collectors-rest#state-tracking-expression-fields) for more information.")
    stateMergeExpression: Optional[str] = Field(None, description="JavaScript expression that defines which state to keep when merging a task's newly reported state with previously saved state. Evaluates `prevState` and `newState` variables, resolving to the state to keep.")
    manageState: Optional[dict[str, Any]] = Field(None, description="Controls for viewing and managing the collector state.")


class InputAnthropicComplianceGroupsConf(CriblModel):
    """Groups"""

    enabled: Optional[bool] = Field(None, description="Enabled")
    cronSchedule: Optional[str] = Field(None, description="Schedule on which to run this collection job")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")


class InputAnthropicComplianceOrgRolesConf(CriblModel):
    """Organization Roles"""

    enabled: Optional[bool] = Field(None, description="Enabled")
    cronSchedule: Optional[str] = Field(None, description="Schedule on which to run this collection job")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")


class InputAnthropicComplianceOrgUsersConf(CriblModel):
    """Organization Users"""

    enabled: Optional[bool] = Field(None, description="Enabled")
    cronSchedule: Optional[str] = Field(None, description="Schedule on which to run this collection job")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")


class InputAnthropicComplianceOrganizationsConf(CriblModel):
    """Organizations"""

    enabled: Optional[bool] = Field(None, description="Enabled")
    cronSchedule: Optional[str] = Field(None, description="Schedule on which to run this collection job")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")


class InputAnthropicComplianceProjectDetailsConf(CriblModel):
    """Project Details"""

    enabled: Optional[bool] = Field(None, description="Enabled")
    cronSchedule: Optional[str] = Field(None, description="Schedule on which to run this collection job")
    earliest: Optional[str] = Field(None, description="Earliest time for data collection, relative to now")
    latest: Optional[str] = Field(None, description="Latest time for data collection, relative to now")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")
    stateTracking: Optional[bool] = Field(None, description="Track collection progress between consecutive scheduled executions")
    stateUpdateExpression: Optional[str] = Field(None, description="JavaScript expression that defines how to update the state from an event. Use the event's data and the current state to compute the new state. See [Understanding State Expression Fields](https://docs.cribl.io/stream/collectors-rest#state-tracking-expression-fields) for more information.")
    stateMergeExpression: Optional[str] = Field(None, description="JavaScript expression that defines which state to keep when merging a task's newly reported state with previously saved state. Evaluates `prevState` and `newState` variables, resolving to the state to keep.")
    manageState: Optional[dict[str, Any]] = Field(None, description="Controls for viewing and managing the collector state.")


class InputAnthropicComplianceProjectsConf(CriblModel):
    """Projects"""

    enabled: Optional[bool] = Field(None, description="Enabled")
    cronSchedule: Optional[str] = Field(None, description="Schedule on which to run this collection job")
    earliest: Optional[str] = Field(None, description="Earliest time for data collection, relative to now")
    latest: Optional[str] = Field(None, description="Latest time for data collection, relative to now")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")
    stateTracking: Optional[bool] = Field(None, description="Track collection progress between consecutive scheduled executions")
    stateUpdateExpression: Optional[str] = Field(None, description="JavaScript expression that defines how to update the state from an event. Use the event's data and the current state to compute the new state. See [Understanding State Expression Fields](https://docs.cribl.io/stream/collectors-rest#state-tracking-expression-fields) for more information.")
    stateMergeExpression: Optional[str] = Field(None, description="JavaScript expression that defines which state to keep when merging a task's newly reported state with previously saved state. Evaluates `prevState` and `newState` variables, resolving to the state to keep.")
    manageState: Optional[dict[str, Any]] = Field(None, description="Controls for viewing and managing the collector state.")


class InputAnthropicEnterpriseAnalyticsContentConfigItem(CriblModel):

    contentType: str = Field(..., description="Content type")
    disabled: Optional[bool] = Field(None, description="Enabled")
    stateTracking: Optional[bool] = Field(None, description="Track collection progress between runs. When enabled, each run resumes from where the last one left off, preventing duplicate data. The API refreshes approximately every 4 hours; runs between refreshes produce zero events until new finalized data becomes available. This is expected behavior.")
    stateUpdateExpression: Optional[str] = Field(None, description="JavaScript expression evaluated per event to compute new state. The default tracks the data_refreshed_at watermark reported by the API.")
    stateMergeExpression: Optional[str] = Field(None, description="JavaScript expression to merge state across distributed Workers. The default keeps the most recent watermark.")
    manageState: Optional[bool] = Field(None, description="Manage state")
    groupBy: Optional[list[str]] = Field(None, description="Dimensions for breaking down usage. Leave empty to collect a single summed row per time bucket.")
    # values: 1d=Daily (1d), 1h=Hourly (1h), 1m=Per-minute (1m)
    bucketWidth: Optional[str] = Field(None, description="Time bucket size for aggregated results. Smaller buckets yield more events per collection run.")
    cronSchedule: str = Field(..., description="Cron schedule for collection runs. The API refreshes data approximately every 4 hours, so polling more frequently will not yield new results.")
    earliest: Optional[str] = Field(None, description="Earliest time for data collection, relative to now. Used as the initial lower bound on first run before any state exists. Maximum 365 days (API limit). Examples: -7d@d, -24h, -30d.")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")


class InputAppscopeFilterConfAllowItem(CriblModel):

    procname: str = Field(..., description="Specify the name of a process or family of processes.")
    arg: Optional[str] = Field(None, description="Specify a string to substring-match against process command-line.")
    config: str = Field(..., description="Choose a config to apply to processes that match the process name and/or argument.")


class InputAppscopePersistenceConf(CriblModel):
    """Persistence"""

    enable: Optional[bool] = Field(None, description="Spool events and metrics on disk for Cribl Edge and Search")
    timeWindow: Optional[str] = Field(None, description="Time span for each file bucket")
    maxDataSize: Optional[str] = Field(None, description="Maximum disk space allowed to be consumed (examples: 420MB, 4GB). When limit is reached, older data will be deleted.")
    maxDataTime: Optional[str] = Field(None, description="Maximum amount of time to retain data (examples: 2h, 4d). When limit is reached, older data will be deleted.")
    compress: Optional[Literal['none', 'gzip']] = Field(None, description="Data compression format")
    destPath: Optional[str] = Field(None, description="Path to use to write metrics. Defaults to $CRIBL_HOME/state/appscope")


class InputCloudflareHecTlsConf(CriblModel):
    """TLS settings (server side)"""

    disabled: Optional[bool] = Field(None, description="Enable or disable TLS. Defaults to enabled for Cloudflare sources.")
    requestCert: Optional[bool] = Field(None, description="Require clients to present their certificates. Used to perform client authentication using SSL certs.")
    caPath: Optional[str] = Field(None, description="Path on server containing CA certificates to use. PEM format. Can reference $ENV_VARS.")
    rejectUnauthorized: Optional[bool] = Field(None, description="Reject certificates not authorized by a CA in the CA certificate path or by another trusted CA (such as the system's)")
    commonNameRegex: Optional[str] = Field(None, description="Regex matching allowable common names in peer certificates' subject attribute")
    certificateName: Optional[str] = Field(None, description="The name of the predefined certificate")
    privKeyPath: Optional[str] = Field(None, description="Path on server containing the private key to use. PEM format. Can reference $ENV_VARS. Defaults to the built-in Cribl private key when TLS is enabled.")
    passphrase: Optional[str] = Field(None, description="Passphrase to use to decrypt private key")
    certPath: Optional[str] = Field(None, description="Path on server containing certificates to use. PEM format. Can reference $ENV_VARS. Defaults to the built-in Cribl certificate when TLS is enabled.")
    minVersion: Optional[Literal['TLSv1', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3']] = Field(None, description="Minimum TLS version to accept from clients.")
    maxVersion: Optional[Literal['TLSv1', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3']] = Field(None, description="Maximum TLS version to accept from clients.")


class InputCrowdstrikeCheckpointingConf(CriblModel):
    """Checkpoint settings used to resume processing after an interruption. Not applied when fan-out is enabled."""

    enabled: bool = Field(..., description="Resume processing files after an interruption")
    retries: Optional[float] = Field(None, description="The number of times to retry processing when a processing error occurs. If Skip file on error is enabled, this setting is ignored.")


class InputCrowdstrikePreprocessConf(CriblModel):
    """Optional preprocessing step that pipes collected data through an external command before ingestion. Not applied when fan-out is enabled."""

    disabled: bool = Field(..., description="Disabled")
    command: Optional[str] = Field(None, description="Command to feed the data through (via stdin) and process its output (stdout)")
    args: Optional[list[str]] = Field(None, description="Arguments to be added to the custom command")


class InputDatadogAgentProxyModeConf(CriblModel):
    """Proxy mode settings for Datadog Agent requests."""

    enabled: bool = Field(..., description="Forward key validation requests from the Datadog Agent to the Datadog API. If disabled, Stream handles key validation requests locally by always responding that the key is valid.")
    rejectUnauthorized: Optional[bool] = Field(None, description="Whether to reject certificates that cannot be verified against a valid CA (such as self-signed certificates)")


class InputDatadogAgentSamplingRulesItem(CriblModel):

    service: str = Field(..., description="Datadog service name")
    environment: str = Field(..., description="Datadog environment name (example: prod, staging)")
    rate: float = Field(..., description="Sampling rate for this service/environment combination (0.0–1.0)")


class InputDatagenSamplesItem(CriblModel):

    sample: str = Field(..., description="Data Generator File Name")
    eventsPerSec: float = Field(..., description="Maximum number of events to generate per second per Worker Node. Defaults to 10.")


class InputEdgePrometheusPodFilterItem(CriblModel):

    filter: str = Field(..., description="JavaScript expression applied to pods objects. Return 'true' to include it.")
    description: Optional[str] = Field(None, description="Optional description of this rule's purpose")


class InputEdgePrometheusTargetsItem(CriblModel):

    protocol: Optional[Literal['http', 'https']] = Field(None, description="Protocol to use when collecting metrics")
    host: str = Field(..., description="Name of host from which to pull metrics.")
    port: Optional[float] = Field(None, description="The port number in the metrics URL for discovered targets.")
    path: Optional[str] = Field(None, description="Path to use when collecting metrics from discovered targets")


class InputElasticProxyModeConf(CriblModel):
    """Proxy mode settings for Elasticsearch requests."""

    enabled: bool = Field(..., description="Enable proxying of non-bulk API requests to an external Elastic server. Enable this only if you understand the implications. See [Cribl Docs](https://docs.cribl.io/stream/sources-elastic/#proxy-mode) for more details.")
    authType: Optional[str] = Field(None, description="Enter credentials directly, or select a stored secret")
    username: Optional[str] = Field(None, description="Username")
    password: Optional[str] = Field(None, description="Password")
    credentialsSecret: Optional[str] = Field(None, description="Select or create a secret that references your credentials")
    url: Optional[str] = Field(None, description="URL of the Elastic server to proxy non-bulk requests to, such as http://elastic:9200")
    rejectUnauthorized: Optional[bool] = Field(None, description="Reject certificates that cannot be verified against a valid CA (such as self-signed certificates)")
    removeHeaders: Optional[list[str]] = Field(None, description="List of headers to remove from the request to proxy")
    timeoutSec: Optional[float] = Field(None, description="Amount of time, in seconds, to wait for a proxy request to complete before canceling it")
    xtemplate_url: Optional[str] = Field(None, alias="__template_url", description="Binds 'url' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'url' at runtime.")


class InputEventhubAmqpAuthConfCertificateConf(CriblModel):
    """Certificate credentials for OAuth authentication."""

    certificateName: str = Field(..., description="The certificate you registered as credentials for your app in the Azure portal")
    certPath: str = Field(..., description="Path on server containing certificates to use. PEM format. Can reference $ENV_VARS.")
    privKeyPath: str = Field(..., description="Path on server containing the private key to use. PEM format. Can reference $ENV_VARS.")
    passphrase: Optional[str] = Field(None, description="Passphrase to use to decrypt private key")


class InputGrafanaLokiAuthConf(CriblModel):
    """Authentication settings for Loki requests."""

    # values: credentialsSecret=Basic (credentials secret), textSecret=Token (text secret)
    authType: Optional[Literal['none', 'basic', 'credentialsSecret', 'token', 'textSecret']] = Field(None, description="Loki logs authentication type")
    username: Optional[str] = Field(None, description="Username")
    password: Optional[str] = Field(None, description="Password")
    token: Optional[str] = Field(None, description="Bearer token to include in the authorization header")
    credentialsSecret: Optional[str] = Field(None, description="Select or create a secret that references your credentials")
    textSecret: Optional[str] = Field(None, description="Select or create a stored text secret")


class InputGrafanaPrometheusAuthConf(CriblModel):
    """Authentication settings for Prometheus Remote Write requests."""

    # values: credentialsSecret=Basic (credentials secret), textSecret=Token (text secret)
    authType: Optional[Literal['none', 'basic', 'credentialsSecret', 'token', 'textSecret']] = Field(None, description="Remote Write authentication type")
    username: Optional[str] = Field(None, description="Username")
    password: Optional[str] = Field(None, description="Password")
    token: Optional[str] = Field(None, description="Bearer token to include in the authorization header")
    credentialsSecret: Optional[str] = Field(None, description="Select or create a secret that references your credentials")
    textSecret: Optional[str] = Field(None, description="Select or create a stored text secret")


class InputHttpAuthTokensExtItem(CriblModel):

    authType: Optional[Literal['manual', 'secret']] = Field(None, description="Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate")
    tokenSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    token: Optional[str] = Field(None, description="Shared secret to be provided by any client (Authorization: )")
    description: Optional[str] = Field(None, description="Description")
    metadata: Optional[list[HecTokenMetadataParam]] = Field(None, description="Fields to add to events referencing this token")


class InputHttpRawAuthTokensExtItem(CriblModel):

    authType: Optional[Literal['manual', 'secret']] = Field(None, description="Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate")
    tokenSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    token: Optional[str] = Field(None, description="Shared secret to be provided by any client (Authorization: )")
    description: Optional[str] = Field(None, description="Description")
    metadata: Optional[list[HecTokenMetadataParam]] = Field(None, description="Fields to add to events referencing this token")


class InputJournalFilesRulesItem(CriblModel):

    filter: str = Field(..., description="JavaScript expression applied to Journal objects. Return 'true' to include it.")
    description: Optional[str] = Field(None, description="Optional description of this rule's purpose")


class InputKubeLogsRulesItem(CriblModel):

    filter: str = Field(..., description="JavaScript expression applied to Pod objects. Return 'true' to include it.")
    description: Optional[str] = Field(None, description="Optional description of this rule's purpose")


class InputKubeMetricsPersistenceConf(CriblModel):
    """persistence"""

    enable: Optional[bool] = Field(None, description="Spool metrics on disk for Cribl Search")
    timeWindow: Optional[str] = Field(None, description="Time span for each file bucket")
    maxDataSize: Optional[str] = Field(None, description="Maximum disk space allowed to be consumed (examples: 420MB, 4GB). When limit is reached, older data will be deleted.")
    maxDataTime: Optional[str] = Field(None, description="Maximum amount of time to retain data (examples: 2h, 4d). When limit is reached, older data will be deleted.")
    compress: Optional[Literal['none', 'gzip']] = Field(None, description="Data compression format")
    destPath: Optional[str] = Field(None, description="Path to use to write metrics. Defaults to $CRIBL_HOME/state/")


class InputMicrosoftCopilotCertOptionsConf(CriblModel):
    """Certificate credentials for Microsoft Graph OAuth authentication."""

    certificateName: Optional[str] = Field(None, description="The name of a predefined certificate")
    privKeyPath: str = Field(..., description="Path to the private key (PEM format). Can reference $ENV_VARS.")
    passphrase: Optional[str] = Field(None, description="Passphrase to decrypt the private key")
    certPath: str = Field(..., description="Path to the certificate (PEM format). Can reference $ENV_VARS.")


class InputMicrosoftCopilotRetryRulesConf(CriblModel):
    """HTTP retry behavior for failed collection requests."""

    # values: none=Disabled
    type: Literal['none', 'backoff', 'static'] = Field(..., description="The algorithm to use when performing HTTP retries")
    interval: Optional[float] = Field(None, description="Time interval between failed request and first retry (kickoff). Maximum allowed value is 20,000 ms (1/3 minute).")
    limit: Optional[float] = Field(None, description="The maximum number of times to retry a failed HTTP request")
    multiplier: Optional[float] = Field(None, description="Base for exponential backoff, e.g., base 2 means that retries will occur after 2, then 4, then 8 seconds, and so on")
    codes: Optional[list[float]] = Field(None, description="List of HTTP codes that trigger a retry. Leave empty to use the default list of 429, 500, and 503.")
    enableHeader: Optional[bool] = Field(None, description="Honor any Retry-After header that specifies a delay (in seconds) or a timestamp after which to retry the request. The delay is limited to 20 seconds, even if the Retry-After header specifies a longer delay. When disabled, all Retry-After headers are ignored.")
    retryConnectTimeout: Optional[bool] = Field(None, description="Make a single retry attempt when a connection timeout (ETIMEDOUT) error occurs")
    retryConnectReset: Optional[bool] = Field(None, description="Retry request when a connection reset (ECONNRESET) error occurs")


class InputNetskopeContentConfigItem(CriblModel):

    contentType: str = Field(..., description="Content type")
    contentDescription: Optional[str] = Field(None, description="Description")
    disabled: Optional[bool] = Field(None, description="Enabled")
    cursorIndex: str = Field(..., description="Server-side index name Netskope uses for tracking data export state. Change only if you need a separate export cursor.")
    cronSchedule: str = Field(..., description="Schedule on which to collect this content type")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")
    logLevel: Optional[Literal['error', 'warn', 'info', 'debug', 'silly']] = Field(None, description="Collector runtime log level")


class InputOffice365MgmtContentConfigItem(CriblModel):

    contentType: Optional[str] = Field(None, description="Microsoft 365 Management Activity API Content Type")
    description: Optional[str] = Field(None, description="If interval type is minutes the value entered must evenly divisible by 60 or save will fail")
    interval: Optional[float] = Field(None, description="Interval")
    logLevel: Optional[Literal['error', 'warn', 'info', 'debug']] = Field(None, description="Collector runtime Log Level")
    enabled: Optional[bool] = Field(None, description="Enabled")


class InputOffice365ServiceContentConfigItem(CriblModel):

    contentType: Optional[str] = Field(None, description="Microsoft 365 Services API Content Type")
    description: Optional[str] = Field(None, description="If interval type is minutes the value entered must evenly divisible by 60 or save will fail")
    interval: Optional[float] = Field(None, description="Interval")
    logLevel: Optional[Literal['error', 'warn', 'info', 'debug']] = Field(None, description="Collector runtime Log Level")
    enabled: Optional[bool] = Field(None, description="Enabled")


class InputProvenanceTypeOptional(CriblModel):
    """Read-only metadata that records how the Source was created. Preserved on update when omitted from the request body. Cannot be set on create."""

    origin: Optional[Literal['data_source_discovery']] = Field(None, description="Feature that created the Source.")
    destinationArn: Optional[str] = Field(None, description="ARN of the S3 bucket or Firehose delivery stream configured as the Source.")
    sourceArn: Optional[str] = Field(None, description="ARN of the AWS resource that produces the logs.")
    sourceService: Optional[str] = Field(None, description="Resolved DSD source-service offering, when known.")
    accountId: Optional[str] = Field(None, description="Cloud tenant or scope id the Source was configured for (for example an AWS account id, GCP project or folder id, or Azure subscription or resource group id).")
    templateFamily: Optional[Literal['cloudformation', 'terraform']] = Field(None, description="Infrastructure-as-code family that provisioned the AWS resources (absent means cloudformation).")


class InputSalesforceContentConfigItem(CriblModel):

    contentType: str = Field(..., description="Content type")
    disabled: Optional[bool] = Field(None, description="Enabled")
    stateTracking: Optional[bool] = Field(None, description="Track collection progress between consecutive scheduled executions.")
    stateUpdateExpression: Optional[str] = Field(None, description="JavaScript expression that defines how to update the state from an event. Use the event's data and the current state to compute the new state. See [Understanding State Expression Fields](https://docs.cribl.io/stream/collectors-rest#state-tracking-expression-fields) for more information.")
    stateMergeExpression: Optional[str] = Field(None, description="JavaScript expression that defines which state to keep when merging a task's newly reported state with previously saved state. Evaluates `prevState` and `newState` variables, resolving to the state to keep.")
    manageState: Optional[dict[str, Any]] = Field(None, description="Controls for viewing and managing the collector state.")
    contentDescription: Optional[str] = Field(None, description="Brief description of what this content type collects.")
    objectName: Optional[str] = Field(None, description="Salesforce object API name to query (examples: LoginHistory, SetupAuditTrail, Account)")
    fields: Optional[list[str]] = Field(None, description="Field API names to include in the query.")
    cursor: Optional[str] = Field(None, description="Timestamp field used for time filtering and breaker rule routing (examples: LoginTime, CreatedDate)")
    filter: Optional[str] = Field(None, description="Optional SOQL WHERE conditions, entered as a Cribl expression that evaluates to a SOQL string. Wrap the value in backticks (example: `CountryIso = 'US'`). The expression is evaluated once when the Source initializes — not per collection run. Combined with cursor-based time filtering using AND. SOQL syntax is not validated locally; invalid conditions will fail at collection time.")
    cronSchedule: Optional[str] = Field(None, description="Schedule on which to run this collection job")
    earliest: Optional[str] = Field(None, description="Earliest time for data collection, relative to now")
    latest: Optional[str] = Field(None, description="Latest time for data collection, relative to now")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")
    xtemplate_filter: Optional[str] = Field(None, alias="__template_filter", description="Binds 'filter' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'filter' at runtime.")


class InputSnmpSnmpV3AuthConfV3UsersItem(CriblModel):

    name: str = Field(..., description="SNMPv3 security name.")
    # values: sha=SHA1
    authProtocol: Optional[Literal['none', 'md5', 'sha', 'sha224', 'sha256', 'sha384', 'sha512']] = Field(None, description="Authentication protocol for the SNMPv3 user.")
    authKeyType: Optional[str] = Field(None, description="Select Manual to enter the key directly, or Secret to use a stored text secret")
    authKey: Optional[str] = Field(None, description="Authentication key for the SNMPv3 user.")
    authKeySecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    # values: aes=AES128, aes256b=AES256b (Blumenthal), aes256r=AES256r (Reeder)
    privProtocol: Optional[str] = Field(None, description="Privacy protocol")
    privKeyType: Optional[str] = Field(None, description="Select Manual to enter the key directly, or Secret to use a stored text secret")
    privKey: Optional[str] = Field(None, description="Privacy key for the SNMPv3 user.")
    privKeySecret: Optional[str] = Field(None, description="Select or create a stored text secret")


class InputSplunkAuthTokensItem(CriblModel):

    authType: Optional[Literal['manual', 'secret']] = Field(None, description="Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate")
    tokenSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    token: Optional[str] = Field(None, description="Shared secrets to be provided by any Splunk forwarder. If empty, unauthorized access is permitted.")
    description: Optional[str] = Field(None, description="Description")


class InputSplunkHecAuthTokensItem(CriblModel):

    authType: Optional[Literal['manual', 'secret']] = Field(None, description="Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate")
    tokenSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    token: str = Field(..., description="Shared secret to be provided by any client (Authorization: )")
    enabled: Optional[bool] = Field(None, description="If true, the token is active and can be used for authentication.")
    description: Optional[str] = Field(None, description="Optional token description")
    allowedIndexesAtToken: Optional[list[str]] = Field(None, description="Enter the values you want to allow in the HEC event index field at the token level. Supports wildcards. To skip validation, leave blank.")
    metadata: Optional[list[HecTokenMetadataParam]] = Field(None, description="Fields to add to events referencing this token")


class InputSplunkSearchEndpointHeadersItem(CriblModel):

    name: str = Field(..., description="Header Name")
    value: str = Field(..., description="JavaScript expression to compute the header's value, normally enclosed in backticks (e.g., `${earliest}`). If a constant, use single quotes (e.g., 'earliest'). Values without delimiters (e.g., earliest) are evaluated as strings.")


class InputSplunkSearchEndpointParamsItem(CriblModel):

    name: str = Field(..., description="Parameter Name")
    value: str = Field(..., description="JavaScript expression to compute the parameter's value, normally enclosed in backticks (e.g., `${earliest}`). If a constant, use single quotes (e.g., 'earliest'). Values without delimiters (e.g., earliest) are evaluated as strings.")


class InputSystemMetricsContainerConfFiltersItem(CriblModel):

    expr: str = Field(..., description="Expression")


class InputSystemMetricsHostConfCustomConfCpuConf(CriblModel):
    """Select the level of detail for CPU metrics"""

    mode: Optional[str] = Field(None, description="Select the level of detail for CPU metrics")
    perCpu: Optional[bool] = Field(None, description="Generate metrics for each CPU")
    detail: Optional[bool] = Field(None, description="Generate metrics for all CPU states")
    time: Optional[bool] = Field(None, description="Generate raw, monotonic CPU time counters")


class InputSystemMetricsHostConfCustomConfDiskConf(CriblModel):
    """Select the level of detail for disk metrics"""

    mode: Optional[str] = Field(None, description="Select the level of detail for disk metrics")
    detail: Optional[bool] = Field(None, description="Generate full disk metrics")
    inodes: Optional[bool] = Field(None, description="Generate filesystem inode metrics")
    devices: Optional[list[str]] = Field(None, description="Block devices to include/exclude. Examples: sda*, !loop*. Wildcards and ! (not) operators are supported. All devices are included if this list is empty.")
    mountpoints: Optional[list[str]] = Field(None, description="Filesystem mountpoints to include/exclude. Examples: /, /home, !/proc*, !/tmp. Wildcards and ! (not) operators are supported. All mountpoints are included if this list is empty.")
    fstypes: Optional[list[str]] = Field(None, description="Filesystem types to include/exclude. Examples: ext4, !*tmpfs, !squashfs. Wildcards and ! (not) operators are supported. All types are included if this list is empty.")
    perDevice: Optional[bool] = Field(None, description="Generate separate metrics for each device")


class InputSystemMetricsHostConfCustomConfMemoryConf(CriblModel):
    """Select the level of detail for memory metrics"""

    mode: Optional[str] = Field(None, description="Select the level of detail for memory metrics")
    detail: Optional[bool] = Field(None, description="Generate metrics for all memory states")


class InputSystemMetricsHostConfCustomConfNetworkConf(CriblModel):
    """Select the level of detail for network metrics"""

    mode: Optional[str] = Field(None, description="Select the level of detail for network metrics")
    detail: Optional[bool] = Field(None, description="Generate full network metrics")
    protocols: Optional[bool] = Field(None, description="Generate protocol metrics for ICMP, ICMPMsg, IP, TCP, UDP and UDPLite")
    devices: Optional[list[str]] = Field(None, description="Network interfaces to include/exclude. Examples: eth0, !lo. All interfaces are included if this list is empty.")
    perInterface: Optional[bool] = Field(None, description="Generate separate metrics for each interface")


class InputSystemMetricsHostConfCustomConfSystemConf(CriblModel):
    """Select the level of detail for system metrics"""

    mode: Optional[str] = Field(None, description="Select the level of detail for system metrics")
    processes: Optional[bool] = Field(None, description="Generate metrics for the numbers of processes in various states")


class InputSystemMetricsPersistenceConf(CriblModel):
    """persistence"""

    enable: Optional[bool] = Field(None, description="Spool metrics to disk for Cribl Edge and Search")
    timeWindow: Optional[str] = Field(None, description="Time span for each file bucket")
    maxDataSize: Optional[str] = Field(None, description="Maximum disk space allowed to be consumed (examples: 420MB, 4GB). When limit is reached, older data will be deleted.")
    maxDataTime: Optional[str] = Field(None, description="Maximum amount of time to retain data (examples: 2h, 4d). When limit is reached, older data will be deleted.")
    compress: Optional[Literal['none', 'gzip']] = Field(None, description="Data compression format")
    destPath: Optional[str] = Field(None, description="Path to use to write metrics. Defaults to $CRIBL_HOME/state/system_metrics")


class InputSystemStateCollectorsConfDiskConf(CriblModel):
    """Creates events for physical disks, partitions, and file systems"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStateCollectorsConfDnsConf(CriblModel):
    """Creates events for DNS resolvers and search entries"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStateCollectorsConfFirewallConf(CriblModel):
    """Creates events for Firewall rules entries"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStateCollectorsConfHostsfileConf(CriblModel):
    """Creates events based on entries collected from the hosts file"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStateCollectorsConfInterfacesConf(CriblModel):
    """Creates events for each of the host’s network interfaces"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStateCollectorsConfLoginUsersConf(CriblModel):
    """Creates events from list of logged-in users"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStateCollectorsConfMetadataConf(CriblModel):
    """Creates events based on the host system’s current state"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStateCollectorsConfPortsConf(CriblModel):
    """Creates events from list of listening ports"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStateCollectorsConfRoutesConf(CriblModel):
    """Creates events based on entries collected from the host’s network routes"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStateCollectorsConfServicesConf(CriblModel):
    """Creates events from the list of services"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStateCollectorsConfUserConf(CriblModel):
    """Creates events for local users and groups"""

    enable: Optional[bool] = Field(None, description="Enabled")


class InputSystemStatePersistenceConf(CriblModel):
    """Disk spooling settings for collected system state data."""

    enable: Optional[bool] = Field(None, description="Spool metrics to disk for Cribl Edge and Search")
    timeWindow: Optional[str] = Field(None, description="Time span for each file bucket")
    maxDataSize: Optional[str] = Field(None, description="Maximum disk space allowed to be consumed (examples: 420MB, 4GB). When limit is reached, older data will be deleted.")
    maxDataTime: Optional[str] = Field(None, description="Maximum amount of time to retain data (examples: 2h, 4d). When limit is reached, older data will be deleted.")
    compress: Optional[Literal['none', 'gzip']] = Field(None, description="Data compression format")
    destPath: Optional[str] = Field(None, description="Path to use to write metrics. Defaults to $CRIBL_HOME/state/system_state")


class InputWefSubscriptionsItemQueriesItem(CriblModel):

    path: str = Field(..., description="The Path attribute from the relevant XML Select element")
    queryExpression: str = Field(..., description="The XPath query inside the relevant XML Select element")


class InputWefTlsConf(CriblModel):
    """mTLS settings"""

    disabled: Optional[bool] = Field(None, description="Enable TLS")
    rejectUnauthorized: Optional[bool] = Field(None, description="Required for WEF certificate authentication")
    requestCert: Optional[bool] = Field(None, description="Required for WEF certificate authentication")
    certificateName: Optional[str] = Field(None, description="Name of the predefined certificate")
    privKeyPath: str = Field(..., description="Path on server containing the private key to use. PEM format. Can reference $ENV_VARS.")
    passphrase: Optional[str] = Field(None, description="Passphrase to use to decrypt private key")
    certPath: str = Field(..., description="Path on server containing certificates to use. PEM format. Can reference $ENV_VARS.")
    caPath: str = Field(..., description="Server path containing CA certificates (in PEM format) to use. Can reference $ENV_VARS. If multiple certificates are present in a .pem, each must directly certify the one preceding it.")
    commonNameRegex: Optional[str] = Field(None, description="Regex matching allowable common names in peer certificates' subject attribute")
    minVersion: Optional[str] = Field(None, description="Minimum TLS version")
    maxVersion: Optional[str] = Field(None, description="Maximum TLS version")
    ocspCheck: Optional[bool] = Field(None, description="Enable OCSP check of certificate")
    ocspCheckFailClose: Optional[bool] = Field(None, description="If enabled, checks will fail on any OCSP error. Otherwise, checks will fail only when a certificate is revoked, ignoring other errors.")


class InputWindowsMetricsHostConfCustomConfCpuConf(CriblModel):
    """Select the level of details for CPU metrics"""

    mode: Optional[str] = Field(None, description="Select the level of details for CPU metrics")
    perCpu: Optional[bool] = Field(None, description="Generate metrics for each CPU")
    detail: Optional[bool] = Field(None, description="Generate metrics for all CPU states")
    time: Optional[bool] = Field(None, description="Generate raw, monotonic CPU time counters")


class InputWindowsMetricsHostConfCustomConfDiskConf(CriblModel):
    """Select the level of details for disk metrics"""

    mode: Optional[str] = Field(None, description="Select the level of details for disk metrics")
    perVolume: Optional[bool] = Field(None, description="Generate separate metrics for each volume")
    detail: Optional[bool] = Field(None, description="Generate full disk metrics")
    volumes: Optional[list[str]] = Field(None, description="Windows volumes to include/exclude. E.g.: C:, !E:, etc. Wildcards and ! (not) operators are supported. All volumes are included if this list is empty.")


class InputWindowsMetricsHostConfCustomConfMemoryConf(CriblModel):
    """Select the level of details for memory metrics"""

    mode: Optional[str] = Field(None, description="Select the level of details for memory metrics")
    detail: Optional[bool] = Field(None, description="Generate metrics for all memory states")


class InputWindowsMetricsHostConfCustomConfNetworkConf(CriblModel):
    """Select the level of details for network metrics"""

    mode: Optional[str] = Field(None, description="Select the level of details for network metrics")
    detail: Optional[bool] = Field(None, description="Generate full network metrics")
    protocols: Optional[bool] = Field(None, description="Generate protocol metrics for ICMP, ICMPMsg, IP, TCP, UDP and UDPLite")
    devices: Optional[list[str]] = Field(None, description="Network interfaces to include/exclude. All interfaces are included if this list is empty.")
    perInterface: Optional[bool] = Field(None, description="Generate separate metrics for each interface")


class InputWindowsMetricsHostConfCustomConfSystemConf(CriblModel):
    """Select the level of details for system metrics"""

    mode: Optional[str] = Field(None, description="Select the level of details for system metrics")
    detail: Optional[bool] = Field(None, description="Generate metrics for all system information")


class InputWindowsMetricsPersistenceConf(CriblModel):
    """persistence"""

    enable: Optional[bool] = Field(None, description="Spool metrics to disk for Cribl Edge and Search")
    timeWindow: Optional[str] = Field(None, description="Time span for each file bucket")
    maxDataSize: Optional[str] = Field(None, description="Maximum disk space allowed to be consumed (examples: 420MB, 4GB). When limit is reached, older data will be deleted.")
    maxDataTime: Optional[str] = Field(None, description="Maximum amount of time to retain data (examples: 2h, 4d). When limit is reached, older data will be deleted.")
    compress: Optional[Literal['none', 'gzip']] = Field(None, description="Data compression format")
    destPath: Optional[str] = Field(None, description="Path to use to write metrics. Defaults to $CRIBL_HOME/state/windows_metrics")


class InputWizContentConfigItem(CriblModel):

    contentType: str = Field(..., description="The name of the Wiz query")
    contentDescription: Optional[str] = Field(None, description="Description")
    enabled: Optional[bool] = Field(None, description="Enable content")
    stateTracking: Optional[bool] = Field(None, description="Track collection progress between consecutive scheduled executions")
    stateUpdateExpression: Optional[str] = Field(None, description="JavaScript expression that defines how to update the state from an event. Use the event's data and the current state to compute the new state. See [Understanding State Expression Fields](https://docs.cribl.io/stream/collectors-rest#state-tracking-expression-fields) for more information.")
    stateMergeExpression: Optional[str] = Field(None, description="JavaScript expression that defines which state to keep when merging a task's newly reported state with previously saved state. Evaluates `prevState` and `newState` variables, resolving to the state to keep.")
    manageState: Optional[dict[str, Any]] = Field(None, description="Controls for viewing and managing the collector state.")
    contentQuery: str = Field(..., description="Template for POST body to send with the Collect request. Reference global variables, or functions using template params: `${C.vars.myVar}`, or `${Date.now()}`, `${param}`.")
    cronSchedule: str = Field(..., description="A cron schedule on which to run this job")
    earliest: str = Field(..., description="Earliest time, relative to now. Format supported: [+|-]@ (ex: -1hr, -42m, -42m@h)")
    latest: str = Field(..., description="Latest time, relative to now. Format supported: [+|-]@ (ex: -1hr, -42m, -42m@h)")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Units default to seconds if not specified. Enter 0 for unlimited time.")
    logLevel: Optional[Literal['error', 'warn', 'info', 'debug', 'silly']] = Field(None, description="Collector runtime log level")
    maxPages: Optional[float] = Field(None, description="Maximum number of pages to retrieve per collection task. Defaults to 0. Set to 0 to retrieve all pages.")


class KeyValueMetadataConfOutputFilesystem(CriblModel):

    key: str = Field(..., description="Key")
    value: str = Field(..., description="Value")


class LogLabelConfOutputGoogleCloudLogging(CriblModel):

    label: str = Field(..., description="Label name")
    valueExpression: str = Field(..., description="JavaScript expression to compute the label's value.")


class NameFieldType(CriblModel):
    """Reference to a field by its original text and parsed path segments."""

    raw: str = Field(..., description="Field name or expression before parsing.")
    path: list[float | str] = Field(..., description="Path segments for the field name. For example, [\"level1\", \"level2\"] represents level1.level2.")
    literal: Optional[bool] = Field(None, description="If true, raw is a constant value rather than a field to read from the event.")


class OauthHeaderConfInputServicenowTable(CriblModel):

    name: str = Field(..., description="OAuth header name")
    value: str = Field(..., description="OAuth header value")


class OauthParamConfInputKafka(CriblModel):

    name: str = Field(..., description="Parameter Name")
    value: str = Field(..., description="Parameter Value")


class OauthParamConfInputServicenowTable(CriblModel):

    name: str = Field(..., description="OAuth parameter name")
    value: str = Field(..., description="OAuth parameter value")


class OrphanFileRecoveryType(CriblModel):
    """Orphan file recovery"""

    disabled: Optional[bool] = Field(None, description="Periodically scan the staging directory for files not tracked by any Worker manifest to recover them")
    periodMin: Optional[float] = Field(None, description="Minimum interval between reconciliation runs")


class OutputAzureDataExplorerAdditionalPropertiesItem(CriblModel):

    key: str = Field(..., description="Key")
    value: str = Field(..., description="Value")


class OutputAzureDataExplorerCertificateConf(CriblModel):
    """Certificate credentials for OAuth authentication."""

    certificateName: Optional[str] = Field(None, description="The certificate you registered as credentials for your app in the Azure portal")


class OutputAzureDataExplorerExtentTagsItem(CriblModel):

    # values: dropBy=drop-by, ingestBy=ingest-by
    prefix: Optional[str] = Field(None, description="Prefix (optional)")
    value: str = Field(..., description="Value")


class OutputAzureDataExplorerIngestIfNotExistsItem(CriblModel):

    value: str = Field(..., description="Value")


class OutputChronicleCustomLabelsItem(CriblModel):

    key: str = Field(..., description="Key")
    value: str = Field(..., description="Value")
    rbacEnabled: Optional[bool] = Field(None, description="Designate this label for role-based access control and filtering")


class OutputElasticUrlsItem(CriblModel):

    url: str = Field(..., description="The URL to an Elastic node to send events to. Example: http://elastic:9200/_bulk")
    weight: Optional[float] = Field(None, description="Assign a weight (>0) to each endpoint to indicate its traffic-handling capability")
    xtemplate_url: Optional[str] = Field(None, alias="__template_url", description="Binds 'url' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'url' at runtime.")


class OutputGoogleChronicleExtraLogTypesItem(CriblModel):

    logType: str = Field(..., description="Log Type")
    description: Optional[str] = Field(None, description="Description")


class OutputLocalSearchStorageColumnMappingsItem(CriblModel):

    columnName: str = Field(..., description="Name of the column that will store field value")
    columnType: Optional[str] = Field(None, description="Type of the column in the database")
    columnValueExpression: str = Field(..., description="JavaScript expression to compute value to be inserted into the table")


class OutputLocalSearchStorageStatsDestinationConf(CriblModel):
    """Internal destination settings for batch metadata and statistics."""

    url: Optional[str] = Field(None, description="URL of the database that stores batch metadata and statistics.")
    database: Optional[str] = Field(None, description="Name of the database that stores batch metadata and statistics.")
    tableName: Optional[str] = Field(None, description="Name of the table that stores batch metadata and statistics.")
    authType: Optional[str] = Field(None, description="Authentication method for the statistics destination.")
    username: Optional[str] = Field(None, description="Username for the statistics destination.")
    sqlUsername: Optional[str] = Field(None, description="SQL username for the statistics destination.")
    password: Optional[str] = Field(None, description="Password for the statistics destination.")
    waitForAsyncInserts: Optional[bool] = Field(None, description="Whether to wait for asynchronous inserts to complete.")
    concurrency: Optional[float] = Field(None, description="Maximum number of concurrent requests to the statistics destination.")


class OutputMicrosoftFabricSaslConf(CriblModel):
    """Authentication parameters to use when connecting to bootstrap server. Using TLS is highly recommended."""

    disabled: bool = Field(..., description="Disabled")
    mechanism: Optional[Literal['plain', 'oauthbearer']] = Field(None, description="SASL mechanism")
    username: Optional[str] = Field(None, description="The username for authentication. This should always be $ConnectionString.")
    textSecret: Optional[str] = Field(None, description="Select or create a stored text secret corresponding to the SASL JASS Password Primary or Password Secondary")
    clientSecretAuthType: Optional[Literal['secret', 'certificate']] = Field(None, description="Authentication method")
    clientTextSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    certificateName: Optional[str] = Field(None, description="Select or create a stored certificate")
    certPath: Optional[str] = Field(None, description="Path to the client certificate file.")
    privKeyPath: Optional[str] = Field(None, description="Path to the client private key file.")
    passphrase: Optional[str] = Field(None, description="Passphrase used to decrypt the client private key.")
    oauthEndpoint: Optional[Literal['https://login.microsoftonline.com', 'https://login.microsoftonline.us', 'https://login.partner.microsoftonline.cn']] = Field(None, description="Endpoint used to acquire authentication tokens from Azure")
    clientId: Optional[str] = Field(None, description="client_id to pass in the OAuth request parameter")
    tenantId: Optional[str] = Field(None, description="Directory ID (tenant identifier) in Azure Active Directory")
    scope: Optional[str] = Field(None, description="Scope to pass in the OAuth request parameter")
    xtemplate_mechanism: Optional[str] = Field(None, alias="__template_mechanism", description="Binds 'mechanism' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'mechanism' at runtime.")
    xtemplate_oauthEndpoint: Optional[str] = Field(None, alias="__template_oauthEndpoint", description="Binds 'oauthEndpoint' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'oauthEndpoint' at runtime.")
    xtemplate_clientId: Optional[str] = Field(None, alias="__template_clientId", description="Binds 'clientId' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'clientId' at runtime.")
    xtemplate_tenantId: Optional[str] = Field(None, alias="__template_tenantId", description="Binds 'tenantId' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'tenantId' at runtime.")
    xtemplate_scope: Optional[str] = Field(None, alias="__template_scope", description="Binds 'scope' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'scope' at runtime.")


class OutputNetflowHostsItem(CriblModel):

    host: str = Field(..., description="Destination host")
    port: float = Field(..., description="Destination port, default is 2055")
    xtemplate_host: Optional[str] = Field(None, alias="__template_host", description="Binds 'host' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'host' at runtime.")
    xtemplate_port: Optional[str] = Field(None, alias="__template_port", description="Binds 'port' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'port' at runtime.")


class OutputNewrelicMetadataItem(CriblModel):

    name: str = Field(..., description="Name of the metadata field.")
    value: str = Field(..., description="JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)")


class OutputRouterRulesItem(CriblModel):

    filter: str = Field(..., description="JavaScript expression to select events to send to output")
    output: str = Field(..., description="Output to send matching events to")
    description: Optional[str] = Field(None, description="Description of this rule's purpose")
    final: Optional[bool] = Field(None, description="Flag to control whether to stop the event from being checked against other rules")


class OutputSnmpHostsItem(CriblModel):

    host: str = Field(..., description="Destination host")
    port: float = Field(..., description="Destination port, default is 162")
    xtemplate_host: Optional[str] = Field(None, alias="__template_host", description="Binds 'host' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'host' at runtime.")
    xtemplate_port: Optional[str] = Field(None, alias="__template_port", description="Binds 'port' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'port' at runtime.")


class OutputSnowflakeStreamingPemConf(CriblModel):
    """Private key"""

    keyName: str = Field(..., description="Select the stored secret containing the RSA private key (PEM format) for Snowflake key-pair authentication")


class OutputSplunkHecUrlsItem(CriblModel):

    url: str = Field(..., description="URL to a Splunk HEC endpoint to send events to, e.g., http://localhost:8088/services/collector/event")
    weight: Optional[float] = Field(None, description="Assign a weight (>0) to each endpoint to indicate its traffic-handling capability")
    xtemplate_url: Optional[str] = Field(None, alias="__template_url", description="Binds 'url' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'url' at runtime.")


class OutputSplunkLbIndexerDiscoveryConfigsConfAuthTokensItem(CriblModel):

    authType: Optional[Literal['manual', 'secret']] = Field(None, description="Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate")
    authToken: Optional[str] = Field(None, description="Shared secret to be provided by any client (in authToken header field). If empty, unauthorized access is permitted.")
    textSecret: Optional[str] = Field(None, description="Select or create a stored text secret")


class OutputWebhookUrlsItem(CriblModel):

    url: str = Field(..., description="URL of a webhook endpoint to send events to, such as http://localhost:10200")
    weight: Optional[float] = Field(None, description="Assign a weight (>0) to each endpoint to indicate its traffic-handling capability")
    xtemplate_url: Optional[str] = Field(None, alias="__template_url", description="Binds 'url' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'url' at runtime.")


class OutputXsiamUrlsItem(CriblModel):

    weight: Optional[float] = Field(None, description="Assign a weight (>0) to each endpoint to indicate its traffic-handling capability")


class PatternListConfSerdeTypeGrok(CriblModel):

    pattern: str = Field(..., description="Grok pattern to extract fields. Syntax supported: %{PATTERN_NAME:FIELD_NAME}")


class PqType(CriblModel):
    """Persistent queue settings for this Source."""

    # values: smart=Smart (Deprecated), always=Always On
    mode: Optional[Literal['smart', 'always']] = Field(None, description="With Smart mode (deprecated), PQ will write events to the filesystem only when it detects backpressure from the processing engine. Smart mode will have no new development starting July 2026, followed by End of Support and feature removal (auto-migrating to Always On) in January 2027. We recommend using Always On mode instead. With Always On mode, PQ will always write events directly to the queue before forwarding them to the processing engine.")
    maxBufferSizeBytes: Optional[str] = Field(None, description="The maximum size to hold in memory before writing events to disk. Enter a numeral with units of KB, MB, etc. The minimum value is 64KB and the maximum value is 10MB.")
    maxBufferSize: Optional[float] = Field(None, description="Maximum number of events to hold in memory before writing the events to disk. Deprecated and only supported in workers < v4.17.0. Use maxBufferSizeBytes instead.")
    commitFrequency: Optional[float] = Field(None, description="The number of events to send downstream before committing that Stream has read them. Lower values increase cursor-write IOPS and can add disk pressure, including on shared storage.")
    maxFileSize: Optional[str] = Field(None, description="The maximum size to store in each queue file before closing and optionally compressing. Enter a numeral with units of KB, MB, etc.")
    maxSize: Optional[str] = Field(None, description="The maximum disk space that the queue can consume (as an average per Worker Process) before queueing stops. Enter a numeral with units of KB, MB, etc.")
    path: Optional[str] = Field(None, description="The location for the persistent queue files. To this field's value, the system will append: //inputs/")
    compress: Optional[Literal['none', 'gzip']] = Field(None, description="Codec to use to compress the persisted data")
    # values: drop=Drop new data
    onBackpressure: Optional[Literal['block', 'drop']] = Field(None, description="Whether to block or drop events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged.")
    pqControls: Optional[dict[str, Any]] = Field(None, description="Management controls for the persistent queue.")


class PreprocessType(CriblModel):
    """Optional preprocessing step that pipes collected data through an external command before ingestion."""

    disabled: bool = Field(..., description="Disabled")
    command: Optional[str] = Field(None, description="Command to feed the data through (via stdin) and process its output (stdout)")
    args: Optional[list[str]] = Field(None, description="Arguments to be added to the custom command")


class PrometheusAuthType(CriblModel):
    """Authentication settings for Grafana Cloud requests."""

    # values: token=Auth token, textSecret=Auth token (text secret), credentialsSecret=Basic (credentials secret)
    authType: Optional[Literal['none', 'token', 'textSecret', 'basic', 'credentialsSecret']] = Field(None, description="Authentication type")
    token: Optional[str] = Field(None, description="Bearer token to include in the authorization header. In Grafana Cloud, this is generally built by concatenating the username and the API key, separated by a colon. Example: :")
    textSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    username: Optional[str] = Field(None, description="Username for authentication")
    password: Optional[str] = Field(None, description="Password (API key in Grafana Cloud domain) for authentication")
    credentialsSecret: Optional[str] = Field(None, description="Select or create a secret that references your credentials")


class RefreshRequestParamConfHealthCheckAuthenticationOauthSecret(CriblModel):

    name: str = Field(..., description="Name")
    value: str = Field(..., description="Value")


class RegexListConfSerdeTypeRegex(CriblModel):

    regex: str = Field(..., description="Regex literal with named capturing groups, such as (?bar), or _NAME_ and _VALUE_ capturing groups, such as (?[^ =]+)=(?[^,]+)")


class RetryRulesType(CriblModel):
    """HTTP retry behavior for failed collection requests."""

    # values: none=Disabled
    type: Literal['none', 'backoff', 'static'] = Field(..., description="The algorithm to use when performing HTTP retries")
    interval: Optional[float] = Field(None, description="Time interval between failed request and first retry (kickoff). Maximum allowed value is 20,000 ms (1/3 minute).")
    limit: Optional[float] = Field(None, description="The maximum number of times to retry a failed HTTP request")
    multiplier: Optional[float] = Field(None, description="Base for exponential backoff, e.g., base 2 means that retries will occur after 2, then 4, then 8 seconds, and so on")
    codes: Optional[list[float]] = Field(None, description="List of HTTP codes that trigger a retry. Leave empty to use the default list of 429 and 503.")
    enableHeader: Optional[bool] = Field(None, description="Honor any Retry-After header that specifies a delay (in seconds) or a timestamp after which to retry the request. The delay is limited to 20 seconds, even if the Retry-After header specifies a longer delay. When disabled, all Retry-After headers are ignored.")
    retryConnectTimeout: Optional[bool] = Field(None, description="Make a single retry attempt when a connection timeout (ETIMEDOUT) error occurs")
    retryConnectReset: Optional[bool] = Field(None, description="Retry request when a connection reset (ECONNRESET) error occurs")


class RetryRulesTypeFailed(CriblModel):
    """HTTP retry behavior for failed collection requests."""

    # values: none=Disabled
    type: Literal['none', 'backoff', 'static'] = Field(..., description="The algorithm to use when performing HTTP retries")
    interval: Optional[float] = Field(None, description="Time interval between failed request and first retry (kickoff). Maximum allowed value is 20,000 ms (1/3 minute).")
    limit: Optional[float] = Field(None, description="The maximum number of times to retry a failed HTTP request")
    multiplier: Optional[float] = Field(None, description="Base for exponential backoff, e.g., base 2 means that retries will occur after 2, then 4, then 8 seconds, and so on")
    codes: Optional[list[float]] = Field(None, description="List of http codes that trigger a retry. Leave empty to use the default list of 429, 500, and 503.")
    enableHeader: Optional[bool] = Field(None, description="Honor any Retry-After header that specifies a delay (in seconds) or a timestamp after which to retry the request. The delay is limited to 20 seconds, even if the Retry-After header specifies a longer delay. When disabled, all Retry-After headers are ignored.")
    retryConnectTimeout: Optional[bool] = Field(None, description="Make a single retry attempt when a connection timeout (ETIMEDOUT) error occurs")
    retryConnectReset: Optional[bool] = Field(None, description="Retry request when a connection reset (ECONNRESET) error occurs")


class RetrySettingsType(CriblModel):
    """Retry settings for failed file uploads."""

    enabled: Optional[bool] = Field(None, description="Apply exponential backoff with jitter when file uploads fail repeatedly.")
    initialBackoffMs: Optional[float] = Field(None, description="Initial delay before first retry attempt. Valid range: 1s-5min (1000-300000ms). Values outside this range will be clamped to the nearest valid value.")
    backoffMultiplier: Optional[float] = Field(None, description="Multiplier applied to backoff delay after each retry. Valid range: 1-10. Values outside this range will be clamped to the nearest valid value.")
    maxBackoffMs: Optional[float] = Field(None, description="Maximum delay between retry attempts. Valid range: 1s-10min (1000-600000ms). Values outside this range will be clamped to the nearest valid value.")
    jitterPercent: Optional[float] = Field(None, description="Random jitter percentage added to backoff delay to prevent thundering herd. Valid range: 0-100. Values outside this range will be clamped to the nearest valid value.")


class RootNodeConfRedisDeploymentTypeCluster(CriblModel):

    host: str = Field(..., description="Hostname of cluster node. Must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at init time. Example referencing a Global Variable: `myBucket-${C.vars.myVar}`.")
    port: float = Field(..., description="Port of cluster node")


class RuleConfInputKubeMetrics(CriblModel):

    filter: str = Field(..., description="JavaScript expression applied to Kubernetes objects. Return 'true' to include it.")
    description: Optional[str] = Field(None, description="Optional description of this rule's purpose")


class SaslExtensionConfInputKafka(CriblModel):

    name: str = Field(..., description="Field Name")
    value: str = Field(..., description="Field Value")


class SearchFilterConfInputPrometheus(CriblModel):

    Name: str = Field(..., description="See https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html for information. Attributes can be manually entered if not present in the list.")
    Values: list[str] = Field(..., description="Values to match within this row's attribute. If empty, search will return only running EC2 instances.")


class SetConfInputSystemMetrics(CriblModel):

    name: str = Field(..., description="Set Name")
    filter: str = Field(..., description="Filter Expression")
    includeChildren: Optional[bool] = Field(None, description="Include Child Processes")


class TimestampFormatTypeEventBreakerExistingOrNewNew(CriblModel):
    """Configuration for extracting and parsing timestamps from events."""

    type: Literal['auto', 'format', 'current'] = Field(..., description="Method to use for timestamp extraction. Use auto for automatic detection, format to specify a strptime format, or current to use the current system time.")
    length: Optional[float] = Field(None, description="Maximum number of characters to search for a timestamp value from the beginning of the match.")
    format: Optional[str] = Field(None, description="Strptime format string for parsing timestamps (for example, %Y-%m-%d %H:%M:%S).")


class TlsOptionsTypeRedisDeploymentTypeStandalone(CriblModel):
    """TLS settings for encrypting the connection to Redis."""

    rejectUnauthorized: Optional[bool] = Field(None, description="Reject certificates that are not authorized by a CA in the 'CA certificate path', or by another trusted CA (such as the system's CA)")
    servername: Optional[str] = Field(None, description="Server name for the SNI (Server Name Indication) TLS extension. Must be a host name, not an IP address.")
    certificateName: Optional[str] = Field(None, description="The name of the predefined certificate")
    caPath: Optional[str] = Field(None, description="Path on client in which to find CA certificates to verify the server's certificate. PEM format. Can reference $ENV_VARS.")
    privKeyPath: Optional[str] = Field(None, description="Path on client in which to find the private key to use. PEM format. Can reference $ENV_VARS.")
    certPath: Optional[str] = Field(None, description="Path on client in which to find certificates to use. PEM format. Can reference $ENV_VARS.")
    passphrase: Optional[str] = Field(None, description="Passphrase to use to decrypt private key")
    minVersion: Optional[Literal['TLSv1', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3']] = Field(None, description="Minimum TLS version to use when connecting")
    maxVersion: Optional[Literal['TLSv1', 'TLSv1.1', 'TLSv1.2', 'TLSv1.3']] = Field(None, description="Maximum TLS version to use when connecting")


class AuthType(CriblModel):
    """Credentials to use when authenticating with the schema registry"""

    disabled: bool = Field(..., description="Disabled")
    oauthEnabled: Optional[bool] = Field(None, description="Authenticate with the schema registry using OAuth instead of basic HTTP authentication")
    tokenUrl: Optional[str] = Field(None, description="URL of the token endpoint to use for OAuth authentication")
    clientId: Optional[str] = Field(None, description="Client ID to use for OAuth authentication")
    oauthSecretType: Optional[str] = Field(None, description="Source of the OAuth client secret.")
    clientTextSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    oauthParams: Optional[list[OauthParamConfInputKafka]] = Field(None, description="Additional fields to send to the token endpoint, such as scope or audience")
    identityPoolId: Optional[str] = Field(None, description="Confluent Cloud identity pool ID. Sent as the `Confluent-Identity-Pool-Id` header on requests to the schema registry.")
    logicalCluster: Optional[str] = Field(None, description="Confluent Cloud Schema Registry logical cluster ID. Sent as the `target-sr-cluster` header on requests to the schema registry.")
    credentialsSecret: Optional[str] = Field(None, description="Select or create a secret that references your credentials")
    xtemplate_tokenUrl: Optional[str] = Field(None, alias="__template_tokenUrl", description="Binds 'tokenUrl' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'tokenUrl' at runtime.")
    xtemplate_clientId: Optional[str] = Field(None, alias="__template_clientId", description="Binds 'clientId' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'clientId' at runtime.")
    xtemplate_identityPoolId: Optional[str] = Field(None, alias="__template_identityPoolId", description="Binds 'identityPoolId' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'identityPoolId' at runtime.")
    xtemplate_logicalCluster: Optional[str] = Field(None, alias="__template_logicalCluster", description="Binds 'logicalCluster' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'logicalCluster' at runtime.")


class FunctionConfSchemaAggregateMetrics(CriblModel):

    passthrough: Optional[bool] = Field(None, description="Pass through the original events along with the aggregation events")
    preserveGroupBys: Optional[bool] = Field(None, description="Preserve the structure of the original aggregation event's groupby fields")
    sufficientStatsOnly: Optional[bool] = Field(None, description="Output only statistics that are sufficient for the supplied aggregations")
    prefix: Optional[str] = Field(None, description="A prefix that is prepended to all of the fields output by this Aggregations Function")
    timeWindow: Optional[str] = Field(None, description="The time span of the tumbling window for aggregating events. Must be a valid time string (such as 10s).")
    aggregations: Optional[list[FunctionConfSchemaAggregateMetricsAggregationsItem]] = Field(None, description="Combination of Aggregation function and output metric type")
    groupbys: Optional[list[str]] = Field(None, description="Optional: One or more dimensions to group aggregates by. Supports wildcard expressions. Wrap dimension names in quotes if using literal identifiers, such as 'service.name'. Warning: Using wildcard '*' causes all dimensions in the event to be included, which can result in high cardinality and increased memory usage. Exclude dimensions that can result in high cardinality before using wildcards. Example: !_time, !_numericValue, *")
    flushEventLimit: Optional[float] = Field(None, description="The maximum number of events to include in any given aggregation event")
    flushMemLimit: Optional[str] = Field(None, description="The memory usage limit to impose upon aggregations. Defaults to 80% of the process memory; value configured above default limit is ignored. Accepts numerals with units like KB and MB (example: 128MB).")
    cumulative: Optional[bool] = Field(None, description="Enable to retain aggregations for cumulative aggregations when flushing out an aggregation table event. When disabled (the default), aggregations are reset to 0 on flush.")
    shouldTreatDotsAsLiterals: Optional[bool] = Field(None, description="Treat dots in dimension names as literals. This is useful for top-level dimensions that contain dots, such as 'service.name'.")
    add: Optional[list[FunctionConfSchemaAggregateMetricsAddItem]] = Field(None, description="Set of key-value pairs to evaluate and add/set")
    flushOnInputClose: Optional[bool] = Field(None, description="Flush aggregations when an input stream is closed. If disabled, Time Window Settings control flush behavior.")
    lagTolerance: Optional[str] = Field(None, description="The tumbling window tolerance to late events. Must be a valid time string (such as 10s). Defaults to the smaller of Time Window and 1 minute.")
    idleTimeLimit: Optional[str] = Field(None, description="How long to wait before flushing a bucket that has not received events. Must be a valid time string (such as 10s). Defaults to the smaller of Time Window and 1 minute.")


class FunctionConfSchemaAggregation(CriblModel):

    passthrough: Optional[bool] = Field(None, description="Pass through the original events along with the aggregation events")
    preserveGroupBys: Optional[bool] = Field(None, description="Preserve the structure of the original aggregation event's groupby fields")
    sufficientStatsOnly: Optional[bool] = Field(None, description="Output only statistics that are sufficient for the supplied aggregations")
    metricsMode: Optional[bool] = Field(None, description="Enable to output the aggregates as metrics. When disabled, aggregates are output as events.")
    prefix: Optional[str] = Field(None, description="A prefix that is prepended to all of the fields output by this Aggregations Function")
    timeWindow: Optional[str] = Field(None, description="The time span of the tumbling window for aggregating events. Must be a valid time string (such as 10s).")
    aggregations: Optional[list[str]] = Field(None, description="Aggregate function to perform on events. Example: sum(bytes).where(action=='REJECT').as(TotalBytes)")
    groupbys: Optional[list[str]] = Field(None, description="Optional: One or more fields to group aggregates by. Supports wildcard expressions. Warning: Using wildcard '*' causes all fields in the event to be included, which can result in high cardinality and increased memory usage. Exclude fields that can result in high cardinality before using wildcards. Example: !_time, !_numericValue, *")
    flushEventLimit: Optional[float] = Field(None, description="The maximum number of events to include in any given aggregation event")
    flushMemLimit: Optional[str] = Field(None, description="The memory usage limit to impose upon aggregations. Defaults to 80% of the process memory; value configured above default limit is ignored. Accepts numerals with units like KB and MB (example: 128MB).")
    cumulative: Optional[bool] = Field(None, description="Enable to retain aggregations for cumulative aggregations when flushing out an aggregation table event. When disabled (the default), aggregations are reset to 0 on flush.")
    searchAggMode: Optional[str] = Field(None, description="Allows Cribl Search-specific aggregation configuration")
    add: Optional[list[FunctionConfSchemaAggregationAddItem]] = Field(None, description="Set of key-value pairs to evaluate and add/set")
    shouldTreatDotsAsLiterals: Optional[bool] = Field(None, description="Treat dots in dimension names as literals. This is useful for top-level dimensions that contain dots, such as 'service.name'.")
    flushOnInputClose: Optional[bool] = Field(None, description="Flush aggregations when an input stream is closed. If disabled, Time Window Settings control flush behavior.")
    printUndefineds: Optional[bool] = Field(None, description="When enabled (e.g. for Cribl Search), convert undefined expression results to null so requested-but-missing fields appear in JSON output. When disabled (default), undefined is preserved.")
    lagTolerance: Optional[str] = Field(None, description="The tumbling window tolerance to late events. Must be a valid time string (such as 10s). Defaults to the smaller of Time Window and 1 minute.")
    idleTimeLimit: Optional[str] = Field(None, description="How long to wait before flushing a bucket that has not received events. Must be a valid time string (such as 10s). Defaults to the smaller of Time Window and 1 minute.")


class FunctionConfSchemaAutoTimestamp(CriblModel):

    srcField: Optional[str] = Field(None, description="Field to search for a timestamp")
    dstField: Optional[str] = Field(None, description="Field to place timestamp in")
    defaultTimezone: Optional[str] = Field(None, description="Timezone to assign to timestamps without timezone info")
    timeExpression: Optional[str] = Field(None, description="Expression to use to format time. Current time, as a JavaScript Date object, is in global `time`. You can access other fields' values via __e..")
    offset: Optional[float] = Field(None, description="The offset into the string from which to look for a timestamp")
    maxLen: Optional[float] = Field(None, description="Maximum string length at which to look for a timestamp")
    # values: now=Current Time, last=Last Event's Time
    defaultTime: Optional[str] = Field(None, description="How to set the time field if no timestamp is found")
    latestDateAllowed: Optional[str] = Field(None, description="The latest timestamp value allowed relative to now, such as +42days. Parsed values after this date will be set to the Default time.")
    spacer: Optional[str] = Field(None, description="UI layout spacer; no effect on event processing.")
    earliestDateAllowed: Optional[str] = Field(None, description="The earliest timestamp value allowed relative to now, such as -42years. Parsed values prior to this date will be set to the Default time.")
    timestamps: Optional[list[FunctionConfSchemaAutoTimestampTimestampsItem]] = Field(None, description="Add regex/strptime pairs to extract additional timestamp formats")


class FunctionConfSchemaCef(CriblModel):

    outputField: Optional[str] = Field(None, description="The field to which the CEF formatted event will be output")
    header: Optional[list[FunctionConfSchemaCefHeaderItem]] = Field(None, description="Set of header key/value pairs")
    extension: Optional[list[FunctionConfSchemaCefExtensionItem]] = Field(None, description="Set of extension key-value pairs")


class FunctionConfSchemaDetectionRulesLocalOverridesConf(CriblModel):
    """Instance-level tuning applied after the rule set is merged. Managed by Cribl Security; not intended for direct editing."""

    disabled: Optional[list[str]] = Field(None, description="Rule IDs to silence entirely.")
    fieldOverrides: Optional[list[FunctionConfSchemaDetectionRulesLocalOverridesConfFieldOverridesItem]] = Field(None, description="Patch scalar fields of a rule without copying its full definition.")
    inlineRules: Optional[list[FunctionConfSchemaDetectionRulesLocalOverridesConfInlineRulesItem]] = Field(None, description="Full rule definitions authored here rather than delivered with the corpus.")


class FunctionConfSchemaDnsLookup(CriblModel):

    dnsLookupFields: Optional[list[FunctionConfSchemaDnsLookupDnsLookupFieldsItem]] = Field(None, description="List of field names on which to perform DNS lookup")
    reverseLookupFields: Optional[list[FunctionConfSchemaDnsLookupReverseLookupFieldsItem]] = Field(None, description="List of field names on which to perform reverse DNS lookup")
    dnsServers: Optional[list[str]] = Field(None, description="IPs, in RFC 5952 format, of the DNS servers to use for resolution. Examples: IPv4 1.1.1.1, 4.2.2.2:53, or IPv6 [2001:4860:4860::8888], [2001:4860:4860::8888]:1053. If not specified, system's DNS will be used.")
    cacheTTL: Optional[float] = Field(None, description="How frequently to expire and refetch DNS cache. Use 0 to disable.")
    maxCacheSize: Optional[float] = Field(None, description="The maximum number of DNS resolutions to be cached locally. Leave at default unless you understand the implications of changing.")
    useResolvConf: Optional[bool] = Field(None, description="Attempt to resolve DNS short names using the search or domain directive from /etc/resolv.conf")
    lookupFallback: Optional[bool] = Field(None, description="If unable to resolve a DNS short name, make a DNS.lookup() call to resolve it. Caution: This might degrade performance in unrelated areas of @{product}.")
    domainOverrides: Optional[list[str]] = Field(None, description="Specify fallback values for the DNS resolver to use when it cannot resolve a DNS short name")
    lookupFailLogLevel: Optional[str] = Field(None, description="Log level to use when a DNS lookup fails.")


class FunctionConfSchemaEval(CriblModel):

    add: Optional[list[FunctionConfSchemaEvalAddItem]] = Field(None, description="Set of key-value pairs to evaluate and add/set")
    keep: Optional[list[str]] = Field(None, description="List of fields to keep. Supports * wildcards. Takes precedence over 'Remove fields'.")
    remove: Optional[list[str]] = Field(None, description="List of fields to remove. Supports * wildcards. Fields that match 'Keep fields' will not be removed. Enclose field names containing special characters in single or double quotes.")
    printUndefineds: Optional[bool] = Field(None, description="When enabled (e.g. for Cribl Search), convert undefined expression results to null so requested-but-missing fields appear in JSON output. When disabled (default), undefined is preserved.")


class FunctionConfSchemaEventBreaker(CriblModel):

    # values: existing=Use Existing, new=Create New
    existingOrNew: Optional[str] = Field(None, description="Whether to use an existing event breaker ruleset or create a new one inline.")
    shouldMarkCriblBreaker: Optional[bool] = Field(None, description="Add this Function name to the cribl_breaker field")
    # values: json=JSON Newline Delimited, header=File Header, aws_vpcflow=AWS VPC Flow Log, azure_flowlog=Azure VNet Flow Log
    ruleType: Optional[Literal['regex', 'json', 'json_array', 'header', 'timestamp', 'csv', 'aws_cloudtrail', 'aws_vpcflow', 'azure_flowlog']] = Field(None, description="Type of event-breaking rule to apply when creating a new inline ruleset.")
    maxEventBytes: Optional[float] = Field(None, description="The maximum number of bytes that an event can be before being flushed to the Pipelines")
    timestampAnchorRegex: Optional[str] = Field(None, description="Regex to match before attempting timestamp extraction. Use $ (end of string anchor) to not perform extraction.")
    timestamp: Optional[TimestampFormatTypeEventBreakerExistingOrNewNew] = Field(None, description="Configuration for extracting and parsing timestamps from events.")
    timestampTimezone: Optional[str] = Field(None, description="Timezone to assign to timestamps without timezone info")
    timestampEarliest: Optional[str] = Field(None, description="The earliest timestamp value allowed relative to now, such as -42years. Parsed values prior to this date will be set to current time.")
    timestampLatest: Optional[str] = Field(None, description="The latest timestamp value allowed relative to now, such as +42days. Parsed values after this date will be set to current time.")
    existingRule: Optional[str] = Field(None, description="ID of an existing event breaker ruleset to apply.")


class FunctionConfSchemaGeoip(CriblModel):

    file: Optional[str] = Field(None, description="Select an uploaded Maxmind database, or specify path to a Maxmind database with .mmdb extension")
    inField: Optional[str] = Field(None, description="Field name in which to find an IP to look up. Can be nested.")
    outField: Optional[str] = Field(None, description="Field name in which to store the GeoIP lookup results")
    additionalFields: Optional[list[FunctionConfSchemaGeoipAdditionalFieldsItem]] = Field(None, description="Additional IP fields on which to perform GeoIP lookups.")
    outFieldMappings: Optional[dict[str, Any]] = Field(None, description="Search-specific mappings for granular control over event enrichment")


class FunctionConfSchemaGrok(CriblModel):

    pattern: Optional[str] = Field(None, description="Grok pattern to extract fields. Syntax supported: %{PATTERN_NAME:FIELD_NAME}")
    patternList: Optional[list[PatternListConfSerdeTypeGrok]] = Field(None, description="Additional Grok patterns to apply to the source field.")
    source: Optional[str] = Field(None, description="Field on which to perform Grok extractions")


class FunctionConfSchemaHandlebars(CriblModel):

    templates: Optional[list[FunctionConfSchemaHandlebarsTemplatesItem]] = Field(None, description="Array of template definitions. Uses event.__template_id to select template at runtime.")
    targetField: Optional[str] = Field(None, description="Field name to store the rendered template result. Defaults to _raw.")
    parseJson: Optional[bool] = Field(None, description="Parse the rendered template as JSON and store as an object instead of a string. Useful for building structured data like Slack blocks.")
    removeOnNull: Optional[bool] = Field(None, description="Remove the target field if the rendered result is empty or null.")


class FunctionConfSchemaJoin(CriblModel):
    """Join Configuration"""

    kind: Optional[str] = Field(None, description="Join kind, e.g. inner")
    hints: Optional[dict[str, Any]] = Field(None, description="Hints passed to the join function")
    fieldConditions: Optional[list[FunctionConfSchemaJoinFieldConditionsItem]] = Field(None, description="Fields to use when joining")
    searchJobId: Optional[str] = Field(None, description="The id for this search job.")
    stageId: Optional[str] = Field(None, description="The stage we are joining with.")


class FunctionConfSchemaLookup(CriblModel):

    file: Optional[str] = Field(None, description="Path to the lookup file. Reference environment variables via $. Example: $HOME/file.csv")
    dbLookup: Optional[bool] = Field(None, description="Enable to use a disk-based lookup. This option displays only the settings relevant to disk-based mode and hides those for in-memory lookups.")
    matchMode: Optional[str] = Field(None, description="Specifies the matching method based on the format and logic used in the lookup file")
    matchType: Optional[str] = Field(None, description="Further defines how to handle multiple matches: return the first match, the most specific match, or all matches")
    reloadPeriodSec: Optional[float] = Field(None, description="Checks the lookup file periodically for changes and reloads it if modified. Set to -1 to disable reloading (default). Useful for lookups not managed by Stream or not updated by an external process. [Learn more](https://docs.cribl.io/stream/lookup-function/#advanced-settings)")
    inFields: Optional[list[FunctionConfSchemaLookupInFieldsItem]] = Field(None, description="Fields that should be used to key into the lookup table")
    outFields: Optional[list[FunctionConfSchemaLookupOutFieldsItem]] = Field(None, description="Fields to add to events after matching lookup. Defaults to all if not specified.")
    addToEvent: Optional[bool] = Field(None, description="Add the looked-up values to _raw, as key=value pairs")
    ignoreCase: Optional[bool] = Field(None, description="Whether to ignore case when performing lookups using Match Mode: Regex.")


class FunctionConfSchemaMask(CriblModel):

    rules: Optional[list[FunctionConfSchemaMaskRulesItem]] = Field(None, description="List of masking rules, each specifying a regex to match and an expression to replace matched content.")
    fields: Optional[list[str]] = Field(None, description="Fields on which to apply the masking rules. Supports * wildcards, except when used on internal fields.")
    depth: Optional[int] = Field(None, description="Depth to which the Mask Function will search for fields to mask")
    flags: Optional[list[FunctionConfSchemaMaskFlagsItem]] = Field(None, description="Fields to evaluate if one or more masking rules are matched")


class FunctionConfSchemaMetricsExport(CriblModel):
    """Metrics export Configuration"""

    searchJobId: Optional[str] = Field(None, description="Unique identifier for the Search Job that runs this Function.")
    dataset: Optional[str] = Field(None, description="Unique identifier for the metrics Dataset.")
    nameField: Optional[NameFieldType] = Field(None, description="Reference to a field by its original text and parsed path segments.")
    timeField: Optional[NameFieldType] = Field(None, description="Reference to a field by its original text and parsed path segments.")
    valueField: Optional[NameFieldType] = Field(None, description="Reference to a field by its original text and parsed path segments.")
    typeField: Optional[NameFieldType] = Field(None, description="Reference to a field by its original text and parsed path segments.")
    labelFields: Optional[Any] = Field(None, description="Field references to attach as labels to each exported metric. Specify one field or a list of fields.")
    tee: Optional[bool] = Field(None, description="If true, pass processed events to downstream Functions. If false, emit export statistics.")
    flushMs: Optional[float] = Field(None, description="Interval, in milliseconds, between export statistics updates.")
    suppressPreviews: Optional[bool] = Field(None, description="If true, emit export statistics only when processing completes. If false, emit periodic statistics.")


class FunctionConfSchemaNotificationPoliciesPoliciesItem(CriblModel):

    id: str = Field(..., description="Unique identifier for this policy")
    disabled: Optional[bool] = Field(None, description="If true, this policy will be skipped during evaluation")
    waitToGroup: Optional[int] = Field(None, description="Time to wait (in minutes) to group similar alerts before sending")
    groupByLabels: Optional[list[str]] = Field(None, description="Event fields to use for grouping")
    conditions: Optional[list[list[Any]]] = Field(None, description="List of conditions. If ANY condition matches (OR), the policy applies. Each condition is a list of tags that must ALL match (AND).")
    templateTargetPairs: list[FunctionConfSchemaNotificationPoliciesPoliciesItemTemplateTargetPairsItem] = Field(..., description="List of targets to route to and the templates to use")
    final: Optional[bool] = Field(None, description="If true, stop evaluating further policies after this one matches")
    order: int = Field(..., description="Evaluation order of this policy (lower numbers evaluated first)")


class FunctionConfSchemaPublishMetrics(CriblModel):

    fields: Optional[list[FunctionConfSchemaPublishMetricsFieldsItem]] = Field(None, description="List of metrics from event to extract and format. Formatted metrics can be used by a destination to pass metrics to a metrics aggregation platform.")
    overwrite: Optional[bool] = Field(None, description="Overwrite previous metric specs. Leave disabled to append.")
    dimensions: Optional[list[str]] = Field(None, description="Optional list of dimensions to include in events. Wildcards supported. If you don't specify metrics, values will be appended to every metric found in the event. When you add a new metric, dimensions will be present only in those new metrics.")
    removeMetrics: Optional[list[str]] = Field(None, description="Optional list of metric field names to look for when removing metrics. When a metric's field name matches an element in this list, the metric will be removed from the event.")
    removeDimensions: Optional[list[str]] = Field(None, description="Optional list of dimensions to remove from every metric found in the event. Wildcards supported.")


class FunctionConfSchemaRedis(CriblModel):

    commands: Optional[list[FunctionConfSchemaRedisCommandsItem]] = Field(None, description="List of Redis commands to execute against the specified keys.")
    deploymentType: Optional[str] = Field(None, description="How the Redis server is configured. Defaults to Standalone")
    # values: credentialsSecret=User Secret, textSecret=Admin Secret
    authType: Optional[str] = Field(None, description="Authentication method to use when connecting to Redis.")
    maxBlockSecs: Optional[float] = Field(None, description="Maximum amount of time (seconds) to wait before assuming that Redis is down and passing events through. Use 0 to disable.")
    enableClientSideCaching: Optional[bool] = Field(None, description="Enable client-side cache. Redundant when using Redis write operations. See more options at Settings > General > Limits > Redis Cache.")
    url: Optional[str] = Field(None, description="Redis URL to connect to. Format: redis[s]://[[user][:password@]][host][:port][/db-number][?db=db-number[&password=bar[&option=value]]]. Must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at init time. Example referencing a Global Variable: `myBucket-${C.vars.myVar}`")
    xtemplate_url: Optional[str] = Field(None, alias="__template_url", description="Binds 'url' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'url' at runtime.")
    tlsOptions: Optional[TlsOptionsTypeRedisDeploymentTypeStandalone] = Field(None, description="TLS settings for encrypting the connection to Redis.")
    rootNodes: Optional[list[RootNodeConfRedisDeploymentTypeCluster]] = Field(None, description="Root nodes to which the cluster connection should be initiated")
    tls: Optional[bool] = Field(None, description="Use TLS for connections to this cluster")
    # values: master=Masters, replica=Replicas, all=Masters and Replicas
    scaleReads: Optional[Literal['master', 'replica', 'all']] = Field(None, description="Which nodes read commands should be sent to")
    masterName: Optional[str] = Field(None, description="Name of the Redis Sentinel master group to connect to.")
    username: Optional[str] = Field(None, description="Username for Redis authentication.")
    xtemplate_username: Optional[str] = Field(None, alias="__template_username", description="Binds 'username' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'username' at runtime.")
    password: Optional[str] = Field(None, description="Password for Redis authentication.")
    xtemplate_password: Optional[str] = Field(None, alias="__template_password", description="Binds 'password' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'password' at runtime.")
    credentialsSecret: Optional[str] = Field(None, description="Secret that references Redis username and password")
    textSecret: Optional[str] = Field(None, description="Secret that references Redis admin password")


class FunctionConfSchemaRegexExtract(CriblModel):

    regex: Optional[str] = Field(None, description="Regex literal with named capturing groups, such as (?bar), or _NAME_ and _VALUE_ capturing groups, such as (?[^ =]+)=(?[^,]+)")
    regexList: Optional[list[RegexListConfSerdeTypeRegex]] = Field(None, description="Additional regex patterns to apply for field extraction.")
    source: Optional[str] = Field(None, description="Field on which to perform regex field extraction")
    iterations: Optional[float] = Field(None, description="The maximum number of times to apply regex to source field when the global flag is set, or when using _NAME_ and _VALUE_ capturing groups")
    fieldNameExpression: Optional[str] = Field(None, description="JavaScript expression to format field names when _NAME_n and _VALUE_n capturing groups are used. Original field name is in global variable 'name'. Example: To append XX to all field names, use `${name}_XX` (backticks are literal). If empty, names will be sanitized using this regex: /^[_0-9]+|[^a-zA-Z0-9_]+/g. You can access other fields values via __e..")
    overwrite: Optional[bool] = Field(None, description="Overwrite existing event fields with extracted values. If disabled, existing fields will be converted to an array.")


class FunctionConfSchemaRegexFilter(CriblModel):

    regex: Optional[str] = Field(None, description="Regex to test against")
    regexList: Optional[list[FunctionConfSchemaRegexFilterRegexListItem]] = Field(None, description="Additional regex patterns to test against the field.")
    field: Optional[str] = Field(None, description="Name of the field to apply the regex on (defaults to _raw)")


class FunctionConfSchemaRename(CriblModel):

    baseFields: Optional[list[str]] = Field(None, description="Fields whose children will inherit the Rename fields and Rename expression operations. Supports wildcards. If empty, only top-level fields will be renamed.")
    rename: Optional[list[FunctionConfSchemaRenameRenameItem]] = Field(None, description="Set of key-value pairs to rename fields, where key is the current name and value is the new name. Does not support internal fields.")
    renameExpr: Optional[str] = Field(None, description="Optional JavaScript expression whose returned value will be used to rename fields. Use the 'name' and 'value' global variables to access field names/values. Example: `name.startsWith('data') ? name.toUpperCase() : name`. You can access other field values via __e..")
    wildcardDepth: Optional[int] = Field(None, description="For wildcards specified in Parent fields, sets the maximum depth within events to match and rename fields. Enter `0` to match only top-level fields. Defaults to `5` levels down.")


class FunctionConfSchemaSampling(CriblModel):

    rules: Optional[list[FunctionConfSchemaSamplingRulesItem]] = Field(None, description="Events matching these rules will be sampled at the given rate")


class FunctionConfSchemaSensitiveDataScanner(CriblModel):

    rules: Optional[list[FunctionConfSchemaSensitiveDataScannerRulesItem]] = Field(None, description="List of scanning rulesets to apply, each with a ruleset ID and a mitigation expression.")
    fields: Optional[list[str]] = Field(None, description="Rulesets act on the events contained in these fields. Mitigation expressions apply to the scan results. Supports wildcards (*).")
    excludeFields: Optional[list[str]] = Field(None, description="Fields that the mitigation expression will not be applied to. Supports wildcards (*).")
    flags: Optional[list[FunctionConfSchemaSensitiveDataScannerFlagsItem]] = Field(None, description="Fields to add when mitigation is applied to an event")
    includeDetectedRules: Optional[bool] = Field(None, description="Add matching ruleset IDs to a field called \"__detected\"")
    backgroundDetection: Optional[bool] = Field(None, description="Run detection in the background without blocking event processing.")


class FunctionConfSchemaSerde(CriblModel):

    mode: Optional[str] = Field(None, description="Extract creates new fields. Reserialize extracts and filters fields, and then reserializes.")
    # values: elff=Extended Log File Format, clf=Common Log Format, kvp=Key=Value Pairs, json=JSON Object, delim=Delimited values, regex=Regular Expression
    type: Optional[str] = Field(None, description="Parser or formatter type to use.")
    keep: Optional[list[str]] = Field(None, description="List of fields to keep. Supports wildcards (*). Takes precedence over 'Fields to remove'.")
    remove: Optional[list[str]] = Field(None, description="List of fields to remove. Supports wildcards (*). Cannot remove fields that match 'Fields to keep'.")
    fieldFilterExpr: Optional[str] = Field(None, description="Expression evaluated against {index, name, value} context. Return truthy to keep a field, or falsy to remove it.")
    allowedKeyChars: Optional[list[str]] = Field(None, description="A list of characters that may be present in a key name, even though they are normally separator or control characters")
    allowedValueChars: Optional[list[str]] = Field(None, description="A list of characters that may be present in a value, even though they are normally separator or control characters")
    fields: Optional[list[str]] = Field(None, description="The fields to be extracted, listed in order. Will auto-generate if empty.")
    regex: Optional[str] = Field(None, description="Regex literal with named capturing groups, such as (?bar), or _NAME_ and _VALUE_ capturing groups, such as(?[^ =]+)=(?[^,]+)")
    regexList: Optional[list[RegexListConfSerdeTypeRegex]] = Field(None, description="Additional regex patterns to apply for field extraction.")
    iterations: Optional[float] = Field(None, description="The maximum number of times to apply regex to source field when the global flag is set, or when using _NAME_ and _VALUE_ capturing groups")
    fieldNameExpression: Optional[str] = Field(None, description="JavaScript expression to format field names when _NAME_n and _VALUE_n capturing groups are used. Original field name is in global variable 'name'. Example: To append XX to all field names, use `${name}_XX` (backticks are literal). If empty, names will be sanitized using this regex: /^[_0-9]+|[^a-zA-Z0-9_]+/g. You can access other fields values via __e..")
    overwrite: Optional[bool] = Field(None, description="Overwrite existing event fields with extracted values. If disabled, existing fields will be converted to an array.")
    pattern: Optional[str] = Field(None, description="Grok pattern to extract fields. Syntax supported: %{PATTERN_NAME:FIELD_NAME}")
    patternList: Optional[list[PatternListConfSerdeTypeGrok]] = Field(None, description="Additional Grok patterns to apply to the source field.")


class FunctionConfSchemaSidlookup(CriblModel):

    fields: Optional[list[FunctionConfSchemaSidlookupFieldsItem]] = Field(None, description="Set of expressions matched to lookup responses")


class FunctionConfSchemaSnmpTrapSerialize(CriblModel):

    strict: Optional[bool] = Field(None, description="Prevent event serialization if any required fields are missing. When disabled, @{product} will attempt to serialize the event even if required fields are missing, which could cause unexpected behavior at the downstream receiver.")
    dropFailedEvents: Optional[bool] = Field(None, description="When disabled, `snmpSerializeErrors` will be set on the event, and the `__snmpRaw` field will be removed to prevent @{product} from sending the event from the SNMP Trap Destination")
    v3User: Optional[FunctionConfSchemaSnmpTrapSerializeV3UserConf] = Field(None, description="SNMPv3 user configuration, including authentication and privacy protocol settings.")


class InputAppscopeFilterConf(CriblModel):
    """Rules that select processes for AppScope instrumentation."""

    allow: Optional[list[InputAppscopeFilterConfAllowItem]] = Field(None, description="Specify processes that AppScope should be loaded into, and the config to use.")
    transportURL: Optional[str] = Field(None, description="To override the UNIX domain socket or address/port specified in General Settings (while leaving Authentication settings as is), enter a URL.")


class InputEventhubAmqpAuthConf(CriblModel):
    """Authentication settings for the Event Hubs AMQP connection."""

    # values: connection-string=Connection String, oauth-bearer=OAuth Bearer
    mechanism: str = Field(..., description="Authentication mechanism")
    textSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    clientSecretAuthType: Optional[Literal['secret', 'certificate']] = Field(None, description="Authentication method")
    clientTextSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    certificate: Optional[InputEventhubAmqpAuthConfCertificateConf] = Field(None, description="Certificate credentials for OAuth authentication.")
    oauthEndpoint: Optional[Literal['https://login.microsoftonline.com', 'https://login.microsoftonline.us', 'https://login.partner.microsoftonline.cn']] = Field(None, description="Endpoint used to acquire authentication tokens from Azure")
    clientId: Optional[str] = Field(None, description="client_id to pass in the OAuth request parameter")
    tenantId: Optional[str] = Field(None, description="Directory ID (tenant identifier) in Azure Active Directory")
    fullyQualifiedNamespace: Optional[str] = Field(None, description="The fully qualified Event Hubs namespace that the consumer is associated with. This is likely to be similar to {yournamespace}.servicebus.windows.net.")
    xtemplate_oauthEndpoint: Optional[str] = Field(None, alias="__template_oauthEndpoint", description="Binds 'oauthEndpoint' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'oauthEndpoint' at runtime.")
    xtemplate_clientId: Optional[str] = Field(None, alias="__template_clientId", description="Binds 'clientId' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'clientId' at runtime.")
    xtemplate_tenantId: Optional[str] = Field(None, alias="__template_tenantId", description="Binds 'tenantId' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'tenantId' at runtime.")
    xtemplate_fullyQualifiedNamespace: Optional[str] = Field(None, alias="__template_fullyQualifiedNamespace", description="Binds 'fullyQualifiedNamespace' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'fullyQualifiedNamespace' at runtime.")


class InputEventhubAmqpCheckpointingConfBlobStoreConf(CriblModel):
    """Azure Blob Storage"""

    containerName: str = Field(..., description="Azure Blob Storage container used to store checkpoints. Must be 3–63 lowercase alphanumeric characters or hyphens.")
    authType: Optional[Literal['secret', 'clientSecret', 'clientCert', 'clientAssertion', 'clientAssertion_rpc']] = Field(None, description="Authentication method")
    textSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    storageAccountName: Optional[str] = Field(None, description="The name of your Azure storage account")
    tenantId: Optional[str] = Field(None, description="The service principal's tenant ID")
    clientId: Optional[str] = Field(None, description="The service principal's client ID")
    azureCloud: Optional[str] = Field(None, description="The Azure cloud to use. Defaults to Azure Public Cloud.")
    endpointSuffix: Optional[str] = Field(None, description="Endpoint suffix for the service URL. Takes precedence over the Azure Cloud setting. Defaults to core.windows.net.")
    clientTextSecret: Optional[str] = Field(None, description="Select or create a stored text secret")
    certificate: Optional[CertificateType] = Field(None, description="Certificate credentials for the Azure service principal.")
    xtemplate_storageAccountName: Optional[str] = Field(None, alias="__template_storageAccountName", description="Binds 'storageAccountName' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'storageAccountName' at runtime.")
    xtemplate_tenantId: Optional[str] = Field(None, alias="__template_tenantId", description="Binds 'tenantId' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'tenantId' at runtime.")
    xtemplate_clientId: Optional[str] = Field(None, alias="__template_clientId", description="Binds 'clientId' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'clientId' at runtime.")
    xtemplate_azureCloud: Optional[str] = Field(None, alias="__template_azureCloud", description="Binds 'azureCloud' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'azureCloud' at runtime.")


class InputOpenaiContentConfigItem(CriblModel):

    contentType: str = Field(..., description="Content type")
    contentDescription: Optional[str] = Field(None, description="Description")
    collectPath: str = Field(..., description="OpenAI Organization API path")
    docsUrl: Optional[str] = Field(None, description="Docs URL")
    disabled: Optional[bool] = Field(None, description="Enabled")
    stateTracking: Optional[bool] = Field(None, description="Track collection progress between consecutive scheduled executions.")
    stateUpdateExpression: Optional[str] = Field(None, description="JavaScript expression that defines how to update the state from an event. Use the event's data and the current state to compute the new state. See [Understanding State Expression Fields](https://docs.cribl.io/stream/collectors-rest#state-tracking-expression-fields) for more information.")
    stateMergeExpression: Optional[str] = Field(None, description="JavaScript expression that defines which state to keep when merging a task's newly reported state with previously saved state. Evaluates `prevState` and `newState` variables, resolving to the state to keep.")
    manageState: Optional[dict[str, Any]] = Field(None, description="Controls for viewing and managing the collector state.")
    requestParams: list[RefreshRequestParamConfHealthCheckAuthenticationOauthSecret] = Field(..., description="Query-string parameters to send with this endpoint")
    # values: response_body=Response Body Attribute, response_header=Response Header Attribute, response_header_link=RFC 5988 Link Header
    paginationType: str = Field(..., description="Pagination type")
    paginationAttribute: Optional[list[str]] = Field(None, description="Pagination attributes")
    paginationLastPageExpr: Optional[str] = Field(None, description="Last page expression")
    maxPages: Optional[float] = Field(None, description="Maximum number of pages to retrieve per collection task. Set to 0 only when unlimited pagination is required.")
    paginationNextRelationAttribute: Optional[str] = Field(None, description="Used only for RFC 5988 link-header pagination")
    paginationCurRelationAttribute: Optional[str] = Field(None, description="Optional relation that represents the current page")
    cronSchedule: str = Field(..., description="A cron schedule on which to run this job")
    earliest: str = Field(..., description="Relative to the current time")
    latest: str = Field(..., description="Relative to the current time")
    jobTimeout: Optional[str] = Field(None, description="Maximum time the job is allowed to run (examples: 30, 45s, 15m). Enter 0 for unlimited time.")
    logLevel: Optional[str] = Field(None, description="Collector runtime log level.")
    endpointMetadata: Optional[list[HecTokenMetadataParam]] = Field(None, description="Fields automatically added to events from this Content Type")


class InputSnmpSnmpV3AuthConf(CriblModel):
    """Authentication parameters for SNMPv3 trap. Set the log level to debug if you are experiencing authentication or decryption issues."""

    v3AuthEnabled: bool = Field(..., description="Enabled")
    allowUnmatchedTrap: Optional[bool] = Field(None, description="Pass through traps that don't match any of the configured users. @{product} will not attempt to decrypt these traps.")
    v3Users: Optional[list[InputSnmpSnmpV3AuthConfV3UsersItem]] = Field(None, description="User credentials for receiving v3 traps")


class InputSystemMetricsContainerConf(CriblModel):
    """Select the level of detail for container metrics"""

    mode: Optional[str] = Field(None, description="Select the level of detail for container metrics")
    dockerSocket: Optional[list[str]] = Field(None, description="Full paths for Docker's UNIX-domain socket")
    dockerTimeout: Optional[float] = Field(None, description="Timeout, in seconds, for the Docker API")
    filters: Optional[list[InputSystemMetricsContainerConfFiltersItem]] = Field(None, description="Containers matching any of these will be included. All are included if no filters are added.")
    allContainers: Optional[bool] = Field(None, description="Include stopped and paused containers")
    perDevice: Optional[bool] = Field(None, description="Generate separate metrics for each device")
    detail: Optional[bool] = Field(None, description="Generate full container metrics")


class InputSystemMetricsHostConfCustomConf(CriblModel):
    """Custom host metric collection settings."""

    system: Optional[InputSystemMetricsHostConfCustomConfSystemConf] = Field(None, description="Select the level of detail for system metrics")
    cpu: Optional[InputSystemMetricsHostConfCustomConfCpuConf] = Field(None, description="Select the level of detail for CPU metrics")
    memory: Optional[InputSystemMetricsHostConfCustomConfMemoryConf] = Field(None, description="Select the level of detail for memory metrics")
    network: Optional[InputSystemMetricsHostConfCustomConfNetworkConf] = Field(None, description="Select the level of detail for network metrics")
    disk: Optional[InputSystemMetricsHostConfCustomConfDiskConf] = Field(None, description="Select the level of detail for disk metrics")


class InputSystemStateCollectorsConf(CriblModel):
    """System state collectors to enable and configure."""

    hostsfile: Optional[InputSystemStateCollectorsConfHostsfileConf] = Field(None, description="Creates events based on entries collected from the hosts file")
    interfaces: Optional[InputSystemStateCollectorsConfInterfacesConf] = Field(None, description="Creates events for each of the host’s network interfaces")
    disk: Optional[InputSystemStateCollectorsConfDiskConf] = Field(None, description="Creates events for physical disks, partitions, and file systems")
    metadata: Optional[InputSystemStateCollectorsConfMetadataConf] = Field(None, description="Creates events based on the host system’s current state")
    routes: Optional[InputSystemStateCollectorsConfRoutesConf] = Field(None, description="Creates events based on entries collected from the host’s network routes")
    dns: Optional[InputSystemStateCollectorsConfDnsConf] = Field(None, description="Creates events for DNS resolvers and search entries")
    user: Optional[InputSystemStateCollectorsConfUserConf] = Field(None, description="Creates events for local users and groups")
    firewall: Optional[InputSystemStateCollectorsConfFirewallConf] = Field(None, description="Creates events for Firewall rules entries")
    services: Optional[InputSystemStateCollectorsConfServicesConf] = Field(None, description="Creates events from the list of services")
    ports: Optional[InputSystemStateCollectorsConfPortsConf] = Field(None, description="Creates events from list of listening ports")
    loginUsers: Optional[InputSystemStateCollectorsConfLoginUsersConf] = Field(None, description="Creates events from list of logged-in users")


class InputWefSubscriptionsItem(CriblModel):

    subscriptionName: str = Field(..., description="Subscription name")
    version: Optional[str] = Field(None, description="Version UUID for this subscription. If any subscription parameters are modified, this value will change.")
    contentFormat: str = Field(..., description="Content format in which the endpoint should deliver events")
    heartbeatInterval: float = Field(..., description="Maximum time (in seconds) between endpoint checkins before considering it unavailable")
    batchTimeout: float = Field(..., description="Interval (in seconds) over which the endpoint should collect events before sending them to Stream")
    readExistingEvents: Optional[bool] = Field(None, description="Newly subscribed endpoints will send previously existing events. Disable to receive new events only.")
    sendBookmarks: Optional[bool] = Field(None, description="Keep track of which events have been received, resuming from that point after a re-subscription. This setting takes precedence over 'Read existing events'. See [Cribl Docs](https://docs.cribl.io/stream/sources-wef/#subscriptions) for more details.")
    compress: Optional[bool] = Field(None, description="Receive compressed events from the source")
    targets: list[str] = Field(..., description="The DNS names of the endpoints that should forward these events. You may use wildcards, such as *.mydomain.com")
    locale: Optional[str] = Field(None, description="The RFC-3066 locale the Windows clients should use when sending events. Defaults to \"en-US\".")
    querySelector: Optional[str] = Field(None, description="Query builder mode")
    metadata: Optional[list[HecTokenMetadataParam]] = Field(None, description="Fields to add to events ingested under this subscription")
    queries: Optional[list[InputWefSubscriptionsItemQueriesItem]] = Field(None, description="Queries")
    xmlQuery: Optional[str] = Field(None, description="The XPath query to use for selecting events")


class InputWindowsMetricsHostConfCustomConf(CriblModel):
    """Custom host metric collection settings."""

    system: Optional[InputWindowsMetricsHostConfCustomConfSystemConf] = Field(None, description="Select the level of details for system metrics")
    cpu: Optional[InputWindowsMetricsHostConfCustomConfCpuConf] = Field(None, description="Select the level of details for CPU metrics")
    memory: Optional[InputWindowsMetricsHostConfCustomConfMemoryConf] = Field(None, description="Select the level of details for memory metrics")
    network: Optional[InputWindowsMetricsHostConfCustomConfNetworkConf] = Field(None, description="Select the level of details for network metrics")
    disk: Optional[InputWindowsMetricsHostConfCustomConfDiskConf] = Field(None, description="Select the level of details for disk metrics")


class OutputSplunkLbIndexerDiscoveryConfigsConf(CriblModel):
    """List of configurations to set up indexer discovery in Splunk Indexer clustering environment."""

    site: str = Field(..., description="Clustering site of the indexers from where indexers need to be discovered. In case of single site cluster, it defaults to 'default' site.")
    masterUri: str = Field(..., description="Full URI of Splunk cluster manager (scheme://host:port). Example: https://managerAddress:8089")
    refreshIntervalSec: float = Field(..., description="Time interval, in seconds, between two consecutive indexer list fetches from cluster manager")
    rejectUnauthorized: Optional[bool] = Field(None, description="During indexer discovery, reject cluster manager certificates that are not authorized by the system's CA. Disable to allow untrusted (for example, self-signed) certificates.")
    authTokens: Optional[list[OutputSplunkLbIndexerDiscoveryConfigsConfAuthTokensItem]] = Field(None, description="Tokens required to authenticate to cluster manager for indexer discovery")
    authType: Optional[Literal['manual', 'secret']] = Field(None, description="Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate")
    authToken: Optional[str] = Field(None, description="Shared secret to be provided by any client (in authToken header field). If empty, unauthorized access is permitted.")
    textSecret: Optional[str] = Field(None, description="Select or create a stored text secret")


class ProcessType(CriblModel):
    """Process metric collection settings."""

    sets: Optional[list[SetConfInputSystemMetrics]] = Field(None, description="Configure sets to collect process metrics")


class FunctionConfSchemaDetectionRules(CriblModel):
    """Detection Rules"""

    localOverrides: Optional[FunctionConfSchemaDetectionRulesLocalOverridesConf] = Field(None, description="Instance-level tuning applied after the rule set is merged. Managed by Cribl Security; not intended for direct editing.")


class FunctionConfSchemaNotificationPolicies(CriblModel):
    """Notification Policies Configuration"""

    policies: Optional[list[FunctionConfSchemaNotificationPoliciesPoliciesItem]] = Field(None, description="List of notification routing policies evaluated in order")


class InputEventhubAmqpCheckpointingConf(CriblModel):
    """Azure Blob Storage settings used to persist Event Hubs checkpoints."""

    blobStore: InputEventhubAmqpCheckpointingConfBlobStoreConf = Field(..., description="Azure Blob Storage")


class InputSystemMetricsHostConf(CriblModel):
    """Select level of detail for host metrics"""

    mode: Optional[Literal['basic', 'all', 'custom', 'disabled']] = Field(None, description="Select level of detail for host metrics")
    custom: Optional[InputSystemMetricsHostConfCustomConf] = Field(None, description="Custom host metric collection settings.")


class InputWindowsMetricsHostConf(CriblModel):
    """Select level of detail for host metrics"""

    mode: Optional[Literal['basic', 'all', 'custom', 'disabled']] = Field(None, description="Select level of detail for host metrics")
    custom: Optional[InputWindowsMetricsHostConfCustomConf] = Field(None, description="Custom host metric collection settings.")


class KafkaSchemaRegistryAuthenticationType(CriblModel):
    """Kafka Schema Registry Authentication"""

    disabled: bool = Field(..., description="Disabled")
    schemaRegistryURL: Optional[str] = Field(None, description="URL for accessing the Confluent Schema Registry. Example: http://localhost:8081. To connect over TLS, use https instead of http.")
    connectionTimeout: Optional[float] = Field(None, description="Maximum time to wait for a Schema Registry connection to complete successfully")
    requestTimeout: Optional[float] = Field(None, description="Maximum time to wait for the Schema Registry to respond to a request")
    maxRetries: Optional[float] = Field(None, description="Maximum number of times to try fetching schemas from the Schema Registry")
    auth: Optional[AuthType] = Field(None, description="Credentials to use when authenticating with the schema registry")
    tls: Optional[TlsSettingsClient] = Field(None, description="TLS settings (client side)")
    xtemplate_schemaRegistryURL: Optional[str] = Field(None, alias="__template_schemaRegistryURL", description="Binds 'schemaRegistryURL' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'schemaRegistryURL' at runtime.")


class KafkaSchemaRegistryAuthenticationTypeTemplateschemaRegistryUrlAuth(CriblModel):
    """Kafka Schema Registry Authentication"""

    disabled: bool = Field(..., description="Disabled")
    schemaRegistryURL: Optional[str] = Field(None, description="URL for accessing the Confluent Schema Registry. Example: http://localhost:8081. To connect over TLS, use https instead of http.")
    connectionTimeout: Optional[float] = Field(None, description="Maximum time to wait for a Schema Registry connection to complete successfully")
    requestTimeout: Optional[float] = Field(None, description="Maximum time to wait for the Schema Registry to respond to a request")
    maxRetries: Optional[float] = Field(None, description="Maximum number of times to try fetching schemas from the Schema Registry")
    auth: Optional[AuthType] = Field(None, description="Credentials to use when authenticating with the schema registry")
    tls: Optional[TlsSettingsClient] = Field(None, description="TLS settings (client side)")
    defaultKeySchemaId: Optional[float] = Field(None, description="Used when __keySchemaIdOut is not present, to transform key values, leave blank if key transformation is not required by default.")
    defaultValueSchemaId: Optional[float] = Field(None, description="Used when __valueSchemaIdOut is not present, to transform _raw, leave blank if value transformation is not required by default.")
    xtemplate_schemaRegistryURL: Optional[str] = Field(None, alias="__template_schemaRegistryURL", description="Binds 'schemaRegistryURL' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'schemaRegistryURL' at runtime.")
