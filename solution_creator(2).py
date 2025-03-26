
# solution_creator.py
import gradio as gr
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_solutions(problem):
    try:
        prompt = f"""
        Someone is facing this problem: \"{problem}\"

        Generate 3 powerful, innovative, and realistic solutions they can take action on immediately.
        Present them clearly and use simple, human language.
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a world-class creative problem solver helping humans find practical solutions to their problems."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=600
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ ERROR: {str(e)}"

custom_css = """
body {
    background-color: #121212;
    color: #F4F4F4;
    font-family: 'Inter', sans-serif;
}

.gradio-container {
    background-color: #121212;
    color: #F4F4F4;
}

textarea, input, button {
    font-family: 'Inter', sans-serif;
}

button {
    background-color: #1E90FF;
    color: #121212;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
    border-radius: 6px;
    transition: background-color 0.2s ease;
}

button:hover {
    background-color: #00FFD1;
    color: #121212;
}

.output-textbox {
    background-color: #2C2F36;
    color: #F4F4F4;
}
"""

with gr.Blocks(css=custom_css) as interface:
    gr.Markdown("""<h1 style='text-align: center; color: #1E90FF;'>SOLVANTA</h1>
    <p style='text-align: center;'>The AI engine that gets you <strong>unstuck</strong>.</p>""")
    
    problem_input = gr.Textbox(label="Describe Your Problem", lines=4, placeholder="What's keeping you stuck?", elem_classes="input-textbox")
    output = gr.Textbox(label="AI Solutions", lines=10, interactive=False, elem_classes="output-textbox")
    submit_btn = gr.Button("Generate Solutions")

    submit_btn.click(generate_solutions, inputs=problem_input, outputs=output)

interface.launch(server_name="0.0.0.0", server_port=7860, inline=False)
