import os
import sys
from PIL import Image, ImageEnhance, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
INP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "source-photo.jpg")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "source-prepped.png")

img = Image.open(INP).convert("RGBA")
# Convert to grayscale
gray = img.convert("L")
# Increase contrast
enhancer = ImageEnhance.Contrast(gray)
out = enhancer.enhance(1.5)
# If original had alpha, paste onto white
white = Image.new("L", img.size, 255)
white.paste(out, (0, 0), img.split()[3])

white.save(OUT)
print("wrote", OUT)
