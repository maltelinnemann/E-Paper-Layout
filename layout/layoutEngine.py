import random
from datetime import datetime, timedelta
from layout import day

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
        sayings = [
            "Ein Tag ohne Lächeln ist ein verlorener Tag.",
            "Die beste Zeit für einen Neuanfang ist jetzt.",
            "Lebe jeden Tag, als wäre es dein letzter.",
            "Träume nicht dein Leben, sondern lebe deinen Traum.",
            "Die Zukunft gehört denen, die an die Schönheit ihrer Träume glauben."
        ]
        self.saying = random.choice(sayings)
        return self.saying
    