from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 啟用 CORS

load_dotenv()

# 配置 API 密鑰
API_KEY = os.getenv("GEMINI_API_KEY")

# 添加路由來提供 HTML 頁面
@app.route('/')
def index():
    return render_template('index.html')

def generate_text(prompt):
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        
        headers = {
            "Content-Type": "application/json"
        }
        
        params = {
            "key": API_KEY
        }
        
        data = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.9,
                "topP": 1,
                "topK": 1,
                "maxOutputTokens": 2048
            }
        }
        
        response = requests.post(url, headers=headers, params=params, json=data)
        response.raise_for_status()
        
        result = response.json()
        if "candidates" in result:
            return {"success": True, "text": result["candidates"][0]["content"]["parts"][0]["text"]}
        else:
            return {"success": False, "error": "Unexpected response format"}
            
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": f"API request failed: {str(e)}"}
    except json.JSONDecodeError as e:
        return {"success": False, "error": f"Failed to parse response: {str(e)}"}
    except Exception as e:
        return {"success": False, "error": f"Unexpected error: {str(e)}"}

@app.route('/generate', methods=['POST'])
def generate():
    if not API_KEY:
        return jsonify({"success": False, "error": "GEMINI_API_KEY not found"}), 500
    
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"success": False, "error": "No prompt provided"}), 400
    
    result = generate_text(data['prompt'])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)


# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # 配置 API 密鑰
# API_KEY = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=API_KEY)

# def generate_text(prompt):
#     try:
#         # 使用指定的模型
#         model = genai.GenerativeModel("gemini-2.0-flash")
        
#         # 設置生成參數
#         generation_config = {
#             "temperature": 0.9,
#             "top_p": 1,
#             "top_k": 1,
#             "max_output_tokens": 2048,
#         }
        
#         # 生成回應
#         response = model.generate_content(
#             prompt,
#             generation_config=generation_config
#         )
        
#         # 檢查回應是否成功
#         if response:
#             return response.text
#         else:
#             print("Empty response received")
#             return None
            
#     except Exception as e:
#         print(f"Error generating content: {str(e)}")
#         return None

# if __name__ == "__main__":
#     if not API_KEY:
#         print("Error: GEMINI_API_KEY not found in environment variables")
#         exit(1)
        
#     prompt = "Write a short poem about the moon."
#     result = generate_text(prompt)
#     if result:
#         print("\nGenerated Text:")
#         print("--------------")
#         print(result)
#     else:
#         print("Failed to generate text")


# import requests
# import os
# from dotenv import load_dotenv
# import json

# load_dotenv()

# # 配置 API 密鑰
# API_KEY = os.getenv("GEMINI_API_KEY")

# def generate_text(prompt):
#     try:
#         # 使用正確的 API endpoint
#         url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        
#         headers = {
#             "Content-Type": "application/json"
#         }
        
#         params = {
#             "key": API_KEY
#         }
        
#         data = {
#             "contents": [{
#                 "parts": [{
#                     "text": prompt
#                 }]
#             }],
#             "generationConfig": {
#                 "temperature": 0.9,
#                 "topP": 1,
#                 "topK": 1,
#                 "maxOutputTokens": 2048
#             }
#         }
        
#         response = requests.post(url, headers=headers, params=params, json=data)
#         print(f"DEBUG - Status Code: {response.status_code}")  # 除錯用
#         print(f"DEBUG - Response: {response.text}")  # 除錯用
#         response.raise_for_status()
        
#         result = response.json()
#         if "candidates" in result:
#             return result["candidates"][0]["content"]["parts"][0]["text"]
#         else:
#             print(f"Unexpected response format: {result}")
#             return None
            
#     except requests.exceptions.RequestException as e:
#         print(f"API request failed: {e}")
#         return None
#     except json.JSONDecodeError as e:
#         print(f"Failed to parse response: {e}")
#         return None
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return None

# if __name__ == "__main__":
#     if not API_KEY:
#         print("Error: GEMINI_API_KEY not found in environment variables")
#         exit(1)
        
#     prompt = "Write a short poem about the moon."
#     result = generate_text(prompt)
#     if result:
#         print("\nGenerated Text:")
#         print("--------------")
#         print(result)
#     else:
#         print("Failed to generate text")
