"""TypedDict configurations for Collector variants."""
from typing import Literal, NotRequired, TypedDict


# --- Shared TypedDicts for nested collector fields ---


class NameValueParam(TypedDict):
    """A name-value pair used for headers, params, etc.

    Attrs:
        name: Parameter or header name.
        value: Parameter or header value.
    """
    name: str
    value: str


class ExtractorParam(TypedDict):
    """An extractor that enriches discovery results with template tokens.

    Attrs:
        key: Template token key.
        expression: JavaScript expression to evaluate.
    """
    key: str
    expression: str


class EnvVarParam(TypedDict):
    """An environment variable to pass to a script.

    Attrs:
        name: Variable name (alphanumeric, underscores, hyphens).
        value: Variable value.
    """
    name: str
    value: str


class CertificateParam(TypedDict):
    """Certificate credentials for Azure service principal.

    Attrs:
        certificateName: Name of the certificate.
    """
    certificateName: str


class MicrosoftGraphDeltaParam(TypedDict, total=False):
    """Microsoft Graph deltaLink state-tracking settings.

    Attrs:
        deltaLinkAttribute: Attribute name for the delta link.
    """
    deltaLinkAttribute: str


class StateTrackingParam(TypedDict, total=False):
    """State tracking settings.

    Attrs:
        enabled: If true, state tracking is enabled.
    """
    enabled: bool


class SchedulingParam(TypedDict, total=False):
    """Internal settings for scheduled execution.

    Attrs:
        stateTracking: State tracking configuration.
    """
    stateTracking: StateTrackingParam


class CollectorRetryRulesParam(TypedDict):
    """Settings that control how the Collector retries failed HTTP requests.

    Attrs:
        type: Retry strategy type.
        interval: Wait time in ms between retries (0-20000).
        limit: Maximum number of retries (0-20).
        multiplier: Backoff multiplier (1-20, backoff type only).
        maxIntervalMs: Maximum backoff interval in ms (backoff type only).
        codes: HTTP status codes that trigger a retry (100-599).
        enableHeader: Honor Retry-After response header.
        retryConnectTimeout: Retry on connection timeout.
        retryConnectReset: Retry on connection reset.
        retryHeaderName: Custom retry header name.
    """
    type: Literal['none', 'backoff', 'static']
    interval: NotRequired[float]
    limit: NotRequired[float]
    multiplier: NotRequired[float]
    maxIntervalMs: NotRequired[float]
    codes: NotRequired[list[int]]
    enableHeader: NotRequired[bool]
    retryConnectTimeout: NotRequired[bool]
    retryConnectReset: NotRequired[bool]
    retryHeaderName: NotRequired[str]


class CollectorPaginationParam(TypedDict):
    """Settings that control how the Collector paginates through results.

    Attrs:
        type: Pagination strategy type.
        maxPages: Maximum number of pages to fetch.
        lastPageExpr: Expression to detect the last page.
        attribute: Response attribute path containing the next page token.
        nextRelationAttribute: Link relation for the next page (header_link type).
        curRelationAttribute: Link relation for the current page (header_link type).
        offsetField: Request field name for the offset parameter.
        offset: Starting offset value.
        limitField: Request field name for the limit parameter.
        limit: Page size limit.
        totalRecordField: Response field containing total record count.
        zeroIndexed: If true, pages/offsets are zero-indexed.
        pageField: Request field name for the page number.
        page: Starting page number.
        sizeField: Request field name for the page size.
        size: Page size.
        totalPageField: Response field containing total page count.
    """
    type: Literal['none', 'response_body', 'response_header', 'response_header_link', 'request_offset', 'request_page']
    maxPages: NotRequired[float]
    lastPageExpr: NotRequired[str]
    attribute: NotRequired[str | list[str]]
    nextRelationAttribute: NotRequired[str]
    curRelationAttribute: NotRequired[str]
    offsetField: NotRequired[str]
    offset: NotRequired[float]
    limitField: NotRequired[str]
    limit: NotRequired[float]
    totalRecordField: NotRequired[str]
    zeroIndexed: NotRequired[bool]
    pageField: NotRequired[str]
    page: NotRequired[float]
    sizeField: NotRequired[str]
    size: NotRequired[float]
    totalPageField: NotRequired[str]


