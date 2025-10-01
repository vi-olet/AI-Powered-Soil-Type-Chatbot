# AI-Powered-Soil-Type-Chatbot


A command-line AI chatbot that answers questions about soil types at a specified location (default: Iowa, USA). It fetches soil data from the [SoilGrids API](https://rest.isric.org/soilgrids/v2.0/) and uses a **mock LLM** (predefined responses simulating a large language model) to provide conversational answers. The project is designed to integrate with real LLMs (e.g., Hugging Face, Gemini) when API connectivity is available, making it a lightweight AI prototype for agricultural applications.

## Features
- Fetches soil type for a given latitude/longitude (default: 42.0, -93.5, Central Iowa).
- Responds to questions like "What's the soil type at my field?" or "Is the soil good for corn?" using mock LLM responses.
- Operates offline with Chernozem as the fallback soil type if SoilGrids is unavailable.
- Simple, terminal-based interface for AI-driven soil queries.

## Prerequisites
- Python 3.8+
- Required Python packages (see `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/soil-chatbot.git
   cd soil-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the chatbot:
   ```bash
   python soil_chatbot.py
   ```

## Usage
- Run `python soil_chatbot.py`.
- At the prompt, ask questions like:
  - "What's the soil type at my field?"
  - "Is the soil good for corn?"
- Type `quit` to exit.
- If offline, the mock LLM uses Chernozem as the default soil type.

## Example Output
```
Fetching soil data...
Soil type: Chernozem
Ask about the soil at your field (or 'quit'): What's the soil type at my field?
Hey, your Iowa field has Chernozem soil—rich and fertile, great for crops like soybeans or corn!
Ask about the soil at your field (or 'quit'): Is the soil good for corn?
The Chernozem soil in your field is awesome for most crops, like corn or soybeans, due to its nutrient-rich profile. What are you planting?
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [SoilGrids](https://rest.isric.org/) for soil data.
- Built with Python and the `requests` library for AI-driven soil analysis.
