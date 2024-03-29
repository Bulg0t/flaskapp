# -*- coding: utf-8 -*-
# quiz-orm/main.py

import os
from app import app, baza
from views import *
from models import *
from dane import *


if __name__ == '__main__':
    if not os.path.exists(app.config['DATABASE']):
        baza.create_tables((Pytanie, Odpowiedz))
        dodaj_pytania(pobierz_dane('pytania.csv'))

    app.run(debug=True)
