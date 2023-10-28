import pandas as pd


class Loader:
    @classmethod
    def load_data(cls, file_path):
        """

        :param file_path:
        :return:
        """
        data_in_dataframe = pd.read_excel(file_path)
        data_in_dataframe = data_in_dataframe[data_in_dataframe.columns[1::]]
        print(data_in_dataframe)
        print("Null values in dataframe? :{0}".format(data_in_dataframe.isnull().values.any()))
        return data_in_dataframe


class Processor:
    @classmethod
    def refactor_data(cls, data_in_dataframe):
        captions = data_in_dataframe['Caption'].tolist()
        labels = [1 if label == "positive" else 0 for label in data_in_dataframe['LABEL'].tolist()]

        return captions, labels
