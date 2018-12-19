from gensim.models.keyedvectors import KeyedVectors
import os
import sys
import gensim

# if sys.args[1]=='wv':
#     m = "word2vec-master"
# if sys.args[1]=='g':
#     m = "glove"
# if sys.args[1]=='ft':
#     m = "fastText"

# if sys.args[2]=='brown':
#     m = "brown"
# if sys.args[1]=='bnc':
#     m = "bnc"

if sys.argv[1]=='wv':
    model = KeyedVectors.load_word2vec_format('./word2vec-master/ner_vectors.bin', binary=True)
    model.save_word2vec_format('coref_vectors.txt', binary=False)

    model = KeyedVectors.load_word2vec_format('./word2vec-master/nocoref_vectors.bin', binary=True)
    model.save_word2vec_format('nocoref_vectors.txt', binary=False)

    os.system("python filterVocab.py vocabulary.txt < coref_vectors.txt > filt_coref_vectors.txt")
    os.system("python filterVocab.py vocabulary.txt < nocoref_vectors.txt > filt_nocoref_vectors.txt")

    os.system("python ./eval-word-vectors/all_wordsim.py filt_nocoref_vectors.txt ./eval-word-vectors/data/word-sim")
    os.system("python ./eval-word-vectors/all_wordsim.py filt_coref_vectors.txt ./eval-word-vectors/data/word-sim")

# model = KeyedVectors.load_word2vec_format('./glove/coref_vectors.bin', binary=True)
# model.save_word2vec_format('coref_vectors.txt', binary=False)


# model = KeyedVectors.load_word2vec_format('./glove/nocoref_vectors.bin', binary=True)
# model.save_word2vec_format('nocoref_vectors.txt', binary=False)

if sys.argv[1]=='g':
    print("using glove vectors")
    os.system("python filterVocab.py vocabulary.txt < ./glove/ner_vectors.txt > filt_coref_vectors.txt")
    os.system("python filterVocab.py vocabulary.txt < ./glove/nocoref_vectors.txt > filt_nocoref_vectors.txt")

    os.system("python ./eval-word-vectors/all_wordsim.py filt_nocoref_vectors.txt ./eval-word-vectors/data/word-sim")
    os.system("python ./eval-word-vectors/all_wordsim.py filt_coref_vectors.txt ./eval-word-vectors/data/word-sim")

if sys.argv[1]=='f':
    print("using fastText vectors")
    os.system("python filterVocab.py vocabulary.txt < ./fastText/ner_vectors.vec > filt_coref_vectors.txt")
    os.system("python filterVocab.py vocabulary.txt < ./fastText/nocoref_vectors.vec > filt_nocoref_vectors.txt")

    os.system("python ./eval-word-vectors/all_wordsim.py filt_nocoref_vectors.txt ./eval-word-vectors/data/word-sim")
    os.system("python ./eval-word-vectors/all_wordsim.py filt_coref_vectors.txt ./eval-word-vectors/data/word-sim")

if sys.argv[1]=='o':
    print("using OIWE vectors")
    os.system("python filterVocab.py vocabulary.txt < ./OIWE/coref_vectors.txt > filt_coref_vectors.txt")
    os.system("python filterVocab.py vocabulary.txt < ./OIWE/nocoref_vectors.txt > filt_nocoref_vectors.txt")

    os.system("python ./eval-word-vectors/all_wordsim.py filt_nocoref_vectors.txt ./eval-word-vectors/data/word-sim")
    os.system("python ./eval-word-vectors/all_wordsim.py filt_coref_vectors.txt ./eval-word-vectors/data/word-sim")
