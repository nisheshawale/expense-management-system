import re
import spacy


nlp = spacy.load("en_core_web_sm")


def lemmatize(text):
    text = re.sub(r"'s\b", "", text)
    doc = nlp(text)

    lemmas = []
    for token in doc:
        lemmas.append(token.lemma_)

    return " ".join(lemmas)
