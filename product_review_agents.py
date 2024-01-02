from crewai import Agent
from tools import FindProductVideoTools, FindProductReviewTools
from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI


class ProductReviewAgents():
    def research_analyst(self):
        return Agent(
        role='Product Video Researcher',
        goal="""Find the best product review videos from youtube""",
        backstory="""Known for your indepth knowledge of various videos that 
        analyze different products on youtube. Now you have to find the best video that 
        reviews the given product.""",
        llm=OpenAI(temperature=0.7),
        verbose=True,
        tools=[
            FindProductVideoTools.find_product_video_id,
            FindProductReviewTools.find_product_reviews
        ]
  )