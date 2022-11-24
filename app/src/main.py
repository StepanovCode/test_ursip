from openpyxl import *
from copy import copy
import psycopg2
from dotenv import load_dotenv
import os
import logging
import sys
import pandas as pd
import contextlib
from app.services.parsing import parsing
from app.services.conversions_df import conversions_form_q
from app.server.moduls import FormularsTable, Formulars, FormQ

FORM_Q = 'form_q'


def main():
    df = parsing("../static/parse/Задание бек.xlsx", 3, 10)

    formular = Formulars(FORM_Q)
    formular.create_formulars_table()
    form_id = formular.select_from_formulars_table()
    if form_id is None:
        formular.insert_into_formulars_table()
        form_id = formular.select_from_formulars_table()
    if form_id is None:
        return 0
    df = conversions_form_q(df, form_id)

    form_q = FormQ(df)
    form_q.create_table()
    form_q.insert_data()


if __name__ == '__main__':
    main()
