"""Pydantic models for Cribl API responses."""
from __future__ import annotations

from enum import IntEnum
from typing import Annotated, Any, ClassVar, Generic, Literal, NotRequired, TypedDict, TypeVar

from pydantic import BaseModel, ConfigDict, Field


# --- Enums ---


class EstimatedIngestRate(IntEnum):
    """Estimated ingest rate for a Cribl.Cloud Worker Group.

    Attrs:
        RATE_12_MB_PER_SEC: 12 MB/sec
        RATE_24_MB_PER_SEC: 24 MB/sec
        RATE_36_MB_PER_SEC: 36 MB/sec
        RATE_48_MB_PER_SEC: 48 MB/sec
        RATE_60_MB_PER_SEC: 60 MB/sec
        RATE_84_MB_PER_SEC: 84 MB/sec
        RATE_120_MB_PER_SEC: 120 MB/sec
        RATE_156_MB_PER_SEC: 156 MB/sec
        RATE_180_MB_PER_SEC: 180 MB/sec
    """

    RATE_12_MB_PER_SEC = 1024
    RATE_24_MB_PER_SEC = 2048
    RATE_36_MB_PER_SEC = 3072
    RATE_48_MB_PER_SEC = 4096
    RATE_60_MB_PER_SEC = 5120
    RATE_84_MB_PER_SEC = 7168
    RATE_120_MB_PER_SEC = 10240
    RATE_156_MB_PER_SEC = 13312
    RATE_180_MB_PER_SEC = 15360


class CaptureLevel(IntEnum):
    """Stage at which events are captured.

    Attrs:
        BEFORE_PRE_PROCESSING_PIPELINE: 1. Before pre-processing Pipeline
        BEFORE_ROUTES: 2. Before the Routes
        BEFORE_POST_PROCESSING_PIPELINE: 3. Before post-processing Pipeline
        BEFORE_DESTINATION: 4. Before the Destination
    """

    BEFORE_PRE_PROCESSING_PIPELINE = 0
    BEFORE_ROUTES = 1
    BEFORE_POST_PROCESSING_PIPELINE = 2
    BEFORE_DESTINATION = 3


class NodeActiveUpgradeStatus(IntEnum):
    """Secondary upgrade state when state is Active.

    Attrs:
        PENDING: Pending
        QUEUED: Queued
        UPGRADING: Upgrading
    """

    PENDING = 0
    QUEUED = 1
    UPGRADING = 2


class NodeFailedUpgradeStatus(IntEnum):
    """Secondary upgrade state when state is Failed.

    Attrs:
        UPGRADE_ERROR_ON_NODE: UpgradeErrorOnNode
        UPGRADE_INSTALLATION_ROLLBACK: UpgradeInstallationRollback
    """

    UPGRADE_ERROR_ON_NODE = 0
    UPGRADE_INSTALLATION_ROLLBACK = 1


class NodeSkippedUpgradeStatus(IntEnum):
    """Secondary upgrade state when state is Skipped.

    Attrs:
        DOWNLOAD_ERROR: DownloadError
        INSTALL_TYPE: InstallType
        MISSING_PACKAGE: MissingPackage
        TOO_OLD: TooOld
    """

    DOWNLOAD_ERROR = 0
    INSTALL_TYPE = 1
    MISSING_PACKAGE = 2
    TOO_OLD = 3


class NodeUpgradeState(IntEnum):
    """Current upgrade state for an Edge Node.

    Attrs:
        ACTIVE: Active
        CURRENT: Current
        FAILED: Failed
        SKIPPED: Skipped
    """

    ACTIVE = 0
    CURRENT = 1
    FAILED = 2
    SKIPPED = 3


class JobState(IntEnum):
    """State of a Job.

    Attrs:
        INITIALIZING: Initializing
        PENDING: Pending
        RUNNING: Running
        PAUSED: Paused
        CANCELLED: Cancelled
        FINISHED: Finished
        FAILED: Failed
        ORPHANED: Orphaned
        UNKNOWN: Unknown
    """

    INITIALIZING = 0
    PENDING = 1
    RUNNING = 2
    PAUSED = 3
    CANCELLED = 4
    FINISHED = 5
    FAILED = 6
    ORPHANED = 7
    UNKNOWN = 8


class SyslogFacility(IntEnum):
    """Default value for syslog message facility.

    Attrs:
        KERN: kern
        USER: user
        MAIL: mail
        DAEMON: daemon
        AUTH: auth
        SYSLOG: syslog
        LPR: lpr
        NEWS: news
        UUCP: uucp
        CRON: cron
        AUTHPRIV: authpriv
        FTP: ftp
        NTP: ntp
        SECURITY: security
        CONSOLE: console
        SOLARIS_CRON: solaris-cron
        LOCAL0: local0
        LOCAL1: local1
        LOCAL2: local2
        LOCAL3: local3
        LOCAL4: local4
        LOCAL5: local5
    """

    KERN = 0
    USER = 1
    MAIL = 2
    DAEMON = 3
    AUTH = 4
    SYSLOG = 5
    LPR = 6
    NEWS = 7
    UUCP = 8
    CRON = 9
    AUTHPRIV = 10
    FTP = 11
    NTP = 12
    SECURITY = 13
    CONSOLE = 14
    SOLARIS_CRON = 15
    LOCAL0 = 16
    LOCAL1 = 17
    LOCAL2 = 18
    LOCAL3 = 19
    LOCAL4 = 20
    LOCAL5 = 21


class SyslogSeverity(IntEnum):
    """Default value for syslog message severity.

    Attrs:
        EMERGENCY: emergency
        ALERT: alert
        CRITICAL: critical
        ERROR: error
        WARNING: warning
        NOTICE: notice
        INFO: info
        DEBUG: debug
    """

    EMERGENCY = 0
    ALERT = 1
    CRITICAL = 2
    ERROR = 3
    WARNING = 4
    NOTICE = 5
    INFO = 6
    DEBUG = 7


class AcknowledgmentsOptions(IntEnum):
    """Control the number of required acknowledgments.

    Attrs:
        LEADER: Leader
        NONE: None
        ALL: All
    """

    LEADER = 1
    NONE = 0
    ALL = -1


# --- Base ---

T = TypeVar("T")


class CriblModel(BaseModel):
    """Base for all SDK models. extra='allow' captures unknown fields in .model_extra."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")


# --- Shared nested models (TLS, SASL) ---
# These are referenced by $ref in many Input/Output schemas.
# Superset approach: all fields optional except where the spec requires them.


class TlsSettingsClient(CriblModel):
    """TLS settings (client side).

    Covers spec schemas: TlsSettingsClientSideType, TlsSettingsClientSideTypeCaPathCertPath,
    TlsSettingsClientSideTypeCaPathCertPathExtended, TlsSettingsClientSideTypeExtended.

    Attrs:
        disabled: If true, TLS is disabled on this connection.
        rejectUnauthorized: Reject certs not authorized by a CA in the CA path or system trust.
        servername: Server name for SNI TLS extension (must be a host name, not IP).
        certificateName: The name of the predefined certificate.
        caPath: Path to CA certificates (PEM). Can reference $ENV_VARS.
        privKeyPath: Path to private key for mutual auth (PEM). Can reference $ENV_VARS.
        certPath: Path to certificates for mutual auth (PEM). Can reference $ENV_VARS.
        passphrase: Passphrase to decrypt private key.
        minVersion: Minimum TLS version.
        maxVersion: Maximum TLS version.
    """
    disabled: bool | None = None
    rejectUnauthorized: bool | None = None
    servername: str | None = None
    certificateName: str | None = None
    caPath: str | None = None
    privKeyPath: str | None = None
    certPath: str | None = None
    passphrase: str | None = None
    minVersion: str | None = None
    maxVersion: str | None = None


class TlsSettingsServer(CriblModel):
    """TLS settings (server side).

    Covers spec schema: TlsSettingsServerSideType.

    Attrs:
        disabled: If true, TLS is disabled on this connection.
        requestCert: Require clients to present certificates (mutual auth).
        rejectUnauthorized: Reject certs not authorized by a CA in the path or system trust.
        commonNameRegex: Regex matching allowable common names in peer certificates.
        certificateName: The name of the predefined certificate.
        privKeyPath: Path to private key (PEM). Can reference $ENV_VARS.
        passphrase: Passphrase to decrypt private key.
        certPath: Path to certificates (PEM). Can reference $ENV_VARS.
        caPath: Path to CA certificates (PEM). Can reference $ENV_VARS.
        minVersion: Minimum TLS version.
        maxVersion: Maximum TLS version.
    """
    disabled: bool | None = None
    requestCert: bool | None = None
    rejectUnauthorized: bool | None = None
    commonNameRegex: str | None = None
    certificateName: str | None = None
    privKeyPath: str | None = None
    passphrase: str | None = None
    certPath: str | None = None
    caPath: str | None = None
    minVersion: str | None = None
    maxVersion: str | None = None


class SaslAuthentication(CriblModel):
    """SASL authentication parameters for broker connections.

    Covers spec schemas: AuthenticationType, AuthenticationTypeUse.

    Attrs:
        disabled: If true, authentication is disabled.
        username: Username for authentication.
        password: Password or connection-string key.
        authType: Enter credentials directly, or select a stored secret.
        credentialsSecret: Select or create a secret that references credentials.
        mechanism: SASL mechanism (e.g. PLAIN, SCRAM-SHA-256, GSSAPI, OAUTHBEARER).
        keytabLocation: Location of keytab file for Kerberos authentication.
        principal: Authentication principal (e.g. kafka_user@example.com).
        brokerServiceClass: Kerberos service class for Kafka brokers.
        oauthEnabled: Enable OAuth authentication.
        tokenUrl: URL of the token endpoint for OAuth.
        clientId: Client ID for OAuth authentication.
        oauthSecretType: OAuth secret type.
        clientTextSecret: Text secret for OAuth client.
        textSecret: Password as stored text secret.
    """
    disabled: bool | None = None
    username: str | None = None
    password: str | None = None
    authType: str | None = None
    credentialsSecret: str | None = None
    mechanism: str | None = None
    keytabLocation: str | None = None
    principal: str | None = None
    brokerServiceClass: str | None = None
    oauthEnabled: bool | None = None
    tokenUrl: str | None = None
    clientId: str | None = None
    oauthSecretType: str | None = None
    clientTextSecret: str | None = None
    textSecret: str | None = None


# --- TypedDicts (typed input params for resource methods) ---


class GitCommitParam(TypedDict):
    """A single commit entry in git log.

    Attrs:
        date: Date and time of the commit.
        hash: Full commit hash.
        message: Commit message.
        short: Abbreviated commit hash.
        author_email: Email address of the commit author.
        author_name: Name of the commit author.
    """
    date: str
    hash: str
    message: str
    short: str
    author_email: NotRequired[str]
    author_name: NotRequired[str]


class GitStatusParam(TypedDict, total=False):
    """Git status of a Worker Group configuration.

    All fields optional — API may return partial status.

    Attrs:
        commit: Commit hash of the currently committed configuration version.
        localChanges: Number of local configuration changes not yet committed.
        log: List of recent configuration commits.
    """
    commit: str
    localChanges: int
    log: list[GitCommitParam]


class CloudParam(TypedDict):
    """Cloud provider configuration for a Worker Group.

    Attrs:
        provider: Cloud provider for the Worker Group.
        region: Cloud region where the Worker Group is deployed.
    """
    provider: Literal["aws", "azure"] | None
    region: str


class TLSParam(TypedDict, total=False):
    """TLS client configuration.

    Attrs:
        caPath: Path to PEM-encoded CA certificate.
        certPath: Path to PEM-encoded TLS certificate.
        certificateName: Certificate name for validation.
        disabled: If true, TLS is disabled for this connection.
        maxVersion: Maximum TLS protocol version to accept.
        minVersion: Minimum TLS protocol version to require.
        passphrase: Passphrase to decrypt the TLS private key.
        privKeyPath: Path to PEM-encoded TLS private key.
        rejectUnauthorized: If true, reject unverifiable certificates.
        servername: Expected server name for SNI.
    """
    caPath: str
    certPath: str
    certificateName: str
    disabled: bool
    maxVersion: Literal["TLSv1.3", "TLSv1.2", "TLSv1.1", "TLSv1"]
    minVersion: Literal["TLSv1.3", "TLSv1.2", "TLSv1.1", "TLSv1"]
    passphrase: str
    privKeyPath: str
    rejectUnauthorized: bool
    servername: str


class ApiSslParam(TypedDict, total=False):
    """TLS configuration for the API server.

    Attrs:
        caPath: Path to PEM-encoded CA certificate for client auth.
        certPath: Path to PEM-encoded TLS certificate.
        certificateName: Name of a predefined Certificate stored in Cribl.
        disabled: If true, TLS is disabled for the API server.
        passphrase: Passphrase to decrypt the TLS private key.
        privKeyPath: Path to PEM-encoded TLS private key.
    """
    caPath: str
    certPath: str
    certificateName: str
    disabled: bool
    passphrase: str
    privKeyPath: str


class ApiSettingsParam(TypedDict):
    """API server settings.

    Attrs:
        disabled: If true, the API server is disabled.
        host: Hostname or IP address the API server listens on.
        port: Port number the API server listens on.
        baseUrl: Base URL for the API server (used when behind a reverse proxy).
        disableApiCache: If true, disable the API response cache.
        headers: Custom HTTP response headers to include in every API response.
        idleSessionTTL: Idle session timeout in seconds.
        listenOnPort: If true, bind to the configured port as the server listen port.
        loginRateLimit: Rate limit for login attempts (e.g. '100/min').
        protocol: API protocol: 'http' or 'https'.
        scripts: If true, enable JavaScript scripting support in the API.
        sensitiveFields: List of field names whose values are redacted in API responses and logs.
        ssl: TLS configuration for the API server.
        ssoRateLimit: Rate limit for SSO authentication attempts (e.g. '100/min').
        workerRemoteAccess: If true, enable remote access to Worker Processes via the API.
    """
    disabled: bool
    host: str
    port: int
    baseUrl: NotRequired[str]
    disableApiCache: NotRequired[bool]
    headers: NotRequired[dict[str, Any]]
    idleSessionTTL: NotRequired[int]
    listenOnPort: NotRequired[bool]
    loginRateLimit: NotRequired[str]
    protocol: NotRequired[str]
    scripts: NotRequired[bool]
    sensitiveFields: NotRequired[list[str]]
    ssl: NotRequired[ApiSslParam]
    ssoRateLimit: NotRequired[str]
    workerRemoteAccess: NotRequired[bool]


class AppsSettingsParam(TypedDict):
    """Apps backend settings.

    Attrs:
        enabled: If true, enable Apps.
        appBackendBrokerOrigin: Public origin for App Platform backend broker callbacks (standalone/on-prem only).
        appBackendMaxCallbacksPerInstallation: Maximum number of broker callbacks per minute a single app backend installation may make. Over-limit callbacks receive HTTP 429.
        appBackendMaxCallbacksTotal: Maximum number of broker callbacks per minute across all app backend installations on this Leader. Unlimited when unset. Over-limit callbacks receive HTTP 429.
        appBackendMaxInFlight: Maximum number of concurrent App Platform backend invocations across all apps.
        appScheduleBodyExpressionMaxLength: Maximum number of characters allowed in a schedule bodyExpression.
        appScheduledConcurrentJobLimit: Maximum number of concurrent scheduled App Platform function jobs across all apps on this Leader (group-wide). Changes require a Leader restart.
        appSchedulesMax: Maximum number of schedule records a single App may declare.
    """
    enabled: bool
    appBackendBrokerOrigin: NotRequired[str]
    appBackendMaxCallbacksPerInstallation: NotRequired[int]
    appBackendMaxCallbacksTotal: NotRequired[int]
    appBackendMaxInFlight: NotRequired[int]
    appScheduleBodyExpressionMaxLength: NotRequired[int]
    appScheduledConcurrentJobLimit: NotRequired[int]
    appSchedulesMax: NotRequired[int]


class CustomLogoParam(TypedDict):
    """Custom logo settings.

    Attrs:
        enabled: If true, display the custom logo in the UI.
        logoDescription: Description text displayed alongside the custom logo.
        logoImage: Custom logo image as a base64-encoded data URI (PNG or JPEG, max 2 MB).
    """
    enabled: bool
    logoDescription: NotRequired[str]
    logoImage: NotRequired[str]


class ProxySettingsParam(TypedDict, total=False):
    """Proxy settings.

    Attrs:
        useEnvVars: If true, use proxy settings from environment variables (HTTP_PROXY, HTTPS_PROXY, NO_PROXY).
    """
    useEnvVars: bool


class ShutdownSettingsParam(TypedDict, total=False):
    """Shutdown settings.

    Attrs:
        drainTimeout: Maximum time in milliseconds to wait for in-flight events to drain before forcing a shutdown.
    """
    drainTimeout: int


class SocketsSettingsParam(TypedDict, total=False):
    """Sockets settings.

    Attrs:
        directory: Filesystem directory path where Unix domain socket files are created.
    """
    directory: str


class FeatureFlagOverrideParam(TypedDict, total=False):
    """A feature flag override.

    Attrs:
        disabled: If true, the feature flag is disabled.
        flagId: Unique identifier of the feature flag to override.
    """
    disabled: bool
    flagId: str


class SupportSettingsParam(TypedDict, total=False):
    """Support settings.

    Attrs:
        featureFlagOverrides: List of feature flag overrides applied to this Cribl instance.
        logFileMaxFiles: Maximum number of log files to retain before rotating.
        logFileMaxSize: Maximum size of each log file (e.g. '10 MB').
    """
    featureFlagOverrides: list[FeatureFlagOverrideParam]
    logFileMaxFiles: int
    logFileMaxSize: str


class SystemSettingsSystemParam(TypedDict, total=False):
    """System subsection settings.

    Attrs:
        intercom: If true, enable Intercom integration for in-product messaging.
        upgrade: Upgrade permission policy: 'api' to allow upgrades from UI/API, or False to disable.
    """
    intercom: bool
    upgrade: Literal["api", False]


class UpgradeGroupSettingsParam(TypedDict, total=False):
    """Rolling upgrade group settings.

    Attrs:
        isRolling: If true, perform a rolling upgrade that updates nodes incrementally.
        quantity: Percentage of nodes to upgrade at a time during a rolling upgrade.
        retryCount: Number of times to retry upgrading a node before marking it as failed.
        retryDelay: Delay in milliseconds between upgrade retries.
    """
    isRolling: bool
    quantity: int
    retryCount: int
    retryDelay: int


class UpgradeSettingsParam(TypedDict, total=False):
    """Upgrade settings.

    Attrs:
        automaticUpgradeCheckPeriod: How frequently to check for available upgrades (e.g. '24h').
        disableAutomaticUpgrade: If true, automatic upgrades are disabled.
        enableLegacyEdgeUpgrade: If true, enable the legacy upgrade flow for Edge Nodes.
        packageUrls: List of custom package URLs to use for manual upgrades.
        rejectUnauthorized: If false, skip TLS certificate validation when downloading upgrade packages.
        upgradeSource: Upgrade source: 'cribl' for official packages or 'custom' for a custom URL.
    """
    automaticUpgradeCheckPeriod: str
    disableAutomaticUpgrade: bool
    enableLegacyEdgeUpgrade: bool
    packageUrls: list[str]
    rejectUnauthorized: bool
    upgradeSource: str


class WorkersSettingsParam(TypedDict, total=False):
    """Worker process settings.

    Attrs:
        count: Number of Worker Processes to spawn (0 = use available CPU cores).
        enableHeapSnapshots: If true, enable V8 heap snapshot generation on out-of-memory errors.
        loadThrottlePerc: CPU load percentage threshold above which new connections are throttled.
        memory: Maximum memory (in MB) per Worker Process (0 = no limit).
        minimum: Minimum number of Worker Processes to keep running.
        restartUnresponsiveProcesses: If true, automatically restart unresponsive Worker Processes.
        startupMaxConns: Maximum connections to accept during Worker startup before throttling.
        startupThrottleTimeout: Timeout (ms) to wait for Workers to reach idle before ending startup throttle.
        v8SingleThread: If true, run all worker threads in a single V8 isolate.
        workerProcessConfigUpdateConcurrency: Max Workers that can reload configuration concurrently.
        workerProcessReloadTimeout: Timeout (ms) for a Worker Process to reload configuration.
        workerThreadPoolSize: Size of the Worker thread pool for CPU-bound tasks.
    """
    count: int
    enableHeapSnapshots: bool
    loadThrottlePerc: int
    memory: int
    minimum: int
    restartUnresponsiveProcesses: bool
    startupMaxConns: int
    startupThrottleTimeout: int
    v8SingleThread: bool
    workerProcessConfigUpdateConcurrency: int
    workerProcessReloadTimeout: int
    workerThreadPoolSize: int


class CacheConnectionParam(TypedDict):
    """Cribl Lake dataset cache connection.

    Attrs:
        cacheRef: Reference to the cache connection.
        createdAt: Epoch timestamp of creation.
        retentionInDays: Number of days to retain cached data.
        acceleratedFields: List of accelerated field names for fast search.
        lakehouseConnectionType: Type of lakehouse connection.
        migrationQueryId: Query ID for ongoing migration.
    """
    cacheRef: str
    createdAt: float
    retentionInDays: float
    acceleratedFields: NotRequired[list[str]]
    lakehouseConnectionType: NotRequired[Literal["cache", "zeroPoint"]]
    migrationQueryId: NotRequired[str]


class DatasetMetricsParam(TypedDict, total=False):
    """Dataset size metrics.

    Attrs:
        currentSizeBytes: Current size of the dataset in bytes.
        metricsDate: ISO date when metrics were last calculated.
    """
    currentSizeBytes: float
    metricsDate: str


class ObjectStorageFilterParam(TypedDict, total=False):
    """Glob-to-Datatype mapping for Lake bucket path filters.

    Attrs:
        dataTypeId: Datatype identifier that maps filtered objects to a data type definition.
        filter: Glob pattern for selecting files within the storage path.
        dataPathFormat: Row format for Search v2 Lake path filters. Valid values: "ndjson", "parquet".
        preprocessOuterJson: When true, unwrap the outer JSON envelope before applying the datatype.
    """
    dataTypeId: str
    filter: str
    dataPathFormat: Literal["ndjson", "parquet"]
    preprocessOuterJson: bool


class DatasetMetadataRunInfoParam(TypedDict, total=False):
    """Details from the most recent acceleration scan.

    Attrs:
        earliestScannedTime: Timestamp (Unix seconds) for the earliest event observed during the scan.
        finishedAt: Timestamp (Unix milliseconds) when the acceleration run finished.
        latestScannedTime: Timestamp (Unix seconds) for the latest event observed during the scan.
        objectCount: Number of objects on the acceleration manifest after the scan completed.
    """
    earliestScannedTime: int
    finishedAt: int
    latestScannedTime: int
    objectCount: int


class DatasetMetadataParam(TypedDict, total=False):
    """Key-value metadata for a Dataset search configuration.

    Attrs:
        earliest: Rolling time window that defines how far back acceleration scans (e.g. "-30d").
        enableAcceleration: If true, the system automatically backfills and refreshes Dataset metadata.
        fieldList: Fields for which acceleration gathers statistics. Required when scan mode is detailed.
        latestRunInfo: Details from the most recent acceleration scan.
    """
    earliest: str
    enableAcceleration: bool
    fieldList: list[str]
    latestRunInfo: DatasetMetadataRunInfoParam


class DatasetSearchConfigParam(TypedDict, total=False):
    """Dataset search configuration.

    Attrs:
        datatypes: Data type identifiers included in this dataset.
        description: Human-readable description of the dataset.
        metadata: Key-value metadata for the Dataset search configuration.
        pathFilters: Glob-to-Datatype mappings for the Lake bucket path.
        searchVersion: Search schema version. Valid values: "v1", "v2".
        tags: Comma-separated tags for filtering.
    """
    datatypes: list[str]
    description: str
    metadata: DatasetMetadataParam
    pathFilters: list[ObjectStorageFilterParam]
    searchVersion: Literal["v1", "v2"]
    tags: str


class PackTagsParam(TypedDict, total=False):
    """Categorization tags for a Pack.

    Attrs:
        dataType: List of data type tags.
        domain: List of domain tags (e.g. 'security', 'observability').
        technology: List of technology tags (e.g. 'aws', 'splunk').
        streamtags: List of stream tags for routing and filtering.
    """
    dataType: list[str]
    domain: list[str]
    technology: list[str]
    streamtags: list[str]


class BackupsSettingsParam(TypedDict, total=False):
    """Configuration backup settings.

    Attrs:
        backupPersistence: How long to retain backups (duration string, e.g. '24h').
        backupsDirectory: Filesystem path where configuration backups are stored.
    """
    backupPersistence: str
    backupsDirectory: str


class PiiSettingsParam(TypedDict, total=False):
    """PII detection settings.

    Attrs:
        enablePiiDetection: If true, enable PII detection for events.
    """
    enablePiiDetection: bool


class RollbackSettingsParam(TypedDict, total=False):
    """Automatic rollback settings.

    Attrs:
        rollbackEnabled: If true, enable automatic rollback on upgrade failure.
        rollbackRetries: Number of retry attempts before marking rollback as failed.
        rollbackTimeout: Max duration (ms) to wait for rollback to complete.
    """
    rollbackEnabled: bool
    rollbackRetries: int
    rollbackTimeout: int


class SniSettingsParam(TypedDict, total=False):
    """SNI routing settings.

    Attrs:
        disableSNIRouting: If true, disable Server Name Indication routing.
    """
    disableSNIRouting: bool


class TlsSettingsParam(TypedDict, total=False):
    """Global TLS settings.

    Attrs:
        defaultCipherList: Cipher suite list (DEFAULT = system default).
        defaultEcdhCurve: ECDH curve name (auto = let Node.js choose).
        maxVersion: Maximum TLS protocol version.
        minVersion: Minimum TLS protocol version.
        rejectUnauthorized: If true, reject unverifiable certificates.
    """
    defaultCipherList: str
    defaultEcdhCurve: str
    maxVersion: str
    minVersion: str
    rejectUnauthorized: bool


class TLSClientParams(TypedDict):
    """TLS client connection settings (request body).

    Attrs:
        disabled: If true, TLS is disabled for the connection.
        caPath: Path to the Certificate Authority (CA) certificate file in PEM format.
        certPath: Path to the client certificate file in PEM format.
        certificateName: Name of a certificate stored in Cribl.
        maxVersion: Maximum TLS version to allow for the connection. Valid values: "TLSv1.3", "TLSv1.2", "TLSv1.1", "TLSv1".
        minVersion: Minimum TLS version to allow for the connection. Valid values: "TLSv1.3", "TLSv1.2", "TLSv1.1", "TLSv1".
        passphrase: Passphrase for the private key.
        privKeyPath: Path to the private key file in PEM format.
        rejectUnauthorized: If true, reject connections to servers with unverified TLS certificates.
        servername: Server name for TLS Server Name Indication (SNI) extension.
    """
    disabled: bool
    caPath: NotRequired[str]
    certPath: NotRequired[str]
    certificateName: NotRequired[str]
    maxVersion: NotRequired[Literal["TLSv1.3", "TLSv1.2", "TLSv1.1", "TLSv1"]]
    minVersion: NotRequired[Literal["TLSv1.3", "TLSv1.2", "TLSv1.1", "TLSv1"]]
    passphrase: NotRequired[str]
    privKeyPath: NotRequired[str]
    rejectUnauthorized: NotRequired[bool]
    servername: NotRequired[str]


# --- Auth ---


class Security(BaseModel):
    """Authentication configuration.

    Use bearer_auth for token-based auth (on-prem login flow).
    Use client_id + client_secret for OAuth2 client credentials (cloud).

    The token_url and audience defaults come from the OpenAPI spec's
    securitySchemes.clientOauth definition.
    """

    CLOUD_TOKEN_URL: ClassVar[str] = "https://login.cribl.cloud/oauth/token"
    CLOUD_AUDIENCE: ClassVar[str] = "https://api.cribl.cloud"

    bearer_auth: str | None = Field(default=None, description="Pre-existing bearer token for on-prem or manual auth.")
    """Pre-existing bearer token for on-prem or manual auth."""
    client_id: str | None = Field(default=None, description="OAuth2 client ID for cloud client-credentials flow.")
    """OAuth2 client ID for cloud client-credentials flow."""
    client_secret: str | None = Field(default=None, description="OAuth2 client secret for cloud client-credentials flow.")
    """OAuth2 client secret for cloud client-credentials flow."""
    username: str | None = Field(default=None, description="Username for on-prem login via POST /auth/login.")
    """Username for on-prem login via POST /auth/login."""
    password: str | None = Field(default=None, description="Password for on-prem login via POST /auth/login.")
    """Password for on-prem login via POST /auth/login."""
    audience: str | None = Field(default=None, description="OAuth2 audience. Defaults to https://api.cribl.cloud for cloud.")
    """OAuth2 audience. Defaults to https://api.cribl.cloud for cloud."""
    token_url: str | None = Field(default=None, description="OAuth2 token endpoint. Defaults to https://login.cribl.cloud/oauth/token for cloud.")
    """OAuth2 token endpoint. Defaults to https://login.cribl.cloud/oauth/token for cloud."""


