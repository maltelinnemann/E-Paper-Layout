import random
from datetime import datetime, timedelta
from layout import day
from layout.sayingAPI import SayingAPI

class LayoutEngine:
    def __init__(self):
        self.today = self.set_date()
        self.saying = self.set_saying()
        self.days = self.set_days()
    
    def set_date(self):
        self.today = datetime.now().strftime("%Y-%m-%d")
        return self.today
    
    def set_days(self, days=3):
        if hasattr(self, 'days') and self.days:
            return self.days
        
        day_instance = None
        self.days = []
        for i in range(days):
            day_date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
            self.days.append(day.day(day_date))
        
        return self.days
    
    def set_saying(self):
        if not hasattr(self, 'saying_api'):
            self.saying_api = SayingAPI(api_key="dilJLfYptrHC1hrJrug9mA==6a2h3hNBOQC5FkLI")
        self.saying = self.saying_api.get_saying_within_limit(max_length=32)
        return self.saying
    