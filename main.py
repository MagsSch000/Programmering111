from PIL import Image, ImageEnhance

dog = Image.open("dog.jpg")

# Steg 1: Gör svartvit
bw_dog = dog.convert("L")

# Steg 2: Höj kontrasten
hc_dog = ImageEnhance.Contrast(bw_dog).enhance(1.4)

# Steg 3: Minska ljusheten (brightness)
emo_dog = ImageEnhance.Brightness(hc_dog).enhance(0.6)

# Steg 4: Spara bilden
emo_dog.save("emo_dog.jpg")
