from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class StemKind(Enum):
    GUITAR = "guitar"
    BASS = "bass"
    DRUMS = "drums"
    VOCALS = "vocals"
    PIANO = "piano"
    OTHER = "other"


@dataclass(frozen=True)
class Song:
    id: str
    path: Path


@dataclass(frozen=True)
class Stem:
    song_id: str
    kind: StemKind
    path: Path
    model: str
    duration_s: float
