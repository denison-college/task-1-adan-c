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
        
# merge_left tests
def test_merge_left_simple():
    row, score = game_2048.merge_left([2, 2, 0, 0])
    assert row == game_2048.merge_left([4, 0, 0, 0])
    assert score == 4

def test_merge_left_double_merge():
    row, score = game_2048.merge_left([2, 2, 4, 4])
    assert row == [4, 8, 0, 0]
    assert score == 12

def test_merge_left_no_merge():
    row, score = game_2048.merge_left([2, 4, 8, 16])
    assert row == [2, 4, 8, 16]
    assert score == 0
    

# move tests
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
    assert score == (4 + 8 + 4)

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
    assert score == (4 + 8)

# moves_available tests
def test_moves_available_true():
    board = [
        [2, 4, 8],
        [16, 32, 64],
        [128, 128, 256]
    ]
    assert game_2048.moves_available(board) is True
game_2048.moves_available
def test_moves_available_false():
    board = [
        [2, 4, 8],
        [16, 32, 64],
        [128, 256, 512]
    ]
    assert game_2048.moves_available(board) is False