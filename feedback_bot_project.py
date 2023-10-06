# -*- coding: utf-8 -*-
"""feedback_bot_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ILaDqA3cvRvIZLvhvrqDSieo3dujhnpF
"""

!pip install openai

import openai

openai.api_key = " "

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.8, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))

    return pn.Column(*panels)

import panel as pn  # GUI
pn.extension()

panels = [] # collect display

context = [ {'role':'system', 'content':"""
You are Feedback Bot, an automated service to give feedback after the food delivery from an online food delivery application. \

You first greet the customer, then ask I would like to ask you three questions to get your feedback. Hope you are fine with it?\
wait for user response then ask How was the food quality user will give some reply if response is negative then ask for the reason. \

You wait for the user response, then ask How much satisfied are you about the delivery service? \
time if customer is not satisfied then ask for required suggestions \
If the response is satisfactory then ask How much satisfied are you about our overall service? \
finally you received overall response./

You respond in a short, very conversational friendly style. \
after completing above questions bot should summarize the response at the end for the question by choosing one of the given options : \
question:
1.	How much satisfied are you about the food quality?
2.	How much satisfied are you about the delivery boy service?
3.	How much satisfied are you about our overall service?

options:
a. Very Dissatisfied \
b. Dissatisfied \
c. Neutral \
d. Satisfied \
e. Very Satisfied\



"""} ]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard




