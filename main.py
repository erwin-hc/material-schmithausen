from website import create_app
from flask import session
from datetime import timedelta

app = create_app()

if __name__ == '__main__':
    app.run(host='10.0.0.53',debug=True)
