echo "Starting first model training"
cd chatbot
python3 train_chatbot.py

cd ../
mv chatbot/chatbot_model.h5 chatbot_data/chatbot_model.h5
mv chatbot/classes.pkl chatbot_data/classes.pkl
mv chatbot/words.pkl chatbot_data/words.pkl

echo "Finished processing first model"

echo "Starting second model training"

cd custom_ner_model_pl
python3 -m spacy download pl_core_news_lg
python3 train_chatbot.py
python3 -m spacy init fill-config base_config.cfg config.cfg
python3 -m spacy train config.cfg --output ./ --paths.train ./train.spacy --paths.dev ./train.spacy

cd ../
mv custom_ner_model_pl/model-best chatbot_data/model-best
echo "Finished processing second model"