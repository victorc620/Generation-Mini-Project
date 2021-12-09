Mini Project Week 2
Now that our app can create and list products, it should be simple enough to do the same for couriers. We'll also dump our data into .txt files so we don't lose it. Try
to ensure code that writes or reads from a text file is separated from the code that prints a list for example.

We'll also add a couple of basic unit tests.

# Goals
As a user I want to:
create a product or courier and add it to a list
view all products or couriers
persist my data
STRETCH I want to be able to update or delete a product or courier
Spec
A product should just be a string containing its name, i.e: "Coke Zero"
A list of products should be a list of strings , i.e: ["Coke Zero"]
A courier should just be a string containing its name, i.e: "John"
A list of couriers should be a list of strings , i.e: ["John"]
Data should be persisted to a .txt file on a new line for each courier or product , ie:
John
Claire
Pseudo Code
LOAD products list from products.txt
LOAD couriers list from couriers.txt
PRINT main menu options
GET user input for main menu option
IF user input is 0:
SAVE products list to products.txt
SAVE couriers list to couriers.txt
EXIT app

# Products menu
ELSE IF user input is 1:
PRINT product menu options
GET user input for product menu option
IF user inputs 0:
RETURN to main menu
ELSE IF user input is 1:
PRINT products list
ELSE IF user input is 2:

# CREATE new product
GET user input for product name
APPEND product name to products list
ELSE IF user input is 3:

# STRETCH GOAL - UPDATE existing product
PRINT product names with its index value
GET user input for product index value
GET user input for new product name
UPDATE product name at index in products list
ELSE IF user input is 4:

# STRETCH GOAL - DELETE product
# STRETCH GOAL - DELETE product
PRINT products list
GET user input for product index value
DELETE product at index in products list

# couriers menu
ELSE IF user input is 2:
PRINT courier menu options
GET user input for courier menu option
IF user inputs 0:
RETURN to main menu
ELIF user inputs 1:
PRINT couriers list
ELSE IF user input is 2:

# CREATE new courier
GET user input for courier name
APPEND courier name to couriers list
ELSE IF user input is 3:

# STRETCH GOAL - UPDATE existing courier
PRINT courier names with its index value
GET user input for courier index value
GET user input for new courier name
UPDATE courier name at index in couriers list
ELSE IF user input is 4:

# STRETCH GOAL - DELETE courier
PRINT courier list
GET user input for courier index value
DELETE courier at index in courier list