class AuthToken(BaseModel):
    """Response from /auth/login — contains the bearer token for subsequent requests."""

    token: str = Field(description="Bearer token to include in the Authorization header for subsequent API requests.")
    """Bearer token to include in the Authorization header for subsequent API requests."""
    force_password_change: bool = Field(
        alias="forcePasswordChange",
        description="If true, the user must change their password before accessing the API.",
    )
    """If true, the user must change their password before accessing the API."""


# --- Streaming ---


class CapturedEvent(CriblModel):
    """A single event from a live data capture (NDJSON stream)."""

    raw: str | None = Field(default=None, alias="_raw", description="Raw event data.")
    """Raw event data."""
    time: float | None = Field(default=None, alias="_time", description="Timestamp of the event.")
    """Timestamp of the event."""


# --- Health ---


class HealthOverlayStatus(CriblModel):
    """Overlay state of a Cribl process."""

    state: Literal["active", "inactive"] | None = Field(default=None, description="Current overlay state.")
    """Current overlay state."""


class HealthServerStatus(CriblModel):
    """Health status of the Leader or Worker Node."""

    is_captain: bool | None = Field(
        default=None,
        alias="isCaptain",
        description="Whether this node is the captain (job scheduling coordinator).",
    )
    """Whether this node is the captain (job scheduling coordinator)."""
    overlay: HealthOverlayStatus = Field(description="Overlay state for this process.")
    """Overlay state for this process."""
    role: Literal["primary", "standby"] | None = Field(default=None, description="Leader Node role: 'primary' or 'standby'.")
    """Leader Node role: 'primary' or 'standby'."""
    start_time: int = Field(alias="startTime", description="Timestamp (Unix epoch) when the Cribl process started.")
    """Timestamp (Unix epoch) when the Cribl process started."""
    status: Literal["healthy", "standby", "shutting down"] = Field(description="Health state: 'healthy', 'standby', or 'shutting down'.")
    """Health state: 'healthy', 'standby', or 'shutting down'."""


class HealthyWorkerStatus(CriblModel):
    """Worker health status when all Worker Processes are up and healthy."""

    status: Literal["healthy"] = Field(description="Always 'healthy'.")
    """Always 'healthy'."""


class MixedWorkerStatus(CriblModel):
    """Worker health status when some Worker Processes are up and some are not."""

    ready: int = Field(description="Number of probed Worker Processes that reported up.")
    """Number of probed Worker Processes that reported up."""
    status: Literal["mixed"] = Field(description="Always 'mixed'.")
    """Always 'mixed'."""
    workers: int = Field(description="Number of Worker Processes probed.")
    """Number of Worker Processes probed."""


class DownWorkerStatus(CriblModel):
    """Worker health status when no Worker Processes are up, or the server is shutting down / in standby."""

    status: Literal["down"] = Field(description="Always 'down'.")
    """Always 'down'."""


WorkerHealthStatus = Annotated[
    HealthyWorkerStatus | MixedWorkerStatus, Field(discriminator="status")
]
"""Worker Process health payload for a 200 response from `GET /health/workers`: all up ('healthy') or a partial set up ('mixed')."""


# --- Git/Versioning ---


class CurrentBranchResult(CriblModel):
    branch: str = Field(description="Name of the Git branch that the Cribl configuration is currently checked out to.")
    """Name of the Git branch that the Cribl configuration is currently checked out to."""


class GitLogResult(BaseModel):
    """A git commit log entry."""

    author_email: str | None = Field(default=None, alias="author_email", description="Author email.")
    """Author email."""
    author_name: str | None = Field(default=None, alias="author_name", description="Author name.")
    """Author name."""
    body: str | None = Field(default=None, description="Commit body/extended message.")
    """Commit body/extended message."""
    date: str | None = Field(default=None, description="Commit date.")
    """Commit date."""
    hash: str | None = Field(default=None, description="Commit hash.")
    """Commit hash."""
    message: str | None = Field(default=None, description="Commit message.")
    """Commit message."""
    refs: str | None = Field(default=None, description="Refs associated with this commit.")
    """Refs associated with this commit."""


class BranchInfo(BaseModel):
    """A git branch."""

    id: str = Field(description="Unique identifier.")
    """Unique identifier."""
    srcGroup: str | None = Field(
        default=None,
        alias="__srcGroup",
        description="Fleet or group id this entity was inherited from when served by a Config Helper for a child fleet. Present when inherited from parent, including when the child has a local overlay. Omitted when the entity is local and not inherited. Display-only; never persisted.",
    )
    """Fleet or group id this entity was inherited from when served by a Config Helper for a child fleet. Present when inherited from parent, including when the child has a local overlay. Omitted when the entity is local and not inherited. Display-only; never persisted."""
    srcOverridden: bool | None = Field(
        default=None,
        alias="__srcOverridden",
        description="If true, the child fleet has a local overlay on an inherited entity. Omitted when inherited and unmodified, or when local and not inherited. Display-only; never persisted.",
    )
    """If true, the child fleet has a local overlay on an inherited entity. Omitted when inherited and unmodified, or when local and not inherited. Display-only; never persisted."""


class GitCommitAuthor(BaseModel):
    """Author of a git commit."""

    email: str = Field(description="Author email address.")
    """Author email address."""
    name: str = Field(description="Author name.")
    """Author name."""


class GitCommitFiles(BaseModel):
    """Files changed in a git commit."""

    created: list[str] | None = Field(default=None, description="Newly created file paths.")
    """Newly created file paths."""
    deleted: list[str] | None = Field(default=None, description="Deleted file paths.")
    """Deleted file paths."""
    modified: list[str] | None = Field(default=None, description="Modified file paths.")
    """Modified file paths."""
    renamed: list[dict[str, str]] | None = Field(default=None, description="Renamed file paths with old/new mapping.")
    """Renamed file paths with old/new mapping."""


class GitCommitChangeSummary(BaseModel):
    """Summary of line changes in a commit."""

    changes: int = Field(description="Total number of lines changed (insertions plus deletions).")
    """Total number of lines changed (insertions plus deletions)."""
    deletions: int = Field(description="Number of lines deleted.")
    """Number of lines deleted."""
    insertions: int = Field(description="Number of lines inserted.")
    """Number of lines inserted."""


class GitCommitSummary(BaseModel):
    """Result of a git commit operation."""

    author: GitCommitAuthor | None = Field(default=None, description="Author of the commit.")
    """Author of the commit."""
    branch: str | None = Field(default=None, description="Branch the commit was made on.")
    """Branch the commit was made on."""
    commit: str | None = Field(default=None, description="New commit hash.")
    """New commit hash."""
    files: GitCommitFiles | None = Field(default=None, description="Files changed in the commit.")
    """Files changed in the commit."""
    message: str | None = Field(default=None, description="Commit summary message.")
    """Commit summary message."""
    summary: GitCommitChangeSummary | None = Field(default=None, description="Summary of line changes in the commit.")
    """Summary of line changes in the commit."""


class GitInfo(BaseModel):
    """Configuration and status for the Git integration."""

    remote: str | bool = Field(description="Remote repository URL or false if no remote.")
    """Remote repository URL or false if no remote."""
    versioning: bool = Field(description="Whether versioning is enabled.")
    """Whether versioning is enabled."""


class GitFileStatus(BaseModel):
    """Status of a single file in git."""

    index: str | None = Field(default=None, description="Index status character.")
    """Index status character."""
    path: str | None = Field(default=None, description="File path.")
    """File path."""
    working_dir: str | None = Field(default=None, alias="working_dir", description="Working directory status character.")
    """Working directory status character."""


class GitStatusResult(BaseModel):
    """Status of the current working tree."""

    ahead: int | None = Field(default=None, description="Number of commits ahead of remote.")
    """Number of commits ahead of remote."""
    behind: int | None = Field(default=None, description="Number of commits behind remote.")
    """Number of commits behind remote."""
    conflicted: list[str] | None = Field(default=None, description="Conflicted file paths.")
    """Conflicted file paths."""
    created: list[str] | None = Field(default=None, description="Newly created file paths.")
    """Newly created file paths."""
    current: str | None = Field(default=None, description="Current branch name.")
    """Current branch name."""
    deleted: list[str] | None = Field(default=None, description="Deleted file paths.")
    """Deleted file paths."""
    files: list[GitFileStatus] | None = Field(default=None, description="Detailed file status list.")
    """Detailed file status list."""
    modified: list[str] | None = Field(default=None, description="Modified file paths.")
    """Modified file paths."""
    not_added: list[str] | None = Field(default=None, alias="not_added", description="Untracked file paths.")
    """Untracked file paths."""
    renamed: list[str] | None = Field(default=None, description="Renamed file paths.")
    """Renamed file paths."""
    staged: list[str] | None = Field(default=None, description="Array of file paths that are staged for the next commit.")
    """Array of file paths that are staged for the next commit."""
    tracking: str | None = Field(default=None, description="Remote tracking branch.")
    """Remote tracking branch."""


