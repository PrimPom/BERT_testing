from data_loader.data_loading_processing import Loader, Processor
if __name__ == "__main__":

    data = Loader.load_data(file_path="inputs/LabeledText.xlsx")
    captions, labels = Processor.refactor_data(data)
    print(labels)