class CollectorDiscoveryParam(TypedDict):
    """Settings that control how the Collector discovers Collect tasks.

    Attrs:
        discoverType: Discovery type. Valid values: "http", "json", "list", "none".
        discoverUrl: URL to use for HTTP discovery.
        discoverMethod: HTTP method for discovery requests. Valid values: "get", "post", "post_with_body".
        discoverRequestHeaders: Headers to send with discovery requests.
        pagination: Pagination settings for discovery results. Valid values for type: "none", "response_body", "response_header", "response_header_link", "request_offset", "request_page".
        discoverDataField: Path to the data field in the discovery response.
        enableStrictDiscoverParsing: Enable strict JSON parsing of discovery response.
        enableDiscoverCode: Enable custom JavaScript code for discovery.
        manualDiscoverResult: Manual discovery result as a string.
        itemList: List of items to discover (for list type).
    """
    discoverType: Literal['http', 'json', 'list', 'none']
    discoverUrl: NotRequired[str]
    discoverMethod: NotRequired[Literal['get', 'post', 'post_with_body']]
    discoverRequestHeaders: NotRequired[list[NameValueParam]]
    pagination: NotRequired[CollectorPaginationParam]
    discoverDataField: NotRequired[str]
    enableStrictDiscoverParsing: NotRequired[bool]
    enableDiscoverCode: NotRequired[bool]
    manualDiscoverResult: NotRequired[str]
    itemList: NotRequired[list[str]]


# --- Collector Configuration TypedDicts ---


