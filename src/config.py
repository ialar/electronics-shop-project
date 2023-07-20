# -*- coding: utf-8 -*-
import os

CSV_PATH_1 = os.path.dirname(os.path.abspath(__file__)) + '/items.csv'  # верный файл
CSV_PATH_2 = os.path.dirname(os.path.abspath(__file__)) + '/item.csv'  # отсутствующий файл
CSV_PATH_3 = os.path.dirname(os.path.abspath(__file__)) + '/corrupted_item.csv'  # поврежденный файл
