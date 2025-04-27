import requests
import json
import base64
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import os

def get_file_path_tkinter():
    """Opens a file dialog and returns the absolute path of the selected file.

    Returns:
        str: The absolute path of the selected file, or None if no file is selected.
    """

    root = tk.Tk()  # Create a root Tkinter window
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename()  # Open the file dialog

    if file_path:
        return file_path
    else:
        return None

if __name__ == "__main__":
    file_path = get_file_path_tkinter()

    if file_path:
        print("Selected file path (Tkinter):", file_path)
        # Do something with the file path here (e.g., open and read the file)
    else:
        print("No file selected (Tkinter).")






def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer а не дам я свой ключ от openrouter, сами делайте))",
    "Content-Type": "application/json"
}

# Read and encode the image
image_path =  file_path 
base64_image = encode_image_to_base64(image_path)
data_url = f"data:image/jpeg;base64,{base64_image}"









messages = [
  {
  "messages" : [
      {
          "role": "user",
          "content": [
              {
                  "type": "text",
                  "text": "Дано фото чека из магазина. Должно быть только три строки в формате \n <дата> \n <сумма чека> \n <категория чека>, \n " +
                  "дата в формате '30.12.2000', сумма в формате '4312.12', категория строкой ''  в поле 'категория чека' бери значения только из списка категорий: " +
                  "Продукты, "+
                  "Одежда и аксессуары, "+
                  "Кафе и рестораны, "+
                  "Аптеки, "+
                  "Красота и уход, "+
                  "Образование, "+
                  "Спорт товары, "+
                  "Электроника "
              },
              {
                  "type": "image_url",
                  "image_url": {
                      "url": data_url
                  }
              }
          ]
      }
  ], 

"response_format": {
    "type": "json_schema",
    "json_schema": {
    "name": "weather",
    "strict": True,
        "schema": {
            "type": "object",
            "properties": [
                {
                "data_purchase": {
                    "type": "string",
                    "description": "дата выписки чека",
                },
                "items": 
                    {
                    "type": "object",
                    "description": "товары или услуги в чеке",
                    "properties": [
                        {
                        "item_name": {
                            "type": "string",
                            "description": "название товара или услуги",
                        },
                        "item_category": {
                            "type": "string",
                            "description": "категория данного товара или услуги",
                        },
                        "item_sum": {
                            "type": "string",
                            "description": "итоговая сумма по товару или услуге",
                        },
                        },
                    ],
                        
                    },
                },
            ],
            "required": ["data_purchase", "items", "item_name", "item_category", "item_sum"],
            "additionalProperties": False,
        },
    },
},


  
}
]











payload = {
    "model": "google/learnlm-1.5-pro-experimental:free",
    "messages": messages
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
