# This is a crewai file and theses are the steps:
# 1. Setup: load secrets, define LLM and tools
# 2. Assemble the agent
# 3. Define the tasks
# 4. Form the crew
# 5. Kick off the crew

from crewai import Crew
from crewai import Task
from crewai import Agent
import os
from dotenv import load_dotenv
from crewai_tools import CSVSearchTool

# Load the secrets
load_dotenv()

# Define the LLM
os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"

# Define the tools
my_tool1 = CSVSearchTool('dataset_reduced_500.csv')

# Assemble the agent

analyst = Agent(
    role='Data Analyst',
    goal='Identify seismic risk areas in Greece',
    backstory="""You're a seismic expert and Data Analyst, focusing on earthquake data in Greece.
  Your task involves analyzing earthquake occurrences to identify the highest and lowest magnitudes,
  as well as detecting clusters of seismic activity. This analysis is crucial for pinpointing vulnerable areas,
  enabling authorities to devise emergency response plans tailored to the seismic risk profile of different regions.""",
    tools=[my_tool1],  # Optional, defaults to an empty list
    # llm=my_llm,  # Optional
    # function_calling_llm=my_llm,  # Optional
    max_iter=15,  # Optional
    max_rpm=None,  # Optional
    verbose=True,  # Optional
    allow_delegation=True,  # Optional
    # step_callback=my_intermediate_step_callback,  # Optional
    memory=True  # Optional
)

seismic_risk_advisor = Agent(
    role='Seismic Risk Expert',
    goal='Provide advise to the Greek government on how to prepare for future seismic events.',
    backstory="""You're a seismic expert focused on risk analysis.
  You have provided other countries with advise on how to prepare for future seismic events.
  Based on your eperience of how other big earthquakes have affected the world, you are tasked with providing advise to the Greek government on how to prepare for future seismic events.""",
    tools=[my_tool1],  # Optional, defaults to an empty list
    # llm=my_llm,  # Optional
    # function_calling_llm=my_llm,  # Optional
    max_iter=15,  # Optional
    max_rpm=None,  # Optional
    verbose=True,  # Optional
    allow_delegation=True,  # Optional
    # step_callback=my_intermediate_step_callback,  # Optional
    memory=True  # Optional
)

# Define the tasks

task1 = Task(
    description=(
        "Identify the highest magnitude earthquake in Greece during the period of time studied."
        "Identify 2 areas with the highest seismic activity in the last 30 days."
        "Provide a brief description of the areas."
    ),
    expected_output="A comprehensive report with the seismic activity in Greece in the 2 areas with the highest seismic activity in the last 30 days.",
    tools=[my_tool1],
    allow_delegation=True,
    agent=analyst,
    output_file='seismic_risk_report.md'
)

task2 = Task(
    description=(
        "Provide advise to the Greek government on how to prepare for future seismic events."
    ),
    expected_output="A comprehensive report with the 3 most important things the Greek government should do to prepare for future seismic events.",
    tools=[my_tool1],
    allow_delegation=False,
    agent=seismic_risk_advisor,
    output_file='emergency_response.md'
)

# Form the crew


crew = Crew(
    tasks=[task1, task2],
    agents=[analyst, seismic_risk_advisor]
)

# Kick off the crew
crew.kickoff()
