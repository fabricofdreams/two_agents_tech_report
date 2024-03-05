# CrewAI Seismic Risk Analysis Documentation

## Overview

This project utilizes the CrewAI framework to analyze seismic risks in Greece. By assembling a crew of agents with specific roles and goals, the project aims to identify areas of high seismic activity and provide expert advice on preparing for future seismic events. This document outlines how to set up and execute the project, detailing the setup process, agent assembly, task definition, and execution.

## Prerequisites

Before starting, ensure you have the following prerequisites installed:

- Python 3.6 or later
- crewai package
- dotenv package (for loading environment variables)
- An appropriate CSV dataset for analyzing seismic activity (`dataset_reduced_500.csv` in this case)

## Setup

1. **Environment Preparation:**
   Load necessary secrets and define the Large Language Model (LLM) to be used for the project, specifying the OpenAI model name in the environment variables.

   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()
   os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"
   ```

2. **Define Tools:**
   Initialize any tools required by the agents. In this example, a `CSVSearchTool` is used to analyze a dataset on seismic activity.

   ```python
   from crewai_tools import CSVSearchTool
   my_tool1 = CSVSearchTool('dataset_reduced_500.csv')
   ```

## Assembling the Agents

Create agent instances with specific roles, goals, and tools. This project includes two agents: a Data Analyst and a Seismic Risk Expert.

### Data Analyst Agent

- **Role:** Data Analyst
- **Goal:** Identify seismic risk areas in Greece.
- **Backstory:** An expert in analyzing earthquake data to pinpoint vulnerable areas.

### Seismic Risk Advisor Agent

- **Role:** Seismic Risk Expert
- **Goal:** Advise the Greek government on future seismic event preparations.
- **Backstory:** A seasoned expert who has advised various countries on earthquake preparedness.

## Defining the Tasks

Set up tasks for the agents to execute, detailing the descriptions, expected outputs, and specifying the associated agent.

### Task 1

- **Description:** Identify the highest magnitude earthquake and areas of highest seismic activity in Greece.
- **Expected Output:** A report detailing seismic activity in the specified areas.

### Task 2

- **Description:** Provide advice on preparing for future seismic events.
- **Expected Output:** A report outlining key preparation strategies for the Greek government.

## Forming the Crew

Instantiate a `Crew` object with the defined tasks and agents. This is a crucial step that groups everything together for execution.

```python
from crewai import Crew

crew = Crew(
    tasks=[task1, task2],
    agents=[analyst, seismic_risk_advisor]
)
```

## Execution

Kick off the crew's operation, initiating the task execution process.

```python
crew.kickoff()
```

## Output

Upon successful execution, the crew generates two reports:

- `seismic_risk_report.md`: Contains details on the seismic activity in Greece, focusing on the areas with the highest activity.
- `emergency_response.md`: Provides advice to the Greek government on preparing for future seismic events.

## Conclusion

This project demonstrates the power of the CrewAI framework in assembling a team of AI-driven agents to tackle complex analysis tasks, such as seismic risk assessment. By leveraging specific tools and detailed task descriptions, CrewAI enables efficient and targeted analysis, resulting in actionable insights and recommendations.
