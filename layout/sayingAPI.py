import requests
import random


class SayingAPI:
    def __init__(self, api_key=None):
        self.api_url = "https://api.api-ninjas.com/v1/quotes"
        self.api_key = api_key
        self.saying_data = None
        # Header für API Key
        self.headers = {}
        if self.api_key:
            self.headers['X-Api-Key'] = self.api_key

    def fetch_random_saying(self):
        """Holt einen zufälligen Spruch/Zitat von der API Ninjas Quotes API"""
        try:
            response = requests.get(self.api_url, headers=self.headers)
            if response.status_code == 200:
                self.saying_data = response.json()
                return self.saying_data
            elif response.status_code == 401:
                print("Ungültiger API Key. Verwende Fallback-Sprüche.")
                return None
            elif response.status_code == 429:
                print("Rate Limit erreicht. Verwende Fallback-Sprüche.")
                return None
            else:
                raise Exception(f"API Fehler: Status {response.status_code}")
        except Exception as e:
            print(f"Fehler beim Abrufen der Sprüche: {e}")
            return None

    def get_text_saying(self):
        """Gibt den Text des Spruchs zurück"""
        if self.saying_data and len(self.saying_data) > 0:
            return self.saying_data[0].get('quote', 'Kein Spruch verfügbar')
        return None

    def get_author(self):
        """Gibt den Autor des Spruchs zurück"""
        if self.saying_data and len(self.saying_data) > 0:
            return self.saying_data[0].get('author', 'Unbekannt')
        return None

    def get_random_saying_with_fallback(self):
        """Holt einen zufälligen Spruch oder gibt einen Fallback-Spruch zurück"""
        saying = self.fetch_random_saying()
        if saying:
            return self.get_text_saying()
        else:
            # Fallback-Sprüche falls die API nicht funktioniert
            fallback_sayings = [
                "Der frühe Vogel fängt den Wurm",
                "Alles hat seine Zeit",
                "Geduld ist eine Tugend",
                "Der Weg ist das Ziel",
                "Lachen ist die beste Medizin",
                "Kleine Schritte führen zum Ziel",
                "Jeder Tag ist ein Neuanfang",
                "Vertraue deinem Weg",
                "Zeit heilt alle Wunden",
                "Übung macht den Meister",
                "Reden ist Silber",
                "Wer rastet, der rostet",
                "Ohne Fleiß kein Preis",
                "Besser spät als nie",
                "Gleich und gleich gesellt sich",
                "Wo ein Wille ist, ist ein Weg",
                "Steter Tropfen höhlt Stein",
                "Eile mit Weile",
                "Gemeinsam sind wir stark",
                "Das Glück liegt auf der Straße",
                "Morgenstund hat Gold im Mund",
                "Ein guter Anfang ist die halbe Miete",
                "Der Apfel fällt nicht weit vom Stamm",
                "Man sieht nur mit dem Herzen gut",
                "Das Leben ist kein Ponyhof",
                "Gut Ding will Weile haben",
                "Wer zuletzt lacht, lacht am besten",
                "Ein Bild sagt mehr als tausend Worte",
                "Der Krug geht so lange zum Brunnen",
                "Bis er bricht"
            ]
            return random.choice(fallback_sayings)

    def get_saying_within_limit(self, max_length=32, max_attempts=5):
        """Holt einen Spruch der maximal max_length Zeichen hat"""
        # API Ninjas gibt oft zu lange Zitate zurück
        for attempt in range(max_attempts):
            saying = self.fetch_random_saying()
            if saying:
                text = self.get_text_saying()
                if text and len(text) <= max_length:
                    return text
            
            # Falls API nicht funktioniert oder zu lange Zitate zurückgibt, verwende Fallback-Sprüche
            if attempt == max_attempts - 1:
                fallback_sayings = [
                    "Der frühe Vogel fängt den Wurm",
                    "Alles hat seine Zeit",
                    "Geduld ist eine Tugend",
                    "Der Weg ist das Ziel",
                    "Lachen ist die beste Medizin",
                    "Kleine Schritte führen zum Ziel",
                    "Jeder Tag ist ein Neuanfang",
                    "Vertraue deinem Weg",
                    "Zeit heilt alle Wunden",
                    "Übung macht den Meister",
                    "Reden ist Silber",
                    "Wer rastet, der rostet",
                    "Ohne Fleiß kein Preis",
                    "Besser spät als nie",
                    "Gleich und gleich gesellt sich",
                    "Wo ein Wille ist, ist ein Weg",
                    "Steter Tropfen höhlt Stein",
                    "Eile mit Weile",
                    "Gemeinsam sind wir stark",
                    "Das Glück liegt auf der Straße",
                    "Morgenstund hat Gold im Mund",
                    "Ein guter Anfang ist die halbe Miete",
                    "Der Apfel fällt nicht weit vom Stamm",
                    "Man sieht nur mit dem Herzen gut",
                    "Das Leben ist kein Ponyhof",
                    "Gut Ding will Weile haben",
                    "Wer zuletzt lacht, lacht am besten",
                    "Ein Bild sagt mehr als tausend Worte",
                    "Der Krug geht so lange zum Brunnen",
                    "Bis er bricht"
                ]
                # Wähle einen Fallback-Spruch der die richtige Länge hat
                suitable_fallbacks = [s for s in fallback_sayings if len(s) <= max_length]
                if suitable_fallbacks:
                    return random.choice(suitable_fallbacks)
                else:
                    # Falls alle zu lang sind, kürze den ersten
                    return fallback_sayings[0][:max_length-3] + "..."
        
        return "Kein passender Spruch gefunden."
