#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Retrieve and Display Sections:

import wikipediaapi

headers = {
    'User-Agent': 'Your-User-Agent-String',
}

wiki = wikipediaapi.Wikipedia('en', headers=headers)
page = wiki.page(input())
sections = page.sections
print(f"Sections of {page.title}:")
for i, section in enumerate(sections, 1):
    print(f"{i}. {section.title}")


# In[2]:


#User Input for Section Selection:

user_input = input("Enter the number of the section you want to summarize and paraphrase: ")
try:
    section_number = int(user_input)
    if 1 <= section_number <= len(sections):
        section = sections[section_number - 1]
        section_text = section.text
        print(f"You selected section {section_number}: {section.title}")
        print(f"Section text:\n{section_text}")
    else:
        print(f"Invalid input. Please enter a number between 1 and {len(sections)}.")
except ValueError:
    print(f"Invalid input. Please enter a number, not a word or a symbol.")



# In[3]:


#Summarize the Selected Section:
import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are my personal assistant, summarize the text"},
        {"role": "user", "content": section_text}
    ],max_tokens=150
)

summary = response["choices"][0]["message"]["content"]
print(f"Summary:\n{summary}")


# In[7]:


#Paraphrase the Summary: 

import openai

openai.api_key = "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"

summary_to_paraphrase = summary

response_paraphrase = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are my personal assistant."},
        {"role": "user", "content": f"Paraphrase the following summary:\n{summary_to_paraphrase}"},
    ],max_tokens=150
)

paraphrased_summary = response_paraphrase["choices"][0]["message"]["content"]
print(f"Paraphrased Summary:\n{paraphrased_summary}")


# In[ ]:




