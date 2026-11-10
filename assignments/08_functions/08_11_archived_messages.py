
# Jace Conrad
# Chapter 8
# dif 4/10
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

text_messages = ["Do you feel the power of python?", "the 76ers won last night!", 
"We have our first game this weekend!"]

sent_messages = []


send_messages(text_messages[:], sent_messages)

print("\nOriginal list:")
print(text_messages)

print("\nSent messages list:")
print(sent_messages)