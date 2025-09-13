
import platform

import google.generativeai as genai
from .config.api_config import API_KEY, AI_MODEL

class DesktopAssistant:
    def __init__(self):
        self.perception = Perception()
        self.gemini = Gemini(api_key=API_KEY, model=AI_MODEL)

    def _execute_plan(self, plan):
        print(f"Executing plan: {plan}")

class Perception:
    def __init__(self):
        self.latest_text_boxes = []

class Gemini:
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model
        genai.configure(api_key=self.api_key)

    def generate_plan(self, command, context):
        prompt = f"You are a helpful assistant. Your goal is to generate a plan to execute a command given by the user. The user command is: '{command}'. The context is: {context}. Please generate a plan as a list of strings, where each string is a command to be executed. If no plan is needed, return an empty string."
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(prompt)
        plan = response.text.strip().split('\n')
        if plan == ['']:
            return None
        return plan

    def generate_text(self, command):
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(f"You are a helpful assistant. The user command is: '{command}'. Please generate a conversational response.")
        return response.text.strip()

