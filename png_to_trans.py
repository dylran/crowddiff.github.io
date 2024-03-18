from PIL import Image

def convert_white_to_transparent(image_path, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to RGBA if it's not already in that mode
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Get the image data
    img_data = img.getdata()

    # Create a new image data list with transparency
    new_data = []
    for item in img_data:
        # Replace white pixels with transparent pixels
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            new_data.append((255, 255, 255, 0))  # Set alpha to 0 (transparent)
        else:
            new_data.append(item)

    # Update image data
    img.putdata(new_data)

    # Save the image with transparency
    img.save(output_path, "PNG")

# Example usage:
input_image_path = "/data/crowdiff.github.io/static/images/jhu_web.png"
output_image_path = "/data/crowdiff.github.io/static/images/trans_jhu_web.png"
convert_white_to_transparent(input_image_path, output_image_path)
