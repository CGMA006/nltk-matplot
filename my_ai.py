import nltk
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('punkt_tab')

text = "hattile padyo pwa pwa pwa. phush phush"

from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.probability import FreqDist
# print(word_tokenize(text))

# print (sent_tokenize(text))

fd = FreqDist(text)

print (fd.most_common())

fd.plot()

plt.show()