class DiffLine(CriblModel):
    """A single line in a git diff hunk (insert, delete, or context)."""

    type: Literal["insert", "delete", "context"] = Field(description="Line change type.")
    """Line change type."""
    content: str = Field(description="Full content of the line, including the diff prefix character.")
    """Full content of the line, including the diff prefix character."""
    new_number: int | None = Field(default=None, alias="newNumber", description="Line number in the new file.")
    """Line number in the new file."""
    old_number: int | None = Field(default=None, alias="oldNumber", description="Line number in the original file.")
    """Line number in the original file."""


class DiffBlock(CriblModel):
    """A diff hunk showing changed lines in a file."""

    header: str = Field(description="Unified diff hunk header (e.g. '@@ -1,5 +1,8 @@').")
    """Unified diff hunk header (e.g. '@@ -1,5 +1,8 @@')."""
    lines: list[DiffLine] = Field(description="Array of diff lines in this hunk.")
    """Array of diff lines in this hunk."""
    new_start_line: int = Field(alias="newStartLine", description="Starting line number in the new file for this hunk.")
    """Starting line number in the new file for this hunk."""
    old_start_line: int = Field(alias="oldStartLine", description="Starting line number in the original file for this hunk.")
    """Starting line number in the original file for this hunk."""
    old_start_line2: int | None = Field(default=None, alias="oldStartLine2", description="Starting line in the original file for the second parent (combined diffs).")
    """Starting line in the original file for the second parent (combined diffs)."""


class DiffFile(CriblModel):
    """A single file entry in a git diff."""

    added_lines: int = Field(alias="addedLines", description="Number of lines added in this file.")
    """Number of lines added in this file."""
    blocks: list[DiffBlock] = Field(description="Array of diff blocks (hunks) showing changed line ranges.")
    """Array of diff blocks (hunks) showing changed line ranges."""
    deleted_lines: int = Field(alias="deletedLines", description="Number of lines deleted in this file.")
    """Number of lines deleted in this file."""
    is_combined: bool = Field(alias="isCombined", description="If true, this is a combined diff (merge commit).")
    """If true, this is a combined diff (merge commit)."""
    is_git_diff: bool = Field(alias="isGitDiff", description="If true, this diff was generated by Git.")
    """If true, this diff was generated by Git."""
    language: str | None = Field(default=None, description="Programming language or file format detected for syntax highlighting. Omitted for extensionless files.")
    """Programming language or file format detected for syntax highlighting. Omitted for extensionless files."""
    new_name: str = Field(alias="newName", description="New file path after the change.")
    """New file path after the change."""
    old_name: str = Field(alias="oldName", description="Original file path before the change.")
    """Original file path before the change."""
    changed_percentage: float | None = Field(default=None, alias="changedPercentage", description="Percentage of lines in the file that changed.")
    """Percentage of lines in the file that changed."""
    checksum_after: str | None = Field(default=None, alias="checksumAfter", description="Checksum of the new file.")
    """Checksum of the new file."""
    checksum_before: str | list[str] | None = Field(default=None, alias="checksumBefore", description="Checksum of the original file. May be an array for combined diffs.")
    """Checksum of the original file. May be an array for combined diffs."""
    deleted_file_mode: str | None = Field(default=None, alias="deletedFileMode", description="File mode of the deleted file.")
    """File mode of the deleted file."""
    is_binary: bool | None = Field(default=None, alias="isBinary", description="If true, this is a binary file.")
    """If true, this is a binary file."""
    is_copy: bool | None = Field(default=None, alias="isCopy", description="If true, this file was copied from another path.")
    """If true, this file was copied from another path."""
    is_deleted: bool | None = Field(default=None, alias="isDeleted", description="If true, this file was deleted in the commit.")
    """If true, this file was deleted in the commit."""
    is_new: bool | None = Field(default=None, alias="isNew", description="If true, this file was added in the commit.")
    """If true, this file was added in the commit."""
    is_rename: bool | None = Field(default=None, alias="isRename", description="If true, this file was renamed.")
    """If true, this file was renamed."""
    is_too_big: bool | None = Field(default=None, alias="isTooBig", description="If true, the diff was truncated.")
    """If true, the diff was truncated."""
    mode: str | None = Field(default=None, description="Combined file mode when both old and new modes are the same.")
    """Combined file mode when both old and new modes are the same."""
    new_file_mode: str | None = Field(default=None, alias="newFileMode", description="File mode of the new file (when added).")
    """File mode of the new file (when added)."""
    new_mode: str | None = Field(default=None, alias="newMode", description="File mode of the new file.")
    """File mode of the new file."""
    old_mode: str | list[str] | None = Field(default=None, alias="oldMode", description="File mode of the original file. May be an array for combined diffs.")
    """File mode of the original file. May be an array for combined diffs."""
    unchanged_percentage: float | None = Field(default=None, alias="unchangedPercentage", description="Percentage of lines unchanged.")
    """Percentage of lines unchanged."""


class GitDiffResult(BaseModel):
    """Diff of file changes in a commit."""

    diff_json: list[DiffFile] = Field(
        alias="diffJson",
        description="Array of file diffs in the specified commit.",
    )
    """Array of file diffs in the specified commit."""


class GitShowResult(CriblModel):
    """Result of git show for a specific commit."""

    commit_message: str = Field(alias="commitMessage", description="Full commit message of the specified commit.")
    """Full commit message of the specified commit."""
    diff_json: list[DiffFile] | None = Field(
        default=None, alias="diffJson",
        description="Diff of the file changes introduced by the commit.",
    )
    """Diff of the file changes introduced by the commit."""


class GitFile(BaseModel):
    """A file entry in the git configuration tree."""

    name: str = Field(description="Path of the file relative to the configuration root.")
    """Path of the file relative to the configuration root."""
    autoIncludedInCommit: bool | None = Field(default=None, description="If true, this file is automatically included in commits without being explicitly listed.")
    """If true, this file is automatically included in commits without being explicitly listed."""
    children: list["GitFile"] | None = Field(default=None, description="Nested files and subdirectories when this entry is a directory (recursive).")
    """Nested files and subdirectories when this entry is a directory (recursive)."""
    state: str | None = Field(default=None, description="Git status code for the file: M for modified, A for added, or D for deleted.")
    """Git status code for the file: M for modified, A for added, or D for deleted."""


class GitFilesResponse(BaseModel):
    """Response containing files from a git commit."""

    commit_message: str | None = Field(default=None, alias="commitMessage", description="Commit message.")
    """Commit message."""
    count: int | None = Field(default=None, description="Number of files.")
    """Number of files."""
    items: list[GitFile] | None = Field(default=None, description="List of files in the commit.")
    """List of files in the commit."""


class GitCountResult(BaseModel):
    """Count of git items (commits, files, etc.)."""

    count: int = Field(description="Number of items.")
    """Number of items."""


class OutputTestResponse(CriblModel):
    """Result of testing a Destination by sending sample events."""

    outputId: str = Field(description="The id of the Destination that was tested.")
    """The id of the Destination that was tested."""
    success: bool = Field(description="If true, the Destination test succeeded. Otherwise, false.")
    """If true, the Destination test succeeded. Otherwise, false."""
    details: dict[str, Any] | None = Field(default=None, description="Additional details about the Destination test, such as per-event results and transport-level information.")
    """Additional details about the Destination test, such as per-event results and transport-level information."""
    error: str | None = Field(default=None, description="Error message that describes a failed Destination test.")
    """Error message that describes a failed Destination test."""
    successDetail: str | None = Field(default=None, description="Human-readable description for a successful Destination test result.")
    """Human-readable description for a successful Destination test result."""


class OutputSamplesResponse(CriblModel):
    """Sample events from a Destination."""

    events: list[dict[str, Any]] = Field(description="Array of sample events returned from a Destination test.")
    """Array of sample events returned from a Destination test."""


class GitRevertAuditFiles(CriblModel):
    """Files affected by a revert operation, grouped by change type."""

    created: list[str] | None = Field(default=None, description="Array of file paths that were created in the commit.")
    """Array of file paths that were created in the commit."""
    deleted: list[str] | None = Field(default=None, description="Array of file paths that were deleted in the commit.")
    """Array of file paths that were deleted in the commit."""
    modified: list[str] | None = Field(default=None, description="Array of file paths that were modified in the commit.")
    """Array of file paths that were modified in the commit."""
    renamed: list[dict[str, str]] | None = Field(default=None, description="Array of file rename operations, each containing the original path and the new path.")
    """Array of file rename operations, each containing the original path and the new path."""


class GitRevertAudit(CriblModel):
    """Audit record for a revert operation."""

    id: str = Field(description="SHA-1 hash of the revert commit that was created.")
    """SHA-1 hash of the revert commit that was created."""
    files: GitRevertAuditFiles | None = Field(default=None, description="Files affected by the revert, grouped by change type.")
    """Files affected by the revert, grouped by change type."""
    group: str | None = Field(default=None, description="Worker Group the revert was applied to, if applicable.")
    """Worker Group the revert was applied to, if applicable."""


class GitRevertResult(CriblModel):
    """Result of a git revert operation."""

    audit: GitRevertAudit = Field(description="Audit record for the revert operation, including the commit hash and affected files.")
    """Audit record for the revert operation, including the commit hash and affected files."""
    reverted: bool = Field(description="If true, the revert was applied successfully. Otherwise, false.")
    """If true, the revert was applied successfully. Otherwise, false."""


# --- System ---


class SystemSettings(CriblModel):
    """System-level settings for a Cribl instance."""

    api: ApiSettingsParam | None = Field(default=None, description="API server configuration for the Cribl instance.")
    """API server configuration for the Cribl instance."""
    apps: AppsSettingsParam | None = Field(default=None, description="App configuration.")
    """App configuration."""
    backups: BackupsSettingsParam | None = Field(default=None, description="Configuration backup settings, including storage location and retention period.")
    """Configuration backup settings, including storage location and retention period."""
    customLogo: CustomLogoParam | None = Field(default=None, description="Custom logo configuration for the Cribl UI login page and navigation bar.")
    """Custom logo configuration for the Cribl UI login page and navigation bar."""
    pii: PiiSettingsParam | None = Field(default=None, description="Personally identifiable information (PII) detection configuration.")
    """Personally identifiable information (PII) detection configuration."""
    proxy: ProxySettingsParam | None = Field(default=None, description="HTTP proxy configuration for outbound connections.")
    """HTTP proxy configuration for outbound connections."""
    rollback: RollbackSettingsParam | None = Field(default=None, description="Automatic rollback settings applied when an upgrade fails.")
    """Automatic rollback settings applied when an upgrade fails."""
    shutdown: ShutdownSettingsParam | None = Field(default=None, description="Graceful shutdown configuration.")
    """Graceful shutdown configuration."""
    sni: SniSettingsParam | None = Field(default=None, description="Server Name Indication (SNI) routing configuration.")
    """Server Name Indication (SNI) routing configuration."""
    sockets: SocketsSettingsParam | None = Field(default=None, description="Unix domain socket configuration.")
    """Unix domain socket configuration."""
    support: SupportSettingsParam | None = Field(default=None, description="Support and diagnostics settings.")
    """Support and diagnostics settings."""
    system: SystemSettingsSystemParam | None = Field(default=None, description="System-level operational settings for the Cribl instance.")
    """System-level operational settings for the Cribl instance."""
    tls: TlsSettingsParam | None = Field(default=None, description="Global TLS/SSL settings applied to all outbound connections that do not specify their own TLS configuration.")
    """Global TLS/SSL settings applied to all outbound connections that do not specify their own TLS configuration."""
    upgradeGroupSettings: UpgradeGroupSettingsParam | None = Field(default=None, description="Rolling upgrade group settings that control how many nodes are upgraded at a time.")
    """Rolling upgrade group settings that control how many nodes are upgraded at a time."""
    upgradeSettings: UpgradeSettingsParam | None = Field(default=None, description="Automatic upgrade scheduling and package source configuration.")
    """Automatic upgrade scheduling and package source configuration."""
    workers: WorkersSettingsParam | None = Field(default=None, description="Worker Process configuration.")
    """Worker Process configuration."""


# --- Workers/Nodes ---


class AwsHeartbeatMetadata(CriblModel):
    """AWS instance metadata collected from a node."""

    enabled: bool = Field(description="If true, the AWS metadata collector is enabled on the node.")
    """If true, the AWS metadata collector is enabled on the node."""
    instanceId: str | None = Field(default=None, description="AWS EC2 instance ID.")
    """AWS EC2 instance ID."""
    region: str | None = Field(default=None, description="AWS region name.")
    """AWS region name."""
    tags: dict[str, str] | None = Field(default=None, description="AWS EC2 instance tags.")
    """AWS EC2 instance tags."""
    type: str | None = Field(default=None, description="AWS EC2 instance type.")
    """AWS EC2 instance type."""
    zone: str | None = Field(default=None, description="AWS availability zone name.")
    """AWS availability zone name."""


class AzureHeartbeatMetadata(CriblModel):
    """Azure instance metadata collected from a node."""

    enabled: bool = Field(description="If true, the Azure metadata collector is enabled on the node.")
    """If true, the Azure metadata collector is enabled on the node."""
    hostname: str | None = Field(default=None, description="Azure VM hostname.")
    """Azure VM hostname."""
    instanceId: str | None = Field(default=None, description="Azure instance ID.")
    """Azure instance ID."""
    name: str | None = Field(default=None, description="Azure VM name.")
    """Azure VM name."""
    region: str | None = Field(default=None, description="Azure location or region.")
    """Azure location or region."""
    resourceGroup: str | None = Field(default=None, description="Azure resource group name.")
    """Azure resource group name."""
    subscriptionId: str | None = Field(default=None, description="Azure subscription ID.")
    """Azure subscription ID."""
    tags: dict[str, str] | None = Field(default=None, description="Azure tags.")
    """Azure tags."""
    type: str | None = Field(default=None, description="Azure VM size or instance type.")
    """Azure VM size or instance type."""
    vmId: str | None = Field(default=None, description="Azure VM ID.")
    """Azure VM ID."""
    zone: str | None = Field(default=None, description="Azure availability zone.")
    """Azure availability zone."""


class OsHeartbeatMetadata(CriblModel):
    """Operating system metadata collected from a node."""

    addresses: list[str] = Field(description="Network addresses reported by the operating system.")
    """Network addresses reported by the operating system."""
    enabled: bool | None = Field(default=None, description="If true, the OS metadata collector is enabled on the node.")
    """If true, the OS metadata collector is enabled on the node."""
    id: str | None = Field(default=None, description="Operating system distribution name.")
    """Operating system distribution name."""
    version: str | None = Field(default=None, description="Operating system version.")
    """Operating system version."""


class KubeOwnerMetadata(CriblModel):
    """Kubernetes owner resource for a Pod."""

    kind: str = Field(description="Kubernetes owner resource kind.")
    """Kubernetes owner resource kind."""
    name: str = Field(description="Kubernetes owner resource name.")
    """Kubernetes owner resource name."""


class KubeHeartbeatMetadata(CriblModel):
    """Kubernetes metadata collected from a node."""

    enabled: bool = Field(description="If true, the Kubernetes metadata collector is enabled on the node.")
    """If true, the Kubernetes metadata collector is enabled on the node."""
    namespace: str | None = Field(default=None, description="Kubernetes Namespace name.")
    """Kubernetes Namespace name."""
    node: str | None = Field(default=None, description="Kubernetes Node name.")
    """Kubernetes Node name."""
    owner: KubeOwnerMetadata | None = Field(default=None, description="Kubernetes owner resource for the Pod.")
    """Kubernetes owner resource for the Pod."""
    pod: str | None = Field(default=None, description="Kubernetes Pod name.")
    """Kubernetes Pod name."""
    source: str | None = Field(default=None, description="Kubernetes config source.")
    """Kubernetes config source."""


class HeartbeatMetadata(CriblModel):
    """Cloud, Kubernetes, and operating system metadata collected from a node."""

    aws: AwsHeartbeatMetadata | None = Field(default=None, description="AWS instance metadata collected from the node.")
    """AWS instance metadata collected from the node."""
    azure: AzureHeartbeatMetadata | None = Field(default=None, description="Azure instance metadata collected from the node.")
    """Azure instance metadata collected from the node."""
    hostOs: OsHeartbeatMetadata | None = Field(default=None, description="Host operating system metadata collected from the node.")
    """Host operating system metadata collected from the node."""
    kube: KubeHeartbeatMetadata | None = Field(default=None, description="Kubernetes metadata collected from the node.")
    """Kubernetes metadata collected from the node."""
    os: OsHeartbeatMetadata | None = Field(default=None, description="Operating system metadata collected from the node.")
    """Operating system metadata collected from the node."""


class HBCriblConfigInfo(CriblModel):
    """Configuration bundle and policy revision metadata for a node."""

    version: str | None = Field(default=None, description="Configuration bundle version.")
    """Configuration bundle version."""
    hbPeriodSeconds: int | None = Field(default=None, description="Worker-to-Leader heartbeat interval, in seconds.")
    """Worker-to-Leader heartbeat interval, in seconds."""
    featuresRev: str | None = Field(default=None, description="Feature flags revision string for the bundle.")
    """Feature flags revision string for the bundle."""
    logStreamEnv: str | None = Field(default=None, description="GitOps or LogStream environment label associated with the bundle.")
    """GitOps or LogStream environment label associated with the bundle."""
    policyRev: str | None = Field(default=None, description="Current policies revision string.")
    """Current policies revision string."""
    apiCredentialsRev: str | None = Field(default=None, description="Current API credentials revision string.")
    """Current API credentials revision string."""
    teamsRev: str | None = Field(default=None, description="Current teams revision string.")
    """Current teams revision string."""
    usersRev: str | None = Field(default=None, description="Current users revision string.")
    """Current users revision string."""


class HBLeaderInfo(CriblModel):
    """Leader connection details when the node is a Worker or Edge reporting upstream."""

    host: str | None = Field(default=None, description="Leader hostname or IP address.")
    """Leader hostname or IP address."""
    port: int | None = Field(default=None, description="Leader TCP port.")
    """Leader TCP port."""
    servername: str | None = Field(default=None, description="TLS server name (SNI) for the Leader connection.")
    """TLS server name (SNI) for the Leader connection."""
    tls: bool | None = Field(default=None, description="If true, TLS is enabled for the Leader connection.")
    """If true, TLS is enabled for the Leader connection."""


