import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage,HumanMessage
from src.langgraphAgenticAI.ui.uiconfigfile import config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config() #config
        self.user_controls={}