import requests as rq
import tkinter as tk
import pandas as pd
import math
import re
import fractions

def run(metar):
    # Create the root Tk()
    root = tk.Tk()
    # Set the title
    root.title("COSC505 - Weather")
    # Create two frames, the list is on top of the Canvas
    list_frame = tk.Frame(root)
    draw_frame = tk.Frame(root)
    # Set the list grid in c,r = 0,0
    list_frame.grid(column=0, row=0)
    # Set the draw grid in c,r = 0,1
    draw_frame.grid(column=0,row=1)

    # Create the canvas on the draw frame, set the width to 800 and height to 600
    canvas = tk.Canvas(draw_frame, width=800, height=600)
    # Reset the size of the grid
    canvas.pack()

    # THESE ARE EXAMPLES! You need to populate this list with the available airports in the METAR 
    # which is given by metar parameter passed into this function.
    choices = df["Airport"].tolist()

    # Create a variable that will store the currently selected choice.
    listvar = tk.StringVar(root)
    # Immediately set the choice to the first element. Double check to make sure choices[0] is valid!
    listvar.set(choices[0])

    # Create the dropdown menu with the given choices and the update variable. This is stored on the
    # list frame. You must make sure that choices is already fully populated.
    dropdown = tk.OptionMenu(list_frame, listvar, *choices)
    # The dropdown menu is on the top of the screen. This will make sure it is in the middle.
    dropdown.grid(row=0,column=1)
    # This function is called whenever the user selects another. Change this as you see fit.
    def drop_changed(*args):
        # pulling the information from the row that corresponds to the selected airport. Converting it to a list so I can extract the info in the future
        airport_values = df.loc[df["Airport"] == listvar.get()].values.flatten().tolist()
        # pulling the relevant info from the list to create defined variable to use in the canvas.create_ commands later.
        time_value = airport_values[8]
        wind_speed_text = airport_values[11]
        gust_text = airport_values[12]
        alt_text = airport_values[7]
        Temp_Text = airport_values[13]
        Dew_Text = airport_values[14]
        vis_text = airport_values[15]
        wind_dir = airport_values[9]
        wind_speed_value = airport_values[10]
        # defining the coordinates for the boxes that display the temp and dew point gauges based on their values
        temp_gauge = 300 - (airport_values[5] * 2.22)
        dew_gauge = 300 - (airport_values[6] * 2.22)
        vis_gauge = 300 + (40 * airport_values[4])


        # defining the x2, y2 coordinates for the given cardinal direction ranges based on degrees
        if wind_dir == 0:
            x2 = 350
            y2 = 150
        elif 11 < wind_dir <= 34: 
            x2 = 372
            y2 = 105
        elif 34 < wind_dir <= 56:
            x2 = 385
            y2 = 115
        elif 56 < wind_dir <= 79:
            x2 = 395
            y2 = 131
        elif 79 < wind_dir <= 101:
            x2 = 400
            y2 = 150
        elif 101 < wind_dir <= 124:
            x2 = 395
            y2 = 169
        elif 124 < wind_dir <= 146:
            x2 = 385
            y2 = 186
        elif 146 < wind_dir <= 169:
            x2 = 372
            y2 = 196
        elif 169 < wind_dir <= 191:
            x2 = 350
            y2 = 200
        elif 191 < wind_dir <= 214:
            x2 = 327
            y2 = 196
        elif 214 < wind_dir <= 236:
            x2 = 314
            y2 = 186
        elif 236 < wind_dir <= 259:
            x2 = 304
            y2 = 169
        elif 259 < wind_dir <= 281:
            x2 = 300
            y2 = 150
        elif 281 < wind_dir <= 304:
            x2 = 304
            y2 = 131
        elif 304 < wind_dir <= 326:
            x2 = 314
            y2 = 115
        elif 326 < wind_dir <= 349:
            x2 = 327
            y2 = 105
        else:
            x2 = 350
            y2 = 100

        # for fun, changing the thickness of the arrow based on wind speeds (thicker line = faster speeds)
        if wind_speed_value <= 10:
            arrow_width = 2
        elif 10 < wind_speed_value <= 20:
            arrow_width = 4
        else:
            arrow_width = 6
        canvas.delete("all")
        # text for the airport label
        canvas.create_text(150, 100, font=("Times New Roman", 24), text=listvar.get(), fill="red", tags="airport_text")
        # text for the time
        canvas.create_text(150,130, font=("Times New Roman", 18), text= time_value, fill="blue", tags="time_text")
        # creating the gray wind gauge base circle
        canvas.create_oval(300,100,400,200,fill="gray",tags="wind_dir_circle")
        # creating the red circle in the middle
        canvas.create_oval(345,145,355,155, fill="red", tags="red_circle")
        # creating the wind gauge line
        canvas.create_line(350,150,x2,y2,arrow=tk.LAST, width = arrow_width) 
        # creating wind gauge text
        canvas.create_text(350,210, font=("Times New Roman", 10), text=wind_speed_text, fill="black", tags="wind_text")
        canvas.create_text(350,225, font=("Times New Roman", 10), text=gust_text, fill="black", tags="gust_text")             
        # creating the black altimeter base circle
        canvas.create_oval(300,250,400,350,fill="black",tags="wind_dir_circle")
        # creating the altimeter text
        canvas.create_text(350,300, font=("Times New Roman", 10), text=alt_text, fill="white", tags="alt_text")       
        # creating the temp gauge base rectangle
        canvas.create_rectangle(500,100,600,300, width=5,outline="black")  
        # creating the temp gauge temp bar
        canvas.create_rectangle(500, temp_gauge, 600, 300, width = 5, outline = "black", fill = "red", tags = "temp_bar")
        # creating the temp gauge dew bar
        canvas.create_rectangle(500, dew_gauge, 600, 300, width = 5, outline = "black", fill = "blue", tags = "dew_bar")
        # creating the text for the temp gauge
        canvas.create_text(550,315, font=("Times New Roman", 10), text=Temp_Text, fill="red", tags="temp_text")
        canvas.create_text(550,330, font=("Times New Roman", 10), text=Dew_Text, fill="blue", tags="dew_text")
        # creating the visibility gauge base rectangle
        canvas.create_rectangle(300,400,700,500, width=5,outline="black")
        # creating visibility fill bar
        canvas.create_rectangle(300, 400, vis_gauge, 500, width = 5, outline = "black", fill = "orange", tags = "vis_bar")
        # creating the visibility gauge text
        canvas.create_text(320,510, font=("Times New Roman", 10), text=vis_text, fill="green", tags="miles_text")
    # Listen for the dropdown to change. When it does, the function drop_changed is called.
    listvar.trace("w", drop_changed)
    # You need to draw the text manually with the first choice.
    drop_changed()
    # mainloop() is necessary for handling events
    tk.mainloop()

