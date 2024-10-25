import google.generativeai as genai

genai.configure(api_key="AIzaSyDKTQG4QEVPTwbKwiGpT_cHM1Pf_EtGbbY")
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
chat.send_message("From here on only respond in Yoda speak")
# to customize your bot:
# - make it respond verbally instead of with text in the console
# - add to the chat history before the chat begins to control the
#   behavior of the LLM.
# - Improve the User Interface of the program
# - come up with a list of possible use cases
usrmsg = ""
while True:
    usrmsg = input("Enter a message: ")
    if usrmsg == "quit":
        break
    from google.generativeai.types import HarmCategory, HarmBlockThreshold
    response = chat.send_message(usrmsg, safety_settings={HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH})
    print(response.text)
    