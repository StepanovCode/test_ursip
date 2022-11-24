import pandas


def conversions_form_q(df, form_id):
    df.insert(1, 'form_id', form_id)
    df.reset_index()
    df.drop(df.columns[0], axis=1, inplace=True)
    return df

# TODO: Добавить расчетный тотал по Qoil, Qliq, сгруппированный по датам (даты можете указать свои,
#  добавив программно, не изменяя исходный файл, при условии, что дни будут разные, а месяц и год одинаковые)
