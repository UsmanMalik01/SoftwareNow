from PIL import Image
import numpy as np
import os
import time

# Define the file path for the original image
original_image_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'Assignment-2', 'chapter1.jpg')

# Open the original image
original_image = Image.open(original_image_path)

# Get the size of the image
width, height = original_image.size

# Generate a number (n) based on the current time
current_time = int(time.time())
generated_number = (current_time % 100) + 50

# Create a new blank image with the same size and mode as the original image
new_image = Image.new('RGB', (width, height))

# Iterate over each pixel in the original image
for x in range(width):
    for y in range(height):
        # Get the pixel value at the current position
        r, g, b = original_image.getpixel((x, y))
        
        # Add the generated number to the original pixel values
        r_new = min(r + generated_number, 255)  # Ensure that the value doesn't exceed 255
        g_new = min(g + generated_number, 255)
        b_new = min(b + generated_number, 255)
        
        # Set the pixel value in the new image
        new_image.putpixel((x, y), (r_new, g_new, b_new))

# Save the new image with the name 'chapter1out.png'
output_image_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'Assignment-2', 'chapter1out.png')
new_image.save(output_image_path)

# Calculate the sum of red (r) pixel values in the new image
red_sum = np.sum(np.array(new_image)[:, :, 0])

# Output the sum of red pixel values
print(red_sum)
