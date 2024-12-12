from sentence_transformers import SentenceTransformer
# sbert_model = SentenceTransformer('bert-base-nli-mean-tokens'), Initially load using this, then start using pickle to save time.
with open("sbert",'rb') as f:
    sbert_model = pickle.load(f)

print("sbert loaded")

# I am adding the texts in this list,
# We can also add sentences of a large text individually to get more precise results when we query.
documents = [
    '''Taj mahal is an immense mausoleum of white marble, built in Agra between 1631 and 1648 by order of the Mughal emperor Shah Jahan in memory of his favourite wife, the Taj Mahal is the jewel of Muslim art in India and one of the universally admired masterpieces of the world's heritage.''',
 ]
