from crewai import Task
from textwrap import dedent

class ProductReviewTasks():
    def research(self, agent, product):
        return Task(description=dedent(f"""
            Collect and summarize the most recent comments from the 
            products review from youtube.
            Maje sure to capture the sentiment of each comment, 
            what the user liked, did not like as well as other 
            features that they wish were present.

            Your final answer MUST be a report that includes a
            comprehensive summary of the reviews, capturing 
            the most loved features.
            
            {self.__tip_section()}

            Selected product by the customer: {product}
            """),
            agent=agent
        )
    
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commision!"