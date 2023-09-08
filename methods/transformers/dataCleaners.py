# import pandas as pd


class DataCleaner:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def remove_duplicates(self):
        self.dataframe = self.dataframe.drop_duplicates()

    def handle_missing_values(self, method="drop", columns=None):
        if method == "drop":
            self.dataframe = self.dataframe.dropna(subset=columns)
        elif method == "fill":
            # Preencha os valores nulos com um valor específico, por exemplo, 0
            self.dataframe.fillna(0, inplace=True, subset=columns)
        elif method == "mean":
            # Preencha os valores nulos com a média das colunas
            mean = self.dataframe.mean()
            self.dataframe.fillna(mean, inplace=True, subset=columns)

    def clean_data(self):
        self.remove_duplicates()
        self.handle_missing_values(method="mean")

    def get_cleaned_dataframe(self):
        return self.dataframe
