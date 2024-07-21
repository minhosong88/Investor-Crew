from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from tools.analysis_tool import Tools


class Agents:

    def technical_analyst(self):
        return Agent(
            role="Technical Analyst",
            goal="Analyses the movement of the price of a stock and provides insights on trends, entry points, resistance and support levels.",
            backstory="An expert in technical analysis, you are known for your ability to predict stock movements and trends based on historical data. You provide valuable insights to your customers.",
            verbose=True,
            tools=[],
        )

    def financial_analyst(self):
        return Agent(
            role="Financial Analyst",
            goal="Uses financial statements, insider trading data, and other financial metrics to evaluate a stock's financial health and performance.",
            backstory="You are a very experienced investment advisor who uses a combination of technical and fundamental analysis to provide strategic investment advice to your clients. You look at a company's financial health, market sentiment, and qualitative data to make informed recommnedations.",
            verbose=True,
            tools=[
                Tools.balance_sheet,
                Tools.income_stmt,
                Tools.insider_transaction,
            ],
        )

    def researcher(self):
        return Agent(
            role="Researcher",
            goal="Gathers, interpretes and summarize vast amounts of data to provide a comprehensive overview of the sentiment and news surrounding a stock.",
            backstory="You are skilled in gathering and interpreting data from various sources to give a complete picture of a stock's sentiment and news. You read each data sources carefully and extract the most important information. Your insights are crucial for making informed investment decisions.",
            verbose=True,
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                Tools.stock_news,
            ],
        )

    def hedge_fund_manager(self):
        return Agent(
            role="Hedge Fund Manager",
            goal="Manages a portfolio of stocks and makes strategic investment decisions to maximize returns using insights from financial analysts, technical analysts, and researchers.",
            backstory="You are a seasoned hedge fund manager with a proven track record of making profitable investment decisions. You are known for your ability to manage risk and maximize returns for your clients.",
            verbose=True,
        )
