import streamlit as st
import openai
from anthropic import Anthropic
from groq import Groq
import io

def parse_api_keys(file_content):
    api_keys = {}
    for line in file_content.split('\n'):
        if '=' in line:
            key, value = line.strip().split('=', 1)
            api_keys[key] = value
    return api_keys

def init_clients(api_keys):
    openai.api_key = api_keys.get("OPENAI_API_KEY")
    anthropic_client = Anthropic(api_key=api_keys.get("ANTHROPIC_API_KEY"))
    groq_client = Groq(api_key=api_keys.get("GROQ_API_KEY"))
    return anthropic_client, groq_client

def query_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error querying ChatGPT: {str(e)}"

def query_llama(client, prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-70b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error querying Llama 3: {str(e)}"

def query_gemma(client, prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gemma-7b-it",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error querying Gemma: {str(e)}"

def query_claude(client, prompt):
    try:
        message = client.completions.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens_to_sample=1000,
            temperature=0,
            prompt=f"\n\nHuman: {prompt}\n\nAssistant:",
        )
        return message.completion
    except Exception as e:
        return f"Error querying Claude: {str(e)}"

st.title("Multi-LLM Query App")

uploaded_file = st.file_uploader("Upload API Keys File", type="txt")

if uploaded_file is not None:
    file_content = io.StringIO(uploaded_file.getvalue().decode("utf-8")).read()
    api_keys = parse_api_keys(file_content)
    st.success("API keys loaded successfully!")

    anthropic_client, groq_client = init_clients(api_keys)

    available_models = []
    if "OPENAI_API_KEY" in api_keys:
        available_models.append("ChatGPT")
    if "GROQ_API_KEY" in api_keys:
        available_models.extend(["Llama 3", "Gemma 7B-IT"])
    if "ANTHROPIC_API_KEY" in api_keys:
        available_models.append("Claude")

    selected_models = st.multiselect("Choose models", options=available_models, default=available_models)

    user_input = st.text_area("Enter your query:", height=100)

    if st.button("Submit"):
        if user_input and selected_models:
            cols = st.columns(len(selected_models))
            for i, model in enumerate(selected_models):
                with cols[i]:
                    st.subheader(model)
                    if model == "ChatGPT":
                        st.write(query_chatgpt(user_input))
                    elif model == "Llama 3":
                        st.write(query_llama(groq_client, user_input))
                    elif model == "Gemma 7B-IT":
                        st.write(query_gemma(groq_client, user_input))
                    elif model == "Claude":
                        st.write(query_claude(anthropic_client, user_input))
        elif not user_input:
            st.warning("Please enter a query.")
        else:
            st.warning("Please select at least one model.")
else:
    st.info("Please upload an API keys file to proceed.")