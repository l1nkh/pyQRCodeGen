Script that creaetes any number of QRCodes based off an input file.

# QR Code Generator

This is a script that creates QR Codes based off a json file, however it fulfills
a very specific purpose.

The script will require 3 arguments for it to work:
- **Argument 1**: The path of the Json File you will generate the QRCodes from. ```(example: C:/Users/johndoe/Desktop/data.json)```
- **Argument 2**: Argument 2: URL you want to direct the user to. ```(example: www.localhost.com/home)```
- **Argument 3**: Directory where the QRCodes will be saved to. ```(example: C:/Users/johndoe/Desktop)```

**Example:**

  ```py qr_code_generator.py C:/Users/johndoe/Desktop/data.json www.localhost.com/home C:/Users/johndoe/Desktop```

This will output any number of qrcode files into the specified directory.

## Also:

In the current script the Json filed must have this fields:
1. `id`
2. `alt`

Both will serve their purpose as the id will be used to complete the link and the
alternative subscription to complete the qrCode name.

### Json file example:
```json
[
    {
        "id": 1,
        "alt": "Neil Armstrong's Spacesuit",
        "src": "/assets/NeilArmstrong.glb",
        "poster": "/assets/NeilArmstrong.webp",
        "environmentImage": "/assets/moon_1k.hdr"
    },
    {
        "id": 2,
        "alt": "Mars Rover",
        "src": "/assets/MarsRover.glb",
        "poster": "/assets/MarsRover.webp",
        "environmentImage": "/assets/mars_1k.hdr"
    }
]
```