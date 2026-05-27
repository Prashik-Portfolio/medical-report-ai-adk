from google.adk.agents import Agent

from agent.prompts import MEDICAL_REPORT_PROMPT
from agent.tools import save_report_as_pdf


medical_report_agent = Agent(
    name="medical_report_agent",

    model="gemini-2.5-flash",

    description=(
        "AI assistant that analyzes medical scan images "
        "and generates structured preliminary radiology reports."
    ),

    instruction=MEDICAL_REPORT_PROMPT,

    tools=[save_report_as_pdf]
)

root_agent = medical_report_agent