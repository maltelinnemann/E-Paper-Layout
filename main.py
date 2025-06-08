import logging
from PIL import Image
import os
import sys
from lib import epd7in5b_V2

def display_image(black_image_path, red_image_path):
    import logging
    from PIL import Image
    from lib import epd7in5b_V2

    # Initialize the display
    epd = epd7in5b_V2.EPD()
    epd.init()
    logging.info("init and Clear")
    epd.Clear()

    # Lade die fertigen Schwarz- und Rotbilder
    black_image = Image.open(black_image_path).convert("1").resize((epd.width, epd.height), Image.LANCZOS)
    red_image = Image.open(red_image_path).convert("1").resize((epd.width, epd.height), Image.LANCZOS)

    # Zeige beide Layer an
    epd.display(epd.getbuffer(black_image), epd.getbuffer(red_image))
    logging.info("Image displayed")


if __name__ == '__main__':
    display_image("Images/layout_black.bmp", "Images/layout_red.bmp");