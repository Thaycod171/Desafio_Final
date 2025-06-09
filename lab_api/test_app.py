import unittest
from app import app

class APINewTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_cadastro_com_dados(self):
        response = self.client.post('/register', json={
            'username': 'testeuser',
            'password': '123456'
        })
        self.assertIn(response.status_code, [200, 201, 409]) 
        self.assertIn('message', response.json)

    def test_metodo_nao_permitido(self):
        response = self.client.put('/login')
        self.assertEqual(response.status_code, 405)

    def test_acesso_com_token_invalido(self):
        response = self.client.get('/protected', headers={
            'Authorization': 'Bearer token_invalido'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('msg', response.json)

if __name__ == '__main__':
    unittest.main()
