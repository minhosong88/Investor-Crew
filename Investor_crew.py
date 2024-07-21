from crewai import Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI
from investor_agents import Agents
from investor_tasks import Tasks
import streamlit as st

from dotenv import load_dotenv
import os
load_dotenv()
model = os.getenv('OPENAI_MODEL_NAME')


class Investor_Crew:

    def __init__(self, company):
        self.company = company

    def run(self):
        agents = Agents()
        tasks = Tasks()

        researcher = agents.researcher()
        technical_analyst = agents.technical_analyst()
        finance_analyst = agents.financial_analyst()
        hedge_fund_manager = agents.hedge_fund_manager()

        research_task = tasks.research(researcher)
        technical_task = tasks.technical_analysis(technical_analyst)
        financial_task = tasks.finacial_analysis(finance_analyst)
        recommend_task = tasks.investment_recommendation(
            hedge_fund_manager,
            [
                research_task,
                technical_task,
                financial_task,
            ]
        )
        crew = Crew(
            agents=[
                researcher,
                technical_analyst,
                finance_analyst,
                hedge_fund_manager,
            ],
            tasks=[
                research_task,
                technical_task,
                financial_task,
                recommend_task,
            ],
            verbose=True,
            process=Process.hierarchical,
            manager_llm=ChatOpenAI(model=model),
            memory=True,
        )

        result = crew.kickoff(
            inputs=dict(
                company=self.company,
            ),
        )

        return result


st.set_page_config(
    page_title="Stock Analysis with CrewAI",
    page_icon="👨🏻‍👩🏾‍👦‍👧🏽",)
st.markdown(
    """
    # Investor Crew AI
    
    Welcome to Our Professional Stock Analysis Crew!
    
    Write down the name of a company, then our professional crew will do the research, the analysis and finally recommend to buy, hold or sell the stock of the company.
    
    """
)
company = st.text_input("Enter a company name:")

if company:
    company = Investor_Crew(company)
    with st.spinner('Analyzing...'):
        result = company.run()
    st.success('Analysis complete!')
    with open("investment_recommendation.md", "r") as file:
        final_decision = file.read()
    st.write(final_decision)
