import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from loguru import logger
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import ZBarSymbol
from google.colab.patches import cv2_imshow
import imutils
from kraken import binarization
from PIL import Image