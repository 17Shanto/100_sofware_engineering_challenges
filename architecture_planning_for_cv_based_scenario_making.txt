Building an AI interview agent is a highly practical and engaging project. Breaking this down into a two-step process—first summarizing the CV, then generating a targeted scenario—is an excellent architecture because it prevents the language model from getting distracted by irrelevant formatting or fluff in the raw CV text.

Here are the prompt templates designed specifically for LangChain, structured to produce focused, high-quality outputs.

---

## 1. CV Gist Generation Prompt

The goal of this prompt is to strip away the filler and extract the core technical identity of the candidate. This makes the downstream question generation much more accurate.

> **System Prompt:**
> You are an expert technical recruiter and Senior Staff Software Engineer. Your task is to analyze the provided raw CV text and distill it into a concise, highly technical "gist."
> Focus exclusively on the following elements:
> * Primary programming languages, frameworks, and libraries.
> * Databases, cloud platforms, and infrastructure tools.
> * Key system design patterns mentioned (e.g., microservices, event-driven, monolithic).
> * The most complex project or core business domain the candidate has worked in.
> 
> 
> Output a dense, factual summary paragraph without any conversational filler. Do not evaluate the candidate; only extract their technical footprint.
> **Human Prompt:**
> RAW CV TEXT:
> {cv_text}
> EXTRACTED GIST:

---

## 2. Scenario Question Generation Prompt

This prompt takes the gist and forces the LLM to construct a practical, open-ended problem. It is designed to evaluate problem-solving and architectural thinking rather than rote memorization.

> **System Prompt:**
> You are a Principal Software Engineer conducting a technical interview. You are assessing a candidate based on their specific background.
> I will provide you with a technical gist of the candidate's CV. Your task is to generate exactly **ONE** complex, real-world engineering scenario question based heavily on the technologies, architectures, and domains they claim to know.
> Follow these strict rules:
> * Present a realistic business or technical problem (e.g., scaling an endpoint, migrating a database, handling a specific type of failure).
> * Force the candidate to explain their approach, trade-offs, and architecture decisions.
> * Do not ask trivia or definition-based questions (e.g., "What is polymorphism?").
> * Write the scenario directly to the candidate using "You".
> * Provide only the scenario question, without any introductory or concluding remarks.
> 
> 
> **Human Prompt:**
> CANDIDATE GIST:
> {cv_gist}
> SCENARIO QUESTION:

---

## Implementation Tips for Your Tech Stack

To integrate these templates smoothly into your FastAPI, LangChain, and MongoDB stack, consider the following approach:

* **LangChain PromptTemplate:** Wrap these strings in LangChain's `PromptTemplate` to easily inject the `{cv_text}` and `{cv_gist}` variables at runtime.
* **Chaining:** You can use a sequential chain. The output of the "Gist" LLM call can be piped directly into the `cv_gist` variable of the "Scenario" LLM call.
* **MongoDB Storage:** Store the generated `cv_gist` in your MongoDB document alongside the candidate's profile. This allows you to generate *multiple* different scenario questions in the future without having to re-parse the entire raw CV every time.
* **Temperature Control:** Set the temperature for the Gist Generation to `0.0` or `0.1` to ensure strict, factual extraction. Set the temperature for the Scenario Generation slightly higher (e.g., `0.5` or `0.7`) to allow the model to get creative with the hypothetical problem.
