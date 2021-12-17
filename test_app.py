from unittest.mock import patch, Mock, mock_open
from app import (
    menu_input, 
    load_csv_to_list_of_dict
    )

def menu_input(max_menu_index):
    while True:
        try:
            action = int(input("Enter your action: "))
            if action>max_menu_index:
                raise Exception
        except Exception:
            print("\nERROR: Please enter an valid action")
            continue
        return action
    
@patch("builtins.input")
def test_menu_input_hp(mock_input: Mock):
    max_menu_index = 5
    mock_input.return_value = 5
    expected = 5
    
    result = menu_input(max_menu_index)
    
    assert result == expected

@patch("builtins.input")
def test_menu_input_uhp(mock_input: Mock):
    max_menu_index = 5
    mock_input.side_effect = [7,5]
    expected = 5
    
    result = menu_input(max_menu_index)
    
    assert result == expected
    assert mock_input.call_count == 2
    
@patch("builtins.open", new_callable=mock_open, read_data="test\n0")
def test_load_csv_to_list_of_dict(mock_open):
    expected = [{'test': '0'}]
    result = load_csv_to_list_of_dict("file_name")
    assert expected == result
    
# @patch("builtins.open", new_callable=mock_open, read_data="data")
# def test_patch(mock_file):
#     assert open("path/to/open").read() == "data"
#     mock_file.assert_called_with("path/to/open")
    

# with patch("builtins.open", mock_open(read_data="data")) as mock_file:
#     assert open("path/to/open").read() == "data"
# mock_file.assert_called_with("path/to/open")