class RestCollectorConf(TypedDict):
    """Configuration for Rest collector.

    Attrs:
        discovery: Settings that control how the Collector discovers Collect tasks.
        collectUrl: URL (constant or JavaScript expression) to use for the Collect operation
        collectMethod: Collect method. Valid values: "get", "post", "post_with_body", "other".
        collectVerb: Custom HTTP method when collectMethod is "other".
        collectBody: Template for body to send with the Collect request (when collectMethod is "other" or "post_with_body").
        collectRequestParams: Parameters to send with each Collect request.
        collectRequestHeaders: Headers to send with each Collect request.
        pagination: Settings that control how the Collector paginates through Collect results.
        authentication: Authentication method for Discover and Collect REST calls.
        timeout: HTTP request inactivity timeout. Use 0 to disable.
        maxResponseBodySize: Maximum amount of data to buffer from a single response body.
        useRoundRobinDns: Use round-robin DNS lookup.
        disableTimeFilter: Disable Collector event time filtering when a date range is specified
        decodeUrl: Decode the URL before sending requests (including pagination requests)
        rejectUnauthorized: Reject certificates that cannot be verified against a valid CA.
        captureHeaders: Enable to add response headers to the resHeaders field.
        stopOnEmptyResults: Stop pagination when the Event Breaker produces no events
        safeHeaders: List of headers that are safe to log in plain text
        retryRules: Settings that control how the Collector retries failed HTTP requests.
        microsoftGraphDelta: Microsoft Graph deltaLink state-tracking settings.
        __scheduling: Internal settings for scheduled execution of this Collector.
        username: Username
        password: Password
        credentialsSecret: Select or create a stored secret that references your credentials
        loginUrl: URL to use for login API call.
        loginBody: Template for POST body to send with login request.
        getAuthTokenFromHeader: Extract the auth token from the HTTP Authorization response header.
        authHeaderKey: Authorization header key to pass in Discover and Collect calls.
        authHeaderExpr: JavaScript expression used to compute the Authorization header.
        authRequestHeaders: Authentication headers
        tokenRespAttribute: Path to token attribute in login response body.
        clientSecretParamName: Parameter name for client secret.
        clientSecretParamValue: Secret value for the client secret parameter.
        authRequestParams: OAuth request parameters added to the POST body.
        refreshTokenField: Field name containing a refresh token.
        rotateRefreshToken: Update stored refresh token value on each successful refresh.
        refreshUrl: Override the refresh endpoint URL.
        refreshRequestParams: Parameters to include in the refresh token request body.
        textSecret: Select or create a text secret.
        scopes: Scopes to use during authentication.
        serviceAccountCredentials: Google Cloud service account credentials JSON.
        subject: Email address of a user account with Super Admin permissions.
        hmacFunctionId: HMAC Function to use with authentication
    """

    discovery: NotRequired[CollectorDiscoveryParam]
    collectUrl: str
    collectMethod: Literal['get', 'post', 'post_with_body', 'other']
    collectVerb: NotRequired[str]
    collectBody: NotRequired[str]
    collectRequestParams: NotRequired[list[NameValueParam]]
    collectRequestHeaders: NotRequired[list[NameValueParam]]
    pagination: NotRequired[CollectorPaginationParam]
    authentication: Literal['none', 'basic', 'basicSecret', 'login', 'loginSecret', 'oauth', 'oauthSecret', 'google_oauth', 'google_oauthSecret', 'hmac']
    timeout: NotRequired[float]
    maxResponseBodySize: NotRequired[str]
    useRoundRobinDns: NotRequired[bool]
    disableTimeFilter: NotRequired[bool]
    decodeUrl: NotRequired[bool]
    rejectUnauthorized: NotRequired[bool]
    captureHeaders: NotRequired[bool]
    stopOnEmptyResults: NotRequired[bool]
    safeHeaders: NotRequired[list[str]]
    retryRules: NotRequired[CollectorRetryRulesParam]
    microsoftGraphDelta: NotRequired[MicrosoftGraphDeltaParam]
    __scheduling: NotRequired[SchedulingParam]
    username: NotRequired[str]
    password: NotRequired[str]
    credentialsSecret: NotRequired[str]
    loginUrl: NotRequired[str]
    loginBody: NotRequired[str]
    getAuthTokenFromHeader: NotRequired[bool]
    authHeaderKey: NotRequired[str]
    authHeaderExpr: NotRequired[str]
    authRequestHeaders: NotRequired[list[NameValueParam]]
    tokenRespAttribute: NotRequired[str]
    clientSecretParamName: NotRequired[str]
    clientSecretParamValue: NotRequired[str]
    authRequestParams: NotRequired[list[NameValueParam]]
    refreshTokenField: NotRequired[str]
    rotateRefreshToken: NotRequired[bool]
    refreshUrl: NotRequired[str]
    refreshRequestParams: NotRequired[list[NameValueParam]]
    textSecret: NotRequired[str]
    scopes: NotRequired[list[str]]
    serviceAccountCredentials: NotRequired[str]
    subject: NotRequired[str]
    hmacFunctionId: NotRequired[str]


class AzureBlobCollectorConf(TypedDict):
    """Configuration for AzureBlob collector.

    Attrs:
        outputName: An optional predefined Destination for auto-populating Collect settings.
        authType: Authentication method.
        containerName: Container to collect from.
        path: The directory from which to collect data.
        extractors: Extractors that enrich discovery results with template tokens.
        recurse: Recurse through subdirectories
        includeMetadata: Include Azure Blob metadata in collected events.
        includeTags: Include Azure Blob tags in collected events.
        maxBatchSize: Maximum number of metadata objects to batch before recording as results
        disableTimeFilter: Disable Collector event time filtering when a date range is specified
        parquetChunkSizeMB: Maximum file size for each Parquet chunk
        parquetChunkDownloadTimeout: Maximum time allowed for downloading a Parquet chunk.
        connectionString: Azure storage account Connection String.
        textSecret: Text secret
        storageAccountName: The name of your Azure storage account
        tenantId: The service principal's tenant ID
        clientId: The service principal's client ID
        clientTextSecret: Text secret containing the client secret
        endpointSuffix: The endpoint suffix for the service URL.
        azureCloud: The Azure cloud to use.
        certificate: Certificate credentials for the service principal.
    """

    outputName: NotRequired[str]
    authType: NotRequired[Literal['manual', 'secret', 'clientSecret', 'clientCert']]
    containerName: str
    path: NotRequired[str]
    extractors: NotRequired[list[ExtractorParam]]
    recurse: NotRequired[bool]
    includeMetadata: NotRequired[bool]
    includeTags: NotRequired[bool]
    maxBatchSize: NotRequired[float]
    disableTimeFilter: NotRequired[bool]
    parquetChunkSizeMB: NotRequired[float]
    parquetChunkDownloadTimeout: NotRequired[float]
    connectionString: NotRequired[str]
    textSecret: NotRequired[str]
    storageAccountName: NotRequired[str]
    tenantId: NotRequired[str]
    clientId: NotRequired[str]
    clientTextSecret: NotRequired[str]
    endpointSuffix: NotRequired[str]
    azureCloud: NotRequired[str]
    certificate: NotRequired[CertificateParam]


