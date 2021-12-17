from unittest.mock import patch, Mock, mock_open
from app import (
    menu_input,
    create_new_item,
    load_csv_to_list_of_dict
    )
    
@patch("builtins.input")
def test_menu_input_hp(mock_input: Mock):
    max_menu_index = 5
    mock_input.return_value = 5
    expected = 5
    
    result = menu_input(max_menu_index)
    
    assert result == expected

# Unit Test for create_new_item(item_list, list_name)
@patch("builtins.input")
def test_create_new_item_prod_hp(mock_input: Mock):
    item = {}
    item_list=[{"name": "product_1", "price":10}]
    list_name = "product"
    mock_input.side_effect = ["test_product_name", 1.5]
    expected = [{"name": "product_1", "price":10},{"name": "test_product_name", "price":1.5}]
    
    result = create_new_item(item_list, list_name)
    
    assert result == expected
    
@patch("builtins.input")
def test_create_new_item_cour_hp(mock_input: Mock):
    item = {}
    item_list=[{"name": "courier_1", "phone":88888888}]
    list_name = "courier"
    mock_input.side_effect = ["test_courier_name", 77777777]
    expected = [{"name": "courier_1", "phone":88888888},{"name": "test_courier_name", "phone":77777777}]
    
    result = create_new_item(item_list, list_name)
    
    assert result == expected
    
    

# Unit Test for menu_input(max_menu_index)
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