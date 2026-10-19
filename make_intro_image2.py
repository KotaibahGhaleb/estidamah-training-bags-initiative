from PIL import Image, ImageDraw

img = Image.open(r"C:\Users\ASUS\AppData\Local\Temp\devin-pasted-images\1792387225036506000-12116-0-pasted.jpg").convert("RGB")
w, h = img.size
print("image size:", w, h)

draw = ImageDraw.Draw(img)

cx, cy = int(w * 0.5), int(h * 0.60)
r = int(w * 0.035)

draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(250, 204, 21))

t = r * 0.55
draw.polygon(
    [
        (cx - t * 0.6 + r * 0.08, cy - t),
        (cx - t * 0.6 + r * 0.08, cy + t),
        (cx + t + r * 0.08, cy),
    ],
    fill=(255, 255, 255),
)

img.save("intro_with_play2.png")
print("saved intro_with_play2.png")
