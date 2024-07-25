# Omnilogue: Multi-LLM Query App

Omnilogue is a Streamlit-based application that allows users to query multiple Language Models (LLMs) simultaneously. It supports ChatGPT, Claude, Llama 3, and Gemma 2B-9B-IT.

Live demo: [https://omnilogue.streamlit.app](https://omnilogue.streamlit.app)

## Demo
[![A short demo](http://img.youtube.com/vi/rmk1EyUAFvM/0.jpg)](http://www.youtube.com/watch?v=rmk1EyUAFvM)


## Features

- Query multiple LLMs simultaneously
- Upload API keys securely
- Select models based on available API keys
- Compare responses from different models

## Local Setup

1. Clone the repository:
```bash
git clone https://github.com/parthmshah1302/omnilogue.git
cd omnilogue
```

2. Create a conda environment using the provided `environment.yml` file:
```bash
conda env create -f environment.yml
```
3. Activate the environment:
```bash
conda activate multi-llm-app
```
4. Create an API keys file:
Create a text file named `api_keys.txt` with the following content (no double quotes):

```txt
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GROQ_API_KEY=your_groq_api_key
```
Replace `your_openai_api_key`, `your_anthropic_api_key`, and `your_groq_api_key` with your actual API keys.

5. Run the Streamlit app:
```bash
streamlit run app.py
```


6. Open your web browser and navigate to `http://localhost:8501` to use the app locally.

## Usage

1. Upload your `api_keys.txt` file using the file uploader in the app.
2. Select the models you want to query from the available options.
3. Enter your query in the text area.
4. Click the "Submit" button to send your query to the selected models.
5. View the responses from each model in the respective columns.

## Deployment

The app is currently deployed at [https://omnilogue.streamlit.app](https://omnilogue.streamlit.app). You can use this link to access the application without local setup.

## Security Note

Never share your API keys publicly. The `api_keys.txt` file should be kept secure and not committed to version control. **The deployed version does not store the API keys anywhere.** 

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.