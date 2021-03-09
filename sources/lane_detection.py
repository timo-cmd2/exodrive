import cv2
import numpy as np
import math
from datetime import datetime
from matplotlib import pyplot as plt
from collections import deque
from scipy.stats  import mode
from scipy.optimize import curve_fit
from yolo_model import BoundBox

# abstract definitions
WHITE = (255, 255, 255)
YELLOW = (66, 244, 238)
GREEN = (80, 220, 60)
LIGHT_CYAN = (255, 255, 224)
DARK_BLUE = (139, 0, 0)
GRAY = (128, 128, 128)
BLUE = (255,0,0)
RED = (0,0,255)
ORANGE =(0,165,255)
BLACK =(0,0,0)
vehicles = [1,2,3,5,6,7,8]
animals =[15,16,17,18,19,21,22,23,]
humans =[0]
