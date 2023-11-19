import requests

def query_password_strength(password):
    try:
        url = "http://localhost:5000/predict"
        response = requests.post(url, json={"password": password})
        if response.status_code == 200:
            return response.json()["strength"]
        else:
            return "Erro na solicitação: " + response.text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    try:
        password = input("Digite uma senha para verificar sua força: ")
        strength = query_password_strength(password)
        print(f"A força da senha é: {strength}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    input("Pressione Enter para sair...")
