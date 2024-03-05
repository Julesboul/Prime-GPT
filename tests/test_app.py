from tests.conftest import client

class TestApp:
    def test_index(self, client):
        response = client.get('/')
        assert response.status_code == 200

    def test_result(self, client):

        test_file = open("tests/files/test.pdf", "rb")
        response = client.post('/result', data={"typeFormat" : 1, "resume": (test_file, "tests/files/test.pdf")}) 

        assert response.status_code == 200
    
    def test_result_no_resume(self, client):

        response = client.post('/result') 

        assert response.status_code == 302

    def test_result_wrong_extension(self, client):

        test_file = open("tests/files/test.pdf", "rb")
        response = client.post('/result', data={"typeFormat" : 1, "resume": (test_file, "tests/files/test.txt")}) 

        assert response.status_code == 302
    
    def test_result_no_extension(self, client):

        test_file = open("tests/files/test.pdf", "rb")
        response = client.post('/result', data={"typeFormat" : 1, "resume": (test_file, "tests/files/test")}) 

        assert response.status_code == 302
    
    def test_result_empty_file(self, client):

        test_file = open("tests/files/test_empty.pdf", "rb")
        response = client.post('/result', data={"typeFormat" : 2, "resume": (test_file, "tests/files/test_empty.pdf")}) 

        assert response.status_code == 302

    def test_generic_error(self, client):

        test_file = open("tests/files/test.pdf", "rb")
        response = client.post('/result', data={"resume": (test_file, "tests/files/test.pdf")}) 

        assert response.status_code == 302

    def test_error(self, client):
        response = client.get('/error') 

        assert response.status_code == 200
    
    def test_error(self, client):
        response = client.get("/error/'Error message'") 

        assert response.status_code == 200

    def test_format_1(self, client):
        response = client.get('/format1') 

        assert response.status_code == 200

    def test_format_2(self, client):
        response = client.get('/format2') 

        assert response.status_code == 200