from PIL import Image, ImageDraw, ImageFont
import math

def generate_layout():
    # Display-Größe (z. B. 800x480 für ein 7.5" E-Paper)
    WIDTH, HEIGHT = 800, 480

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
    font_large = ImageFont.truetype("fonts/DejaVuSans-Bold.ttf", 42)
    font_medium = ImageFont.truetype("fonts/DejaVuSans.ttf", 32)
    font_small = ImageFont.truetype("fonts/DejaVuSans.ttf", 26)

    # Icons laden 
    sunIcon = Image.open("icons/sun.png").convert("1").resize((70, 70), Image.LANCZOS)
    rainIcon = Image.open("icons/rain.png").convert("1").resize((70, 70), Image.LANCZOS)
    cloudIcon = Image.open("icons/cloud.png").convert("1").resize((70, 70), Image.LANCZOS)
    
    # Datum
    draw.text((80, 50), "Sonntag, 8. Juni 2025", font=font_large, fill=BLACK)

    # Spruch
    draw_red.text((230, 160), "„Grillen, Chillen, Kiste killen“", font=font_medium, fill=RED)

    # Trennlinie
    draw.line((20, 240, WIDTH-20, 240), fill=BLACK, width=3)
    draw.line((330, 270, 330, HEIGHT-60), fill=BLACK, width=1)

    # Wetter Heute
    draw.text((125, 270), "Heute", font=font_medium, fill=BLACK)
    draw.text((100, 400), "20,1°C   90%", font=font_small, fill=BLACK)
    img_red.paste(sunIcon, (165 - math.ceil(sunIcon.width / 2), 320))

    # Wetter Morgen
    draw.text((400, 270), "Morgen", font=font_medium, fill=BLACK)
    draw.text((418, 400), "16,1°C", font=font_small, fill=BLACK)
    img_red.paste(cloudIcon, (455 - math.ceil(cloudIcon.width / 2), 310))

    # Wetter Übermorgen
    draw.text((575, 270), "Dienstag", font=font_medium, fill=BLACK)
    draw.text((600, 400), "25,9°C", font=font_small, fill=BLACK)
    img_red.paste(rainIcon, (638 - math.ceil(rainIcon.width / 2), 320))

    # Speichern zur Vorschau
    img_black.save("Images/layout_black.bmp")
    img_red.save("Images/layout_red.bmp")

if __name__ == "__main__":
    generate_layout()
    print("Layout generated and saved as layout.bmp")