class CriblLakeCollectorConf(TypedDict):
    """Configuration for CriblLake collector.

    Attrs:
        storageLocationId: Storage location for the Lake Dataset
        dataset: Lake dataset to collect data from.
    """

    storageLocationId: NotRequired[str]
    dataset: str


class DatabaseCollectorConf(TypedDict):
    """Configuration for Database collector.

    Attrs:
        connectionId: Select an existing Connection.
        query: An expression that resolves to the query string.
        queryValidationEnabled: Enforces basic query validation allowing only a single select statement.
        defaultBreakers: Hidden Default Breakers
        __scheduling: Internal settings for scheduled execution of this Collector.
    """

    connectionId: str
    query: str
    queryValidationEnabled: NotRequired[bool]
    defaultBreakers: NotRequired[Literal['Cribl']]
    __scheduling: NotRequired[SchedulingParam]


class FilesystemCollectorConf(TypedDict):
    """Configuration for Filesystem collector.

    Attrs:
        outputName: Select a predefined Destination for auto-populating Collector settings.
        path: The directory from which to collect data.
        extractors: Extractors that enrich discovery results with template tokens.
        recurse: Recurse through subdirectories
        maxBatchSize: Maximum number of metadata files to batch before recording as results
    """

    outputName: NotRequired[str]
    path: str
    extractors: NotRequired[list[ExtractorParam]]
    recurse: NotRequired[bool]
    maxBatchSize: NotRequired[float]


class GoogleCloudStorageCollectorConf(TypedDict):
    """Configuration for GoogleCloudStorage collector.

    Attrs:
        outputName: Name of the predefined Destination for auto-populating Collect settings.
        bucket: Name of the bucket to collect from.
        path: The directory from which to collect data.
        extractors: Extractors that enrich discovery results with template tokens.
        endpoint: Google Cloud Storage service endpoint.
        disableTimeFilter: Disable Collector event time filtering when a date range is specified
        recurse: Recurse through subdirectories
        maxBatchSize: Maximum number of metadata objects to batch before recording as results
        authType: Authentication method.
        parquetChunkSizeMB: Maximum file size for each Parquet chunk
        parquetChunkDownloadTimeout: Maximum time allowed for downloading a Parquet chunk.
        serviceAccountCredentials: Google Cloud service account credentials JSON.
        textSecret: Select or create a stored text secret.
    """

    outputName: NotRequired[str]
    bucket: str
    path: NotRequired[str]
    extractors: NotRequired[list[ExtractorParam]]
    endpoint: NotRequired[str]
    disableTimeFilter: NotRequired[bool]
    recurse: NotRequired[bool]
    maxBatchSize: NotRequired[float]
    authType: NotRequired[Literal['auto', 'manual', 'secret']]
    parquetChunkSizeMB: NotRequired[float]
    parquetChunkDownloadTimeout: NotRequired[float]
    serviceAccountCredentials: NotRequired[str]
    textSecret: NotRequired[str]


