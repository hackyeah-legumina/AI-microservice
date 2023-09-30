import spacy
import spacy_transformers
import json
from spacy.tokens import DocBin
from tqdm import tqdm
from spacy.util import filter_spans
from pathlib import Path
from spacy.cli.download import download
from spacy.cli.init_config import fill_config
from spacy.cli.train import train


def init_static_context():
    _init_ner_model()


def _init_ner_model():
    nlp_ner = spacy.load("model-best")
    doc = nlp_ner(
        "Dzień dobry, interesuję się studiami na Akademii Teatralnej im. Aleksandra Zelwerowicza w Warszawie. Czy m")

    spacy.displacy.render(doc, style="ent", jupyter=True)