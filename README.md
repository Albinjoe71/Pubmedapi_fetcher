# PubMed Paper Fetcher

This Python project was built to fetch research papers from the PubMed database based on a user-provided query. The program focuses on identifying papers authored by individuals affiliated with pharmaceutical or biotech companies and outputs the filtered results in a CSV file.

---

## What Was Done in This Project

### 1. **Fetching Papers**
- We used the **PubMed API** to retrieve research papers based on a search query provided by the user.
- The program supports PubMed’s advanced query syntax to enable flexible and precise searches.

### 2. **Filtering Non-Academic Authors**
- Authors affiliated with pharmaceutical or biotech companies were identified using heuristic-based filtering (e.g., looking for keywords like "pharma" in affiliations).
- The filtered papers were formatted into a CSV file with key metadata, including:
  - PubMed ID
  - Title
  - Publication Date
  - Names of Non-Academic Authors
  - Company Affiliations

### 3. **Command-Line Interface (CLI)**
- A simple CLI was created to:
  - Accept a search query.
  - Provide options to save the results to a CSV file or display them in the terminal.
  - Enable debugging for troubleshooting.

### 4. **Code Modularity and Packaging**
- The project was structured into modular components:
  - **`fetcher.py`**: Handles API interactions and filtering.
  - **`cli.py`**: Provides the user interface through command-line arguments.
- The project was packaged with **Poetry** for dependency management, and the script can be executed directly via Poetry.

### 5. **Output**
- Results were saved in a CSV file, making them easy to analyze or share. The CSV includes:
  - PubMed ID
  - Title of the paper
  - Publication date
  - Non-academic authors and their company affiliations.

---

## Limitations of the Current Approach

While the project successfully retrieves and filters papers, it has some limitations:
1. **Heuristic-Based Filtering**:
   - The filtering relies on specific keywords like "pharma" in author affiliations, which may miss non-academic authors affiliated with companies that don't use those terms.

2. **Lack of Abstract Analysis**:
   - The program does not analyze the paper's abstract or content, which limits its ability to determine relevance.

---

## Optimization Ideas: Taking It to the Next Level

### 1. **Using Named Entity Recognition (NER)**
- **What is NER?**
  - NER is a Natural Language Processing (NLP) technique to extract named entities such as organizations, locations, or people's names from text.
  
- **How NER Can Help:**
  - NER can dynamically identify company names and affiliations from author metadata or paper abstracts, making filtering more accurate than static keyword searches.
  
- **Tools**: 
  - **SpaCy** or **Hugging Face Transformers** for implementing NER.

---

### 2. **Using Natural Language Understanding (NLU)**
- **What is NLU?**
  - NLU extends NLP by understanding the intent and context behind the text.

- **How NLU Can Help:**
  - Analyze abstracts or the body of papers to:
    - Determine relevance to specific industries (e.g., pharmaceutical research).
    - Rank papers based on their significance to the search query.

- **Example**: Use NLU to prioritize papers that describe innovative drug trials.

---

### 3. **Leveraging Large Language Models (LLMs)**
- **What are LLMs?**
  - LLMs like OpenAI's GPT or Hugging Face models can process large text datasets and answer complex queries.

- **How LLMs Can Help:**
  - Summarize paper abstracts to provide users with concise insights.
  - Perform deeper text analysis to identify the role of non-academic authors in the research.
  
- **Example**: Integrate LLMs to classify papers based on their focus (e.g., clinical trials, molecular research).

---

### 4. **Creating a Retrieval-Augmented Generation (RAG) System**
- **What is RAG?**
  - RAG combines search retrieval and generative AI. It retrieves relevant information from a knowledge base and generates responses based on the retrieved data.

- **How RAG Can Help:**
  - Fetch relevant paper content from PubMed and use an LLM to answer user-specific questions like:
    - "What are the most cited papers on COVID-19 vaccines by biotech companies?"
    - "Which companies contributed to the development of a specific drug?"

- **Example**: Build a system where users can ask questions, and the RAG pipeline provides detailed, accurate answers by combining PubMed results with AI-generated insights.

---

## Future Work
1. **Graph Database Integration**:
   - Use **Neo4j** or **AWS Neptune** to represent papers, authors, and affiliations as nodes and their relationships as edges.
   - Enable advanced queries like finding collaboration networks between researchers and companies.

2. **NER and NLU Integration**:
   - Implement tools like **SpaCy** for NER and **Hugging Face Transformers** for NLU to improve filtering and relevance ranking.

3. **LLM Integration**:
   - Use models like GPT or BERT to provide intelligent summarization and deeper insights into research content.

4. **User-Friendly Interface**:
   - Create a web-based front-end for easier interaction with the system.

---

## How to Run the Project

### Prerequisites
- Python 3.7 or later
- Poetry (for dependency management)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Albinjoe71/Pubmedapi_fetcher/
   cd pubmed-fetcher
