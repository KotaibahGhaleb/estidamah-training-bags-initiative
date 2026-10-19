from PIL import Image, ImageDraw

img = Image.open("public/الشاشة الختامية - مبادرة الحقائب التدريبية.png").convert("RGB")
w, h = img.size
print("image size:", w, h)

draw = ImageDraw.Draw(img)

# Play button: yellow circle at (50%, 57%) - same spot as the website
cx, cy = int(w * 0.5), int(h * 0.57)
r = int(w * 0.035)  # ~7% of width diameter, matching the site

# circle
draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(250, 204, 21))  # yellow-400

# white triangle, slightly offset right like the site icon
t = r * 0.55
draw.polygon(
    [
        (cx - t * 0.6 + r * 0.08, cy - t),
        (cx - t * 0.6 + r * 0.08, cy + t),
        (cx + t + r * 0.08, cy),
    ],
    fill=(255, 255, 255),
)

img.save("public/intro_with_play.png")
print("saved public/intro_with_play.png")
