# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# connecting to mysql database 
import mysql.connector


class CattreatsPipeline:
    
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)
        
        # Extract and convert 'price' field to float
        price_key = 'price_usd'
        price_value = adapter.get(price_key)

        # Check if price is available and not empty
        if price_value:
            # Remove '$' and convert to float
            price_value = price_value.replace('$', '')

            try:
                # Convert the substring to a float
                adapter[price_key] = float(price_value)
            except ValueError:
                print(f"Invalid price format for item {item}")
        else:
            adapter[price_key] = '0.0'
        
        # Extract and convert 'rating' field to float
        rating_key = 'ratings'
        rating_string = adapter.get(rating_key)

        # Find the position of the first space in the string
        first_space_index = rating_string.find(' ')

        if first_space_index != -1:
            # Extract the numeric rating substring and strip any leading/trailing spaces
            rating_str = rating_string[:first_space_index].strip()

            try:
                # Convert the substring to a float
                rating_float = float(rating_str)
                adapter[rating_key] = rating_float
            except ValueError:
                print(f"Invalid numeric rating format for item {item}")
        else:
            adapter[rating_key] = 0.0
            
        # See if there are stocks in a specific item by looking at their label. 
        label_key = 'product_labels'
        label_value = adapter.get(label_key)

        if label_value:
            # Put the label value to the data handler. 
            adapter[label_key] = label_value
        else:
            adapter[label_key] = 'Cat Treats'
            
        # Ingredient formula. 
        formula_key = 'ingredient_formula'
        formula_value = adapter.get(formula_key)

        if formula_value:
            # Put the label value to the data handler. 
            adapter[formula_key] = formula_value
        else:
            adapter[formula_key] = 'Not Provided'
        
        return item
    

class ScrapeToSQL:
    
    # initially create the table to an existing database. 
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'welcome123', #add your password here if you have one set 
            database = 'ScrapingScrapy'
        )
        
        # to execute commands
        self.cur = self.conn.cursor()
        
        # create table for cat treats 
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS cat_treats (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(255),
                price_usd FLOAT,
                brand_name VARCHAR(255),
                ratings FLOAT,
                product_labels VARCHAR(255),
                ingredient_formula TEXT
            )
        """)
    
    # inserting the scraped data to the database. 
    def process_item(self, item, spider):
        
        # Define insert statement
        self.cur.execute("""
            INSERT INTO cat_treats (
                product_name,
                price_usd,
                brand_name,
                ratings,
                product_labels,
                ingredient_formula
            ) VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )""", (
            item["product_name"],
            item["price_usd"],
            item["brand_name"],
            item["ratings"],
            item["product_labels"],
            item["ingredient_formula"]
        ))
        
        # Commit the changes after executing the query
        self.conn.commit()
        return item

    # closing the database execution. 
    def close_spider(self, spider):
        
        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()