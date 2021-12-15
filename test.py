item_index_string = str(input("Enter list of product index values (seperated with comma): "))
index_list = item_index_string.split(",")
order_item_list =  [index.strip() for index in item_index_string.split(",")]
print(order_item_list)