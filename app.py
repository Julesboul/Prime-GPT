from flask import Flask, render_template, request, redirect, url_for

from exceptions import EmptyFileException, NoExtensionException, NotAllowedExtensionException
from services.utils import UtilsService
from services.api_gpt import ApiGPTService

def create_app(config):

    app = Flask(__name__)
    app.config.from_object("config")
    app.config["TESTING"] = config.get("TESTING")

    @app.route('/', methods=['GET'])
    def index():
        return render_template("index.html")
        
    @app.route('/result', methods=['POST'])
    def result():

        ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'png'}

        try:

            if 'resume' not in request.files :
                return render_template("result.html")

            resume = request.files.get('resume')
            type_format = int(request.form.get('typeFormat'))

            answer = ApiGPTService.ask_chat_gpt(resume, type_format, ALLOWED_EXTENSIONS)

            return render_template("result.html", answer=answer)
        
        except EmptyFileException:

            return redirect(url_for("error", message="Le fichier PDF transmis est vide. Vérifier que son contenu est correctement lisible."))
        
        except NoExtensionException:

            return redirect(url_for("error", message="Le fichier envoyé n'a pas d'extension."))
        
        except NotAllowedExtensionException:

            return redirect(url_for("error", message="Extension non supportée."))

        except:

            return redirect(url_for("generic_error"))
    
    @app.route('/error')
    def generic_error():
        return render_template("error.html")

    @app.route('/error/<message>', methods=['GET'])
    def error(message):

        return render_template("error.html", message=message)

    
    @app.route('/format1', methods=['GET'])
    def format1():

        exemple = UtilsService.get_format(1)
        return render_template("format.html", exemple=exemple)
    
    @app.route('/format2', methods=['GET'])
    def format2():

        exemple = UtilsService.get_format(2)
        return render_template("format.html", exemple=exemple)   

    return app

app = create_app({"TESTING": False})

if __name__ == "__main__":
    app.run()