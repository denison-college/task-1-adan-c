import random
import pytest
import builtins
import game_2048

# TEST display_instructions
def test_display_instructions(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr(builtins, "input", lambda _: "")
    game_2048.display_instructions()

    output = capsys.readouterr().out
    assert "Use W/A/S/D to move tiles" in output

# TEST choose_difficulty
def test_choose_difficulty_easy(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    monkeypatch.setattr(builtins, "input", lambda _: "1")
    result = game_2048.choose_difficulty()
    output = capsys.readouterr().out

    assert "Easy" in output
    assert result == 6


def test_choose_difficulty_medium(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    monkeypatch.setattr(builtins, "input", lambda _: "2")
    result = game_2048.choose_difficulty()
    output = capsys.readouterr().out

    assert "Medium" in output
    assert result == 5


def test_choose_difficulty_hard(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    monkeypatch.setattr(builtins, "input", lambda _: "3")
    result = game_2048.choose_difficulty()
    output = capsys.readouterr().out

    assert "Hard" in output
    assert result == 4


def test_choose_difficulty_invalid(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    monkeypatch.setattr(builtins, "input", lambda _: "x")
    result = game_2048.choose_difficulty()
    output = capsys.readouterr().out

    assert "Invalid difficulty" in output
    assert result is None

# TEST create_grid
def test_create_grid_size():
    size = 4
    grid = game_2048.create_grid(size)
    assert len(grid) == size
    assert all(len(row) == size for row in grid)


def test_create_grid_initial_values():
    size = 3
    grid = game_2048.create_grid(size)
    assert all(cell == 0 for row in grid for cell in row)

# TEST show()
def test_show_output(capsys: pytest.CaptureFixture[str]):
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
    ]

    for line in expected_lines:
        assert line in captured

# TEST merge_left
def test_merge_left_simple():
    row, score = game_2048.merge_left([2, 2, 0, 0])
    assert row == [4, 0, 0, 0]
    assert score == 4


def test_merge_left_double_merge():
    row, score = game_2048.merge_left([2, 2, 4, 4])
    assert row == [4, 8, 0, 0]
    assert score == 12


def test_merge_left_no_merge():
    row, score = game_2048.merge_left([2, 4, 8, 16])
    assert row == [2, 4, 8, 16]
    assert score == 0

# TEST move()
def test_move_left():
    board = [
        [2, 2, 0, 0],
        [4, 0, 4, 0],
        [2, 2, 2, 2],
        [0, 0, 0, 0]
    ]
    new_board, score = game_2048.move(board, "left")

    assert new_board == [
        [4, 0, 0, 0],
        [8, 0, 0, 0],
        [4, 4, 0, 0],
        [0, 0, 0, 0]
    ]
    assert score == 20


def test_move_right():
    board = [
        [2, 2, 0, 0],
        [4, 0, 4, 0]
    ]
    new_board, score = game_2048.move(board, "right")

    assert new_board == [
        [0, 0, 0, 4],
        [0, 0, 0, 8]
    ]
    assert score == 12

# TEST moves_available()
def test_moves_available_true():
    board = [
        [2, 4, 8],
        [16, 32, 64],
        [128, 128, 256]
    ]
    assert game_2048.moves_available(board) is True


def test_moves_available_false():
    board = [
        [2, 4, 8],
        [16, 32, 64],
        [128, 256, 512]
    ]
    assert game_2048.moves_available(board) is False

#   TEST show()
def test_show_output(capsys):
    board = [
        [2, 4, 0],
        [0, 8, 16],
        [32, 0, 64]
    ]
    score = 100

    game_2048.show(board, score)
    captured = capsys.readouterr().out

    assert "Score: 100" in captured
    assert "   2    4    0" in captured
    assert "   0    8   16" in captured
    assert "  32    0   64" in captured

#   TEST add()
def test_add_places_tile(monkeypatch):
    board = [
        [2, 4, 0],
        [0, 0, 16],
        [32, 0, 64]
    ]

    monkeypatch.setattr(random, "choice", lambda x: (1, 1))

    game_2048.add(board)

    assert board[1][1] == 2


def test_add_no_empty_spaces():
    board = [
        [2, 4, 8],
        [16, 32, 64],
        [128, 256, 512]
    ]

    before = [row[:] for row in board]
    game_2048.add(board)

    assert board == before