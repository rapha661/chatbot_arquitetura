import os
from crewai import Agent, Task, Crew
from IPython.display import Markdown

openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o'

# Criação de agentes
agente_principal = Agent(
    role="Principal Agent",
    goal="Interpretar perguntas e delegar para agentes especializados.",
    backstory=(
        "Você trabalha na Telefonica e é responsável "
        "por interpretar as perguntas dos usuários e delegar para os "
        "agentes especializados corretos. Seu cliente atual é {customer}."
    ),
    allow_delegation=True,
    verbose=True
)

agente_microservicos = Agent(
    role="Microservices Specialist",
    goal="Responder perguntas sobre arquitetura de microserviços.",
    backstory=(
        "Você é um especialista em microserviços na crewAI (https://crewai.com). "
        "Seu cliente atual é {customer}, e você deve fornecer respostas detalhadas "
        "e práticas sobre arquitetura de microserviços."
    ),
    allow_delegation=False,
    verbose=True
)

agente_design_patterns = Agent(
    role="Design Patterns Specialist",
    goal="Responder perguntas sobre padrões de projeto e boas práticas.",
    backstory=(
        "Você é um especialista em padrões de projeto na crewAI (https://crewai.com). "
        "Seu cliente atual é {customer}, e você deve fornecer respostas detalhadas "
        "e práticas sobre padrões de projeto e boas práticas."
    ),
    allow_delegation=False,
    verbose=True
)

agente_devops = Agent(
    role="DevOps Specialist",
    goal="Responder perguntas sobre práticas de DevOps.",
    backstory=(
        "Você é um especialista em DevOps na crewAI (https://crewai.com). "
        "Seu cliente atual é {customer}, e você deve fornecer respostas detalhadas "
        "e práticas sobre integração contínua, deploy e automação."
    ),
    allow_delegation=False,
    verbose=True
)

agente_apis = Agent(
    role="APIs Specialist",
    goal="Responder perguntas sobre gerenciamento de APIs e gateways.",
    backstory=(
        "Você é um especialista em APIs na crewAI (https://crewai.com). "
        "Seu cliente atual é {customer}, e você deve fornecer respostas detalhadas "
        "e práticas sobre gerenciamento de APIs e gateways."
    ),
    allow_delegation=False,
    verbose=True
)

agents = [
    agente_principal,
    agente_microservicos,
    agente_design_patterns,
    agente_devops,
    agente_apis
]

# Criação das tasks
task_identificar_tema = Task(
    description=(
        "{customer} enviou a seguinte pergunta:\n"
        "{inquiry}\n\n"
        "{person} da {customer} precisa de uma resposta completa e precisa. "
        "Identifique o tema principal da pergunta para delegar ao agente especializado."
    ),
    expected_output=(
        "Identificação clara do tema da pergunta, como microserviços, monolítico, "
        "design patterns, DevOps ou APIs, para que possa ser delegada ao agente correto."
    ),
    tools=[],
    agent=agente_principal
)

task_pesquisar_informacoes = Task(
    description=(
        "{customer} enviou a seguinte pergunta:\n"
        "{inquiry}\n\n"
        "{person} da {customer} precisa de uma resposta completa e precisa. "
        "Pesquise informações relevantes no repositório de conhecimento ou em APIs externas."
    ),
    expected_output=(
        "Informações detalhadas e relevantes encontradas no repositório de conhecimento "
        "ou em APIs externas, que possam ser usadas para responder à pergunta do cliente."
    ),
    # tools=[docs_scrape_tool],
    agent=agente_principal
)

task_gerar_resposta = Task(
    description=(
        "{customer} enviou a seguinte pergunta:\n"
        "{inquiry}\n\n"
        "{person} da {customer} precisa de uma resposta completa e precisa. "
        "Gere uma resposta detalhada e exemplificada para a pergunta."
    ),
    expected_output=(
        "Uma resposta detalhada e prática que aborda todos os aspectos da pergunta do cliente, "
        "incluindo exemplos práticos e referências relevantes."
    ),
    tools=[],
    agent=agente_principal
)

task_validar_resposta = Task(
    description=(
        "{customer} enviou a seguinte pergunta:\n"
        "{inquiry}\n\n"
        "{person} da {customer} precisa de uma resposta completa e precisa. "
        "Valide a resposta gerada para garantir que segue as melhores práticas de TI."
    ),
    expected_output=(
        "Validação da resposta gerada, garantindo que está completa, precisa e segue as melhores "
        "práticas de TI, mantendo um tom amigável e útil."
    ),
    agent=agente_principal
)

tasks = [
    task_identificar_tema,
    task_pesquisar_informacoes,
    task_gerar_resposta,
    task_validar_resposta
]

# Construção da equipe
crew = Crew(
    agents=agents,
    tasks=tasks,
    verbose=2,
    memory=True
)

# Criação da pergunta
inputs = {
    "customer": "Teste",
    "person": "Raphael",
    "inquiry": "Qual a diferença entre arquitetura monolítica e em camadas?"
}

resultado = crew.kickoff(inputs=inputs)
Markdown(resultado)