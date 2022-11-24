import os
import pandas as pd

from app.services.conversions import WorksheetFormularQ


def parsing(path: str, height_header: int, max_column: int) -> pd.DataFrame:
    try:
        if not isinstance(path, str):
            print(f'Путь {path} не является строкой')
            raise TypeError

        ws_formularq = WorksheetFormularQ(path, height_header, max_column)
        ws = ws_formularq.reformatting_sheet()

        df = pd.DataFrame(ws.values)
        df = df.iloc[:, :10]
        return df

    except TypeError as err:
        print(f'[ERROR]: -- "parsing/parsing" -- TypeError: {err}')
        return df, err
    except Exception as err:
        print(f'[ERROR]: -- "parsing/parsing" -- {err}')


if __name__ == '__main__':
    pass
