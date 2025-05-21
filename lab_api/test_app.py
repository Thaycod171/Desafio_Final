import unittest
from app import app
import werkzeug

# Gambiarrinha pro werkzeug não dar erro
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Cria um cliente de teste da API
        cls.client = app.test_client()


#Verifica se a rota / responde com o status 200 e a mensagem correta
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API is running"})


#Confirma que a rota /login gera um token JWT
    def test_login(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)


#Testa o acesso à rota /protected sem o token JWT, esperando um status de não autorizado (401). 
    def test_protected_no_token(self):
        response = self.client.get('/protected')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
