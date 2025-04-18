import tkinter as tk
import pymongo
#connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["PythonChat"]   # Create or connect to a database named "PythonChat"    
messages_collection = db["messages"]  # Create or connect to a collection named "messages"


# Create the main window
root = tk.Tk()
root.title("Python Chat")
root.geometry("400x500")





root.mainloop()
