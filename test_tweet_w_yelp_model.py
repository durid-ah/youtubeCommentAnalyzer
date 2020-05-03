# A script that tests tweets against the yelp model to test its usability in the process
import fasttext
import pandas as pd
from data_collection_and_process_scripts.preprocessing_tools import strip_down_comment


def main():
    headers = ['target', 'id', 'date', 'flag', 'user', 'text']

    df = pd.read_csv(
        '../Downloads/sentiment140/training.1600000.processed.noemoticon.csv',
        encoding='latin1',
        names=headers
    )

    df = df[:500]
    correct = 0
    flawed = 0

    for index, row in df.iterrows():
        model = fasttext.load_model('./analysis_models/sentiment_model_e5_lr1.0_wn3.bin')
        result = model.predict(strip_down_comment(row.text))
        label = result[0][0]
        target = row.target
        print(target, label, row.text)
        if int(label[-1:]) < 3 and target == 0:
            correct += 1
        elif int(label[-1:]) >=3 and target == 4:
            correct += 1
        else:
            flawed += 1

    print("% correct: ", ((correct / 500) * 100))
    print("% error: ", ((flawed / 500) * 100))


if __name__ == '__main__':
    main()