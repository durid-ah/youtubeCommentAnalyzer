import fasttext
from data_repository import sqlite_functions

conn = sqlite_functions.create_connection("./data_repository/dataset.db")
insert_values = """INSERT INTO training_results (epoch, learning_rate, word_ngrams, precision, recall)
                    VALUES (?,?,?,?,?)"""

epoch = [5, 25]
learning_rate = [0.1, 0.5, 1.0]
word_ngrams = [1, 3, 5]

for i in epoch:
    for j in learning_rate:
        for k in word_ngrams:
            model = fasttext.train_supervised(
                input="tweets.train", epoch=i, lr=j, wordNgrams=k
            )

            model.save_model(
                f"./analysis_models/sentiment_model_e{i}_lr{j}_wn{k}.bin"
            )

            test_values = model.test("tweets.valid")
            print(test_values)
            conn.execute(insert_values, (i, j, k, test_values[1], test_values[2]))
            conn.commit()

conn.close()
