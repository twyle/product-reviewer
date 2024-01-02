from dotenv import load_dotenv
load_dotenv()
from crewai import Crew
from textwrap import dedent

from product_review_agents import ProductReviewAgents
from product_review_tasks import ProductReviewTasks


class ProductReviewCrew:
  def __init__(self, product):
    self.product = product

  def run(self):
    agents = ProductReviewAgents()
    tasks = ProductReviewTasks()

    research_analyst_agent = agents.research_analyst()

    research_task = tasks.research(research_analyst_agent, self.product)

    crew = Crew(
      agents=[
        research_analyst_agent,
      ],
      tasks=[
        research_task,
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Product Analysis Crew")
  print('-------------------------------')
  company = input(
    dedent("""
      What is the product you want to analyze?
    """))
  
  product_crew = ProductReviewCrew(company)
  result = product_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)