class RiffLabError(Exception):
    """Base class for all domain errors."""


class SeparationError(RiffLabError):
    """Raised when a song cannot be separated into stems."""
