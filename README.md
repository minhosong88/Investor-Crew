# Investor-Crew

Welcome to the Investor-Crew repository! This project provides an AI-powered tool for professional stock analysis. By leveraging advanced AI agents and tools, Investor-Crew offers comprehensive research, technical analysis, financial analysis, and investment recommendations for stocks.

## Table of Contents

- [Repository Structure](#repository-structure)
- [Tools](#tools)
- [Investor_Crew.py](#investor_crewpy)
  - [Streamlit Interface](#streamlit-interface)
- [Investor_Agents.py](#investor_agentspy)
- [Investor_Tasks.py](#investor_taskspy)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Repository Structure

- `db/` - Directory for database files.
- `tools/` - Directory containing analysis tools.
  - `analysis_tool.py` - Tools for stock analysis including stock price history, news, financial statements, and insider transactions.
- `.gitattributes` - Git attributes configuration file.
- `.gitignore` - Git ignore configuration file.
- `Investor_crew.py` - Main script to run the Investor-Crew AI.
- `README.md` - Project description and documentation (this file).
- `investor_agents.py` - Definition of AI agents with specific roles and tools.
- `investor_tasks.py` - Definition of tasks for research, analysis, and recommendations.
- `requirements.txt` - List of required Python packages.

## Tools

The `analysis_tool.py` script in the `tools` directory includes the following tools:

- **One month stock price history**: Retrieves a month's worth of stock price data as CSV.
- **Stock news URLs**: Retrieves URLs of news articles related to a stock.
- **Company's income statement**: Retrieves the income statement of a stock as CSV.
- **Company's balance sheet**: Retrieves the balance sheet of a stock as CSV.
- **Get insider transactions**: Retrieves insider transactions of a stock as CSV.

## Investor_Crew.py

This script defines the `Investor_Crew` class, which integrates AI agents and tasks to perform stock analysis. It uses the following agents:

- **Researcher**: Gathers and summarizes data on market sentiment and news.
- **Technical Analyst**: Analyzes stock price movements and trends.
- **Financial Analyst**: Evaluates the financial health and performance of a stock.
- **Hedge Fund Manager**: Makes investment recommendations based on the insights from other agents.

### Streamlit Interface

The `Investor_Crew.py` script also includes a Streamlit interface for user interaction. Users can input a company name, and the AI will provide a comprehensive analysis and investment recommendation.

## Investor_Agents.py

This script defines the `Agents` class with the following agents:

- **Technical Analyst**: Analyzes stock price trends and technical indicators.
- **Financial Analyst**: Uses financial data to evaluate stock performance.
- **Researcher**: Gathers and interprets data on market sentiment and news.
- **Hedge Fund Manager**: Manages stock portfolios and makes investment decisions.

## Investor_Tasks.py

This script defines the `Tasks` class with the following tasks:

- **Research**: Summarizes news and market sentiment.
- **Technical Analysis**: Provides detailed technical analysis of stock price movements.
- **Financial Analysis**: Evaluates the financial health of a company.
- **Investment Recommendation**: Provides a buy or sell recommendation based on the analysis.

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

### Clone the repository:

```bash
git clone https://github.com/minhosong88/Investor-Crew.git
cd Investor-Crew
```

### Set up environment variables by creating a .env file:

```plaintext
OPENAI_MODEL_NAME=your_openai_model_name
```

### Run the Streamlit interface:

```bash
streamlit run Investor_crew.py
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
