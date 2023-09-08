# Dr CADIC Philipp @sulfuroid
# Arduino 16 bits image reverse converter
# Usage: python reverseimage.py path_to_your_file.h width height

# USDT (TRC-20): TDbLJ5nTvzbaaSs21Cmf1Lwvhmc5t9W18f . Thanks for your support.


import argparse
from PIL import Image


def parse_data_from_file(filename):
    data = []
    with open(filename, 'r') as f:
        content = f.read()
        
        # Extract data between curly braces
        start = content.find('{')
        end = content.rfind('}')
        content = content[start+1:end].strip()

        for line in content.splitlines():
            # Skip empty lines and comment lines
            line = line.split("//")[0].strip()  # Remove comments
            if not line:
                continue
            data.extend([int(val.strip(), 16) for val in line.split(",") if val.strip()])
            
    return data


def main():
    parser = argparse.ArgumentParser(description="Convert Arduino image array to JPG")
    parser.add_argument("input_file", type=str, help="Path to the Arduino .h file")
    parser.add_argument("width", type=int, help="Width of the image")
    parser.add_argument("height", type=int, help="Height of the image")
    args = parser.parse_args()

    data = parse_data_from_file(args.input_file)

    img = Image.new("RGB", (args.width, args.height))

    for y in range(args.height):
        for x in range(args.width):
            value = data[y * args.width + x]
            r = (value & 0xF800) >> 8
            g = (value & 0x07E0) >> 3
            b = (value & 0x001F) << 3
            img.putpixel((x, y), (r, g, b))

    output_file = args.input_file.replace('.h', '.jpg')
    img.save(output_file)
    print(f"Image saved as {output_file}")

if __name__ == "__main__":
    main()