# Entry point for running programs
if __name__ == "__main__":
    # pulling all lines of info between "<!-- Data starts here -->" and "<!-- Data ends here -->"
    data = rq.get("https://aviationweather.gov/metar/data?ids=%40TOP&format=raw&date=&hours=0")
    needle = "<!-- Data starts here -->"
    needle_position = data.text.find(needle) + len(needle)
    data = data.text[needle_position:]
    needle = "<!-- Data ends here -->"
    needle_position = data.find(needle)
    data = data[:needle_position]
    # splitting the retrieved info string into a list of strings where each item is a line of the retrieved info
    lines = data.split("\n")
    # creating an empty list to append to later
    data_lines = []
    # iterating over the list of strings to find the airport data that is between "<code>" and "</code>" and appending that information to the data_lines list
    for i in range(0, len(lines)):
        airport_info = re.search(r"<code>(.+)</code>", lines[i])
        if airport_info:
            airport_info = airport_info.group(1)
            data_lines.append(airport_info)
        else:
            continue
# creating an empty dataframe with given column names
    df = pd.DataFrame(columns = ["Airport", "Time", "Wind_Data", "Gust_Speed", "Visibility", "Temp", "Dew", "Altimeter"])
# iterating over each list item (aka each airport's info) to find the necessary info and putting it into the dataframe where each airport and its relevant info becomes a new row
    for i in range(0, len(data_lines)):
        row = data_lines[i]
        airport = re.search(r"^([A-Z]{4}) ", row) # finding the airport ID
        if airport:
            airport = airport.group(1)  # airport = airport ID
        else:
            continue
        time = re.search(r" ([0-9]+)Z ", row) # finding the time
        if time:
            time = time.group(1) # time = time info
        else:
            time = 0    # setting time to a default value in case not found
        air_data = re.search(r" (VRB)?([0-9]+)G?([0-9]+)?KT ", row) # finding the wind speed/direction and gust info
        if air_data:
            wind_data = air_data.group(2) # wind_data = wind speed/direction
            gust_speed = air_data.group(3) # gust_speed = gust speed
            if gust_speed: # not all wind_datas will have gust speed so if gust_speed is present...
                gust_speed = gust_speed # ...gust_speed = gust_speed
            else:
                gust_speed = 0 # default value in case gust_speed is not present
        else:
            wind_data = 0 # default value in case not found
            gust_speed = 0 # default value in case not found
        vis = re.search(r" ([0-9]/)?([0-9]+)SM ",row) # finding visibility data
        if vis:
            vis = vis.group(0) # vis = visibility
        else:
            vis = 0    # default value in case not found
        temp_data = re.search(r" ([0-9]+)/([a-z0-9]+) ", row)
        if temp_data:
            temp = temp_data.group(1)
            dew = temp_data.group(2)
        else: 
            temp = 0 # default value in case not found
            dew = 0  # default value in case not found
        alt = re.search(r" A([0-9]{4}) ", row)
        if alt:
            alt = alt.group(1)
        else:
            alt = 0
        df = df.append({"Airport" : airport, "Altimeter" : alt, "Temp" : temp, "Dew" : dew, "Time" : time, "Wind_Data" : wind_data, "Visibility" : vis, "Gust_Speed" : gust_speed }, ignore_index = True)
    # parse data here

    # cleaning up the time column to be in EST with "am" or "pm"
    df["Time"] = df["Time"].str[2:] # removing the day characters at the beginning of time string
    df["Time"] = df["Time"].astype(str).astype(int) # converting to an integer to do mathon it to convert from zulu to EST
    # converting from zulu to EST
    df["Time"] = (2400 + df["Time"] - 400) % 2400
    # converting from 24 hour to 12hr with "am" and "pm"
    df.loc[df["Time"] < 100, "Time_EST"] = (df["Time"] + 1200).astype(str) + "am"
    df.loc[(df["Time"] <= 1159) & (df["Time"] >= 100), "Time_EST"] = df["Time"].astype(str) + "am"
    df.loc[(df["Time"] >= 1200) & (df["Time"] < 1300), "Time_EST"] = df["Time"].astype(str) + "pm" 
    df.loc[df["Time"] >=1300, "Time_EST"] = (df["Time"] - 1200).astype(str) + "pm"

    
 
    # converting Temp and Dew from celsius to fahrenheit
    df["Temp"] = df["Temp"].astype(str).astype(int) 
    df["Temp"] = round(((df["Temp"] * (9/5)) + 32),1)
    df["Dew"] = df["Dew"].astype(str).astype(int)
    df["Dew"] = round(((df["Dew"] * (9/5)) + 32),1)

    # adding a decimal to the altimeter values
    df["Altimeter"] = df["Altimeter"].str[0:2] + "." + df["Altimeter"].str[2:]

    # removing SM from the visibility column and converting any fractions to decimals    
    df["Visibility"] = df["Visibility"].str[1:-3]
    df["Visibility"] = [round(float(fractions.Fraction(x)), 2) for x in df["Visibility"]]


   
    # separating Wind_Data into Wind_Speed and Wind_Direction and converting to MPH
    df["Wind_Direction"] = df["Wind_Data"].copy()
    df["Wind_Direction"] = df["Wind_Direction"].str[:3]
    df["Wind_Direction"] = df["Wind_Direction"].astype(str).astype(int) 
    df["Wind_Speed"] = df["Wind_Data"].copy()
    df["Wind_Speed"] = df["Wind_Speed"].str[3:5]
    df["Wind_Speed"] = df["Wind_Speed"].astype(int) * 1.15 # converting from knots to MPH
    df["Wind_Speed"] = df["Wind_Speed"].astype(int) # converting to integer again bc that causes the decimal number to become a whole number and in the examples it looks like MPH is displayed as whole numbers

    # creating texts for the display to reference
    # adding MPH and CALM based on wind speeds
    df["Wind_Speed_Text"] = df["Wind_Speed"].copy()
    df["Wind_Speed_Text"] = df["Wind_Speed_Text"].astype(str) + "MPH"
    df.loc[df.Wind_Speed_Text == "0MPH", "Wind_Speed_Text"] = "CALM" # if no wind then replacing 0MPH with CALM

    # # adding Gusts to Gusts
    df["Gust_Speed_Text"] = df["Gust_Speed"].copy()
    df["Gust_Speed_Text"] = df["Gust_Speed"].astype(str).astype(int)
    df.loc[df.Gust_Speed_Text > 0, "Gust_Speed_Text"] = "Gust: " + df["Gust_Speed"].astype(str) + "MPH"
    df.loc[df.Gust_Speed_Text == 0, "Gust_Speed_Text"] = ""

    # creating the text values for temp, dew, and visibility to print
    df["Temp_Text"] = df["Temp"].copy()
    df["Temp_Text"] = df["Temp_Text"].astype(str) + "F"
    df["Dew_Text"] = df["Dew"].copy()
    df["Dew_Text"] = df["Dew_Text"].astype(str) + "F"
    df["Vis_Text"] = df["Visibility"].copy()
    df["Vis_Text"] = df["Vis_Text"].astype(str) + "SM"

    run(data)


