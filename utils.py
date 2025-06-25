def get_openai_api_key():
    return "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"

import os

def get_openai_api_key():
    """
    Retorna a chave da API do OpenAI a partir de uma variável de ambiente.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("A chave da API do OpenAI não foi encontrada. Defina a variável de ambiente 'OPENAI_API_KEY'.")
    return api_key


def get_serper_api_key():
    """
    Retorna a chave da API do Serper a partir de uma variável de ambiente.
    """
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise ValueError("A chave da API do Serper não foi encontrada. Defina a variável de ambiente 'SERPER_API_KEY'.")
    return api_key