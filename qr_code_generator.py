import json
import sys
import qrcode
import os

def qr_code_generator(url, name, id):
    qr = qrcode.QRCode(version = 1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size = 20,
                   border = 2)

    qr.add_data(f"http://{url}/{id}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    img.save(os.path.join(output_directory, f"qrc_{name}_{id}.png"))

def instructions():
    print(" ")
    print(" ")
    print("|||||||||||||||INSTRUCTIONS|||||||||||||||")
    print("To generate a QRCode for a 3D Module from a Json file you need give the input arguments:")
    print("Argument 1: The path of the Json File you will generate the QRCodes from. (example: C:/Users/johndoe/Desktop/data.json)")
    print("Argument 2: URL you want to direct the user to. (example: www.localhost.com/home)")
    print("Argument 3: Directory where the QRCodes will be saved to. (example: C:/Users/johndoe/Desktop)")
    print("Example:")
    print("  py script.py C:/Users/johndoe/Desktop/data.json www.localhost.com/home C:/Users/johndoe/Desktop")

if len(sys.argv) != 4:
    instructions()
    sys.exit(1)

jsonFile = sys.argv[1]
url = sys.argv[2]
output_directory = sys.argv[3]

# Open and read the JSON file
with open(jsonFile, 'r') as f:
    data = json.load(f)

for item in data:
    qr_code_generator(url, item['alt'], item['id'])
    print(item['id'])