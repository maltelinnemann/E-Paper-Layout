from PIL import Image, ImageDraw, ImageFont
import math
import datetime
from layout.layoutEngine import LayoutEngine

# Icons laden 
sunIcon = Image.open("icons/sun.png").convert("1").resize((80, 80), Image.LANCZOS)
rainIcon = Image.open("icons/rain.png").convert("1").resize((80, 80), Image.LANCZOS)
cloudIcon = Image.open("icons/cloud.png").convert("1").resize((80, 80), Image.LANCZOS)


def generate_layout():
    # Display-Größe (z. B. 800x480 für ein 7.5" E-Paper)
    WIDTH, HEIGHT = 800, 480

    # Layout-Engine initialisieren
    layout = LayoutEngine()

    # Farben für E-Paper
    BLACK = 0
    WHITE = 255
    RED = 0  # Wird später separat gerendert, je nach Display-Treiber

    # Neues Bild in Weiß
    img_black = Image.new('1', (WIDTH, HEIGHT), color=WHITE)
    draw = ImageDraw.Draw(img_black)

    img_red = Image.new("1", (WIDTH, HEIGHT), 1)  # 1 = Weiß
    draw_red = ImageDraw.Draw(img_red)

    # Schriftarten laden
    font_large = ImageFont.truetype("fonts/DejaVuSans-Bold.ttf", 46)
    font_medium = ImageFont.truetype("fonts/DejaVuSans.ttf", 38)
    font_small = ImageFont.truetype("fonts/DejaVuSans.ttf", 34)

    
    # Datum
    draw.text((80, 50), textDate(layout), font=font_large, fill=BLACK)

    # Spruch
    draw_red.text((150, 160), textSaying(layout), font=font_medium, fill=RED)
    
    # Trennlinie
    draw.line((20, 240, WIDTH-20, 240), fill=BLACK, width=3)
    draw.line((330, 270, 330, HEIGHT-60), fill=BLACK, width=1)

    # Wetter Heute
    draw.text((120, 270), "Heute", font=font_medium, fill=BLACK)
    draw.text((118, 405), f"{layout.days[0].temperature}°C", font=font_small, fill=BLACK)
    img_red.paste(iconDay(layout.days[0]), (175 - math.ceil(iconDay(layout.days[0]).width / 2), 330 if layout.days[0] == cloudIcon else 310))

    # Wetter Morgen
    draw.text((400, 270), "Morgen", font=font_medium, fill=BLACK)
    draw.text((412, 405), f"{layout.days[1].temperature}°C", font=font_small, fill=BLACK)
    img_red.paste(iconDay(layout.days[1]), (475 - math.ceil(iconDay(layout.days[1]).width / 2), 330 if layout.days[1] == cloudIcon else 310))

    # Wetter Übermorgen
    draw.text((575, 270), layout.days[2].name, font=font_medium, fill=BLACK)
    draw.text((600, 405), f"{layout.days[2].temperature}°C", font=font_small, fill=BLACK)
    img_red.paste(iconDay(layout.days[2]), (655 - math.ceil(iconDay(layout.days[2]).width / 2), 330 if layout.days[2] == cloudIcon else 310))

    # Speichern zur Vorschau
    img_black.save("Images/layout_black.bmp")
    img_red.save("Images/layout_red.bmp")

def textDate(layout):
    month = layout.today[5:7]
    month = translateMonth(month)
    
    return f"{layout.days[0].name}, {layout.today[8:10]}. {month} {layout.today[0:4]}"

def translateMonth(month):
    months = {
        "01": "Januar",
        "02": "Februar",
        "03": "März",
        "04": "April",
        "05": "Mai",
        "06": "Juni",
        "07": "Juli",
        "08": "August",
        "09": "September",
        "10": "Oktober",
        "11": "November",
        "12": "Dezember"
    }
    return months.get(month, month)

def textSaying(layout):
    return layout.saying

def iconDay(day):
    if day.weather == "Clear":
        return sunIcon
    elif day.weather in ["Rain", "Drizzle"]:
        return rainIcon
    elif day.weather in ["Clouds", "Mist", "Fog"]:
        return cloudIcon
    else:
        return "unknown"

if __name__ == "__main__":
    generate_layout()
    print("Layout generated and saved as layout.bmp")

    
    