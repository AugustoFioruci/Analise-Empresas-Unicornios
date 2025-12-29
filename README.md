# 📊 Análise de Empresas Unicórnio (BI + ETL)

## 📌 Visão Geral
Projeto de análise de dados com foco em **empresas unicórnio**, utilizando um pipeline completo de **ETL**, **modelagem dimensional** e **visualização em Power BI**.  
O objetivo é transformar dados brutos em **insights de negócio claros e acionáveis**.

---

## 🧱 Arquitetura do Projeto
**Fluxo de dados:**

CSV (dados brutos) → Python (ETL) → PostgreSQL (Data Warehouse) → Power BI (Dashboard)

---

## 🛠️ Tecnologias Utilizadas
- Python (pandas, numpy)
- SQL / PostgreSQL
- Power BI
- Git & GitHub

---

## 🔄 ETL (Extract, Transform, Load)

### Extração
- Dataset real em formato CSV contendo informações de startups unicórnio.

### Transformação
- Tratamento de valores nulos  
- Padronização de colunas  
- Conversão de tipos e datas  
- Criação de tabelas dimensionais e fato  
- Modelagem em esquema estrela  

### Carga
- Dados carregados no PostgreSQL utilizando SQLAlchemy.

---

## 🗂️ Modelagem de Dados

### Dimensões
- **dim_company**: empresa, país, cidade, indústria  
- **dim_date**: data, ano, mês  

### Fato
- **fact_unicorn**: valuation, data de entrada e relacionamento com dimensões

---

## 📈 KPIs Desenvolvidos
- Quantidade total de empresas unicórnio  
- Valuation médio por empresa (US$ bilhões)  
- Valuation total de mercado (US$ trilhões)  
- Top 10 países com mais unicórnios  
- Evolução do número de unicórnios ao longo do tempo  

---

## 📊 Dashboard (Power BI)
O dashboard permite:
- Análise temporal do crescimento de unicórnios  
- Comparação entre países  
- Filtro dinâmico por período  
- Visualização clara para apoio à tomada de decisão  

---

## 🎯 Principais Insights
- Forte concentração de empresas unicórnio nos Estados Unidos  
- Crescimento acelerado a partir de 2018  
- Alto valuation médio por empresa  

---

## 🚀 Objetivo Profissional
Projeto desenvolvido para **portfólio de Analista de Dados / BI (Júnior)**, demonstrando:
- Estruturação de pipelines de dados  
- Modelagem dimensional  
- Escrita de SQL analítico  
- Comunicação eficiente de dados por meio de dashboards  
****
