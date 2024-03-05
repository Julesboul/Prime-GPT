import os
from dotenv import load_dotenv
from openai import OpenAI


from services.utils import UtilsService
from exceptions import EmptyFileException, NotAllowedExtensionException


load_dotenv()

OPEN_AI_API_KEY = os.getenv('OPEN_AI_API_KEY')

class ApiGPTService:
    """
        Service which interract with the ChatGPT's API.
    """

    def ask_chat_gpt(resume, num, allowed_extensions):

        UtilsService.check_allowed_file(resume.filename, allowed_extensions)

        extension = UtilsService.get_extension(resume.filename)

        if extension == "pdf":

            to_resume = UtilsService.convert_pdf_to_string(resume)

        elif extension == "jpg" or extension == "png":

            to_resume = UtilsService.convert_image_to_string(resume)

        format_answer = UtilsService.get_format(num)

        messages = [{"role": "user", "content" : f"Ceci est un résumé de CV : \n '{format_answer}'"}]

        messages.append({"role": "user", "content" : f"Résume le CV suivant : \n '{to_resume}'"})

        client = OpenAI(api_key=OPEN_AI_API_KEY)
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )

        return chat_completion.choices[0].message.content