class HBCriblInfo(CriblModel):
    """Cribl software and configuration details reported by a node."""

    config: HBCriblConfigInfo | None = Field(default=None, description="Configuration bundle and policy revision metadata for the node.")
    """Configuration bundle and policy revision metadata for the node."""
    deploymentId: str | None = Field(default=None, description="Unique identifier for the deployment assigned for the node.")
    """Unique identifier for the deployment assigned for the node."""
    disableSNIRouting: bool | None = Field(default=None, description="If true, SNI-based routing to the Leader is disabled for the connection.")
    """If true, SNI-based routing to the Leader is disabled for the connection."""
    distMode: str | None = Field(default=None, description="Distributed deployment mode for the instance.")
    """Distributed deployment mode for the instance."""
    edgeNodes: int | None = Field(default=None, description="Count of Edge nodes reported in the Leader heartbeat.")
    """Count of Edge nodes reported in the Leader heartbeat."""
    group: str | None = Field(default=None, description="Worker Group or Edge Fleet name.")
    """Worker Group or Edge Fleet name."""
    guid: str | None = Field(default=None, description="Unique instance identifier for the Cribl node.")
    """Unique instance identifier for the Cribl node."""
    installType: str | None = Field(default=None, description="Value of the CRIBL_INSTALL_TYPE environment variable.")
    """Value of the CRIBL_INSTALL_TYPE environment variable."""
    autoLookupVersions: dict[str, dict[str, str]] | None = Field(default=None, description="Automatically deployed Lookup file names and their deployed versions by context.")
    """Automatically deployed Lookup file names and their deployed versions by context."""
    lookupVersions: dict[str, dict[str, str]] | None = Field(default=None, description="Deployed Lookup file names and their deployed versions by context.")
    """Deployed Lookup file names and their deployed versions by context."""
    master: HBLeaderInfo | None = Field(default=None, description="Leader connection details when the node is a Worker or Edge reporting upstream.")
    """Leader connection details when the node is a Worker or Edge reporting upstream."""
    overlayId: str | None = Field(default=None, description="Currently active overlay identifier on the node.")
    """Currently active overlay identifier on the node."""
    pid: int | None = Field(default=None, description="The process ID.")
    """The process ID."""
    socksEnabled: bool | None = Field(default=None, description="If true, SOCKS proxy connectivity is enabled for the node.")
    """If true, SOCKS proxy connectivity is enabled for the node."""
    startTime: int | None = Field(default=None, description="Timestamp (in Unix time) when the Cribl server process started, in milliseconds.")
    """Timestamp (in Unix time) when the Cribl server process started, in milliseconds."""
    tags: list[str] | None = Field(default=None, description="Tags from the node.")
    """Tags from the node."""
    version: str | None = Field(default=None, description="Cribl software version string for the node.")
    """Cribl software version string for the node."""


class OutpostNodeInfo(CriblModel):
    """Outpost Node information."""

    groupname: str | None = Field(default=None, description="Name of the Outpost Group that contains the Outpost Node.")
    """Name of the Outpost Group that contains the Outpost Node."""
    guid: str = Field(description="Unique identifier for the Outpost Node.")
    """Unique identifier for the Outpost Node."""
    host: str = Field(description="Hostname or IP address for the Outpost Node.")
    """Hostname or IP address for the Outpost Node."""


class NodeProvidedInfo(CriblModel):
    """Metadata reported by a Worker or Edge Node."""

    architecture: str = Field(description="CPU architecture.")
    """CPU architecture."""
    cpus: int = Field(description="Number of CPU cores available on the node.")
    """Number of CPU cores available on the node."""
    cribl: HBCriblInfo = Field(description="Cribl software and configuration details reported by the node.")
    """Cribl software and configuration details reported by the node."""
    env: dict[str, str] = Field(description="Environment variables reported by the node.")
    """Environment variables reported by the node."""
    hostname: str = Field(description="Hostname reported by the node.")
    """Hostname reported by the node."""
    node: str = Field(description="Node.js runtime version running on the node.")
    """Node.js runtime version running on the node."""
    platform: str = Field(description="Operating system platform.")
    """Operating system platform."""
    release: str = Field(description="Operating system kernel release.")
    """Operating system kernel release."""
    totalmem: int = Field(description="Total memory on the node, in bytes.")
    """Total memory on the node, in bytes."""
    apiPort: int | None = Field(default=None, description="API port exposed by the node.")
    """API port exposed by the node."""
    apiScheme: Literal["http", "https"] | None = Field(default=None, description="API scheme derived from the node API TLS configuration.")
    """API scheme derived from the node API TLS configuration."""
    aws: AwsHeartbeatMetadata | None = Field(default=None, description="AWS metadata collected from the node.")
    """AWS metadata collected from the node."""
    azure: AzureHeartbeatMetadata | None = Field(default=None, description="Azure metadata collected from the node.")
    """Azure metadata collected from the node."""
    conn_ip: str | None = Field(default=None, description="Remote ip:port for the worker socket.")
    """Remote ip:port for the worker socket."""
    freeDiskSpace: int | None = Field(default=None, description="Free disk space on the node, in bytes.")
    """Free disk space on the node, in bytes."""
    hostOs: OsHeartbeatMetadata | None = Field(default=None, description="Host operating system metadata collected from the node.")
    """Host operating system metadata collected from the node."""
    isCaptain: bool | None = Field(default=None, description="If true, the node considers itself the elected captain for its group.")
    """If true, the node considers itself the elected captain for its group."""
    isSaasWorker: bool | None = Field(default=None, description="If true, the node runs in Cribl.Cloud.")
    """If true, the node runs in Cribl.Cloud."""
    kube: KubeHeartbeatMetadata | None = Field(default=None, description="Kubernetes metadata collected from the node.")
    """Kubernetes metadata collected from the node."""
    localTime: int | None = Field(default=None, description="Local timestamp (in Unix time) on the node, in milliseconds.")
    """Local timestamp (in Unix time) on the node, in milliseconds."""
    metadata: HeartbeatMetadata | None = Field(default=None, description="Cloud, Kubernetes, and operating system metadata collected from the node.")
    """Cloud, Kubernetes, and operating system metadata collected from the node."""
    os: OsHeartbeatMetadata | None = Field(default=None, description="Operating system metadata collected from the node.")
    """Operating system metadata collected from the node."""
    outpost: OutpostNodeInfo | None = Field(default=None, description="Outpost Node information when the node is connected to an Outpost.")
    """Outpost Node information when the node is connected to an Outpost."""
    totalDiskSpace: int | None = Field(default=None, description="Total disk space on the node, in bytes.")
    """Total disk space on the node, in bytes."""


class NodeUpgradeStatus(CriblModel):
    """Upgrade status reported by an Edge Node."""

    state: NodeUpgradeState | int = Field(description="Current upgrade state (0=Active, 1=Current, 2=Failed, 3=Skipped).")
    """Current upgrade state (0=Active, 1=Current, 2=Failed, 3=Skipped)."""
    timestamp: int = Field(description="Timestamp (in Unix time) when the node entered the upgrade state, in milliseconds.")
    """Timestamp (in Unix time) when the node entered the upgrade state, in milliseconds."""
    active: NodeActiveUpgradeStatus | int | None = Field(default=None, description="Secondary upgrade state when state is Active (0=Pending, 1=Queued, 2=Upgrading).")
    """Secondary upgrade state when state is Active (0=Pending, 1=Queued, 2=Upgrading)."""
    failed: NodeFailedUpgradeStatus | int | None = Field(default=None, description="Secondary upgrade state when state is Failed (0=UpgradeErrorOnNode, 1=UpgradeInstallationRollback).")
    """Secondary upgrade state when state is Failed (0=UpgradeErrorOnNode, 1=UpgradeInstallationRollback)."""
    skipped: NodeSkippedUpgradeStatus | int | None = Field(default=None, description="Secondary upgrade state when state is Skipped.")
    """Secondary upgrade state when state is Skipped."""


class MasterWorkerProcesses(CriblModel):
    """Worker Process counts associated with a node entry."""

    count: int = Field(description="Number of Worker Processes represented by the node entry.")
    """Number of Worker Processes represented by the node entry."""


class MasterWorkerEntry(CriblModel):
    """Worker or Edge Node entry returned by Distributed Management endpoints."""

    id: str = Field(description="Unique identifier for the node.")
    """Unique identifier for the node."""
    group: str = Field(description="The id of the Worker Group, Edge Fleet, or Outpost Group that contains the node.")
    """The id of the Worker Group, Edge Fleet, or Outpost Group that contains the node."""
    firstMsgTime: int = Field(description="Timestamp (in Unix time) when the Leader first received a message from the node.")
    """Timestamp (in Unix time) when the Leader first received a message from the node."""
    lastMsgTime: int = Field(description="Timestamp (in Unix time) when the Leader last received a message from the node.")
    """Timestamp (in Unix time) when the Leader last received a message from the node."""
    workerProcesses: int = Field(description="Number of Worker Processes running on the node.")
    """Number of Worker Processes running on the node."""
    info: NodeProvidedInfo | None = Field(default=None, description="Metadata reported by the node itself.")
    """Metadata reported by the node itself."""
    connectionProtocol: Literal["tcp", "tls", "http2"] | None = Field(default=None, description="Connection protocol used for node-to-Leader communication.")
    """Connection protocol used for node-to-Leader communication."""
    deployable: bool | None = Field(default=None, description="If true, the node can receive configuration deployments.")
    """If true, the node can receive configuration deployments."""
    disconnected: bool | None = Field(default=None, description="If true, the node is disconnected from the Leader.")
    """If true, the node is disconnected from the Leader."""
    offlineDurationMs: int | None = Field(default=None, description="Maximum configured ephemeral offline duration, in milliseconds (base + jitter cap).")
    """Maximum configured ephemeral offline duration, in milliseconds (base + jitter cap)."""
    provisioningTokenId: str | None = Field(default=None, description="The id of the provisioning token used to authenticate the node, if used.")
    """The id of the provisioning token used to authenticate the node, if used."""
    status: str | None = Field(default=None, description="Health status reported for the node.")
    """Health status reported for the node."""
    type: Literal["info", "req", "resp"] | None = Field(default=None, description="RPC message type reported by the node.")
    """RPC message type reported by the node."""
    lastMetrics: dict[str, Any] | None = Field(default=None, description="Latest total, input, and destination metrics cached for UI display.")
    """Latest total, input, and destination metrics cached for UI display."""
    metadata: HeartbeatMetadata | None = Field(default=None, description="Cloud, Kubernetes, and operating system metadata collected from the node.")
    """Cloud, Kubernetes, and operating system metadata collected from the node."""
    nodeUpgradeStatus: NodeUpgradeStatus | None = Field(default=None, description="Upgrade status reported by an Edge Node.")
    """Upgrade status reported by an Edge Node."""
    workers: MasterWorkerProcesses | None = Field(default=None, description="Worker Process counts associated with the node entry.")
    """Worker Process counts associated with the node entry."""


class DeploymentGroupsSummary(CriblModel):
    """Resource counts for Worker Groups or Edge Fleets."""

    count: int = Field(description="Total number of Worker Groups or Edge Fleets.")
    """Total number of Worker Groups or Edge Fleets."""
    destinations: int = Field(description="Total number of Destinations.")
    """Total number of Destinations."""
    packs: int = Field(description="Total number of Packs.")
    """Total number of Packs."""
    pipelines: int = Field(description="Total number of Pipelines.")
    """Total number of Pipelines."""
    quickConnects: int = Field(description="Total number of QuickConnect configurations.")
    """Total number of QuickConnect configurations."""
    routes: int = Field(description="Total number of Routes.")
    """Total number of Routes."""
    sources: int = Field(description="Total number of Sources.")
    """Total number of Sources."""


class DeploymentWorkersSummary(CriblModel):
    """Worker or Edge Node counts and health statistics."""

    alive: int = Field(description="Total number of Worker or Edge Nodes that are connected with healthy status.")
    """Total number of Worker or Edge Nodes that are connected with healthy status."""
    confVersions: int = Field(description="Total number of unique configuration versions across all Worker or Edge Nodes.")
    """Total number of unique configuration versions across all Worker or Edge Nodes."""
    count: int = Field(description="Total number of Worker or Edge Nodes.")
    """Total number of Worker or Edge Nodes."""
    disconnectedCount: int = Field(description="Total number of Worker or Edge Nodes in a disconnected state.")
    """Total number of Worker or Edge Nodes in a disconnected state."""
    groups: int = Field(description="Total number of distinct Worker Groups or Edge Fleets that the Workers or Edge Nodes belong to.")
    """Total number of distinct Worker Groups or Edge Fleets that the Workers or Edge Nodes belong to."""
    softwareVersions: int = Field(description="Total number of unique Cribl software versions across all Worker or Edge Nodes.")
    """Total number of unique Cribl software versions across all Worker or Edge Nodes."""
    unhealthy: int = Field(description="Total number of Worker or Edge Nodes that are connected with a status other than healthy.")
    """Total number of Worker or Edge Nodes that are connected with a status other than healthy."""


class DistributedSummary(CriblModel):
    """Summary of the deployment for the specified Cribl product (Stream or Edge)."""

    groups: DeploymentGroupsSummary = Field(description="Resource counts for Worker Groups or Edge Fleets in the deployment summary.")
    """Resource counts for Worker Groups or Edge Fleets in the deployment summary."""
    workers: DeploymentWorkersSummary | None = Field(default=None, description="Worker or Edge Node counts and health statistics in the deployment summary.")
    """Worker or Edge Node counts and health statistics in the deployment summary."""


class RestartResponse(CriblModel):
    """Result of a restart request for a single Worker or Edge Node."""

    id: str = Field(..., description="Unique identifier for the Worker or Edge Node (GUID).")
    """Unique identifier for the Worker or Edge Node (GUID)."""
    status: Literal["Error", "Restarting"] = Field(..., description="Result of the restart request for this Node (Restarting or Error).")
    """Result of the restart request for this Node (Restarting or Error)."""
    message: str | None = Field(default=None, description="Error message if the restart request failed for this Node.")
    """Error message if the restart request failed for this Node."""


# --- Groups ---


class GitCommitEntry(CriblModel):
    """A Git commit entry from a configuration group's log."""

    author_email: str | None = Field(default=None, description="Email address of the commit author.")
    """Email address of the commit author."""
    author_name: str | None = Field(default=None, description="Name of the commit author.")
    """Name of the commit author."""
    date: str = Field(description="Date and time of the commit.")
    """Date and time of the commit."""
    hash: str = Field(description="Full commit hash.")
    """Full commit hash."""
    message: str = Field(description="Commit message.")
    """Commit message."""
    short: str = Field(description="Abbreviated commit hash.")
    """Abbreviated commit hash."""


class LookupDeploymentEntry(CriblModel):
    """A single lookup file deployment status."""

    file: str = Field(description="File name of the deployed lookup.")
    """File name of the deployed lookup."""
    deployMode: Literal["auto", "manual"] | None = Field(default=None, description="Deploy mode configured on the lookup file.")
    """Deploy mode configured on the lookup file."""
    deployedVersion: str | None = Field(default=None, description="Version of the lookup file currently deployed on the Worker or Node.")
    """Version of the lookup file currently deployed on the Worker or Node."""
    version: str | None = Field(default=None, description="Version of the lookup file currently staged for deployment.")
    """Version of the lookup file currently staged for deployment."""


class ConfigGroupLookups(CriblModel):
    """Lookup deployment status per Worker or Node context."""

    context: str = Field(description="The Worker or Node context for the lookup deployment.")
    """The Worker or Node context for the lookup deployment."""
    lookups: list[LookupDeploymentEntry] = Field(description="List of lookup files deployed to this context.")
    """List of lookup files deployed to this context."""


class ConfigGroupCloud(CriblModel):
    """Cloud provider and region details for a Cribl.Cloud Worker Group."""

    provider: Literal["aws", "azure"] | None = Field(default=None, description="Cloud provider for the Worker Group.")
    """Cloud provider for the Worker Group."""
    region: str = Field(description="Cloud region where the Worker Group is deployed.")
    """Cloud region where the Worker Group is deployed."""


class ConfigGroupGit(CriblModel):
    """Git status of a Worker Group, Outpost Group, or Edge Fleet configuration."""

    commit: str | None = Field(default=None, description="Commit hash of the currently committed configuration version.")
    """Commit hash of the currently committed configuration version."""
    localChanges: int | None = Field(default=None, description="Number of local configuration changes not yet committed.")
    """Number of local configuration changes not yet committed."""
    log: list[GitCommitEntry] | None = Field(default=None, description="List of recent configuration commits.")
    """List of recent configuration commits."""


class ConfigGroup(CriblModel):
    """A Worker Group, Outpost Group, or Edge Fleet configuration."""

    id: str | None = Field(default=None, description="Unique identifier.")
    """Unique identifier."""
    name: str | None = Field(default=None, description="Name of the Worker Group, Outpost Group, or Edge Fleet.")
    """Name of the Worker Group, Outpost Group, or Edge Fleet."""
    description: str | None = Field(default=None, description="Brief description of the Worker Group, Outpost Group, or Edge Fleet.")
    """Brief description of the Worker Group, Outpost Group, or Edge Fleet."""
    type: Literal["edge", "lake_access", "local_search", "outpost", "search", "stream"] | None = Field(default=None, description="Explicit type of the Worker Group, Outpost Group, or Edge Fleet.")
    """Explicit type of the Worker Group, Outpost Group, or Edge Fleet."""
    configVersion: str | None = Field(default=None, description="Commit hash of the deployed configuration version for the Worker Group, Outpost Group, or Edge Fleet.")
    """Commit hash of the deployed configuration version for the Worker Group, Outpost Group, or Edge Fleet."""
    cloud: ConfigGroupCloud | None = Field(default=None, description="Cloud provider and region details for a Cribl.Cloud Worker Group.")
    """Cloud provider and region details for a Cribl.Cloud Worker Group."""
    estimatedIngestRate: int | None = Field(default=None, description="Estimated ingest rate for a Cribl.Cloud Worker Group, in GB/sec.")
    """Estimated ingest rate for a Cribl.Cloud Worker Group, in GB/sec."""
    git: ConfigGroupGit | None = Field(default=None, description="Git status of the Worker Group, Outpost Group, or Edge Fleet configuration.")
    """Git status of the Worker Group, Outpost Group, or Edge Fleet configuration."""
    inherits: str | None = Field(default=None, description="The id of the parent Edge Fleet. If provided, this Fleet inherits configuration from the parent.")
    """The id of the parent Edge Fleet. If provided, this Fleet inherits configuration from the parent."""
    onPrem: bool | None = Field(default=None, description="If true, the Worker Group, Outpost Group, or Edge Fleet uses customer-hosted (on-prem) infrastructure.")
    """If true, the Worker Group, Outpost Group, or Edge Fleet uses customer-hosted (on-prem) infrastructure."""
    provisioned: bool | None = Field(default=None, description="If true, the Cribl.Cloud Worker Group has active Workers provisioned.")
    """If true, the Cribl.Cloud Worker Group has active Workers provisioned."""
    streamtags: list[str] | None = Field(default=None, description="Metadata tags attached to the Worker Group, Outpost Group, or Edge Fleet for categorization and filtering.")
    """Metadata tags attached to the Worker Group, Outpost Group, or Edge Fleet for categorization and filtering."""
    workerCount: int | None = Field(default=None, description="Number of Workers or Nodes currently in the Worker Group, Outpost Group, or Edge Fleet.")
    """Number of Workers or Nodes currently in the Worker Group, Outpost Group, or Edge Fleet."""
    deployingWorkerCount: int | None = Field(default=None, description="Number of Workers or Nodes that are currently deploying the latest configuration version.")
    """Number of Workers or Nodes that are currently deploying the latest configuration version."""
    incompatibleWorkerCount: int | None = Field(default=None, description="Number of Workers or Nodes running a Cribl version that is incompatible with the current upgrade target.")
    """Number of Workers or Nodes running a Cribl version that is incompatible with the current upgrade target."""
    workerRemoteAccess: bool | None = Field(default=None, description="If true, the Leader allows remote access (teleporting) into the Workers or Nodes.")
    """If true, the Leader allows remote access (teleporting) into the Workers or Nodes."""
    collectorsHaEnabled: bool | None = Field(default=None, description="Keeps Collector jobs running if the Leader Node fails. Applies only to Stream Worker Groups.")
    """Keeps Collector jobs running if the Leader Node fails. Applies only to Stream Worker Groups."""
    maxWorkerAge: str | None = Field(default=None, description="Maximum duration a Worker or Node can remain disconnected before the Leader removes it.")
    """Maximum duration a Worker or Node can remain disconnected before the Leader removes it."""
    upgradeVersion: str | None = Field(default=None, description="Target software upgrade version. Applies only to Outpost Groups and Edge Fleets.")
    """Target software upgrade version. Applies only to Outpost Groups and Edge Fleets."""
    lookupDeployments: list[ConfigGroupLookups] | None = Field(default=None, description="Lookup deployment status per Worker or Node context.")
    """Lookup deployment status per Worker or Node context."""
    isFleet: bool | None = Field(default=None, description="Indicates whether this is an Edge Fleet. Deprecated: use type='edge' instead.")
    """Indicates whether this is an Edge Fleet. Deprecated: use type='edge' instead."""
    isSearch: bool | None = Field(default=None, description="Indicates whether this is an internal Search Group. Deprecated: use type='search' instead.")
    """Indicates whether this is an internal Search Group. Deprecated: use type='search' instead."""
    tags: str | None = Field(default=None, description="Legacy system-level tags. Use streamtags instead.")
    """Legacy system-level tags. Use streamtags instead."""
    srcGroup: str | None = Field(
        default=None,
        alias="__srcGroup",
        description="Fleet or group id this entity was inherited from when served by a Config Helper for a child fleet. Present when inherited from parent, including when the child has a local overlay. Omitted when the entity is local and not inherited. Display-only; never persisted.",
    )
    """Fleet or group id this entity was inherited from when served by a Config Helper for a child fleet. Present when inherited from parent, including when the child has a local overlay. Omitted when the entity is local and not inherited. Display-only; never persisted."""
    srcOverridden: bool | None = Field(
        default=None,
        alias="__srcOverridden",
        description="If true, the child fleet has a local overlay on an inherited entity. Omitted when inherited and unmodified, or when local and not inherited. Display-only; never persisted.",
    )
    """If true, the child fleet has a local overlay on an inherited entity. Omitted when inherited and unmodified, or when local and not inherited. Display-only; never persisted."""


