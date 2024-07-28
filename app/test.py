import unittest
import pandas as pd

class TestOrderAnalysis(unittest.TestCase):
    def setUp(self):
        self.orders = pd.read_csv('olist_order_items_dataset.csv')
      
        # Ensure shipping_limit_date is converted to datetime
        self.orders['shipping_limit_date'] = pd.to_datetime(self.orders['shipping_limit_date'])
        
        self.orders['year_month'] = self.orders['shipping_limit_date'].dt.to_period('M')
    
    def test_monthly_revenue(self):
        monthly_revenue = self.orders.groupby('year_month')['price'].sum().reset_index()
        self.assertFalse(monthly_revenue.empty, "Monthly revenue dataframe is empty")
    
    def test_product_revenue(self):
        # Assuming order_item_id is the quantity of the items
        self.orders['total_revenue'] = self.orders['price'] * self.orders['order_item_id']
        product_revenue = self.orders.groupby('product_id')['total_revenue'].sum().reset_index()
        self.assertFalse(product_revenue.empty, "Product revenue dataframe is empty")
    
if __name__ == '__main__':
    unittest.main()
