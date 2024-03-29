from pypdf import PdfReader
from PIL import Image
from pytesseract import pytesseract 
from exceptions import NoExtensionException, NotAllowedExtensionException, FormatNotAcceptedException, EmptyFileException

class UtilsService:
    """
        Service to process files and get informations about it.
    """
    
    def get_extension(filename):
        if '.' in filename:
            return filename.rsplit('.', 1)[1].lower()
        else:
            raise NoExtensionException
        
    def check_allowed_file(filename, ALLOWED_EXTENSIONS):

        extension = UtilsService.get_extension(filename)

        if not (extension in ALLOWED_EXTENSIONS):

            raise NotAllowedExtensionException
        
        return True
    
    def get_format(num):
        """
            Fonction to get the format which will be used to write the ChatGPT's answer.
        """

        if num == 1:

            with open("static/files/format_1.txt", "r", encoding="utf-8") as f1:
                format_1 = f1.read()
                return format_1
        
        elif num == 2:

            with open("static/files/format_2.txt", "r", encoding="utf-8") as f2:
                format_2 = f2.read()
                return format_2
            
        else:

            raise FormatNotAcceptedException
    
    def convert_pdf_to_string(pdf):

        text = ""

        reader = PdfReader(pdf) 
        
        for i in range (len(reader.pages)):
            page = reader.pages[i] 
            text += page.extract_text() 

        if text == "":

            raise EmptyFileException
        
        else:
        
            return text
    
    def convert_image_to_string(img):

        text = ""

        path_to_tesseract = '/.apt/usr/bin/tesseract' # Tessercat's path

        pytesseract.tesseract_cmd = path_to_tesseract 

        img_to_process = Image.open(img) 

        text = pytesseract.image_to_string(img_to_process) 

        if text == "":

            raise EmptyFileException
        
        else:
        
            return text