# --- Pipelines ---


class PipelineFunctionParam(TypedDict, total=False):
    """A Pipeline function entry (common fields across all 60+ function types).

    Attrs:
        id: Identifier of the function type (e.g. 'eval', 'comment', 'mask').
        filter: JavaScript expression that selects data to pass through the Function.
        conf: Configuration specific to the function type (varies per id).
        description: Brief description of the Pipeline function.
        disabled: If true, disable the function so events are not passed through it.
        final: If true, stop passing events to downstream functions after this one executes.
        groupId: Unique identifier of the group that contains the Pipeline Function.
    """
    id: str
    filter: str
    conf: dict[str, Any]
    description: str
    disabled: bool
    final: bool
    groupId: str


class PipelineGroupParam(TypedDict, total=False):
    """A named group of Pipeline functions for organizational display.

    Attrs:
        name: Name of the group.
        description: Brief description of the group.
        disabled: If true, disable all items in the group.
    """
    name: str
    description: str
    disabled: bool


class PipelineConfParam(TypedDict, total=False):
    """Pipeline configuration.

    Attrs:
        asyncFuncTimeout: Timeout (ms) for asynchronous Pipeline functions (0-10000).
        output: Output destination for events processed by this Pipeline.
        description: Brief description of the Pipeline.
        streamtags: Metadata tags used for categorization and filtering.
        functions: List of Functions to pass data through the Pipeline.
        groups: Named groups of Pipeline functions for organizational display in the UI.
    """
    asyncFuncTimeout: int
    output: str
    description: str
    streamtags: list[str]
    functions: list[PipelineFunctionParam]
    groups: dict[str, PipelineGroupParam]


class RouteCommentParam(TypedDict, total=False):
    """A user-provided comment that describes or annotates a Route (input).

    Attrs:
        comment: Brief description of the Route.
        id: Unique identifier for the comment.
        index: Relative position of the comment among all comments for the Route.
        groupId: Unique identifier for the Route Group that the Route is associated with.
    """
    comment: str
    id: str
    index: int
    groupId: str


class RouteGroupParam(TypedDict, total=False):
    """A Route Group entry (input).

    Attrs:
        name: Name of the Route Group.
        index: Relative position of the Route Group among all Route Groups.
        description: Brief description of the Route Group.
    """
    name: str
    index: int
    description: str


class HecTokenMetadataParam(TypedDict, total=False):
    """Key-value metadata entry for an HEC token.

    Attrs:
        name: Key name for the metadata entry.
        value: Value for the metadata entry. Can be a static string or a JavaScript expression.
    """
    name: str
    value: str


class AuthTokenConfOutputCriblHttp(CriblModel):
    """Authentication token for a Cribl HTTP Destination."""

    tokenSecret: str = Field(description="Select or create a stored text secret")
    """Select or create a stored text secret."""
    enabled: bool | None = Field(default=None, description="Enable token")
    """Enable token."""
    description: str | None = Field(default=None, description="Description")
    """Description."""


class UrlConfOutputCriblHttp(CriblModel):
    """Cribl Worker endpoint configuration."""

    url: str = Field(description="URL of a Cribl Worker to send events to, such as http://localhost:10200")
    """URL of a Cribl Worker to send events to, such as http://localhost:10200."""
    weight: float | None = Field(default=None, description="Assign a weight (>0) to each endpoint to indicate its traffic-handling capability")
    """Assign a weight (>0) to each endpoint to indicate its traffic-handling capability."""
    xtemplate_url: str | None = Field(
        default=None,
        alias="__template_url",
        description="Binds 'url' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'url' at runtime.",
    )
    """Binds 'url' to a variable for dynamic value resolution. Set to variable ID (pack-scoped) or 'cribl.'/'edge.' prefixed ID (group-scoped). Variable value overrides 'url' at runtime."""


class ExtraHttpHeaderConfInputElastic(CriblModel):
    """Additional HTTP header configuration."""

    name: str | None = Field(default=None, description="Field Name")
    """Field Name."""
    value: str = Field(description="Field Value")
    """Field Value."""


class ResponseRetrySettingConfOutputWebhook(CriblModel):
    """Retry settings for an HTTP response status."""

    httpStatus: float = Field(description="The HTTP response status code that will trigger retries")
    """The HTTP response status code that will trigger retries."""
    initialBackoff: float | None = Field(default=None, description="How long, in milliseconds, Cribl Stream should wait before initiating backoff. Maximum interval is 600,000 ms (10 minutes).")
    """How long, in milliseconds, Cribl Stream should wait before initiating backoff. Maximum interval is 600,000 ms (10 minutes)."""
    backoffRate: float | None = Field(default=None, description="Base for exponential backoff. A value of 2 (default) means Cribl Stream will retry after 2 seconds, then 4 seconds, then 8 seconds, etc.")
    """Base for exponential backoff. A value of 2 (default) means Cribl Stream will retry after 2 seconds, then 4 seconds, then 8 seconds, etc."""
    maxBackoff: float | None = Field(default=None, description="The maximum backoff interval, in milliseconds, Cribl Stream should apply. Default (and minimum) is 10,000 ms (10 seconds); maximum is 180,000 ms (180 seconds).")
    """The maximum backoff interval, in milliseconds, Cribl Stream should apply. Default (and minimum) is 10,000 ms (10 seconds); maximum is 180,000 ms (180 seconds)."""


class TimeoutRetrySettingsType(CriblModel):
    """Retry settings for timed-out HTTP requests."""

    timeoutRetry: bool = Field(description="Retry timed-out HTTP requests")
    """Retry timed-out HTTP requests."""
    initialBackoff: float | None = Field(default=None, description="How long, in milliseconds, Cribl Stream should wait before initiating backoff. Maximum interval is 600,000 ms (10 minutes).")
    """How long, in milliseconds, Cribl Stream should wait before initiating backoff. Maximum interval is 600,000 ms (10 minutes)."""
    backoffRate: float | None = Field(default=None, description="Base for exponential backoff. A value of 2 (default) means Cribl Stream will retry after 2 seconds, then 4 seconds, then 8 seconds, etc.")
    """Base for exponential backoff. A value of 2 (default) means Cribl Stream will retry after 2 seconds, then 4 seconds, then 8 seconds, etc."""
    maxBackoff: float | None = Field(default=None, description="The maximum backoff interval, in milliseconds, Cribl Stream should apply. Default (and minimum) is 10,000 ms (10 seconds); maximum is 180,000 ms (180 seconds).")
    """The maximum backoff interval, in milliseconds, Cribl Stream should apply. Default (and minimum) is 10,000 ms (10 seconds); maximum is 180,000 ms (180 seconds)."""


class AuthTokenExtConf(CriblModel):
    """Manual or secret-backed authentication token."""

    authType: Literal["manual", "secret"] | None = Field(default=None, description="Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate")
    """Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate."""
    tokenSecret: str | None = Field(default=None, description="Select or create a stored text secret")
    """Select or create a stored text secret."""
    token: str | None = Field(default=None, description="Shared secret to be provided by any client (Authorization: <token>)")
    """Shared secret to be provided by any client (Authorization: <token>)."""
    description: str | None = Field(default=None, description="Description")
    """Description."""
    metadata: list[HecTokenMetadataParam] | None = Field(default=None, description="Fields to add to events referencing this token")
    """Fields to add to events referencing this token."""


class FirehoseAuthTokenExtConf(CriblModel):
    """Authentication token for a Firehose Source."""

    authType: Literal["manual", "secret"] | None = Field(default=None, description="Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate")
    """Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate."""
    tokenSecret: str | None = Field(default=None, description="Select or create a stored text secret")
    """Select or create a stored text secret."""
    token: str = Field(description="Shared secret to be provided by any client (Authorization: <token>)")
    """Shared secret to be provided by any client (Authorization: <token>)."""
    description: str | None = Field(default=None, description="Description")
    """Description."""
    metadata: list[HecTokenMetadataParam] | None = Field(default=None, description="Fields to add to events referencing this token")
    """Fields to add to events referencing this token."""


class AuthTokenSecretExtConf(CriblModel):
    """Secret-backed authentication token."""

    authType: Literal["secret"] | None = Field(default=None, description="Select Secret to use a text secret to authenticate")
    """Select Secret to use a text secret to authenticate."""
    tokenSecret: str | None = Field(default=None, description="Select or create a stored text secret")
    """Select or create a stored text secret."""
    token: str | None = Field(default=None, description="Shared secret to be provided by any client (Authorization: <token>)")
    """Shared secret to be provided by any client (Authorization: <token>)."""
    description: str | None = Field(default=None, description="Description")
    """Description."""
    metadata: list[HecTokenMetadataParam] | None = Field(default=None, description="Fields to add to events referencing this token")
    """Fields to add to events referencing this token."""


class HecAuthTokenConf(AuthTokenSecretExtConf):
    """HEC authentication token."""

    enabled: bool | None = Field(default=None, description="Enable token")
    """Enable token."""
    allowedIndexesAtToken: list[str] | None = Field(default=None, description="Enter the values you want to allow in the HEC event index field at the token level. Supports wildcards. To skip validation, leave blank.")
    """Enter the values you want to allow in the HEC event index field at the token level. Supports wildcards. To skip validation, leave blank."""


class OtlpAuthMethodExtConf(CriblModel):
    """OpenTelemetry authentication method."""

    authType: Literal["token", "tokenSecret", "basic", "basicSecret", "oauth"] = Field(description="Authentication type")
    """Authentication type."""
    token: str | None = Field(default=None, description="Bearer token for Authorization header")
    """Bearer token for Authorization header."""
    description: str | None = Field(default=None, description="Description")
    """Description."""
    metadata: list[HecTokenMetadataParam] | None = Field(default=None, description="Fields to add to events referencing this auth method")
    """Fields to add to events referencing this auth method."""
    enabled: bool | None = Field(default=None, description="Enable")
    """Enable."""
    tokenSecret: str | None = Field(default=None, description="Select or create a stored text secret")
    """Select or create a stored text secret."""
    username: str | None = Field(default=None, description="Username")
    """Username."""
    password: str | None = Field(default=None, description="Password")
    """Password."""
    credentialsSecret: str | None = Field(default=None, description="Select or create a secret that references your credentials")
    """Select or create a secret that references your credentials."""
    issuer: str | None = Field(default=None, description="Expected token issuer (iss claim)")
    """Expected token issuer (iss claim)."""
    jwksUri: str | None = Field(default=None, description="URL of the JWKS endpoint used to fetch signing keys")
    """URL of the JWKS endpoint used to fetch signing keys."""
    audience: str | None = Field(default=None, description="Expected token audience (aud claim)")
    """Expected token audience (aud claim)."""
    scopes: list[str] | None = Field(default=None, description="Scopes the token must grant (optional)")
    """Scopes the token must grant (optional)."""


class HttpAuthTokenExtConf(CriblModel):
    """Authentication token for an HTTP Source."""

    authType: Literal["manual", "secret"] | None = Field(default=None, description="Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate")
    """Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate."""
    tokenSecret: str | None = Field(default=None, description="Select or create a stored text secret")
    """Select or create a stored text secret."""
    token: str | None = Field(default=None, description="Shared secret to be provided by any client (Authorization: <token>)")
    """Shared secret to be provided by any client (Authorization: <token>)."""
    description: str | None = Field(default=None, description="Description")
    """Description."""
    metadata: list[HecTokenMetadataParam] | None = Field(default=None, description="Fields to add to events referencing this token")
    """Fields to add to events referencing this token."""


class SplunkHecTokenMetadataConf(CriblModel):
    """Splunk HEC settings for an authentication token."""

    enabled: bool | None = Field(default=None, description="When enabled, the token value is available on events as __hecToken")
    """When enabled, the token value is available on events as __hecToken."""
    defaultDataset: str | None = None
    allowedIndexesAtToken: list[str] | None = None


class ElasticsearchTokenMetadataConf(CriblModel):
    """Elasticsearch settings for an authentication token."""

    enabled: bool | None = Field(default=None, description="Elasticsearch")
    """Elasticsearch."""
    defaultDataset: str | None = None


class CriblLakeHttpAuthTokenConf(CriblModel):
    """Authentication token for a Cribl Lake HTTP Source."""

    authType: Literal["manual", "secret"] | None = Field(default=None, description="Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate")
    """Select Manual to enter an auth token directly, or select Secret to use a text secret to authenticate."""
    tokenSecret: str | None = Field(default=None, description="Select or create a stored text secret")
    """Select or create a stored text secret."""
    token: str = Field(description="Token")
    """Token."""
    description: str | None = None
    metadata: list[HecTokenMetadataParam] | None = Field(default=None, description="Fields to add to events referencing this token")
    """Fields to add to events referencing this token."""
    splunkHecMetadata: SplunkHecTokenMetadataConf | None = None
    elasticsearchMetadata: ElasticsearchTokenMetadataConf | None = None


class Pipeline(BaseModel):
    """A processing pipeline configuration."""

    id: str = Field(description="Unique identifier for the Pipeline.")
    """Unique identifier for the Pipeline."""
    conf: PipelineConfParam = Field(description="Configuration for the Pipeline, including functions and settings.")
    """Configuration for the Pipeline, including functions and settings."""


# --- Packs ---


class PackTags(CriblModel):
    """Categorization tags for a Pack."""

    dataType: list[str] | None = Field(default=None, description="List of data type tags for the Pack.")
    """List of data type tags for the Pack."""
    domain: list[str] | None = Field(default=None, description="List of domain tags for the Pack.")
    """List of domain tags for the Pack."""
    streamtags: list[str] | None = Field(default=None, description="List of stream tags for routing and filtering.")
    """List of stream tags for routing and filtering."""
    technology: list[str] | None = Field(default=None, description="List of technology tags for the Pack.")
    """List of technology tags for the Pack."""


class PackInfo(CriblModel):
    """Information about a content pack."""

    id: str | None = Field(default=None, description="Unique identifier.")
    """Unique identifier."""
    displayName: str | None = Field(default=None, description="Human-readable display name for the Pack.")
    """Human-readable display name for the Pack."""
    description: str | None = Field(default=None, description="Brief description of the Pack and its purpose.")
    """Brief description of the Pack and its purpose."""
    author: str | None = Field(default=None, description="Name or identifier of the Pack author.")
    """Name or identifier of the Pack author."""
    version: str | None = Field(default=None, description="Version of the Pack, following semantic versioning.")
    """Version of the Pack, following semantic versioning."""
    source: str | None = Field(default=None, description="Source of the Pack — a file path, URL, or Git URL from which the Pack was installed.")
    """Source of the Pack — a file path, URL, or Git URL from which the Pack was installed."""
    spec: str | None = Field(default=None, description="Semver range constraint that was applied when the Pack was installed.")
    """Semver range constraint that was applied when the Pack was installed."""
    collectors: float | None = Field(default=None, description="Number of Collectors (saved jobs) configured within the Pack.")
    """Number of Collectors (saved jobs) configured within the Pack."""
    inputs: float | None = Field(default=None, description="Number of Sources configured within the Pack.")
    """Number of Sources configured within the Pack."""
    outputs: float | None = Field(default=None, description="Number of Destinations configured within the Pack.")
    """Number of Destinations configured within the Pack."""
    exports: list[str] | None = Field(default=None, description="List of entity IDs exported by this Pack and available for use outside the Pack context.")
    """List of entity IDs exported by this Pack and available for use outside the Pack context."""
    dependencies: dict[str, str] | None = Field(default=None, description="Map of Pack dependency identifiers to their version constraints.")
    """Map of Pack dependency identifiers to their version constraints."""
    settings: dict[str, Any] | None = Field(default=None, description="Pack-specific settings object. Contents vary by Pack.")
    """Pack-specific settings object. Contents vary by Pack."""
    tags: PackTags | None = Field(default=None, description="Categorization tags for the Pack.")
    """Categorization tags for the Pack."""
    isDisabled: bool | None = Field(default=None, description="If true, the Pack is disabled.")
    """If true, the Pack is disabled."""
    minLogStreamVersion: str | None = Field(default=None, description="Minimum version of Cribl Stream required to run this Pack.")
    """Minimum version of Cribl Stream required to run this Pack."""
    srcGroup: str | None = Field(
        default=None,
        alias="__srcGroup",
        description="Fleet or group id this entity was inherited from when served by a Config Helper for a child fleet. Present when inherited from parent, including when the child has a local overlay. Omitted when the entity is local and not inherited. Display-only; never persisted.",
    )
    """Fleet or group id this entity was inherited from when served by a Config Helper for a child fleet. Present when inherited from parent, including when the child has a local overlay. Omitted when the entity is local and not inherited. Display-only; never persisted."""
    srcOverridden: bool | None = Field(
        default=None,
        alias="__srcOverridden",
        description="If true, the child fleet has a local overlay on an inherited entity. Omitted when inherited and unmodified, or when local and not inherited. Display-only; never persisted.",
    )
    """If true, the child fleet has a local overlay on an inherited entity. Omitted when inherited and unmodified, or when local and not inherited. Display-only; never persisted."""


