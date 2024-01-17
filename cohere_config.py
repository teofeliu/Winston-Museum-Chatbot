# cohere_config.py
import cohere
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

COHERE_API_KEY = os.environ['COHERE_API_KEY']
co = cohere.Client(COHERE_API_KEY)


