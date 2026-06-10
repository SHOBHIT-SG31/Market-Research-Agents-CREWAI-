from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

# define the crew class here 
@CrewBase
class MarketResearchCrew():
    """MarketResearchCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # provide the path for configuration files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    #=================Agents==============

    @agent
    def market_research_specialist(self) -> Agent:
        return Agent(
            config = self.agents_config["market_research_specialist"]
        )
    
    @agent
    def competitive_intelligenct_analyst(self) -> Agent:
        return Agent(
            config=self.agent_config["competitive_intelligenct_analyst"]
        )
    
    @agent
    def customers_insights_researcher(self) -> Agent:
        return Agent(
            config=self.agent_config["customers_insights_researcher"]
        )
    
    @agent
    def product_strategy_advisor(self) -> Agent:
        return Agent(
            config=self.agent_config["product_strategy_advisor"]
        )
    
    @agent
    def business_analyst(self) -> Agent:
        return Agent(
            config=self.agent_config["business_analyst"]
        )
    
    #========================TASKS=================

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config("market_research_task")
        )
    
    @task
    def competitive_intelligence_task(self) -> Task:
        return Task(
            config=self.tasks_config("competitive_intelligence_task")
        )
    
    @task
    def customer_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config("customer_insights_task")
        )
    
    @task
    def product_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config("product_strategy_task")
        )
    
    @task
    def business_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config["business_analyst_task"]
        )