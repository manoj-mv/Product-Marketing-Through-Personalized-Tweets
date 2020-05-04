from magpie import Magpie


magpie = Magpie()

print("started")
# for training
magpie.init_word_vectors('/home/manoj/twitter_interest/reddit_data/reddit_extracted', vec_dim=100)
labels = ['automotive', 'movies', 'food',
          'travel', 'technology', 'sports', 'politics','health']
print("training started.")
magpie.train('/home/manoj/twitter_interest/reddit_data/reddit_extracted', labels, test_ratio=0.2, epochs=1000)
print("training over.")

# magpie.predict_from_file('data/hep-categories/1002413.txt')
# magpie.predict_from_text("hello")
# loss0.0727

# #for saving models
# magpie.save_word2vec_model('/home/sreeku/Downloads/magpiee/mag/saved_model/word2vec/1')
# magpie.save_scaler('/home/sreeku/Downloads/magpiee/mag/saved_model/scaler/1', overwrite=True)
# magpie.save_model('/home/sreeku/Downloads/magpiee/mag/saved_model/model/1.h5')
magpie.save_word2vec_model('/home/manoj/twitter_interest/saved_model/word2vec/1',overwrite=True)
magpie.save_scaler('/home/manoj/twitter_interest/saved_model/scaler/1', overwrite=True)
magpie.save_model('/home/manoj/twitter_interest/saved_model/model/1.h5')