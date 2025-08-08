import telebot      #ИМПОРТ БИБЛИОТЕКИ telebot
from random import randint
from datetime import datetime
import time
import random
import tensorflow
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image, imageOps
import numpy as np
from keras.models import load_model
import requests



token = "7393376401:AAFaZT6JLWB92S3i2Xu0PowykzJ9XKsVQLc"    #API-ТОКЕН ВАШЕГО БОТА ИЗ BOTFATHER

bot = telebot.TeleBot(token, parse_mode=None)
attempts = 0
