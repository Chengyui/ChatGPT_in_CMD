import os
import openai
# openai.organization = "org-YrU4n40tpxZF6NiZdHl2eqws"
# openai.api_key = os.getenv("OPENAI_API_KEY")
import keyboard
openai.api_key = "sk-your api"


def askChatGPT(messages):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=0)
    return response['choices'][0]['message']['content']


# messages = [
#     {"role": "system", "content": ""},
#     # {"role": "user", "content": "人为什么要吃饭"},
# ]
messages = []
path = "conversation"
content_all = ""
title =""
last_input = "please make a summary as a title for this conversation，and make sure this title is valid as a file name in Windows, you should only output title"
while True:
    choice = input("1 for Continue 2 for end conversion: ")
    if choice=="1":
        first_input = input("input:\n ")
        content_all = content_all+"input: "+first_input+"\n\n"
        mess = dict()
        mess["role"] = "user"
        mess["content"] = first_input
        messages.append(mess)
        content = askChatGPT(messages)
        print("output:\n "+content)
        content_all = content_all+"output: "+content+"\n\n"
        # print("content_all: "+ content_all)
    elif choice=="2":
        mess = dict()
        mess["role"] = "user"
        mess["content"] = last_input
        messages.append(mess)
        content = askChatGPT(messages)
        for i in range(0,4):
            if content[0]=='\n' or content[0]=="\"":
                content = content[1:]
            if content[-1]=='\n' or content[-1]=='\"':
                content = content[:-1]
        title = content+".md"
        # path = path+"/"+title[2:]+".md"
        # print("content_all: "+content_all)
        folder_name = "conversation"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        path = os.path.join(folder_name, title)
        with open(path,'w') as f:
            f.write(content_all)
        print("conversion saved!!!!")
        break







