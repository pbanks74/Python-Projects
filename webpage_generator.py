import webbrowser

f = open("webpage_generator.html", "w")    # Creates file if doesn't exist
f.write("Stay tuned for our amazing summer sale!")   # Adds data to file
f.close()                                                                  

webbrowser.open_new_tab("webpage_generator.html")
