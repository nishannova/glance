from config import *
from loader import LoadData
from pre_process import PreProcess
from scanner import ScanBarCode
from loguru import logger
import time
from utils import save_results

import time

def process_doc(file_path = IMG_DIR["raw"], save=False, ui=False, barcode_type="Code128"):
    start_m = time.time()
    barcode_dtls = dict()

    #Caller
    logger.info("\nBEGINING FILE LOADING FROM DIRECTORY")
    start = time.time()
    loader = LoadData(file_path)
    images = loader.process()
    logger.info(f"\nDATA LOADED SUCCESSFULLY IN: {time.time() - start} Secs")


    #Caller
    logger.info("\nBEGINING PRE-PROCESSING OF IMAGES")
    start = time.time()
    pre_process = PreProcess(images)
    processed_images = pre_process.transform(display=False)
    logger.info(f"\nPRE-PROCESSING COMPLETED SUCCESSFULLY IN: {time.time() - start} Secs")

    if save:
        save_results(processed_images, IMG_DIR["processed"])

    #Caller
    logger.info("\nPROCESSING IMAGE-SCANNING ENGINE FOR BARCODE DETECTION")
    start = time.time()
    scanner = ScanBarCode(images, processed_images, barcode_type=barcode_type)
    scanned_images, barcode_dtls = scanner.fit()
    logger.info(f"\nBARCODE DETECTION COMPLETED SUCCESSFULLY IN: {time.time() - start} Secs")
    logger.info(f"\nENTIRE PROCESSING TOOK: {time.time() - start_m}")

    if save:
        save_results(scanned_images, IMG_DIR["scanned"])
    if ui:
        save_results(scanned_images, file_path, ui=True)

    return barcode_dtls
if __name__=='__main__':
    _ = process_doc(save=True)