import pywhatkit  

# using Exception Handling to avoid unprecedented errors  
try:
    #recepient phone number and time
    # sending message to receiver using pywhatkit  
    pywhatkit.sendwhatmsg("+1 (845) 610-0367", "This is an automated WhatsApp message tutorial", 21, 9)  
    print("Successfully Sent!")  
except Exception as e:  
    # handling exception and printing error message  
    print("An Unexpected Error:", e)
