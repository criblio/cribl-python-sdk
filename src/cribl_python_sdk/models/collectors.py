"""Auto-generated collector models from OpenAPI spec. DO NOT EDIT MANUALLY."""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import Field

from ._core import CriblModel
from ._collector_confs import (
    AzureBlobCollectorConf,
    CriblLakeCollectorConf,
    DatabaseCollectorConf,
    FilesystemCollectorConf,
    GoogleCloudStorageCollectorConf,
    HealthCheckCollectorConf,
    RestCollectorConf,
    S3CollectorConf,
    ScriptCollectorConf,
    SplunkCollectorConf,
)

class CollectorAzureBlob(CriblModel):
    """AzureBlob collector configuration"""

    type: Literal["azure_blob"] = "azure_blob"
    conf: AzureBlobCollectorConf = Field(..., description="Configuration specific to the AzureBlob Collector.")
    destructive: Optional[bool] = Field(default=None, description="Delete any files collected (where applicable)")
    encoding: Optional[str] = Field(default=None, description="Character encoding to use when parsing ingested data.")


class CollectorCriblLake(CriblModel):
    """CriblLake collector configuration"""

    type: Literal["cribl_lake"] = "cribl_lake"
    conf: CriblLakeCollectorConf = Field(..., description="Configuration specific to the CriblLake Collector.")
    destructive: Optional[bool] = Field(default=None, description="Delete any files collected (where applicable)")
    encoding: Optional[str] = Field(default=None, description="Character encoding to use when parsing ingested data.")


class CollectorDatabase(CriblModel):
    """Database collector configuration"""

    type: Literal["database"] = "database"
    conf: DatabaseCollectorConf = Field(..., description="Configuration specific to the Database Collector.")
    destructive: Optional[bool] = Field(default=None, description="Delete any files collected (where applicable)")
    encoding: Optional[str] = Field(default=None, description="Character encoding to use when parsing ingested data.")


class CollectorFilesystem(CriblModel):
    """Filesystem collector configuration"""

    type: Literal["filesystem"] = "filesystem"
    conf: FilesystemCollectorConf = Field(..., description="Configuration specific to the Filesystem Collector.")
    destructive: Optional[bool] = Field(default=None, description="Delete any files collected (where applicable)")
    encoding: Optional[str] = Field(default=None, description="Character encoding to use when parsing ingested data.")


class CollectorGoogleCloudStorage(CriblModel):
    """GoogleCloudStorage collector configuration"""

    type: Literal["google_cloud_storage"] = "google_cloud_storage"
    conf: GoogleCloudStorageCollectorConf = Field(..., description="Configuration specific to the GoogleCloudStorage Collector.")
    destructive: Optional[bool] = Field(default=None, description="Delete any files collected (where applicable)")
    encoding: Optional[str] = Field(default=None, description="Character encoding to use when parsing ingested data.")


class CollectorHealthCheck(CriblModel):
    """HealthCheck collector configuration"""

    type: Literal["health_check"] = "health_check"
    conf: HealthCheckCollectorConf = Field(..., description="Configuration specific to the HealthCheck Collector.")
    destructive: Optional[bool] = Field(default=None, description="Delete any files collected (where applicable)")
    encoding: Optional[str] = Field(default=None, description="Character encoding to use when parsing ingested data.")


class CollectorRest(CriblModel):
    """Rest collector configuration"""

    type: Literal["rest"] = "rest"
    conf: RestCollectorConf = Field(..., description="Configuration specific to the Rest Collector.")
    destructive: Optional[bool] = Field(default=None, description="Delete any files collected (where applicable)")
    encoding: Optional[str] = Field(default=None, description="Character encoding to use when parsing ingested data.")


class CollectorS3(CriblModel):
    """S3 collector configuration"""

    type: Literal["s3"] = "s3"
    conf: S3CollectorConf = Field(..., description="Configuration specific to the S3 Collector.")
    destructive: Optional[bool] = Field(default=None, description="Delete any files collected (where applicable)")
    encoding: Optional[str] = Field(default=None, description="Character encoding to use when parsing ingested data.")


class CollectorScript(CriblModel):
    """Script collector configuration"""

    type: Literal["script"] = "script"
    conf: ScriptCollectorConf = Field(..., description="Configuration specific to the Script Collector.")
    destructive: Optional[bool] = Field(default=None, description="Delete any files collected (where applicable)")
    encoding: Optional[str] = Field(default=None, description="Character encoding to use when parsing ingested data.")


class CollectorSplunk(CriblModel):
    """Splunk collector configuration"""

    type: Literal["splunk"] = "splunk"
    conf: SplunkCollectorConf = Field(..., description="Configuration specific to the Splunk Collector.")
    destructive: Optional[bool] = Field(default=None, description="Delete any files collected (where applicable)")
    encoding: Optional[str] = Field(default=None, description="Character encoding to use when parsing ingested data.")

# --- Discriminated Union ---

from typing import Annotated, Union
from pydantic import Discriminator, Tag

Collector = Annotated[
    Union[
        Annotated[CollectorAzureBlob, Tag("azure_blob")],
        Annotated[CollectorCriblLake, Tag("cribl_lake")],
        Annotated[CollectorDatabase, Tag("database")],
        Annotated[CollectorFilesystem, Tag("filesystem")],
        Annotated[CollectorGoogleCloudStorage, Tag("google_cloud_storage")],
        Annotated[CollectorHealthCheck, Tag("health_check")],
        Annotated[CollectorRest, Tag("rest")],
        Annotated[CollectorS3, Tag("s3")],
        Annotated[CollectorScript, Tag("script")],
        Annotated[CollectorSplunk, Tag("splunk")],
    ],
    Discriminator("type"),
]
