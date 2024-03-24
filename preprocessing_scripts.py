#1 Lowercasing the text
    data_frame["column_name"] = data_frame["column_name"].str.lower()

#2 Removing HTML tags
    import re
    def remove_html_tags(text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

#3 Removing URL
    def remove_url(text):
        pattern = re.compile(r'https?://\S+|www\.\S+')
        return pattern.sub(r'', text)

#4 Removing Punctuations
    import string
    exclude = string.punctuation
    #Method 1
    def remove_punc(text):
        for char in exclude:
            text = text.replace(char,'')
        return text

#Method 2(18 times faster than method 1)
    def remove_punc1(text):
        return text.translate(str.maketrans('', '', exclude))


#5 Converting short forms to full forms
    #CHAT WORDS IS A DICTIONARY WITH FULL FORM AS SLANG.TXT FILE
        def chat_conversion(text):
            new_text = []
            for w in text.split():
                if w.upper() in chat_words:
                    new_text.append(chat_words[w.upper()])
                else:
                    new_text.append(w)
            return " ".join(new_text)

#6 Spelling Correction
    from textblob import TextBlob
    textBlb = TextBlob(incorrect_text)
    textBlb.correct().string

#7 Removing Stopwords
    from nltk.corpus import stopwords
    stopwords.words('english') #for the stopwords in English language
    def remove_stopwords(text):
        new_text = []
        
        for word in text.split():
            if word in stopwords.words('english'):
                new_text.append('')
            else:
                new_text.append(word)
        x = new_text[:]
        new_text.clear()
        return " ".join(x)

#8 Removing Emojis
    #Method 1 - Removing emojis using simple regex
        import re
        def remove_emoji(text):
            emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                "]+", flags=re.UNICODE)
            return emoji_pattern.sub(r'', text)

    #Method 2 - Replace emojis with their names
        import emoji
        emoji.demojize(text)

#9 Tokenization
    #Method 1 - Using split function
        sentence.split() #for splitting the sentence into words
        sentence.split('.') #for splitting the sentence into sentences

    #Method 2 -  using Regular Expressions
        import re
        tokens = re.findall("[\w']+", sentence)

    #Method 3 - Using NLTK
        from nltk.tokenize import word_tokenize,sent_tokenize
        word_tokenize(sentence)
        sent_tokenize(sentence) 

    #Method 4 - Using Spacy
        import spacy
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(sentence)
        tokens = [token.text for token in doc]

#10 Stemming
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()   
    def stem_words(text):
        return " ".join([stemmer.stem(word) for word in text.split()])

#11 Lemmatization
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    def lemmatize_words(text):
        return " ".join([lemmatizer.lemmatize(word) for word in text.split()])