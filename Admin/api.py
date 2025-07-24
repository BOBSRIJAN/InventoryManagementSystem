import os
import google.generativeai as genai
import dotenv

dotenv.load_dotenv()

def Ai(prompt, image=None)-> str:
    api=os.getenv('api')
    try:
        genai.configure(api_key=api)
    except KeyError:
        return "Error: GOOGLE_APapiI_KEY environment variable not set."
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    try:
        if image:
            img = genai.upload_file(image)
            response = model.generate_content(contents=[prompt, img])
        else:
            response = model.generate_content(prompt)
        return f"Ai response: {response.text}"
    except Exception as e:
        return f"An error occurred: {e}"
    
# if __name__=="__main__":
#     print(Ai("tell me the Plant disease",image="media/image.jpeg"),"\nthis is the msg!")# remove this in production