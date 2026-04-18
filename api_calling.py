from google import genai
from dotenv import load_dotenv
import os

# 🔹 Load environment variables
load_dotenv()
my_api_key = os.getenv("GENAI_API_KEY")

# 🔹 Create Gemini client
client = genai.Client(api_key=my_api_key)


# 🔹 Prompt Builder
def build_prompt(selected_option):

    base_prompt = """
You are an expert software debugger and coding assistant.

A user has uploaded a screenshot of a code error.

Your tasks:
1. Identify the programming language.
2. Extract the error message from the image.
3. Explain the error in simple terms.
4. Identify the root cause of the problem.
"""

  
    if selected_option == "Hints":
        return base_prompt + """
Only provide a short hint to solve the issue.
Do NOT provide full solution or code.

### 🧠 Hint:
"""

    
    else:
        return base_prompt + """
Provide full explanation and corrected code.

### 🔍 Error Explanation:
### ⚠️ Root Cause:
### 💡 Solution:
### ✅ Correct Code:
"""


# 🔹 Main API Function
def note_generator(image, selected_option):

    prompt = build_prompt(selected_option)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt, image]   # ✅ correct order
    )

    return response.text