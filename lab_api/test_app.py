import unittest
import requests

BASE_URL = "https://seu-app-no-render.onrender.com"  # 🔁 Substitua pelo seu link real

class APINewTests(unittest.TestCase):

    def test_cadastro_com_dados(self):
        response = requests.post(f"{BASE_URL}/register", json={
            'username': 'testeuser',
            'password': '123456'
        })
        self.assertIn(response.status_code, [200, 201, 409])
        self.assertIn('message', response.json())

    def test_metodo_nao_permitido(self):
        response = requests.put(f"{BASE_URL}/login")
        self.assertEqual(response.status_code, 405)

    def test_acesso_com_token_invalido(self):
        response = requests.get(f"{BASE_URL}/protected", headers={
            'Authorization': 'Bearer token_invalido'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('msg', response.json())

if __name__ == '__main__':
    unittest.main()