class PackInstallInfo(CriblModel):
    """Information about an installed pack."""

    id: str | None = Field(default=None, description="Unique identifier.")
    """Unique identifier."""
    displayName: str | None = Field(default=None, description="Human-readable display name for the Pack.")
    """Human-readable display name for the Pack."""
    description: str | None = Field(default=None, description="Brief description of the Pack and its purpose.")
    """Brief description of the Pack and its purpose."""
    author: str | None = Field(default=None, description="Name or identifier of the Pack author.")
    """Name or identifier of the Pack author."""
    version: str | None = Field(default=None, description="Version of the Pack, following semantic versioning.")
    """Version of the Pack, following semantic versioning."""
    source: str | None = Field(default=None, description="Source of the Pack — a file path, URL, or Git URL from which the Pack was installed.")
    """Source of the Pack — a file path, URL, or Git URL from which the Pack was installed."""
    spec: str | None = Field(default=None, description="Semver range constraint that was applied when the Pack was installed.")
    """Semver range constraint that was applied when the Pack was installed."""
    collectors: float | None = Field(default=None, description="Number of Collectors (saved jobs) configured within the Pack.")
    """Number of Collectors (saved jobs) configured within the Pack."""
    inputs: float | None = Field(default=None, description="Number of Sources configured within the Pack.")
    """Number of Sources configured within the Pack."""
    outputs: float | None = Field(default=None, description="Number of Destinations configured within the Pack.")
    """Number of Destinations configured within the Pack."""
    exports: list[str] | None = Field(default=None, description="List of entity IDs exported by this Pack and available for use outside the Pack context.")
    """List of entity IDs exported by this Pack and available for use outside the Pack context."""
    dependencies: dict[str, str] | None = Field(default=None, description="Map of Pack dependency identifiers to their version constraints.")
    """Map of Pack dependency identifiers to their version constraints."""
    settings: dict[str, Any] | None = Field(default=None, description="Pack-specific settings object. Contents vary by Pack.")
    """Pack-specific settings object. Contents vary by Pack."""
    tags: PackTags | None = Field(default=None, description="Categorization tags for the Pack.")
    """Categorization tags for the Pack."""
    isDisabled: bool | None = Field(default=None, description="If true, the Pack is disabled.")
    """If true, the Pack is disabled."""
    minLogStreamVersion: str | None = Field(default=None, description="Minimum version of Cribl Stream required to run this Pack.")
    """Minimum version of Cribl Stream required to run this Pack."""
    warnings: list[str] | None = Field(default=None, description="List of warning messages generated during Pack installation, if any.")
    """List of warning messages generated during Pack installation, if any."""
    srcGroup: str | None = Field(
        default=None,
        alias="__srcGroup",
        description="Fleet or group id this entity was inherited from when served by a Config Helper for a child fleet. Present when inherited from parent, including when the child has a local overlay. Omitted when the entity is local and not inherited. Display-only; never persisted.",
    )
    """Fleet or group id this entity was inherited from when served by a Config Helper for a child fleet. Present when inherited from parent, including when the child has a local overlay. Omitted when the entity is local and not inherited. Display-only; never persisted."""
    srcOverridden: bool | None = Field(
        default=None,
        alias="__srcOverridden",
        description="If true, the child fleet has a local overlay on an inherited entity. Omitted when inherited and unmodified, or when local and not inherited. Display-only; never persisted.",
    )
    """If true, the child fleet has a local overlay on an inherited entity. Omitted when inherited and unmodified, or when local and not inherited. Display-only; never persisted."""


class PackUninstallInfo(BaseModel):
    """Information about an uninstalled pack."""

    id: str = Field(description="Pack identifier.")
    """Pack identifier."""
    source: str = Field(description="Source location of the pack.")
    """Source location of the pack."""


class UploadPackResponse(BaseModel):
    """Response from uploading a pack."""

    source: str = Field(description="Source path of the uploaded pack.")
    """Source path of the uploaded pack."""


# --- Sources/Destinations ---


class Source(CriblModel):
    """A data source (input). Base type for all input variants."""

    id: str | None = Field(default=None, description="Unique identifier for this source.")
    """Unique identifier for this source."""
    type: str | None = Field(default=None, description="Source type (e.g. 'syslog', 'http', 'splunk_hec').")
    """Source type (e.g. 'syslog', 'http', 'splunk_hec')."""
    disabled: bool | None = Field(default=None, description="If true, source is not active.")
    """If true, source is not active."""
    pipeline: str | None = Field(default=None, description="Pipeline ID to process events from this source.")
    """Pipeline ID to process events from this source."""


class Destination(CriblModel):
    """A data destination (output). Base type for all output variants."""

    id: str | None = Field(default=None, description="Unique identifier for this destination.")
    """Unique identifier for this destination."""
    type: str | None = Field(default=None, description="Destination type (e.g. 's3', 'splunk', 'elastic').")
    """Destination type (e.g. 's3', 'splunk', 'elastic')."""
    disabled: bool | None = Field(default=None, description="If true, destination is not active.")
    """If true, destination is not active."""
    pipeline: str | None = Field(default=None, description="Post-processing pipeline ID.")
    """Post-processing pipeline ID."""


class StatusError(CriblModel):
    """Error information, if applicable."""

    message: str = Field(description="Human-readable message that describes the error.")
    """Human-readable message that describes the error."""
    details: dict[str, Any] | None = Field(default=None, description="Additional error details.")
    """Additional error details."""


class HealthCountType(CriblModel):
    """Counts of health statuses across all Worker Processes."""

    Green: int | None = Field(default=None, description="Number of Worker Processes reporting a healthy (Green) status.")
    """Number of Worker Processes reporting a healthy (Green) status."""
    Red: int | None = Field(default=None, description="Number of Worker Processes reporting a critical (Red) status.")
    """Number of Worker Processes reporting a critical (Red) status."""
    Unknown: int | None = Field(default=None, description="Number of Worker Processes reporting an unknown health status.")
    """Number of Worker Processes reporting an unknown health status."""
    Yellow: int | None = Field(default=None, description="Number of Worker Processes reporting a degraded (Yellow) status.")
    """Number of Worker Processes reporting a degraded (Yellow) status."""


class AggregatedPQStatus(CriblModel):
    """Persistent queue status information (if persistent queue is enabled)."""

    health: Literal["Green", "Red", "Unknown", "Yellow"] = Field(description="Health status of the persistent queue.")
    """Health status of the persistent queue."""
    healthCounts: HealthCountType = Field(description="Counts of persistent queue health statuses for the Source or Destination across all Worker Processes. Includes only statuses with non-zero counts.")
    """Counts of persistent queue health statuses for the Source or Destination across all Worker Processes. Includes only statuses with non-zero counts."""
    timestamp: int = Field(description="Timestamp (in Unix time) when the persistent queue status was last updated.")
    """Timestamp (in Unix time) when the persistent queue status was last updated."""
    error: StatusError | None = Field(default=None, description="Error information for the persistent queue, if applicable.")
    """Error information for the persistent queue, if applicable."""


class AggregatedInputOutputStatusBody(CriblModel):
    """Status information for the Source or Destination, aggregated across all Worker Processes."""

    health: Literal["Green", "Red", "Unknown", "Yellow"] = Field(description="Overall health status of the Source or Destination.")
    """Overall health status of the Source or Destination."""
    healthCounts: HealthCountType = Field(description="Counts of health statuses for the Source or Destination across all Worker Processes. Includes only statuses with non-zero counts.")
    """Counts of health statuses for the Source or Destination across all Worker Processes. Includes only statuses with non-zero counts."""
    timestamp: int = Field(description="Timestamp (in Unix time) when the status was last updated.")
    """Timestamp (in Unix time) when the status was last updated."""
    error: StatusError | None = Field(default=None, description="Error information, if applicable.")
    """Error information, if applicable."""
    metrics: dict[str, Any] | None = Field(default=None, description="Metrics data for the Source or Destination, including base metrics, aggregated across all Worker Processes. For load-balanced Destinations, includes item-level metrics.")
    """Metrics data for the Source or Destination, including base metrics, aggregated across all Worker Processes. For load-balanced Destinations, includes item-level metrics."""
    pq: AggregatedPQStatus | None = Field(default=None, description="Persistent queue status information (if persistent queue is enabled).")
    """Persistent queue status information (if persistent queue is enabled)."""


class InputStatus(BaseModel):
    """Runtime status of a source."""

    id: str = Field(description="Unique identifier of the Source.")
    """Unique identifier of the Source."""
    status: AggregatedInputOutputStatusBody = Field(description="Status information for the Source.")
    """Status information for the Source."""
    type: str | None = Field(default=None, description="Type of the Source.")
    """Type of the Source."""


class OutputStatus(BaseModel):
    """Runtime status of a destination."""

    id: str = Field(description="Unique identifier of the Destination.")
    """Unique identifier of the Destination."""
    status: AggregatedInputOutputStatusBody = Field(description="Status information for the Destination.")
    """Status information for the Destination."""
    type: str | None = Field(default=None, description="Type of the Destination.")
    """Type of the Destination."""


# --- Worker-level PQ and Status ---


class WorkerPQStatus(CriblModel):
    """Persistent queue status for a single Worker Process."""

    health: int = Field(description="Persistent queue health status for the Worker Process, as a numeric code. 0 == Healthy (green; normal operation), 1 == Degraded (yellow; potential issues), 2 == Critical (red; problem or error that affects operation).")
    """Persistent queue health status for the Worker Process, as a numeric code. 0 == Healthy (green; normal operation), 1 == Degraded (yellow; potential issues), 2 == Critical (red; problem or error that affects operation)."""
    metrics: dict[str, Any] = Field(description="Persistent-queue metrics reported for the Worker Process.")
    """Persistent-queue metrics reported for the Worker Process."""
    timestamp: int = Field(description="Timestamp (in Unix time) when the persistent queue status was last reported for the Worker Process, in milliseconds.")
    """Timestamp (in Unix time) when the persistent queue status was last reported for the Worker Process, in milliseconds."""
    error: StatusError | None = Field(default=None, description="Error information for the persistent queue, if applicable.")
    """Error information for the persistent queue, if applicable."""


class StatusType(CriblModel):
    """Runtime status: health, metrics, and optional persistent-queue info."""

    health: Literal["Green", "Red", "Unknown", "Yellow"] | None = Field(default=None, description="Overall health status of the Source or Destination.")
    """Overall health status of the Source or Destination."""
    metrics: dict[str, Any] | None = Field(default=None, description="Metrics data for the Source or Destination.")
    """Metrics data for the Source or Destination."""
    timestamp: int | None = Field(default=None, description="Timestamp (in Unix time) when the status was last updated.")
    """Timestamp (in Unix time) when the status was last updated."""
    pq: WorkerPQStatus | None = Field(default=None, description="Persistent queue status information (if persistent queue is enabled).")
    """Persistent queue status information (if persistent queue is enabled)."""
    error: StatusError | None = Field(default=None, description="Error information, if applicable.")
    """Error information, if applicable."""
    useStatusFromLB: bool | None = Field(default=None, description="Set to prefer status from the LB process, not from the worker process.")
    """Set to prefer status from the LB process, not from the worker process."""


class NotificationSmtpTargetConfig(CriblModel):
    """SMTP configuration for a Notification target."""

    body: str | None = Field(default=None, description="Email body.")
    """Email body."""
    emailRecipient: dict[str, str] | None = Field(default=None, description="Email recipient settings (to, cc, bcc addresses).")
    """Email recipient settings (to, cc, bcc addresses)."""
    subject: str | None = Field(default=None, description="Email subject.")
    """Email subject."""


class NotificationTargetConfig(CriblModel):
    """Override settings for a Notification target."""

    id: str = Field(description="The id of the Notification target.")
    """The id of the Notification target."""
    conf: NotificationSmtpTargetConfig | None = Field(default=None, description="SMTP configuration for the Notification target.")
    """SMTP configuration for the Notification target."""


class NotificationTargetDetails(CriblModel):
    """Details about a referenced Notification target."""

    id: str = Field(description="The id of the Notification target.")
    """The id of the Notification target."""
    type: str = Field(description="The type of the Notification target.")
    """The type of the Notification target."""


class MetadataItem(CriblModel):
    """A metadata tag key-value pair."""

    name: str = Field(description="Name of the metadata field.")
    """Name of the metadata field."""
    value: str = Field(description="JavaScript expression to compute the metadata field's value, enclosed in quotes or backticks.")
    """JavaScript expression to compute the metadata field's value, enclosed in quotes or backticks."""


class TemplateTargetPair(CriblModel):
    """A pairing of a Notification target and template."""

    targetId: str = Field(description="The id of the Notification target to send the Notification to.")
    """The id of the Notification target to send the Notification to."""
    templateId: str = Field(description="The id of the Notification template to use.")
    """The id of the Notification template to use."""


class Notification(CriblModel):
    """Notification attached to a Source or Destination."""

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    src_group: str | None = Field(default=None, alias="__srcGroup", description="Fleet or group id this entity was inherited from. Display-only; never persisted.")
    """Fleet or group id this entity was inherited from. Display-only; never persisted."""
    src_overridden: bool | None = Field(default=None, alias="__srcOverridden", description="If true, the child fleet has a local overlay on an inherited entity. Display-only; never persisted.")
    """If true, the child fleet has a local overlay on an inherited entity. Display-only; never persisted."""
    id: str | None = Field(default=None, description="Unique identifier.")
    """Unique identifier."""
    condition: str | None = Field(default=None, description="The condition that triggers the Notification.")
    """The condition that triggers the Notification."""
    conf: dict[str, Any] | None = Field(default=None, description="Configuration for the condition that triggers the Notification. Supported fields vary depending on the condition.")
    """Configuration for the condition that triggers the Notification. Supported fields vary depending on the condition."""
    disabled: bool | None = Field(default=None, description="If true, the Notification is disabled and the specified condition will not trigger it.")
    """If true, the Notification is disabled and the specified condition will not trigger it."""
    group: str | None = Field(default=None, description="The id of the Worker Group or Edge Fleet that the Notification applies to.")
    """The id of the Worker Group or Edge Fleet that the Notification applies to."""
    metadata: list[MetadataItem] | None = Field(default=None, description="Metadata tags for the Notification.")
    """Metadata tags for the Notification."""
    mode: Literal["direct", "policy"] | None = Field(default=None, description="Delivery mode for Notifications. 'direct': sent directly to targets in templateTargetPairs. 'policy': routed through Notification Policies.")
    """Delivery mode for Notifications. 'direct': sent directly to targets in templateTargetPairs. 'policy': routed through Notification Policies."""
    pack: str | None = Field(default=None, description="The id of the Pack the Notification belongs to.")
    """The id of the Pack the Notification belongs to."""
    targetConfigs: list[NotificationTargetConfig] | None = Field(default=None, description="Override settings to apply for each referenced Notification target.")
    """Override settings to apply for each referenced Notification target."""
    targetDetails: list[NotificationTargetDetails] | None = Field(default=None, description="Additional details about referenced Notification targets. Optionally populated on request.")
    """Additional details about referenced Notification targets. Optionally populated on request."""
    targets: list[str] | None = Field(default=None, description="List of the id values for the Notification targets to send the Notification to.")
    """List of the id values for the Notification targets to send the Notification to."""
    templateTargetPairs: list[TemplateTargetPair] | None = Field(default=None, description="Pairs of Notification target and template ids.")
    """Pairs of Notification target and template ids."""


class SourceResponse(CriblModel):
    """Source configuration with optional Notifications and runtime status.

    Corresponds to the spec's InputResponse (allOf: Input + status/notifications).
    All Input fields pass through via extra="allow"; the most-accessed are declared
    explicitly for type-checker visibility.
    """

    id: str | None = Field(default=None, description="Unique identifier for this source.")
    """Unique identifier for this source."""
    type: str | None = Field(default=None, description="Source type (e.g. 'syslog', 'http').")
    """Source type (e.g. 'syslog', 'http')."""
    disabled: bool | None = Field(default=None, description="If true, source is not active.")
    """If true, source is not active."""
    pipeline: str | None = Field(default=None, description="Post-processing pipeline ID.")
    """Post-processing pipeline ID."""
    status: StatusType | None = Field(default=None, description="Runtime status: health, metrics, and optional persistent-queue info. Fields may be absent when data is unavailable.")
    """Runtime status: health, metrics, and optional persistent-queue info. Fields may be absent when data is unavailable."""
    notifications: list[Notification] | None = Field(default=None, description="Notifications attached to the Source.")
    """Notifications attached to the Source."""


class DestinationResponse(CriblModel):
    """Destination configuration with optional Notifications and runtime status.

    Corresponds to the spec's OutputResponse (allOf: Output + status/notifications).
    All Output fields pass through via extra="allow"; the most-accessed are declared
    explicitly for type-checker visibility.
    """

    id: str | None = Field(default=None, description="Unique identifier for this destination.")
    """Unique identifier for this destination."""
    type: str | None = Field(default=None, description="Destination type (e.g. 's3', 'splunk', 'elastic').")
    """Destination type (e.g. 's3', 'splunk', 'elastic')."""
    disabled: bool | None = Field(default=None, description="If true, destination is not active.")
    """If true, destination is not active."""
    pipeline: str | None = Field(default=None, description="Post-processing pipeline ID.")
    """Post-processing pipeline ID."""
    status: StatusType | None = Field(default=None, description="Runtime status: health, metrics, and optional persistent-queue info. Fields may be absent when data is unavailable.")
    """Runtime status: health, metrics, and optional persistent-queue info. Fields may be absent when data is unavailable."""
    notifications: list[Notification] | None = Field(default=None, description="Notifications attached to the Destination.")
    """Notifications attached to the Destination."""


# --- Deploy Lookups ---


class DeployLookupFileParam(TypedDict):
    """A single lookup file entry in a deploy request.

    Attrs:
        file: Unique identifier (file name) of the lookup to deploy.
        version: Version of the lookup file to deploy.
    """
    file: str
    version: str


class DeployRequestLookupsParam(TypedDict):
    """Lookup context and files to deploy with a commit.

    Attrs:
        context: Lookup context to deploy. Use 'cribl' for the default context or a Pack id for Pack lookups.
        lookups: List of lookup files to deploy in this context.
    """
    context: str
    lookups: list[DeployLookupFileParam]


# --- Routes ---


