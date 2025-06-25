# Assistente de Arquitetura

Este projeto utiliza a biblioteca CrewAI para criar uma equipe de agentes inteligentes capazes de responder perguntas técnicas sobre arquitetura de software, DevOps, APIs e padrões de projeto. O objetivo é simular um sistema de atendimento automatizado para dúvidas técnicas, com agentes especializados em diferentes áreas.

## Funcionalidades

- Delegação automática de perguntas para agentes especializados (Microserviços, Design Patterns, DevOps, APIs).
- Respostas detalhadas e validadas conforme melhores práticas de TI.
- Estrutura modular para fácil expansão de agentes e tarefas.

## Estrutura do Projeto

- `app.py`: Arquivo principal para execução do projeto (pode ser adaptado conforme necessidade).
- `arquitetura.py`: Implementação dos agentes, tarefas e lógica principal da CrewAI.
- `.env`: Armazenar as chaves necessárias para a utlização da ferramenta.
- `requirements.txt`: Dependências do projeto.

## Como rodar

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/chatbot_arquitetura.git
   cd chatbot_arquitetura
   ```

2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

3. Defina a variável de ambiente com sua chave da OpenAI:
   ```sh
   set OPENAI_API_KEY=your_openai_api_key
   ```

4. Execute o script principal:
   ```sh
   python arquitetura.py
   ```

## Exemplo de uso

O sistema irá interpretar perguntas como:
> "Qual a diferença entre arquitetura monolítica e em camadas?"

E irá delegar para o agente mais adequado, retornando uma resposta detalhada.

