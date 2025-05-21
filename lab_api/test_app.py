import unittest
from app import app

class APINewTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def cadastro_com_dados(self):
        # Testa a criação de um novo usuário com dados simulados
        response = self.client.post('/register', json={
            'username': 'testeuser',
            'password': '123456'
        })
        self.assertIn(response.status_code, [200, 201, 409])  # depende se já existe
        self.assertIn('message', response.json)

    def metodo_nao_permitido(self):
        # Envia um método errado para uma rota específica
        response = self.client.put('/login')
        self.assertEqual(response.status_code, 405)

    def acesso_com_token_invalido(self):
        # Tenta acessar uma rota protegida com token inválido
        response = self.client.get('/protected', headers={
            'Authorization': 'Bearer token_invalido'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('msg', response.json)

if __name__ == '__main__':
    unittest.main()
