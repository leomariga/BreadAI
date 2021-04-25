#!/usr/bin/env python
# coding: utf-8

from numpy import loadtxt
from keras.models import load_model
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle
# physical_devices = tf.config.list_physical_devices('GPU') 
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

# load model
class Recipe:
    def __init__(self):

        net_data = pickle.load( open( "net_data.pkl", "rb" ) )
        self.model = load_model(net_data['model_name'])
        self.max_sequence_len = net_data['max_sequence_len']

        self.tokenizer = net_data["tokenizer"]

        

    def generate_text(self, seed_text, next_words):
        for _ in range(next_words):
            token_list = self.tokenizer.texts_to_sequences([seed_text])[0]
            token_list = pad_sequences([token_list], maxlen= self.max_sequence_len-1, padding='pre')
            predicted = self.model.predict_classes(token_list, verbose=0)
            
            output_word = ""
            for word,index in self.tokenizer.word_index.items():
                if index == predicted:
                    output_word = word
                    break
            seed_text += " "+output_word
        return seed_text.title()

    


