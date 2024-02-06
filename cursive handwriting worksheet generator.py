from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont

class AlphabetWorksheet:
    def __init__(self):
        self.pdf = FPDF()
        self.letter_images = {}

    def generate_trace_image(self, letter):
        img = Image.new('RGB', (100, 100), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype("LaEl2-vnz4.ttf", 72)  # Ensure you have the correct font
        d.text((1, 1), letter, font=font, fill=(200, 200, 200))  # Light gray for tracing

        filename = f"{letter}_trace.jpg"
        img.save(filename)
        return filename

    def add_page_for_letter(self, letter):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=24)
        # Add the letter
        self.pdf.cell(175, 10, txt=letter, ln=True, align='C')

        # Add the tracing guide
        if letter in self.letter_images:
            for i in range(6):
                trace_image_path = self.letter_images[letter]
                self.pdf.image(trace_image_path, x=20 + 30 * i, y=30, w=30)
        else:
            for i in range(6):
                trace_image_path = self.letter_images.get(letter.upper())
                self.pdf.image(trace_image_path, x=20 + 30 * i, y=30, w=30)

        # Add lines for practice writing
        y_position = 35
        for _ in range(2):
            self.pdf.line(10, y_position, 200, y_position)
            y_position += 7

        y_position = 50
        for _ in range(2):
            self.pdf.line(10, y_position, 200, y_position)
            y_position += 6

        y_position = 75
        for _ in range(8):
            for _ in range(4):
                self.pdf.line(10, y_position, 200, y_position)
                y_position += 4
            y_position += 10

    def generate_worksheet(self, filename="alphabet_worksheet.pdf"):
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            self.letter_images[letter] = self.generate_trace_image(letter)
            self.add_page_for_letter(letter)
        self.pdf.output(filename)

# Usage
worksheet = AlphabetWorksheet()
worksheet.generate_worksheet()