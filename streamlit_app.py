import streamlit as st
import pandas as pd
import numpy as np
import base64
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
from bs4 import Comment
from PIL import Image
import requests
import re
import plotly as py
import plotly.graph_objects as go
import plotly.express as px
import altair as alt

st.set_page_config(page_title='Hey Batter!', page_icon=':baseball bat:', layout="wide")
