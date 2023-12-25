import pandas as pd
def top_countries(df:pd.DataFrame, countries:list):

    top_countries_df = (
        df.select_columns(["country_region", "value"])
        .groupby(["country_region"])
        .aggregate("sum")
        .sort_values("value", ascending=False)
        .reset_index()
        .head(20)
        .transform_column(
            column_name="country_region",
            function=lambda x: "red" if x in countries else "lightblue",
            dest_column_name="color"
        )
    )
    return top_countries_df 