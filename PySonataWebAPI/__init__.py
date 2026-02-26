import warnings

warnings.warn(
    "PySonataWebAPI is legacy. Migrate to SymfWebAPI: https://github.com/maku2903/symf-webapi-py",
    DeprecationWarning,
    stacklevel=2,
)

from . import WebAPI
