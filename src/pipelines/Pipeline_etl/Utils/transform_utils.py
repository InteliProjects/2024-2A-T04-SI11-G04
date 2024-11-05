def optimize_floats(df):
    # Converte todas as colunas float64 para float32
    float_cols = df.select_dtypes(include=['float64']).columns
    df[float_cols] = df[float_cols].astype('float32')
    return df
