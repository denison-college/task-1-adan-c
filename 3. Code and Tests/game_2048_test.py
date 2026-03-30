from pytest import CaptureFixture, MonkeyPatch

import game_2048
import builtins

# TEST display_instructions
def test_display_instructions(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]) -> None:
    monkeypatch.setattr(builtins, "input", lambda _: "Use W/A/S/D to move tiles")

    game_2048.display_instructions()

    output = capsys.readouterr().out

    assert "Use W/A/S/D to move tiles" in output
   

# TEST choose_difficulty
def test_choose_difficulty_easy(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]):
    monkeypatch.setattr(builtins, "input", lambda _: "1")
    result = game_2048.choose_difficulty()
    output = capsys.readouterr().out

    assert "Easy" in output
    assert result == 6


def test_choose_difficulty_medium(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]):
    monkeypatch.setattr(builtins, "input", lambda _: "2")
    result = game_2048.choose_difficulty()
    output = capsys.readouterr().out

    assert "Medium" in output
    assert result == 5


def test_choose_difficulty_hard(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]):
    monkeypatch.setattr(builtins, "input", lambda _: "3")
    result = game_2048.choose_difficulty()
    output = capsys.readouterr().out

    assert "Hard" in output
    assert result == 4


def test_choose_difficulty_invalid(monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]):
    monkeypatch.setattr(builtins, "input", lambda _: "x")
    result = game_2048.choose_difficulty()
    output = capsys.readouterr().out

    assert "Invalid difficulty" in output
    assert result is None

def test_create_grid_size():
    size = 4
    grid = game_2048.create_grid(size)
    assert len(grid) == size
    assert all(len(row) == size for row in grid)


def test_create_grid_initial_values():
    size = 3
    grid = game_2048.create_grid(size)
    for row in grid:
        assert all(cell == 0 for cell in row)


def test_show_output(capsys: CaptureFixture[builtins.str]):
    board = [
        [0, 2, 4],
        [8, 16, 32],
        [64, 128, 256]
    ]
    score = 100

    game_2048.show(board, score)
    captured = capsys.readouterr().out

    expected_lines = [
        "Score: 100",
        "   0    2    4",
        "   8   16   32",
        "  64  128  256",
        ""
    ]

    for line in expected_lines:
        assert line in captured