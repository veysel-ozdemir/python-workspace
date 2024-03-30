from PIL import Image

# Open the image
image = Image.open("file_name.x")

# Resize the image
new_image = image.resize(size=(500, 500))

# Save the new image
new_image.save("photo.png")
