import argparse
from PIL import Image


def parse_data_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Diviser le contenu en utilisant "const unsigned short"
    sections = content.split("const unsigned short")[1:]

    images = []

    for section in sections:
        # Extraire le nom de l'image
        image_name = section.split("PROGMEM")[0].split("[")[0].strip()

        # Extraire les données entre les accolades
        start = section.find('{')
        end = section.find('}')
        data_section = section[start+1:end].strip()

        data = []

        for line in data_section.splitlines():
            # Supprimer les commentaires et traiter chaque valeur
            line = line.split("//")[0].strip()
            if not line:
                continue
            data.extend([int(val.strip(), 16) for val in line.split(",") if val.strip()])

        images.append((image_name, data))

    return images


def main():
    parser = argparse.ArgumentParser(description="Convert Arduino image arrays to JPGs")
    parser.add_argument("input_file", type=str, help="Path to the Arduino .h file containing multiple images")
    parser.add_argument("width", type=int, help="Width of the images")
    parser.add_argument("height", type=int, help="Height of the images")
    args = parser.parse_args()

    image_sections = parse_data_from_file(args.input_file)

    for image_name, data in image_sections:
        img = Image.new("RGB", (args.width, args.height))

        for y in range(args.height):
            for x in range(args.width):
                value = data[y * args.width + x]
                r = (value & 0xF800) >> 8
                g = (value & 0x07E0) >> 3
                b = (value & 0x001F) << 3
                img.putpixel((x, y), (r, g, b))

        output_file = f"{image_name}.jpg"
        img.save(output_file)
        print(f"Image saved as {output_file}")

if __name__ == "__main__":
    main()
