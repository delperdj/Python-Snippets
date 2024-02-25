# Ascii


from PIL import Image

def image_to_ascii(image_path, output_width=100):
    # ASCII characters used to build the output
    ascii_chars = "@%#*+=-:. "
    
    # Load the image
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {e}")
        return
    
    # Convert image to grayscale
    image = image.convert("L")
    
    # Resize image according to the desired output width
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(output_width * aspect_ratio / 2)  # Dividing by 2 to compensate for characters' height in console
    image = image.resize((output_width, new_height))
    
    # Convert image to ASCII
    pixels = image.getdata()
    ascii_str = ''.join([ascii_chars[pixel//len(ascii_chars)] for pixel in pixels])  # Map each pixel to an ASCII char
    
    # Split the string based on width to create lines
    img_ascii = [ascii_str[index:index+output_width] for index in range(0, len(ascii_str), output_width)]
    
    # Print the ASCII art
    return "\n".join(img_ascii)

# Example usage
image_path = "image.jpg"  # Replace with the path to your JPEG image
ascii_art = image_to_ascii(image_path, 100)
print(ascii_art)
