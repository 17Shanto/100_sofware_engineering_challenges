from langchain_core.output_parsers import StrOutputParser
from .prompt import CvPromt
from src.pdf_to_text.pdf_to_txt import convert_pdf_to_text
from src.llm.mistral_ai import MistralLLM
from langchain_core.prompts import ChatPromptTemplate
from src.pdf_to_text.pdf_to_txt import convert_pdf_to_text

cv_promt = CvPromt()
cv_text = convert_pdf_to_text()
ai_engine = MistralLLM()
# prompt = ChatPromptTemplate.from_template(cv_promt.get_cv_prompt_template())


prompt_template = ChatPromptTemplate.from_template(
            """
            System Prompt: You are an expert technical recruiter and Senior Staff Software Engineer. Your task is to analyze the provided raw CV text and distill it into a concise, highly technical "gist." Focus exclusively on the following elements:
            -Primary programming languages, frameworks, and libraries.
            -Databases, cloud platforms, and infrastructure tools.
            -Key system design patterns mentioned (e.g., microservices, event-driven, monolithic).
            -The most complex project or core business domain the candidate has worked in.

            Output a dense, factual summary paragraph without any conversational filler. Do not evaluate the candidate; only extract their technical footprint. Human Prompt: RAW CV TEXT: {cv_text} EXTRACTED GIST:
            """
        )

gist_chain = prompt_template| ai_engine.mistral_llm | StrOutputParser()



