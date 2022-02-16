from utils import *

# This will goto Config
TRANSFORM_MAP = {
    "RGB_to_grey": convert_grey,
    "morph": morph,
    "sharpen": sharpen_image,
    "Binarize": binarize,
}

#THIS SHOULD GOTO CONFIG
SCANNER_ENGINE = {
    "pyzbar": transform_zbar,
    "opencv": transform_cv,
    

}

IMAGE_PATH = "../images"

IMG_DIR = {
    "raw": "../images/raw",
    "processed": "../images/processed",
    "transformed": "../images/transformed",
    "scanned": "../images/scanned",
}