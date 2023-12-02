from dataclasses import dataclass, field

from dataclasses_json import dataclass_json, config
from pymilvus import IndexType
from pymilvus.client.types import MetricType


@dataclass_json
@dataclass
class IndexParams:
    index_type: IndexType = field(
        default=IndexType.FLAT,
        metadata=config(
            encoder=lambda x: x.name,
            decoder=lambda x: getattr(IndexType, x)
        )
    )
    metric_type: MetricType = field(
        default=MetricType.L2,
        metadata=config(
            encoder=lambda x: x.name,
            decoder=lambda x: getattr(MetricType, x)
        )
    )
    params: dict = field(default_factory=dict)
