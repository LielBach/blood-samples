from pandas import read_csv, to_numeric

def read_samples():
    year_column_name = 'RIDAGEYR'
    index_column_name = 'SEQN'

    blood_samples = read_csv('blood_samples.csv', index_col=index_column_name, skip_blank_lines=True, na_values=" ")
    samples_demographic_data =  read_csv('demographic_data.csv', index_col=index_column_name, skip_blank_lines=True, na_values=" ")\
        .filter([index_column_name, year_column_name])
    cholestrol = read_csv('chol.csv', index_col=index_column_name, skip_blank_lines=True, na_values=" ")
    body_measures = read_csv('body_measures.csv', index_col=index_column_name, skip_blank_lines=True, na_values=" ")\
        .fillna(0)

    complete_data_samples = blood_samples.join(samples_demographic_data)\
                                        .join(cholestrol)\
                                        .join(body_measures)\
                                        .dropna()\
                                        .apply(to_numeric)

    return (complete_data_samples.drop(year_column_name, axis='columns').to_numpy(),
            complete_data_samples.loc[:, year_column_name].to_numpy())