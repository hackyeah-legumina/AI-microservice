import json
from pathlib import Path

import spacy
from spacy.cli.init_config import fill_config
from spacy.cli.train import train
from spacy.tokens import DocBin
from spacy.util import filter_spans
from tqdm import tqdm

nlp = spacy.load("pl_core_news_sm")

with open('data.json', 'r') as f:
    data = json.load(f)

training_data = []
for example in data['examples']:
    temp_dict = {}
    temp_dict['text'] = example['content']
    temp_dict['entities'] = []
    for annotation in example['annotations']:
        start = annotation['start']
        end = annotation['end']
        label = annotation['tag_name'].upper()
        temp_dict['entities'].append((start, end, label))
    training_data.append(temp_dict)

nlp = spacy.blank("pl")

doc_bin = DocBin()
for training_example in tqdm(training_data):
    text = training_example['text']
    labels = training_example['entities']
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in labels:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    filtered_ents = filter_spans(ents)
    doc.ents = filtered_ents
    doc_bin.add(doc)

doc_bin.to_disk("train.spacy")

fill_config(Path("config.cfg"), Path("base_config.cfg"))
train(Path("config.cfg"), Path("my_model"), overrides={"paths.train": "train.spacy", "paths.dev": "train.spacy"})