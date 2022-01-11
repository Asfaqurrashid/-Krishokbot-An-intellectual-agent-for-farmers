#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, jsonify, request
import chatbot_response


# In[ ]:


app = Flask(__name__)

@app.route('/')
def index():
    return "hello_world"

@app.route('/chatbot', methods=['POST'])
def chatbotResponse():
    question = request.form.get('question')
    response = chatbot_response.chatbot_response(question)
    return jsonify({"response": str(response)})

if __name__ == '__main__':
    app.run()


# In[ ]:




