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
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from aiogram.dispatcher.filters import BoundFilter
import ast
import hashlib
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
