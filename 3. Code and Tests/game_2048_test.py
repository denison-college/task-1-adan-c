import game_2048
import pytest

# TEST display_instructions()
def test_display_instructions(monkeypatch, capsys):
    monkeypatch.setattr(builtins, "input", lambda _: "")

    display_instructions()

    output = capsys.readouterr().out

    assert "Use W/A/S/D to move tiles" in output
    assert "Press Enter to return to the menu" in output


# TEST choose_difficulty()
def test_choose_difficulty_easy(monkeypatch, capsys):
    monkeypatch.setattr(builtins, "input", lambda _: "1")
    result = choose_difficulty()
    output = capsys.readouterr().out

    assert "Easy" in output
    assert result == 6


def test_choose_difficulty_medium(monkeypatch, capsys):
    monkeypatch.setattr(builtins, "input", lambda _: "2")
    result = choose_difficulty()
    output = capsys.readouterr().out

    assert "Medium" in output
    assert result == 5


def test_choose_difficulty_hard(monkeypatch, capsys):
    monkeypatch.setattr(builtins, "input", lambda _: "3")
    result = choose_difficulty()
    output = capsys.readouterr().out

    assert "Hard" in output
    assert result == 4


def test_choose_difficulty_invalid(monkeypatch, capsys):
    monkeypatch.setattr(builtins, "input", lambda _: "x")
    result = choose_difficulty()
    output = capsys.readouterr().out

    assert "Invalid difficulty" in output
    assert result is None