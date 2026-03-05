# AI Integration Mini-Lab: Document Assistant

**Model Name & Source:** OpenAI API (Model: `gpt-4o-mini`). 

**Rationale for Selection:** As per the assignment guidelines, I selected the OpenAI API to power this application. Specifically, I used the `gpt-4o-mini` model because it is highly optimized for fast, cost-effective text processing, making it ideal for Agile development. It excels at RAG-style (Retrieval-Augmented Generation) tasks, allowing me to build a simple but meaningful application that parses an uploaded document and answers domain-specific questions with high accuracy and low latency.

**Reflection on Responsible AI Use:**
When building AI tools like this document assistant, responsible AI principles are crucial. One primary concern is hallucination, where the model might generate plausible but incorrect answers based on its training data rather than the user's document. To mitigate this, I implemented a strict system prompt directing the model to "Answer questions ONLY using the uploaded document text" and to explicitly state if it does not know the answer. This bounds the AI's responses to factual retrieval. 

Additionally, data privacy is paramount since users may upload sensitive documents. Using OpenAI's API is a responsible choice here, as their enterprise API privacy policy ensures that user data sent via the API is not used to train their models. Even so, inherent biases in LLMs can influence how they summarize text, meaning human oversight is still required for critical decision-making based on the AI's output.