class RouteConfParam(TypedDict, total=False):
    """A Route configuration entry for create/update requests.

    Attrs:
        id: Unique identifier for the Route. If omitted, the server generates a deterministic identifier.
        name: Name of the Route.
        filter: JavaScript expression to select events for routing.
        pipeline: Pipeline that the Route sends matching events to.
        output: Destination that the Route sends matching events to after the Pipeline processes the events.
        outputExpression: JavaScript expression to evaluate for dynamic Destination selection. Evaluation occurs when the Route is constructed, not for each event.
        enableOutputExpression: If true, use the outputExpression for dynamic Destination selection.
        final: If true (default), matched events do not continue to the next Route. If false, all events continue to the next Route. Must be false to clone events.
        disabled: If true, disable the Route.
        description: Brief description of the Route.
        clones: Array of clone configurations, each with a key-value pair to set or overwrite in cloned events. Original events continue to the next Route.
        groupId: Unique identifier for the Route Group that the Route is associated with.
        context: Context for the Route: 'group' (Worker Group or Edge Fleet) or 'pack'.
        targetContext: Target context for subsequent event processing after applying the Route.
        autoParse: If true, detect each matched event's datatype and extract fields from _raw before the Pipeline processes the event. Otherwise, false (the default).
    """
    id: str
    name: str
    filter: str
    pipeline: str
    output: str
    outputExpression: str
    enableOutputExpression: bool
    final: bool
    disabled: bool
    description: str
    clones: list[dict[str, str]]
    groupId: str
    context: str
    targetContext: str
    autoParse: bool


class RouteConf(CriblModel):
    """A single route configuration within a routing table."""

    id: str | None = Field(default=None, description="Unique identifier for the Route. If omitted, the server generates a deterministic identifier.")
    """Unique identifier for the Route. If omitted, the server generates a deterministic identifier."""
    name: str | None = Field(default=None, description="Name of the Route.")
    """Name of the Route."""
    filter: str | None = Field(default=None, description="JavaScript expression to select events for routing.")
    """JavaScript expression to select events for routing."""
    pipeline: str | None = Field(default=None, description="Pipeline that the Route sends matching events to.")
    """Pipeline that the Route sends matching events to."""
    output: str | None = Field(default=None, description="Destination that the Route sends matching events to after the Pipeline processes the events.")
    """Destination that the Route sends matching events to after the Pipeline processes the events."""
    outputExpression: str | None = Field(default=None, description="JavaScript expression to evaluate for dynamic Destination selection. Evaluation occurs when the Route is constructed, not for each event.")
    """JavaScript expression to evaluate for dynamic Destination selection. Evaluation occurs when the Route is constructed, not for each event."""
    enableOutputExpression: bool | None = Field(default=None, description="If true, use the outputExpression for dynamic Destination selection.")
    """If true, use the outputExpression for dynamic Destination selection."""
    final_: bool | None = Field(default=None, alias="final", description="If true (default), matched events do not continue to the next Route. If false, all events continue to the next Route. Must be false to clone events.")
    """If true (default), matched events do not continue to the next Route. If false, all events continue to the next Route. Must be false to clone events."""
    disabled: bool | None = Field(default=None, description="If true, disable the Route.")
    """If true, disable the Route."""
    description: str | None = Field(default=None, description="Brief description of the Route.")
    """Brief description of the Route."""
    clones: list[dict[str, str]] | None = Field(default=None, description="Array of clone configurations, each with a key-value pair to set or overwrite in cloned events.")
    """Array of clone configurations, each with a key-value pair to set or overwrite in cloned events."""
    groupId: str | None = Field(default=None, description="Unique identifier for the Route Group that the Route is associated with.")
    """Unique identifier for the Route Group that the Route is associated with."""
    context: str | None = Field(default=None, description="Context for the Route: 'group' (Worker Group or Edge Fleet) or 'pack'.")
    """Context for the Route: 'group' (Worker Group or Edge Fleet) or 'pack'."""
    targetContext: str | None = Field(default=None, description="Target context for subsequent event processing after applying the Route.")
    """Target context for subsequent event processing after applying the Route."""
    autoParse: bool | None = Field(default=None, description="If true, detect each matched event's datatype and extract fields from _raw before the Pipeline processes the event, so Functions and Filters can reference the extracted fields. Otherwise, false (the default).")
    """If true, detect each matched event's datatype and extract fields from _raw before the Pipeline processes the event, so Functions and Filters can reference the extracted fields. Otherwise, false (the default)."""


class RouteComment(CriblModel):
    """A user-provided comment that describes or annotates a Route."""

    comment: str = Field(description="Brief description of the Route.")
    """Brief description of the Route."""
    id: str = Field(description="Unique identifier for the comment.")
    """Unique identifier for the comment."""
    index: int = Field(description="Relative position of the comment among all comments for the Route.")
    """Relative position of the comment among all comments for the Route."""
    groupId: str | None = Field(default=None, description="Unique identifier for the Route Group that the Route is associated with.")
    """Unique identifier for the Route Group that the Route is associated with."""


class RouteGroup(CriblModel):
    """A Route Group that organizes Routes."""

    name: str = Field(description="Name of the Route Group.")
    """Name of the Route Group."""
    index: int = Field(description="Relative position of the Route Group among all Route Groups.")
    """Relative position of the Route Group among all Route Groups."""
    description: str | None = Field(default=None, description="Brief description of the Route Group.")
    """Brief description of the Route Group."""


class Routes(CriblModel):
    """A routing table containing route definitions."""

    id: str | None = Field(default=None, description="Unique identifier for the Routing table. The supported value is 'default'.")
    """Unique identifier for the Routing table. The supported value is 'default'."""
    routes: list[RouteConf] | None = Field(default=None, description="Array of Route configurations that define how events are processed and routed.")
    """Array of Route configurations that define how events are processed and routed."""
    comments: list[RouteComment] | None = Field(default=None, description="Array of user-provided comments that describe or annotate Routes.")
    """Array of user-provided comments that describe or annotate Routes."""
    groups: dict[str, RouteGroup] | None = Field(default=None, description="Information about the Route Groups that the Route is associated with.")
    """Information about the Route Groups that the Route is associated with."""


# --- Collectors ---


class SavedJob(CriblModel):
    """A saved job (collector) configuration."""

    id: str | None = Field(default=None, description="Unique name for this Job")
    """Unique name for this Job"""
    type: str | None = Field(default=None, description="Job type")
    """Job type"""


# --- Database Connections ---


class TLSClientConfig(CriblModel):
    """TLS client connection settings."""

    disabled: bool = Field(description="If true, TLS is disabled for the connection.")
    """If true, TLS is disabled for the connection."""
    caPath: str | None = Field(default=None, description="Path to the Certificate Authority (CA) certificate file in PEM format.")
    """Path to the Certificate Authority (CA) certificate file in PEM format."""
    certPath: str | None = Field(default=None, description="Path to the client certificate file in PEM format.")
    """Path to the client certificate file in PEM format."""
    certificateName: str | None = Field(default=None, description="Name of a certificate stored in Cribl.")
    """Name of a certificate stored in Cribl."""
    maxVersion: Literal["TLSv1.3", "TLSv1.2", "TLSv1.1", "TLSv1"] | None = Field(default=None, description="Maximum TLS version to allow for the connection.")
    """Maximum TLS version to allow for the connection."""
    minVersion: Literal["TLSv1.3", "TLSv1.2", "TLSv1.1", "TLSv1"] | None = Field(default=None, description="Minimum TLS version to allow for the connection.")
    """Minimum TLS version to allow for the connection."""
    passphrase: str | None = Field(default=None, description="Passphrase for the private key.")
    """Passphrase for the private key."""
    privKeyPath: str | None = Field(default=None, description="Path to the private key file in PEM format.")
    """Path to the private key file in PEM format."""
    rejectUnauthorized: bool | None = Field(default=None, description="If true, reject connections to servers with unverified TLS certificates.")
    """If true, reject connections to servers with unverified TLS certificates."""
    servername: str | None = Field(default=None, description="Server name for TLS Server Name Indication (SNI) extension.")
    """Server name for TLS Server Name Indication (SNI) extension."""


class DatabaseConnectionPem(CriblModel):
    """RSA private key configuration for Snowflake key-pair authentication."""

    keyName: str = Field(..., description="RSA private key (PEM format) for Snowflake key-pair authentication.")
    """RSA private key (PEM format) for Snowflake key-pair authentication."""


class DatabaseConnectionConfig(CriblModel):
    """A database connection configuration."""

    id: str | None = Field(default=None, description="Unique identifier for the Database Connection.")
    """Unique identifier for the Database Connection."""
    databaseType: Literal["mysql", "oracle", "postgres", "sqlserver", "teradata"] | None = Field(default=None, description="Type of database engine for the connection.")
    """Type of database engine for the connection."""
    authType: Literal["configObj", "connectionString", "secret", "secrets"] | None = Field(default=None, description="Authentication method for the Database Connection.")
    """Authentication method for the Database Connection."""
    description: str | None = Field(default=None, description="Brief description of the Database Connection.")
    """Brief description of the Database Connection."""
    connectionString: str | None = Field(default=None, description="Database connection string with embedded credentials or server information.")
    """Database connection string with embedded credentials or server information."""
    configObj: str | None = Field(default=None, description="JSON configuration object for advanced SQL Server connection settings.")
    """JSON configuration object for advanced SQL Server connection settings."""
    connectionTimeout: int | None = Field(default=None, description="Maximum time (in milliseconds) to wait when establishing the database connection.")
    """Maximum time (in milliseconds) to wait when establishing the database connection."""
    requestTimeout: int | None = Field(default=None, description="Maximum time (in milliseconds) to wait for a database query to complete.")
    """Maximum time (in milliseconds) to wait for a database query to complete."""
    database: str | None = Field(default=None, description="Database to connect to instead of the server default.")
    """Database to connect to instead of the server default."""
    host: str | None = Field(default=None, description="Hostname of the server to connect to.")
    """Hostname of the server to connect to."""
    user: str | None = Field(default=None, description="Database username for authentication. Used with Oracle connections.")
    """Database username for authentication. Used with Oracle connections."""
    password: str | None = Field(default=None, description="Database password for authentication. Used with Oracle connections.")
    """Database password for authentication. Used with Oracle connections."""
    credentialsSecret: str | None = Field(default=None, description="Name of the stored credentials secret containing username and password for SQL Server configObj auth.")
    """Name of the stored credentials secret containing username and password for SQL Server configObj auth."""
    credsSecrets: str | None = Field(default=None, description="Name of the stored credentials secret containing username and password. Used with Oracle connections.")
    """Name of the stored credentials secret containing username and password. Used with Oracle connections."""
    logOnMechanism: str | None = Field(default=None, description="Log On Mechanism for databases that support multiple, like Teradata.")
    """Log On Mechanism for databases that support multiple, like Teradata."""
    textSecret: str | None = Field(default=None, description="Name of the stored text secret containing the connection string.")
    """Name of the stored text secret containing the connection string."""
    sslmode: str | None = Field(default=None, description="HTTPS/TLS connection mode for Teradata. Controls certificate verification behavior.")
    """HTTPS/TLS connection mode for Teradata. Controls certificate verification behavior."""
    tags: str | None = Field(default=None, description="Comma-separated list of tags for categorizing and filtering Database Connections.")
    """Comma-separated list of tags for categorizing and filtering Database Connections."""
    tls: TLSClientConfig | None = Field(default=None, description="TLS client configuration for the database connection.")
    """TLS client configuration for the database connection."""
    accountIdentifier: str | None = Field(default=None, description="Snowflake account identifier in org-account format (example: MYORG-MYACCOUNT).")
    """Snowflake account identifier in org-account format (example: MYORG-MYACCOUNT)."""
    pem: DatabaseConnectionPem | None = Field(default=None, description="RSA private key configuration for Snowflake key-pair authentication.")
    """RSA private key configuration for Snowflake key-pair authentication."""
    role: str | None = Field(default=None, description="Snowflake role to use for the session. When set, requests a role-scoped token.")
    """Snowflake role to use for the session. When set, requests a role-scoped token."""
    warehouse: str | None = Field(default=None, description="Snowflake warehouse to use for queries.")
    """Snowflake warehouse to use for queries."""


# --- Functions ---


class FunctionDef(CriblModel):
    """A Cribl function definition."""

    id: str | None = Field(default=None, description="Unique identifier (function type name).")
    """Unique identifier (function type name)."""
    category: str | None = Field(default=None, description="Function category for grouping.")
    """Function category for grouping."""
    description: str | None = Field(default=None, description="What this function does.")
    """What this function does."""


# --- Lake Datasets ---


class CriblLakeDataset(CriblModel):
    """A Cribl Lake dataset."""

    id: str | None = Field(default=None, description="Unique identifier for the Dataset.")
    """Unique identifier for the Dataset."""
    name: str | None = Field(default=None, description="Dataset name.")
    """Dataset name."""
    description: str | None = Field(default=None, description="Brief description of the Dataset.")
    """Brief description of the Dataset."""
    format: Literal["ddss", "json", "netskope", "parquet"] | None = Field(default=None, description="Storage format used for data persisted in the Dataset.")
    """Storage format used for data persisted in the Dataset."""
    storageClass: Literal["Archive", "Cold", "Cool", "DEEP_ARCHIVE", "GLACIER", "GLACIER_IR", "Hot", "Inferred", "INTELLIGENT_TIERING", "ONEZONE_IA", "STANDARD", "STANDARD_IA"] | None = Field(default=None, description="Storage class used for objects written to the Dataset.")
    """Storage class used for objects written to the Dataset."""
    retentionPeriodInDays: int | None = Field(default=None, description="Dataset retention period, in days.")
    """Dataset retention period, in days."""
    bucketName: str | None = Field(default=None, description="Name of the legacy Cribl Lake bucket that backs the Dataset.")
    """Name of the legacy Cribl Lake bucket that backs the Dataset."""
    storageLocationId: str | None = Field(default=None, description="Unique identifier for the Storage Location that backs the Dataset.")
    """Unique identifier for the Storage Location that backs the Dataset."""
    providerPath: str | None = Field(default=None, description="Storage path within the provider (for example an S3 prefix or Azure container).")
    """Storage path within the provider (for example an S3 prefix or Azure container)."""
    viewName: str | None = Field(default=None, description="Name of the ClickHouse view for the Dataset on the Lakehouse.")
    """Name of the ClickHouse view for the Dataset on the Lakehouse."""
    acceleratedFields: list[str] | None = Field(default=None, description="Accelerated fields for the Dataset. Data is partitioned by these fields in storage to improve query performance.")
    """Accelerated fields for the Dataset. Data is partitioned by these fields in storage to improve query performance."""
    allowRecordErasure: bool | None = Field(default=None, description="If true, the Dataset is opted in to Lake Record Erasure.")
    """If true, the Dataset is opted in to Lake Record Erasure."""
    httpDAUsed: bool | None = Field(default=None, description="If true, the Dataset is used by Direct Access HTTP.")
    """If true, the Dataset is used by Direct Access HTTP."""
    deletionStartedAt: float | None = Field(default=None, description="Timestamp (in Unix time) when Dataset deletion was initiated, in milliseconds.")
    """Timestamp (in Unix time) when Dataset deletion was initiated, in milliseconds."""
    cacheConnection: CacheConnectionParam | None = Field(default=None, description="Lakehouse cache connection settings for the Dataset.")
    """Lakehouse cache connection settings for the Dataset."""
    metrics: DatasetMetricsParam | None = Field(default=None, description="Most recent Dataset metrics snapshot.")
    """Most recent Dataset metrics snapshot."""
    searchConfig: DatasetSearchConfigParam | None = Field(default=None, description="Search configuration for the Dataset.")
    """Search configuration for the Dataset."""


# --- Jobs ---


class TaskErrorInfo(CriblModel):
    """Nested cause of a task error."""

    message: str = Field(description="Human-readable error message.")
    """Human-readable error message."""
    name: str | None = Field(default=None, description="Error name, if available.")
    """Error name, if available."""
    stack: str | None = Field(default=None, description="Truncated stack trace of the error.")
    """Truncated stack trace of the error."""


class TaskErrorDetail(CriblModel):
    """Task error details with nested cause."""

    message: str = Field(description="Human-readable error message.")
    """Human-readable error message."""
    name: str | None = Field(default=None, description="Error name, if available.")
    """Error name, if available."""
    reason: TaskErrorInfo | None = Field(default=None, description="Nested cause of the error, if any.")
    """Nested cause of the error, if any."""
    stack: str | None = Field(default=None, description="Truncated stack trace of the error.")
    """Truncated stack trace of the error."""


class JobStatus(CriblModel):
    """Status of a job, including its current state and failure reason."""

    state: JobState | int = Field(description="State of the Job (0=Initializing, 1=Pending, 2=Running, 3=Paused, 4=Cancelled, 5=Finished, 6=Failed, 7=Orphaned, 8=Unknown).")
    """State of the Job (0=Initializing, 1=Pending, 2=Running, 3=Paused, 4=Cancelled, 5=Finished, 6=Failed, 7=Orphaned, 8=Unknown)."""
    reason: TaskErrorDetail | None = Field(default=None, description="Reason the job entered its current state, typically populated upon failure.")
    """Reason the job entered its current state, typically populated upon failure."""


class JobRunConfig(CriblModel):
    """Run configuration for a job."""

    mode: Literal["list", "preview", "run"] | None = Field(default=None, description="Job run mode. Preview will either return up to N matching results, or will run until capture time T is reached. Discovery will gather the list of files to turn into streaming tasks, without running the data collection job. Full Run will run the collection job.")
    """Job run mode. Preview will either return up to N matching results, or will run until capture time T is reached. Discovery will gather the list of files to turn into streaming tasks, without running the data collection job. Full Run will run the collection job."""
    rescheduleDroppedTasks: bool | None = Field(default=None, description="Reschedule tasks that failed with non-fatal errors")
    """Reschedule tasks that failed with non-fatal errors"""
    maxTaskReschedule: float | None = Field(default=None, description="Maximum number of times a task can be rescheduled")
    """Maximum number of times a task can be rescheduled"""
    logLevel: str | None = Field(default=None, description="Level at which to set task logging")
    """Level at which to set task logging"""
    jobTimeout: str | None = Field(default=None, description="Maximum time the job is allowed to run. Time unit defaults to seconds if not specified (examples: 30, 45s, 15m). Enter 0 for unlimited time.")
    """Maximum time the job is allowed to run. Time unit defaults to seconds if not specified (examples: 30, 45s, 15m). Enter 0 for unlimited time."""
    timeRangeType: Literal["absolute", "relative"] | None = Field(default=None, description="Time range")
    """Time range"""
    earliest: float | str | None = Field(default=None, description="Earliest time to collect data for the selected timezone")
    """Earliest time to collect data for the selected timezone"""
    latest: float | str | None = Field(default=None, description="Latest time to collect data for the selected timezone")
    """Latest time to collect data for the selected timezone"""
    timestampTimezone: str | None = Field(default=None, description="Timezone to use for Earliest and Latest times")
    """Timezone to use for Earliest and Latest times"""
    expression: str | None = Field(default=None, description="A filter for tokens in the provided collect path and/or the events being collected")
    """A filter for tokens in the provided collect path and/or the events being collected"""
    minTaskSize: str | None = Field(default=None, description="Limits the bundle size for small tasks. For example, if your lower bundle size is 1MB, you can bundle up to five 200KB files into one task.")
    """Limits the bundle size for small tasks. For example, if your lower bundle size is 1MB, you can bundle up to five 200KB files into one task."""
    maxTaskSize: str | None = Field(default=None, description="Limits the bundle size for files above the lower task bundle size. For example, if your upper bundle size is 10MB, you can bundle up to five 2MB files into one task. Files greater than this size will be assigned to individual tasks.")
    """Limits the bundle size for files above the lower task bundle size. For example, if your upper bundle size is 10MB, you can bundle up to five 2MB files into one task. Files greater than this size will be assigned to individual tasks."""
    discoverToRoutes: bool | None = Field(default=None, description="Send discover results to Routes")
    """Send discover results to Routes"""


