import pytest
from services.utils import UtilsService
from exceptions import NoExtensionException, NotAllowedExtensionException, FormatNotAcceptedException, EmptyFileException

class TestUtilsService:

    def test_get_extension_success(self):

        filename = "example.pdf"

        assert UtilsService.get_extension(filename) == "pdf"
    
    def test_get_extension_failure(self):

        filename = "example"

        with pytest.raises(NoExtensionException):
            UtilsService.get_extension(filename)

    @pytest.mark.parametrize("filename", ["example.pdf", "example.jpg", "example.png"])
    def test_check_allowed_file_success(self, filename):

        ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'png'}

        assert UtilsService.check_allowed_file(filename, ALLOWED_EXTENSIONS)
    
    def test_check_allowed_file_failure(self):

        ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'png'}
        filename = "example.txt"

        with pytest.raises(NotAllowedExtensionException):
            UtilsService.check_allowed_file(filename, ALLOWED_EXTENSIONS)

    
    def test_get_format_failure(self):
        
        num = 5

        with pytest.raises(FormatNotAcceptedException):
            UtilsService.get_format(num)
    
    @pytest.mark.parametrize("num", [1, 2])
    def test_get_format(self, num):

        assert UtilsService.get_format(num)
    
    def test_convert_pdf_to_string_success(self):

        file_test = "tests/files/test.pdf"

        assert UtilsService.convert_pdf_to_string(file_test)
    
    def test_convert_pdf_to_string_empty(self):

        file_test = "tests/files/test_empty.pdf"

        with pytest.raises(EmptyFileException):
            UtilsService.convert_pdf_to_string(file_test)
    
    
    @pytest.mark.parametrize("file_test", ["tests/files/test.jpg", "tests/files/test.png"])
    def test_convert_image_to_string_success(self, file_test):

        assert UtilsService.convert_image_to_string(file_test)

    
    @pytest.mark.parametrize("empty_file", ["tests/files/test_empty.jpg", "tests/files/test_empty.png"])
    def test_convert_image_to_string_failure(self, empty_file):

        with pytest.raises(EmptyFileException):
            UtilsService.convert_image_to_string(empty_file)
