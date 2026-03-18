import game_2048

def test_display_instructions(capsys):
    game_2048.display_intructions()  
    out = capsys.readouterr().out
    assert "Use W/A/S/D" in out


# def test_choose_difficulty(capsys):
#     game_2048.choose_difficulty() 
#     out = capsys.readouterr().out
#     assert "Choose difficulty:" in out
#     assert "Easy" in out
#     assert "Medium" in out
#     assert "Hard" in out


# def test_create_grid():
#     grid = game_2048.create_grid(4)
#     assert len(grid) == 4
#     assert all(len(row) == 4 for row in grid)
#     assert all(cell == 0 for row in grid for cell in row)