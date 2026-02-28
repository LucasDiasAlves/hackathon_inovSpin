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

* O Problema Real: O isolamento dos fios dentro de um transformador se degrada exponencialmente com a temperatura. Muitas vezes, o equipamento parece estar funcionando bem (matemática de carga estável), mas a IA consegue detectar que o padrão de aquecimento mudou nos últimos meses, indicando que o óleo isolante está perdendo eficiência.

* Impacto: Uma falha dessas pode deixar um bairro ou uma indústria inteira sem energia, gerando multas pesadíssimas para a concessionária.

## Tecnologias Utilizadas
- **Back-end & Orquestração:** 
    - Django 5.x: Framework principal para gestão de usuários, banco de dados e lógica de negócio.
    - FastAPI: Microserviço de alta performance dedicado exclusivamente à camada de Inferência de IA.
    - Django REST Framework (DRF): Para criação dos endpoints de integração.
    - SQLite: Armazenamento de dados históricos de sensores e logs de manutenção. (Nivel para teste)
- **Inteligência Artificial & Ciência de Dados**
    - Scikit-Learn: Biblioteca base para o treinamento e execução dos modelos de classificação e regressão.
    - Pandas & NumPy: Manipulação e tratamento de grandes volumes de dados (ETL).
    - Joblib: Para serialização e carregamento rápido do modelo de IA treinado.
- **Front-end & Visualização:**
    - HTML5 / CSS3 (Bootstrap 5): Interface responsiva e com design industrial moderno.
    - Chart.js : Renderização de gráficos dinâmicos para visualização de séries temporais.
    - JavaScript (Vanilla): Para requisições assíncronas ao backend e atualizações de dashboard sem refresh.
- **DevOps & Integração:**
    - Requests: Biblioteca para comunicação síncrona/assíncrona entre Django e FastAPI.
    - Pydantic: Validação rigorosa de dados na entrada e saída do microserviço de IA.
    - Python-dotenv: Para gerenciar variáveis de ambiente (senhas e chaves de API) de forma segura.

## Arquitetura da Aplicação
A solução foi desenhada para oferecer máxima confiabilidade na tomada de decisão industrial, dividindo-se em duas camadas de inteligência complementares:
**1. Camada de Gestão e Regras de Negócio (Django)**
O Core da aplicação, responsável por:
- Orquestração: Receber os dados de telemetria e gerenciar o fluxo de informações.
- Módulo Determinístico (Matemático): Implementação de cálculos baseados em normas técnicas. Este módulo valida se os dados atuais (Tensão, Corrente, Temperatura) violam limites físicos imediatos, garantindo segurança operacional (Segurança Hard-coded).
- Interface (Dashboard): Visualização em tempo real de métricas e alertas.

**2. Camada de Inteligência Preditiva (FastAPI + ML)**
Um microserviço especializado em processamento de dados históricos
- Motor de Inferência: Executa o modelo de Machine Learning (treinado previamente com dados de sensores).
- Análise de Tendências: Diferente do modelo matemático que olha o "agora", a IA identifica padrões de degradação ao longo do tempo (ex: aumento gradual de temperatura sob carga constante), prevendo falhas que ainda não violaram os limites normativos.
- Output: Retorna o nível de risco e a confiança da predição via JSON para o Django.

**3. Fluxo de Dados e Integração**
- Os dados de sensores (reais ou simulados) entram no Django.
- O Django realiza o Cálculo Matemático (Resultado A).
- Simultaneamente, o Django dispara uma requisição POST assíncrona para o FastAPI (Resultado B).
- O sistema consolida os resultados:
    - Se A e B indicam falha: Alerta de Criticidade Alta.
    - Se apenas B indica falha: Alerta de Manutenção Preditiva (Degradação Latente).


## Principais Funcionalidades
- **Monitoramento de Ativos em Tempo Real:** Dashboard interativo para visualização de telemetria (Tensão, Corrente, Temperatura e Carga).
- **Análise Híbrida de Saúde (Health Score):** Cálculo instantâneo da integridade do equipamento combinando normas técnicas de engenharia (determinístico) e inteligência artificial (probabilístico).
- **Predição de Falhas e Degradação:** Motor de IA que identifica anomalias sutis no comportamento térmico e elétrico, prevendo falhas antes que os limites de segurança sejam atingidos.
- **Geração Automática de Ações Preventivas:** O sistema não apenas aponta o risco, mas sugere intervenções baseadas no nível de criticidade (ex: "Solicitar análise de óleo", "Reduzir carga de pico").
- **Relatórios de Tendências:** Gráficos históricos que permitem comparar valores reais versus valores previstos pelo modelo de Machine Learning.

## Origem Dataset
1.  **Dataset:**  
    - kaggle - Predictive Maintenance Dataset (AI4I 2020) 
---
#### Desenvolvido por: 
*Lucas Dias*
[linkedin](www.linkedin.com/in/lucas-dias-alves-52166a320)
**🗓️ Prazo:** Inicio: 27/02 **|** Entrega: 06/03. **uma semana!**