from dataclasses import FrozenInstanceError
from pathlib import Path

import pytest

from riff_lab.domain.models import Song, Stem, StemKind


def make_stem(**overrides):
    values = dict(
        song_id="abc123",
        kind=StemKind.GUITAR,
        path=Path("/tmp/guitar.wav"),
        model="htdemucs_6s",
        duration_s=215.4,
    )
    values.update(overrides)
    return Stem(**values)


def test_stems_with_same_values_are_equal():
    assert make_stem() == make_stem()


def test_stems_with_different_kind_are_not_equal():
    assert make_stem() != make_stem(kind=StemKind.DRUMS)


def test_stem_is_immutable():
    stem = make_stem()
    with pytest.raises(FrozenInstanceError):
        stem.model = "other"


def test_song_keeps_its_hash_and_path():
    song = Song(id="abc123", path=Path("song.mp3"))
    assert song.id == "abc123"
    assert song.path == Path("song.mp3")
