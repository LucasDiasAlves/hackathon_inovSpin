# HACKATHON InovaSpin 🖥️ - Manutenção Preditiva
---
## Sumario
1. [📝Metodos para a Avaliação](#metodos-para-a-avaliação)
2. [⚡Sobre o projeto](#sobre-o-projeto)
3. [🚀 Problema Abordado](#problema-abordado)
4. [🛠 Tecnologias Utilizadas](#tecnologias-utilizadas)
5. [🏛️ Arquitetura da Aplicação](#arquitetura-da-aplicação)
6. [📊 Principais Funcionalidades](#principais-funcionalidades)
7. [🎲 Origem Dataset](#origem-dataset)
---

## Metodos para a Avaliação
### Metricas 
- O projeto deve posuir **front-end** e **back-end**;
- A **IA** pode ser **simples**, mas deve estar **claramente aplicada**;
- Dados podem ser **simulados** ou **reais**;
- Aplicações aplicadas a **área elétrica** serão um **diferencial**;
- É permitido utilziar modelos de IA como apoio técnico.

### Submissão do Projeto
Os participantes deverão enviar até as 23h59 do dia 06 de março de 2026 os seguintes materiais para o e-mail: tulio.silva@spinengenharia.com.br. Use como titulo: [SPIN INOVAÇÃO HACK] Titulo do projeto.

#### Itens Obrigatórios para Envio
1. **Link do GitHub do Projeto**, contendo:
    - Código-fonte completo (front-end e back-end)
    - Arquivo `README.md` com:
        - Descrição da solução
        - Problema abordado
        - Tecnologias utilizadas
        - Instruções para execução do projeto
        - Arquitetura da aplicação
2. **Currículo atualizado**
    - Em formato PDF
    - Nomear o arquivo como: `Curriculo_NomeSobrenome.pdf`
3. **Link de um vídeo no YouTube (não listado ou público)** contendo o **pitch da solução**, com duração entre **3 minutos.**
---
## Sobre o projeto
### Manutenção Preditiva
**Enunciado:**
Desenvolva uma aplicação que utilize dados históricos para prever falhas ou degradação de sistemas. O modelo de IA deve indicar o nível de risco e sugerir quando ações preventivas devem ser realizadas.
**Objetivo:**
Antecipar problemas e reduzir falhas através da previsão inteligente.

## Problema Abordado
🚩 O Problema: "Degradação Térmica e Sobrecarga em Ativos de Distribuição"
Em sistemas elétricos, o maior inimigo dos equipamentos (como transformadores e motores) é o calor excessivo.

* **O Problema Real:** O isolamento dos fios dentro de um transformador se degrada exponencialmente com a temperatura. Muitas vezes, o equipamento parece estar funcionando bem (matemática de carga estável), mas a IA consegue detectar que o padrão de aquecimento mudou nos últimos meses, indicando que o óleo isolante está perdendo eficiência.

* **Impacto:** Uma falha dessas pode deixar um bairro ou uma indústria inteira sem energia, gerando multas pesadíssimas para a concessionária.

## Tecnologias Utilizadas
- **Back-end & Orquestração:** 
    - **Django 5.x:** Framework principal para gestão de usuários, banco de dados e lógica de negócio.
    - **FastAPI:** Microserviço de alta performance dedicado exclusivamente à camada de Inferência de IA.
    - **Django REST Framework (DRF):** Para criação dos endpoints de integração.
    - **SQLite:** *Armazenamento de dados históricos de sensores e logs de manutenção. (Nivel para teste)
- **Inteligência Artificial & Ciência de Dados**
    - **Scikit-Learn:** Biblioteca base para o treinamento e execução dos modelos de classificação e regressão.
    - **Pandas & NumPy:** Manipulação e tratamento de grandes volumes de dados (ETL).
    - **Joblib:** Para serialização e carregamento rápido do modelo de IA treinado.
- **Front-end & Visualização:**
    - **HTML5 / CSS3 (Bootstrap 5):** Interface responsiva e com design industrial moderno.
    - **Chart.js :** Renderização de gráficos dinâmicos para visualização de séries temporais.
    - **JavaScript:** Orquestração de chamadas assíncronas (Async/Await) para o motor de IA e manipulação dinâmica do DOM para o sistema de temas.
- **DevOps & Integração:**
    - **Requests:** Biblioteca para comunicação síncrona/assíncrona entre Django e FastAPI.
    - **Pydantic:** Validação rigorosa de dados na entrada e saída do microserviço de IA.
    - **Python-dotenv:** Para gerenciar variáveis de ambiente (senhas e chaves de API) de forma segura.

## Arquitetura da Aplicação
A solução foi desenhada para oferecer máxima confiabilidade na tomada de decisão industrial, dividindo-se em duas camadas de inteligência complementares:
**1. Camada de Gestão e Regras de Negócio (Django)**
O Core da aplicação, responsável por:
- **Orquestração**: Receber os dados de telemetria e gerenciar o fluxo de informações.
- **Módulo Determinístico (Matemático)**: Implementação de cálculos baseados em normas técnicas. Este módulo valida se os dados atuais (Tensão, Corrente, Temperatura) violam limites físicos imediatos, garantindo segurança operacional (Segurança Hard-coded).
- **Interface (Dashboard):** Visualização em tempo real de métricas e alertas.

**2. Camada de Inteligência Preditiva (FastAPI + ML)**
Um microserviço especializado em processamento de dados históricos
- **Motor de Inferência:** Executa o modelo de Machine Learning (treinado previamente com dados de sensores).
- **Análise de Tendências:** Diferente do modelo matemático que olha o "agora", a IA identifica padrões de degradação ao longo do tempo (ex: aumento gradual de temperatura sob carga constante), prevendo falhas que ainda não violaram os limites normativos.
- **Output**: Retorna o nível de risco e a confiança da predição via JSON para o Django.

**3. Fluxo de Dados e Integração**
- Os dados de sensores (reais ou simulados) entram no Django.
- O Django realiza o Cálculo Matemático (Resultado A).
- Simultaneamente, o Django dispara uma requisição POST assíncrona para o FastAPI (Resultado B).
- O sistema consolida os resultados:
    - Se A e B indicam falha: Alerta de Criticidade Alta.
    - Se apenas B indica falha: Alerta de Manutenção Preditiva (Degradação Latente).


## Principais Funcionalidades
- **Monitoramento de Ativos com Contexto Global:**
    - Visualização em tempo real de parâmetros críticos (Temperatura, Torque, RPM) integrando uma barra de busca inteligente com auto-complete para navegação rápida entre milhares de dispositivos.
- **Análise Híbrida de Saúde (Health Score):**
    - Diagnóstico duplo que cruza o rigor da Engenharia Determinística (cálculo de Gradiente Térmico $\Delta T$) com a flexibilidade da Inteligência Artificial Probabilística.
- **Predição de Falhas por Anomalia Térmica:**
    - Motor de Machine Learning treinado em dataset massivo (10k+ registros) capaz de identificar riscos elevados (ex: 99%) mesmo quando os limites físicos de engenharia ainda não foram rompidos.
- **Benchmarking de Frota em Tempo Real:**
    - Gráfico comparativo dinâmico que posiciona o ativo atual frente à média de funcionamento da sua categoria (L, M, H) e ao ponto histórico crítico de falha.
- **Interface Adaptativa de Alta Performance:** 
    - Dashboard com suporte nativo a temas (Light/Dark mode), otimizado para centros de comando de monitoramento industrial.
- **Flexibilidade no processamento híbrido:**
    - Projetado para suportar 2 tipos de processamento, **1° - Machine Learning**, treinado com modelo de treinamento supervisionado. **2° - cálculo de Gradiente Térmico $\Delta T$**, permitindo assim os responsaveis estabelerecerem um limite a qual é seguro operar.
- **Integração via Microserviços:**
    - A View do Django atua como orquestradora, realizando chamadas via protocolo HTTP para o microserviço FastAPI. Esta arquitetura permite que o processamento pesado de Machine Learning seja isolado da lógica de negócio principal.

## Origem Dataset
1.  **Dataset:**  
    - kaggle - Predictive Maintenance Dataset (AI4I 2020) 

## Como Executar o Projeto
Para rodar a solução completa, você precisará de dois terminais abertos (um para o Django e outro para o Microsserviço de IA).

### 1. Preparação do Ambiente
```bash
# Clone o repositório
git clone [https://github.com/LucasDiasAlves/hackathon_inovSpin]
cd hackathon_inovSpin

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```
### 2. Rodando o Microserviço de IA (FastAPI)
O motor de predição deve estar ativo para que o Dashboard receba os dados de risco.
```bash
# Navegue até a pasta da IA (se houver uma) ou rode direto:
uvicorn main:app --port 8001 --reload
```
### 3. Rodando o Dashboard (Django)
Em um novo terminal, com o venv ativo:
```bash
# Execute as migrações (o banco db.sqlite3 já contém os dados de teste)
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```
    Acesse em seu navegador: http://127.0.0.1:8000/
---
#### Desenvolvido por: 
*Lucas Dias*
[linkedin](www.linkedin.com/in/lucas-dias-alves-52166a320)
**🗓️ Prazo:** Inicio: 27/02 **|** Entrega: 06/03. **uma semana!**