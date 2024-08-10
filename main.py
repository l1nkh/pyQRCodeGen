import json
import sys
import qrcode

def qr_code_generator(linkCore, name, id):
    qr = qrcode.QRCode(version = 1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size = 20,
                   border = 2)

    qr.add_data(f"http://{linkCore}/{id}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"C:/Users/gogof/Desktop/qrcodes/qrc_{name}_{id}.png")

linkCore = sys.argv[1]
jsonFile = sys.argv[2]

# Open and read the JSON file
with open(jsonFile, 'r') as f:
    data = json.load(f)

for item in data:
    qr_code_generator(linkCore, item['alt'], item['id'])
    print(item['id'])