class JobExecutorConfig(CriblModel):
    """Executor configuration for executor jobs."""

    type: str = Field(description="The type of executor to run")
    """The type of executor to run"""
    storeTaskResults: bool | None = Field(default=None, description="Determines whether or not to write task results to disk")
    """Determines whether or not to write task results to disk"""
    conf: dict[str, Any] | None = Field(default=None, description="Executor-type-specific settings object. Shape varies by executor type.")
    """Executor-type-specific settings object. Shape varies by executor type."""


class RunnableJob(CriblModel):
    """Configuration and run settings for a job (collection, executor, or scheduled search)."""

    id: str | None = Field(default=None, description="Unique name for this Job")
    """Unique name for this Job"""
    description: str | None = Field(default=None, description="Description")
    """Description"""
    type: str | None = Field(default=None, description="Job type")
    """Job type"""
    ttl: str | None = Field(default=None, description="Time to keep the job's artifacts on disk after job completion. This also affects how long a job is listed in the Job Inspector.")
    """Time to keep the job's artifacts on disk after job completion. This also affects how long a job is listed in the Job Inspector."""
    ignoreGroupJobsLimit: bool | None = Field(default=None, description="When enabled, this job's artifacts are not counted toward the Worker Group's finished job artifacts limit. Artifacts will be removed only after the Collector's configured time to live.")
    """When enabled, this job's artifacts are not counted toward the Worker Group's finished job artifacts limit. Artifacts will be removed only after the Collector's configured time to live."""
    removeFields: list[str] | None = Field(default=None, description="List of fields to remove from Discover results. Wildcards (for example, aws*) are allowed. This is useful when discovery returns sensitive fields that should not be exposed in the Jobs user interface.")
    """List of fields to remove from Discover results. Wildcards (for example, aws*) are allowed. This is useful when discovery returns sensitive fields that should not be exposed in the Jobs user interface."""
    collector: CriblModel | None = Field(default=None, description="Collector configuration used to discover and run the Collection job.")
    """Collector configuration used to discover and run the Collection job."""
    executor: JobExecutorConfig | None = Field(default=None, description="Executor configuration, including the executor type and its settings.")
    """Executor configuration, including the executor type and its settings."""
    savedQueryId: str | None = Field(default=None, description="Identifies which search query to run")
    """Identifies which search query to run"""
    # `run` exists on both the Collection and Executor variants with slightly different spec text
    # ("...the Collection job runs." vs "...the Executor job runs."). The flattened model uses the
    # Collection variant's wording (listed first in the spec's oneOf); either is spec-faithful.
    run: JobRunConfig | None = Field(default=None, description="Run settings that control how and when the Collection job runs.")
    """Run settings that control how and when the Collection job runs."""


class JobInfo(CriblModel):
    """Detailed information about a job."""

    id: str = Field(description="Unique identifier for the job.")
    """Unique identifier for the job."""
    status: JobStatus | None = Field(default=None, description="Status of the job, including its current state and failure reason.")
    """Status of the job, including its current state and failure reason."""
    args: RunnableJob | None = Field(default=None, description="Configuration and run settings used to launch the job.")
    """Configuration and run settings used to launch the job."""
    stats: dict[str, Any] | None = Field(default=None, description="Counters and metrics collected during job execution.")
    """Counters and metrics collected during job execution."""
    keep: bool | None = Field(default=None, description="If true, retain the job and its artifacts instead of deleting according to the time-to-live setting.")
    """If true, retain the job and its artifacts instead of deleting according to the time-to-live setting."""
    workerOwner: str | None = Field(default=None, description="The GUID of the worker node that owns this artifact.")
    """The GUID of the worker node that owns this artifact."""


# --- Access Control ---


class ResourcePolicy(CriblModel):
    """A resource access control policy entry."""

    gid: str = Field(description="Unique identifier for the group that owns the resource.")
    """Unique identifier for the group that owns the resource."""
    policy: str = Field(description="String that defines the access control policy for the resource.")
    """String that defines the access control policy for the resource."""
    type: str = Field(description="Resource type that the access control policy applies to.")
    """Resource type that the access control policy applies to."""
    id: str | None = Field(default=None, description="Unique identifier for the resource. Omitted for resource type 'groups'.")
    """Unique identifier for the resource. Omitted for resource type 'groups'."""


class TeamAccessControlList(CriblModel):
    """Access control list for a team."""

    team: str = Field(description="Team identifier.")
    """Team identifier."""
    perms: list[ResourcePolicy] = Field(description="Resource policies assigned to the team.")
    """Resource policies assigned to the team."""


class UserAccessControlList(CriblModel):
    """Access control list for a user."""

    user: str = Field(description="User identifier.")
    """User identifier."""
    perms: list[ResourcePolicy] = Field(description="Resource policies assigned to the user.")
    """Resource policies assigned to the user."""


# --- Cribl.Cloud platform (openapi/management-plane.yml) ---

AwsRegion = Literal[
    "us-west-2",
    "us-east-1",
    "us-east-2",
    "eu-central-1",
    "eu-central-2",
    "eu-west-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "ap-northeast-1",
    "sa-east-1",
    "eu-west-1",
    "eu-west-3",
]
OrganizationRole = Literal["owner", "admin", "billing_reader", "user"]
WorkspaceRole = Literal["owner", "admin", "user", "noaccess"]
ProductName = Literal["edge", "search", "stream", "lake", "insights"]
ProductRole = Literal["admin", "editor", "reader", "user", "noaccess"]
BillingWindow = Literal["monthly", "daily"]
CreditGrantType = Literal["Refund", "Rollover", "Purchased"]
WorkspaceState = Literal["Provisioning", "Active", "Inactive", "Failed", "Deprovisioning"]


class ProductRoleParam(TypedDict):
    """Product-level Role assigned to the API Credential for the Workspace.

    Attrs:
        product: Product name.
        role: Role assigned to the API Credential on the product.
    """

    product: ProductName
    role: ProductRole


class WorkspaceRoleParam(TypedDict):
    """Workspace-level Role assigned to the API Credential.

    Attrs:
        workspaceId: Unique ID of the Workspace.
        workspaceRole: Role assigned to the API Credential on the Workspace.
        products: Product-level Roles assigned to the API Credential for the Workspace.
    """

    workspaceId: str
    workspaceRole: WorkspaceRole
    products: NotRequired[list[ProductRoleParam]]


class ApiCredentialRolesParam(TypedDict):
    """Role assignments for the API Credential.

    Attrs:
        organizationRole: Organization-level Role assigned to the API Credential.
        workspaces: Workspace-level Roles assigned to the API Credential.
    """

    organizationRole: OrganizationRole
    workspaces: NotRequired[list[WorkspaceRoleParam]]


class ProductRoleSchema(CriblModel):
    """Product-level Role assigned to the API Credential for the Workspace."""

    product: ProductName = Field(description="Product name.")
    """Product name."""
    role: ProductRole = Field(description="Role assigned to the API Credential on the product.")
    """Role assigned to the API Credential on the product."""


class WorkspaceRoleSchema(CriblModel):
    """Workspace-level Role assigned to the API Credential."""

    workspaceId: str = Field(description="Unique ID of the Workspace.")
    """Unique ID of the Workspace."""
    workspaceRole: WorkspaceRole = Field(description="Role assigned to the API Credential on the Workspace.")
    """Role assigned to the API Credential on the Workspace."""
    products: list[ProductRoleSchema] | None = Field(
        default=None,
        description="Product-level Roles assigned to the API Credential for the Workspace.",
    )
    """Product-level Roles assigned to the API Credential for the Workspace."""


class ApiCredentialRolesSchema(CriblModel):
    """Role assignments for the API Credential."""

    organizationRole: OrganizationRole = Field(description="Organization-level Role assigned to the API Credential.")
    """Organization-level Role assigned to the API Credential."""
    workspaces: list[WorkspaceRoleSchema] | None = Field(
        default=None,
        description="Workspace-level Roles assigned to the API Credential.",
    )
    """Workspace-level Roles assigned to the API Credential."""


class ApiCredentialResponseSchema(CriblModel):
    """API Credential returned by list and get operations."""

    name: str = Field(description="Human-readable name of the API Credential.")
    """Human-readable name of the API Credential."""
    description: str = Field(description="Brief description of the purpose and usage for the API Credential.")
    """Brief description of the purpose and usage for the API Credential."""
    enabled: bool = Field(description="If true, the API Credential is enabled. Otherwise, false.")
    """If true, the API Credential is enabled. Otherwise, false."""
    organizationId: str = Field(description="Unique ID of the Organization.")
    """Unique ID of the Organization."""
    clientId: str = Field(description="Client ID for the API Credential.")
    """Client ID for the API Credential."""
    roles: ApiCredentialRolesSchema = Field(description="Role assignments for the API Credential.")
    """Role assignments for the API Credential."""
    ipAllowlist: list[str] = Field(
        description="CIDR range enforced as the IP allowlist for the API Credential. An empty array means that the API Credential has no IP restrictions.",
    )
    """CIDR range enforced as the IP allowlist for the API Credential. An empty array means that the API Credential has no IP restrictions."""
    createdBy: str = Field(description="Member who created the API Credential.")
    """Member who created the API Credential."""
    createdDate: str = Field(description="ISO 8601 timestamp when the API Credential was created.")
    """ISO 8601 timestamp when the API Credential was created."""
    lastUpdatedBy: str = Field(description="Member who last updated the API Credential.")
    """Member who last updated the API Credential."""
    lastUpdatedDate: str = Field(description="ISO 8601 timestamp when the API Credential was last updated.")
    """ISO 8601 timestamp when the API Credential was last updated."""


class ApiCredentialsListResponseDTO(CriblModel):
    """List of API Credentials for an Organization."""

    items: list[ApiCredentialResponseSchema] = Field(description="List of API Credentials.")
    """List of API Credentials."""
    count: int = Field(description="Total number of API Credentials listed in the response.")
    """Total number of API Credentials listed in the response."""


class ApiCredentialCreateResponseSchema(CriblModel):
    """API Credential returned when created. Includes the Client Secret."""

    name: str = Field(description="Human-readable name of the API Credential.")
    """Human-readable name of the API Credential."""
    description: str = Field(description="Brief description of the purpose and usage for the API Credential.")
    """Brief description of the purpose and usage for the API Credential."""
    enabled: bool = Field(description="If true, the API Credential is enabled. Otherwise, false.")
    """If true, the API Credential is enabled. Otherwise, false."""
    organizationId: str = Field(description="Unique ID of the Organization.")
    """Unique ID of the Organization."""
    clientId: str = Field(description="Client ID for the API Credential.")
    """Client ID for the API Credential."""
    roles: ApiCredentialRolesSchema = Field(description="Role assignments for the API Credential.")
    """Role assignments for the API Credential."""
    ipAllowlist: list[str] = Field(
        description="CIDR range enforced as the IP allowlist for the API Credential. An empty array means that the API Credential has no IP restrictions.",
    )
    """CIDR range enforced as the IP allowlist for the API Credential. An empty array means that the API Credential has no IP restrictions."""
    createdBy: str = Field(description="Member who created the API Credential.")
    """Member who created the API Credential."""
    createdDate: str = Field(description="ISO 8601 timestamp when the API Credential was created.")
    """ISO 8601 timestamp when the API Credential was created."""
    lastUpdatedBy: str = Field(description="Member who last updated the API Credential.")
    """Member who last updated the API Credential."""
    lastUpdatedDate: str = Field(description="ISO 8601 timestamp when the API Credential was last updated.")
    """ISO 8601 timestamp when the API Credential was last updated."""
    clientSecret: str = Field(
        description="Client Secret for the API Credential. The Client Secret is sensitive information and should be kept private. Returned only in the POST response when the API Credential is created. Never returned in GET responses. If you need the Client Secret again, you must rotate credentials and retrieve the new Client Secret from the POST response.",
    )
    """Client Secret for the API Credential. The Client Secret is sensitive information and should be kept private. Returned only in the POST response when the API Credential is created. Never returned in GET responses. If you need the Client Secret again, you must rotate credentials and retrieve the new Client Secret from the POST response."""


class CreditsUtilizationItemSchema(CriblModel):
    """Credits consumed in a single aggregation window."""

    date: str = Field(description="Date of the aggregation window in ISO 8601 format.")
    """Date of the aggregation window in ISO 8601 format."""
    credits: float = Field(description="Number of credits consumed in the aggregation window.")
    """Number of credits consumed in the aggregation window."""


class ContractUtilizationSchema(CriblModel):
    """Cumulative credit utilization for a contract period."""

    contractStartDate: str = Field(description="Contract start date in ISO 8601 format.")
    """Contract start date in ISO 8601 format."""
    contractEndDate: str | None = Field(
        default=None,
        description="Contract end date in ISO 8601 format. Present only when the contract is closed.",
    )
    """Contract end date in ISO 8601 format. Present only when the contract is closed."""
    items: list[CreditsUtilizationItemSchema] = Field(description="Cumulative credit utilization entries for the contract.")
    """Cumulative credit utilization entries for the contract."""


class ContractsUtilizationResponseDTO(CriblModel):
    """Contract credit utilization data, grouped by contract period."""

    contracts: list[ContractUtilizationSchema] = Field(description="Contract utilization data, grouped by contract period.")
    """Contract utilization data, grouped by contract period."""


class CreditsTimeseriesDimensionSchema(CriblModel):
    """Credit breakdown for a single dimension."""

    dimension: str = Field(description="Dimension label for the credit breakdown.")
    """Dimension label for the credit breakdown."""
    credits: float = Field(description="Number of credits attributed to the dimension.")
    """Number of credits attributed to the dimension."""


class CreditsTimeseriesItemSchema(CriblModel):
    """Credit consumption for a single aggregation window."""

    date: str = Field(description="Date of the aggregation window in ISO 8601 format.")
    """Date of the aggregation window in ISO 8601 format."""
    credits: float = Field(description="Total credits consumed in the aggregation window.")
    """Total credits consumed in the aggregation window."""
    dimensions: list[CreditsTimeseriesDimensionSchema] = Field(description="Credit breakdown by dimension.")
    """Credit breakdown by dimension."""


class CreditsTimeseriesResponseDTO(CriblModel):
    """Credit timeseries data points."""

    items: list[CreditsTimeseriesItemSchema] = Field(description="Credit timeseries data points.")
    """Credit timeseries data points."""
    count: int = Field(description="Total number of items in the response.")
    """Total number of items in the response."""


class CreditsStatsContractSchema(CriblModel):
    """Contract period included in credit stats."""

    startDate: str = Field(description="Contract start date in ISO 8601 format.")
    """Contract start date in ISO 8601 format."""
    endDate: str | None = Field(
        default=None,
        description="Contract end date in ISO 8601 format. Present only when the contract is closed.",
    )
    """Contract end date in ISO 8601 format. Present only when the contract is closed."""


class CreditsStatsResponseDTO(CriblModel):
    """Credit balance totals, consumption totals, and contract date ranges."""

    totalCreditsRemaining: float = Field(description="Credits remaining under the current contract.")
    """Credits remaining under the current contract."""
    totalCreditsUsed: float = Field(description="Credits consumed under the current contract.")
    """Credits consumed under the current contract."""
    totalCreditsAcquired: float = Field(description="Credits acquired under the current contract.")
    """Credits acquired under the current contract."""
    contracts: list[CreditsStatsContractSchema] | None = Field(
        default=None,
        description="All contracts for the Organization, ordered by contract start date in reverse chronological order (newest first).",
    )
    """All contracts for the Organization, ordered by contract start date in reverse chronological order (newest first)."""


class CreditGrantSchema(CriblModel):
    """A credit grant (purchase, rollover, or refund)."""

    date: str = Field(description="Date the grant was issued, in ISO 8601 format.")
    """Date the grant was issued, in ISO 8601 format."""
    creditsAcquired: float = Field(description="Number of credits acquired by the grant.")
    """Number of credits acquired by the grant."""
    type: CreditGrantType = Field(description="Type of the credit grant.")
    """Type of the credit grant."""


class CreditGrantsResponseDTO(CriblModel):
    """Credit grants for the current contract."""

    items: list[CreditGrantSchema] = Field(
        description="Credit grants for the current contract. Listed in reverse chronologial order by grant date (newest first).",
    )
    """Credit grants for the current contract. Listed in reverse chronologial order by grant date (newest first)."""
    count: int = Field(description="Total number of items in the response.")
    """Total number of items in the response."""


class WorkspaceSchema(CriblModel):
    """A Cribl.Cloud Workspace."""

    workspaceId: str = Field(description="Unique identifier for the Workspace.")
    """Unique identifier for the Workspace."""
    region: AwsRegion = Field(description="AWS region where the Workspace is deployed.")
    """AWS region where the Workspace is deployed."""
    leaderFQDN: str = Field(description="Fully Qualified Domain Name (FQDN) of the Workspace Leader.")
    """Fully Qualified Domain Name (FQDN) of the Workspace Leader."""
    state: WorkspaceState = Field(description="Current state of the Workspace.")
    """Current state of the Workspace."""
    alias: str | None = Field(default=None, description="User-friendly alias for the Workspace.")
    """User-friendly alias for the Workspace."""
    description: str | None = Field(default=None, description="Brief description of the Workspace.")
    """Brief description of the Workspace."""
    tags: list[str] | None = Field(default=None, description="Tags associated with the Workspace.")
    """Tags associated with the Workspace."""


class WorkspacesListResponseDTO(CriblModel):
    """List of Workspaces for an Organization."""

    items: list[WorkspaceSchema] = Field(description="List of workspaces")
    """List of workspaces"""
    count: int = Field(description="Total number of workspaces")
    """Total number of workspaces"""


class CloudHealthStatus(CriblModel):
    """Health status of the Cribl.Cloud platform gateway."""

    status: str | None = Field(default=None, description="Health status")
    """Health status"""


class DefaultErrorDTO(CriblModel):
    """Default error response from the Cribl.Cloud platform API."""

    statusCode: int = Field(description="HTTP status code.")
    """HTTP status code."""
    message: str = Field(description="Human-readable error message.")
    """Human-readable error message."""


# --- Pagination ---


class PaginatedResponse(BaseModel, Generic[T]):
    """Generic paginated response wrapper."""

    items: list[T] = Field(description="List of items in this page.")
    """List of items in this page."""
    count: int = Field(description="Number of items in this page.")
    """Number of items in this page."""
    offset: int | None = Field(default=None, description="Offset of this page from the start.")
    """Offset of this page from the start."""
    limit: int | None = Field(default=None, description="Maximum number of items per page.")
    """Maximum number of items per page."""
    total_count: int | None = Field(default=None, alias="totalCount", description="Total number of items across all pages.")
    """Total number of items across all pages."""
