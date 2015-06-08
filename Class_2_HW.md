#Class 2: Command Line and Version Control

1. For chipotle.csv
  1. Each row is an itemized purchase unique to that order, that item and that choice_description. Columns indicate: the id of the order that item+description was a part of (order_id), the quantity of that item+description purchased in that order (quantity), the item name (item_name), the description of choices made for that item broken out into sub-lists for like-choices (choice_description), and the price of that item+description.
  2. 1834 orders
  3. 4623 lines
  4. 368 lines for Steak Burrito, 553 lines for Chicken Burrito, wasn't quite sure how I'd either sum up the quantity ordered or the unique number of orders for each though
  5. 282 lines for Chicken Burrito w/ Black Beans, 105 lines for Chicken Burrito w/ Pinto Beans
2. find . -name *.?sv returns airlines.csv, chipotle.tsv, sms.tsv
3. grep -r -i "dictionary" . | wc -l returns 15 lines
