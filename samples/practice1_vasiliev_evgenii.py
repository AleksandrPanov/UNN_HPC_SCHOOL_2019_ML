import sys
import cv2
import logging as log
import argparse

sys.path.append('../src')
from imagefilter import ImageFilter

def build_argparse():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'your input \
            parameter (image, video, etc)', type = str)
    #
    # Add your code here
    #
    
    return parser

def main():
    log.basicConfig(format="[ %(levelname)s ] %(message)s", 
                             level=log.INFO, stream=sys.stdout)
    log.info("Hello image filtering")
    args = build_argparse().parse_args()
    
    imagePath = args.input
    
    log.info(imagePath)
    
    image_source = cv2.imread(imagePath)
    
    log.info(image_source.shape)
    
    myfilter = ImageFilter(gray = True, shape = (100, 100))
    
    
    image_final = myfilter.process_image(image_source)
    
    cv2.imshow("Original image", image_final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #
    # Add your code here
    #
    
    return
    
if __name__ == '__main__':
    sys.exit(main())