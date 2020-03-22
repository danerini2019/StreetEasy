import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import scipy as stats

brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

