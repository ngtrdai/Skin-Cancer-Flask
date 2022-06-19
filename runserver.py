from os import environ
from SkinCancer_Flask import Create_App

app = Create_App()

if __name__ == '__main__':
    app.run(debug=True)