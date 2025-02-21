from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)



#Para rodar a venv e desativar
# venv\Scripts\activate
# deactivate

#Para rodar a aplicação
# flask run