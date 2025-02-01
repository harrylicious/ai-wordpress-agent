from crewai import Agent, Task, Crew, Process
from tools.wordpress_upload_tool import WordPressUploadTool
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()

def create_crew(topic: str, language_code: str) -> Crew:
    # Instantiate tools
    research_tool = SerperDevTool()
    wordpress_tool = WordPressUploadTool(
        wordpress_url=os.getenv("WORDPRESS_URL"),
        username=os.getenv("WORDPRESS_USERNAME"),
        password=os.getenv("WORDPRESS_PASSWORD")
    )

    # Define agents
    trend_analyst = Agent(
        role="Trend Analyst",
        goal=f"Research current trends related to {topic} and identify viral angles",
        verbose=True,
        allow_delegation=False,
        backstory="""You are a social media expert and trend analyst. You have a knack for 
        identifying viral topics and understanding what makes content shareable. You stay 
        up-to-date with the latest trends and can spot opportunities for engaging content.""",
        tools=[research_tool]
    )
    
    content_creator = Agent(
        role="Content Creator",
        goal="Create engaging, casual content with a friendly tone",
        verbose=True,
        allow_delegation=False,
        backstory="""You are a skilled content creator who specializes in writing 
        conversational, relatable content. You have a talent for breaking down complex 
        topics into easy-to-understand language and adding personality to your writing. 
        You write as if you're having a friendly chat with the reader."""
    )
    
    seo_specialist = Agent(
        role="SEO Specialist",
        goal="Optimize content for search engines while maintaining readability",
        verbose=True,
        allow_delegation=False,
        backstory="""You are an SEO expert who knows how to optimize content for search 
        engines without making it sound robotic. You understand keyword research, 
        meta descriptions, and how to structure content for both readers and search engines.""",
        tools=[research_tool]
    )
    
    translator = Agent(
        role="Language Adapter",
        goal=f"Translate and culturally adapt content for {language_code}",
        verbose=True,
        allow_delegation=False,
        backstory="""You are a cultural adaptation specialist who not only translates 
        language but also adapts content to resonate with the target culture. You understand 
        local idioms, references, and cultural nuances."""
    )
    
    publisher = Agent(
        role="Content Publisher",
        goal="Format and publish the optimized content",
        verbose=True,
        allow_delegation=False,
        backstory=f"""You are a detail-oriented publisher who ensures content is perfectly 
        formatted and properly structured before publication. You have expertise in WordPress 
        and know how to make content visually appealing. Don't include the title in the content.""",
        tools=[wordpress_tool]
    )

    # Define tasks
    trend_analysis_task = Task(
        description=f"""
        Research current trends related to '{topic}' and identify:
        - Popular discussions and viral content
        - Key audience interests and pain points
        - Trending hashtags and keywords
        - Engaging angles for content creation
        """,
        expected_output=f"""A detailed trend analysis report including:
        1. Top trending aspects of the topic
        2. Popular keywords and phrases
        3. Viral content examples
        4. Recommended content angles""",
        agent=trend_analyst
    )

    content_creation_task = Task(
        description=f"""
        Create engaging content based on the trend analysis that:
        - Uses a casual, conversational tone
        - Includes relatable examples and analogies
        - Incorporates storytelling elements
        - Maintains a friendly, approachable voice
        """,
        expected_output="A complete article draft with an engaging title and friendly content.",
        agent=content_creator,
    )

    seo_optimization_task = Task(
        description=f"""
        Optimize the content while maintaining its casual tone:
        - Integrate trending keywords naturally
        - Structure content for readability
        - Create meta description and title tags
        - Add internal linking suggestions
        """,
        expected_output="SEO-optimized content with metadata and structure recommendations",
        agent=seo_specialist,
    )

    translation_task = Task(
        description=f"""
        Translate and culturally adapt the content for {language_code}:
        - Maintain the casual, friendly tone
        - Adapt idioms and references
        - Preserve SEO optimization
        - Ensure cultural relevance
        """,
        expected_output="Culturally adapted content in the target language",
        agent=translator
    )

    publishing_task = Task(
        description=f"""
        Prepare and publish the content:
        - Format for optimal readability
        - Add appropriate media placeholders
        - Set up meta information
        - Publish with proper categorization
        """,
        expected_output="Published content with formatting and meta information",
        agent=publisher
    )

    # Create the crew
    return Crew(
        agents=[trend_analyst, content_creator, seo_specialist, translator, publisher],
        tasks=[
            trend_analysis_task,
            content_creation_task,
            seo_optimization_task,
            translation_task,
            publishing_task
        ],
        process=Process.sequential
    )