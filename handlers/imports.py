import os
import shutil
from PIL import ImageFont
from PIL import Image, ImageDraw, ImageFont
import random
from colour import color_scale, Color
import numpy
import re
import base64
from uuid import uuid4
import requests as requests
from aiogram import types, md
from dispatcher import dp
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from aiogram.dispatcher.filters import BoundFilter