class HealthCheckCollectorConf(TypedDict):
    """Configuration for HealthCheck collector.

    Attrs:
        discovery: Settings that control how the Collector discovers Collect tasks.
        collectUrl: Expression to derive URL to use for the health check operation.
        collectMethod: Health check HTTP method.
        collectRequestHeaders: Optional health check request headers.
        authenticateCollect: Enable to make auth health check call.
        authentication: Authentication method for Discover and Collect REST calls.
        timeout: HTTP request inactivity timeout, use 0 to disable
        rejectUnauthorized: Reject certificates that cannot be verified against a valid CA.
        defaultBreakers: Hidden Default Breakers
        safeHeaders: List of headers that are safe to log in plain text.
        retryRules: Settings that control how the Collector retries failed HTTP requests.
        username: Basic authentication username
        password: Basic authentication password
        credentialsSecret: Select or create a stored secret.
        loginUrl: URL to use for login API call.
        loginBody: Template for POST body to send with login request.
        tokenRespAttribute: Path to token attribute in login response body.
        authHeaderExpr: JavaScript expression to compute the Authorization header.
        authRequestHeaders: Optional authentication request headers.
        clientSecretParamName: Parameter name for client secret.
        clientSecretParamValue: Secret value for the client secret parameter.
        authRequestParams: OAuth request parameters added to the POST body.
        refreshTokenField: Field name containing a refresh token.
        rotateRefreshToken: Update stored refresh token value on each successful refresh.
        refreshUrl: Override the refresh endpoint URL.
        refreshRequestParams: Parameters to include in the refresh token request body.
        textSecret: Select or create a text secret.
    """

    discovery: NotRequired[CollectorDiscoveryParam]
    collectUrl: str
    collectMethod: Literal['get', 'post', 'post_with_body']
    collectRequestHeaders: NotRequired[list[NameValueParam]]
    authenticateCollect: NotRequired[bool]
    authentication: Literal['none', 'basic', 'basicSecret', 'login', 'loginSecret', 'oauth', 'oauthSecret']
    timeout: NotRequired[float]
    rejectUnauthorized: NotRequired[bool]
    defaultBreakers: NotRequired[Literal['Cribl']]
    safeHeaders: NotRequired[list[str]]
    retryRules: NotRequired[CollectorRetryRulesParam]
    username: NotRequired[str]
    password: NotRequired[str]
    credentialsSecret: NotRequired[str]
    loginUrl: NotRequired[str]
    loginBody: NotRequired[str]
    tokenRespAttribute: NotRequired[str]
    authHeaderExpr: NotRequired[str]
    authRequestHeaders: NotRequired[list[NameValueParam]]
    clientSecretParamName: NotRequired[str]
    clientSecretParamValue: NotRequired[str]
    authRequestParams: NotRequired[list[NameValueParam]]
    refreshTokenField: NotRequired[str]
    rotateRefreshToken: NotRequired[bool]
    refreshUrl: NotRequired[str]
    refreshRequestParams: NotRequired[list[NameValueParam]]
    textSecret: NotRequired[str]


