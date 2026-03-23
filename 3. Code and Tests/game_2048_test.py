import game_2048

def test_choose_difficulty(capsys):
    game_2048.choose_difficulty()
    out = capsys.readouterr().out

    assert "Choose difficulty:" in out
    assert "1. Easy (6x6)" in out
    assert "2. Medium (5x5)" in out
    assert "3. Hard (4x4)" in out


def test_create_grid():
    grid = game_2048.create_grid(4)

    assert len(grid) == 4
    assert all(len(row) == 4 for row in grid)
    assert all(cell == 0 for row in grid for cell in row)


def test_display_instructions(monkeypatch, capsys):
    monkeypatch.setattr(game_2048, "main_menu", lambda: None)

    monkeypatch.setattr("builtins.input", lambda _: "")

    game_2048.display_intructions()
    out = capsys.readouterr().out

    assert "Use W/A/S/D to move tiles and combine numbers to reach 2048!" in out


def test_main_menu_easy(monkeypatch, capsys):
    inputs = iter(["1", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game_2048.main_menu()
    out = capsys.readouterr().out

    assert "Easy mode selected" in out
    assert "[0, 0, 0, 0, 0, 0]" in out


def test_main_menu_medium(monkeypatch, capsys):
    inputs = iter(["1", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game_2048.main_menu()
    out = capsys.readouterr().out

    assert "Medium mode selected" in out
    assert "[0, 0, 0, 0, 0]" in out


def test_main_menu_hard(monkeypatch, capsys):
    inputs = iter(["1", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game_2048.main_menu()
    out = capsys.readouterr().out

    assert "Hard mode selected" in out
    assert "[0, 0, 0, 0]" in out

def test_main_menu_invalid(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "9")

    game_2048.main_menu()
    out = capsys.readouterr().out

    assert "Invalid choice." in out
