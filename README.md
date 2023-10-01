# AI - microservice

This repo is part of project for HackYeah2023. Main task is to allow strict backend
frontend communication take advantage of machine learning models

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

#### Via pip
```bash
pip install spacy
pip install jupyter
pip install jupyter-notebook
pip install pandas
pip install nlp
pip install nltk
pip install tensorflow
```

#### Via docker
```dockerfile

```

## Usage

```http request
POST http://localhost:2137/chat
Content-Type: application/json

{
  "text": "Pokaz dostepne uczelnie w Konin"
}
Allowed headers: [BOT_SESSION_ID, LANG]
```

#### Notes
Please bear in mind that due to small training size for increased
training efficiency results may not be 100% accurate