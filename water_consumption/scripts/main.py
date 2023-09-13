#!/bin/python3
from input_data_parse.input_data_parser import WaterConsumption
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("WebAgg")

watCons = WaterConsumption()

print(watCons.get_flat_in_block("C"))