class S3CollectorConf(TypedDict):
    """Configuration for S3 collector.

    Attrs:
        outputName: Name of the predefined Destination for auto-populating Collect settings.
        bucket: S3 Bucket from which to collect data
        parquetChunkSizeMB: Maximum file size for each Parquet chunk
        parquetChunkDownloadTimeout: Maximum time allowed for downloading a Parquet chunk.
        region: Region from which to retrieve data
        path: Directory where data will be collected.
        partitioningScheme: Partitioning scheme used for this dataset.
        extractors: Extractors that enrich discovery results with template tokens.
        awsAuthenticationMethod: AWS authentication method.
        endpoint: S3-compatible endpoint URL.
        enableAssumeRole: Use AssumeRole credentials
        assumeRoleArn: Amazon Resource Name (ARN) of the role to assume
        assumeRoleExternalId: External ID to use when assuming role
        durationSeconds: Duration of the Assumed Role's session, in seconds.
        maxBatchSize: Maximum number of metadata objects to batch before recording as results
        reuseConnections: Reuse connections between requests to improve performance
        rejectUnauthorized: Reject certificates that cannot be verified against a valid CA.
        verifyPermissions: Verify bucket-level permissions.
        disableTimeFilter: Disable Collector event time filtering when a date range is specified
        awsApiKey: AWS access key.
        awsSecretKey: AWS secret key.
        awsSecret: Select or create a stored secret for AWS credentials.
    """

    outputName: NotRequired[str]
    bucket: str
    parquetChunkSizeMB: NotRequired[float]
    parquetChunkDownloadTimeout: NotRequired[float]
    region: NotRequired[str]
    path: NotRequired[str]
    partitioningScheme: NotRequired[Literal['none', 'ddss']]
    extractors: NotRequired[list[ExtractorParam]]
    awsAuthenticationMethod: NotRequired[Literal['auto', 'manual', 'secret']]
    endpoint: NotRequired[str]
    enableAssumeRole: NotRequired[bool]
    assumeRoleArn: NotRequired[str]
    assumeRoleExternalId: NotRequired[str]
    durationSeconds: NotRequired[float]
    maxBatchSize: NotRequired[float]
    reuseConnections: NotRequired[bool]
    rejectUnauthorized: NotRequired[bool]
    verifyPermissions: NotRequired[bool]
    disableTimeFilter: NotRequired[bool]
    awsApiKey: NotRequired[str]
    awsSecretKey: NotRequired[str]
    awsSecret: NotRequired[str]


class ScriptCollectorConf(TypedDict):
    """Configuration for Script collector.

    Attrs:
        discoverScript: Script to discover what to collect.
        collectScript: Script to run to perform data collections.
        shell: Shell to use to execute scripts.
        envVars: Environment variables to expose to the discover and collect scripts.
    """

    discoverScript: str
    collectScript: str
    shell: NotRequired[str]
    envVars: NotRequired[list[EnvVarParam]]


class SplunkCollectorConf(TypedDict):
    """Configuration for Splunk collector.

    Attrs:
        searchHead: Search head base URL.
        search: Search query string.
        earliest: The earliest time boundary for the search.
        latest: The latest time boundary for the search.
        endpoint: REST API used to create a search
        outputMode: Format of the returned output
        collectRequestParams: Optional collect request parameters
        collectRequestHeaders: Optional collect request headers
        authentication: Authentication method for REST calls
        timeout: HTTP request inactivity timeout. Use 0 for no timeout.
        useRoundRobinDns: Use round-robin DNS lookup.
        disableTimeFilter: Disable collector event time filtering when a date range is specified
        rejectUnauthorized: Reject certificates that cannot be verified against a valid CA.
        handleEscapedChars: Pass escape characters directly to Splunk
        retryRules: Settings that control how the Collector retries failed HTTP requests.
        username: Basic authentication username
        password: Basic authentication password
        credentialsSecret: Select or create a stored secret.
        token: Bearer token
        tokenSecret: Select or create a stored secret for Bearer token.
        loginUrl: URL to use for login API call.
        loginBody: Template for POST body to send with login request.
        tokenRespAttribute: Path to token attribute in login response body.
        authHeaderExpr: JavaScript expression to compute the Authorization header.
    """

    searchHead: str
    search: str
    earliest: NotRequired[str]
    latest: NotRequired[str]
    endpoint: str
    outputMode: Literal['csv', 'json']
    collectRequestParams: NotRequired[list[NameValueParam]]
    collectRequestHeaders: NotRequired[list[NameValueParam]]
    authentication: Literal['none', 'basic', 'basicSecret', 'token', 'tokenSecret']
    timeout: NotRequired[float]
    useRoundRobinDns: NotRequired[bool]
    disableTimeFilter: NotRequired[bool]
    rejectUnauthorized: NotRequired[bool]
    handleEscapedChars: NotRequired[bool]
    retryRules: NotRequired[CollectorRetryRulesParam]
    username: NotRequired[str]
    password: NotRequired[str]
    credentialsSecret: NotRequired[str]
    token: NotRequired[str]
    tokenSecret: NotRequired[str]
    loginUrl: NotRequired[str]
    loginBody: NotRequired[str]
    tokenRespAttribute: NotRequired[str]
    authHeaderExpr: NotRequired[str]
