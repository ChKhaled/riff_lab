from pathlib import Path

from riff_lab.services.hashing import HASH_TRUNCATE_LENGTH, hash_file


def write(path: Path, content: bytes) -> Path:
    path.write_bytes(content)
    return path


def test_same_content_different_name_gives_same_hash(tmp_path):
    a = write(
        tmp_path / "sample.wav", b"some audio bytes"
    )  # why not concat tmp with new
    b = write(tmp_path / "renamed_sample.wav", b"some audio bytes")

    assert hash_file(a) == hash_file(b)


def test_different_content_give_different_hash(tmp_path):
    a = write(
        tmp_path / "sample.wav", b"some audio bytes"
    )  # why not concat tmp with new
    b = write(tmp_path / "another_sample.wav", b" some others audio bytes")

    assert not hash_file(a) == hash_file(b)


def test_empty_file_gives_a_valid_hash(tmp_path):
    empty = write(tmp_path / "empty.wav", b"")
    result = hash_file(empty)
    assert len(result) == HASH_TRUNCATE_LENGTH


def test_hash_has_the_expected_length(tmp_path):
    f = write(tmp_path / "sample.wav", b"abc")
    assert len(hash_file(f)) == HASH_TRUNCATE_LENGTH


def test_chunk_size_does_not_change_the_result(tmp_path):
    f = write(tmp_path / "sample.mp3", b"0123456789" * 50)  # 500 bytes
    assert hash_file(f, chunk_size=4) == hash_file(f)


def test_same_file_hashed_twice_is_stable(tmp_path):
    f = write(tmp_path / "sample.wav", b"abc")
    assert hash_file(f) == hash_file(f)
