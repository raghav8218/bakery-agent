# BakeryAgent

A command-line tool that finds popular bakeries in any Indian city, pulls live details from the web, and returns structured data including locations, specialities, contact numbers, and source links.

---

## How It Works

1. **User Input:** You enter the name of a city (e.g., Pune, Bangalore, Kolkata).
2. **Web Search:** The app queries the Tavily Search API for live web results matching popular bakeries, contact info, and specialities.
3. **Structured Extraction:** The search snippets are handed to Google Gemini (`gemini-3.5-flash-lite`) with a strict prompt forbidding hallucinations.
4. **Validation:** Gemini extracts the details directly into Pydantic models (`Bakery` and `BakeryResult`), ensuring real URLs and consistent fields.
5. **Console Output:** The parsed bakery information is printed directly to the terminal.

---

## Tech Stack

- **Python 3.10+**
- **LangChain:** Orchestrates search calls and LLM invocations.
- **Tavily Search API (`langchain-tavily`):** Handles real-time web search retrieval.
- **Google Gemini (`langchain-google-genai`):** Model inference using `gemini-3.5-flash-lite`.
- **Pydantic:** Schema definition and structured output validation.
- **python-dotenv:** Loads API keys from `.env`.

---

## Project Structure

- `main.py` - User prompt loop, runs the search query, and prints the output.
- `tools.py` - Tavily search wrapper returning parsed titles, URLs, and snippet content.
- `llm.py` - Configures Gemini and attaches Pydantic structured output.
- `models.py` - Pydantic schemas (`Bakery`, `BakeryResult`).
- `requirements.txt` - Project dependencies.
- `.env.example` - Template for required environment variables.

---

## Setup & Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### 3. Run

```bash
python main.py
```

Enter a city name when prompted:

```text
enter a city: Mumbai

popular bakeries in Mumbai: 

Name: Yazdani Bakery
Contact: +91 22 2287 0771
Speciality: Irani chai, bun maska, and brun pav.
Location: Fort, South Mumbai 
Source: https://example.com/yazdani-bakery
----------------------------------------
```
