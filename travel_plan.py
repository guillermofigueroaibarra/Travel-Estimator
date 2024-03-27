'''

    Author: Guillermo Figueroa
    Date: 05/14/2021
    Prog: travel_plan.py
    Class: CIS2531
    Description:
                This program prompts the user to enter the name of a city and the number of days the user wants to visit that city,
                the user gets in return the amount of money needed to pay travel expenses for that trip
                
'''




import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import trip as tp



class Travel_Plan:

    '''
        This class estimates the cost for a trip, depending upon
        the city or cities the user goes to.
    '''

    INTRO = "This calculator helps backpackers to determine how much money they will" + \
            "need for travel expenses to one or multiple destinations around the world. This program stores " + \
            "data for the daily cost of expenses for 137 different cities. This daily cost includes" + \
            " #1 dorm bed at a good or cheap hostel  #2 Three budget meals   #3 Two public transportation rides" + \
            " #4 One paid cultural attraction   # Three cheap beers or 'entertainment fund'." + \
            "This information was taken from the website 'www.priceoftravel.com'"
    
                   
                   

    
    def __init__(self):

        # create list of cities the user is planning to visit
        self.__citiesList = []


        # create window
        self.window = tk.Tk()

        # set the window color
        self.window.configure(bg='red4', bd = 50)
        
        # window size
        self.window.title("Backpacker's Travel Calculator")
        # set window placement
        self.window.geometry('1000x750+20+20')


        # ****** MENU OPTIONS ********

        # create the menu bar
        self.menuBar = tk.Menu(self.window)
        self.window.config(menu = self.menuBar)

        
        self.fileMenu = tk.Menu(self.menuBar, tearoff = 0)
        self.menuBar.add_cascade(label = 'File', menu = self.fileMenu)
        self.fileMenu.add_command(label = 'Save',
                                 command = self.saveFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label = 'Exit',
                                  command = self.window.destroy)

        


        

        # ******HEADER*******
        # create header frame
        self.headerFrame = tk.Frame(self.window)

        # label to display title
        self.winTitle = tk.Label(self.headerFrame, text = 'Backpacker Travel Estimator', font = ('Helvetica', 28, 'bold'), bg = 'red4', fg = 'Yellow')
        
        #place title label and image label using grid manager
        self.winTitle.grid(row = 0, column = 0)

        # place frames into the window
        self.headerFrame.pack(side = 'top')






        # ******INTRO**********

        # create Intro frame
        self.introFrame = tk.Frame(self.window)

        # label to display intro text
        self.introText_label = tk.Label(self.introFrame, text = Travel_Plan.INTRO, bg = 'red4', font = ('Helvetica', 10), wraplength = 650, fg = 'yellow', width = 120)


        # pack label into the frame
        self.introText_label.pack(side = 'top')
        
        #place frame into the window
        self.introFrame.pack(side = 'top', anchor = 'center', pady = 3)







        # ******RADIO BUTTONS********

        # create frame for radio buttons
        self.radioButtonFrame = tk.Frame(self.window)

        # label to ask user the city price range
        self.cityPriceRange_Label = tk.Label(self.radioButtonFrame, text = 'Check the cities available! What type of city are you looking for?', bg = 'white')
        

        
        # create radio buttons with integer variable
        self.radio_value = tk.IntVar()
        self.radioB1 = tk.Radiobutton(self.radioButtonFrame,
                                      text = 'Cheap',
                                      variable = self.radio_value,
                                      value = 1,
                                      fg = 'green',
                                      bg = 'white',
                                      command = self.displayCities)
        
        self.radioB2 = tk.Radiobutton(self.radioButtonFrame,
                                      text = 'Mid-Range',
                                      variable = self.radio_value,
                                      value = 2,
                                      fg = 'orange',
                                      bg = 'white',
                                      command = self.displayCities)
        
        self.radioB3 = tk.Radiobutton(self.radioButtonFrame,
                                      text = 'Expensive',
                                      variable = self.radio_value,
                                      value = 3,
                                      fg = 'red',
                                      bg = 'white',
                                      command = self.displayCities)
        
        
        
        self.cityPriceRange_Label.grid(row = 0, column = 0)
        self.radioB1.grid(row = 0, column = 1)
        self.radioB2.grid(row = 0, column = 2)
        self.radioB3.grid(row = 0, column = 3)
       
        

        # place frames into the window
        self.radioButtonFrame.pack(side = 'top', anchor = 'center', pady = 10)





        # ****** FRAME TO DISPLAY SUGGESTIONS ******

        # create frame to display label
        self.displayRec_Frame = tk.Frame(self.window)

        # label to display cities
        self.displayCities = tk.StringVar()
        self.cities_Label = tk.Label(self.displayRec_Frame, width = 100, height = 10,
                                     textvariable = self.displayCities,
                                     wraplength = 650,
                                     bg = 'white')

        self.cities_Label.grid(row = 0, column = 0)

        

         # place frame into window
        self.displayRec_Frame.pack(side = 'top', pady = 10, anchor = 'center')



        # ****** USER INPUT/QUESTIONS *******
        self.questions_Frame = tk.Frame(self.window, bg = 'red4')

        # create label and entry for the city the user wants to visit
        self.city_label = tk.Label(self.questions_Frame, text = 'What city would you like to visit?', bg = 'red4', fg = 'yellow', font = ('Helvetica', 12, 'bold italic'))
        self.city_entry = tk.Entry(self.questions_Frame, width = 30, bg = 'white')

        # create label and entry for the number of days the user wants to spend in that city
        self.days_label = tk.Label(self.questions_Frame, text = 'How many days?', bg = 'red4', fg = 'yellow', font = ('Helvetica', 12, 'bold italic'))
        self.days_entry = tk.Entry(self.questions_Frame, width = 30, bg = 'white')

        # place widgets using grid manager
        self.city_label.grid(row = 0, column = 0, padx = 40)
        self.city_entry.grid(row = 0, column = 1, padx = 40)
        self.days_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.days_entry.grid(row = 1, column = 1, padx = 10, pady = 3)

        # place frames into the window
        self.questions_Frame.pack(side = 'top', anchor = 'center', pady = 5)
        




        # ******* INVALID INPUT MESSAGE LABEL **********


        # string variable to display total
        self.displayError = tk.StringVar()

        
        # create frame for message box
        self.invalidMessage_Frame = tk.Frame(self.window, bg = 'white')

        # create label to display message
        self.message_Label = tk.Label(self.invalidMessage_Frame, textvariable = self.displayError, bg = 'red4', width = 130, fg = 'spring green', wraplength = 700)

        # pack label into frame
        self.message_Label.pack(side = 'left')

        # place frame in the window
        self.invalidMessage_Frame.pack(side = 'top')





        # ****** BUTTONS **********

        # create frame for buttons
        self.button_Frame = tk.Frame(self.window, bg = 'red4', pady = 10)

        # create the buttons
        self.addButton = tk.Button(self.button_Frame, text = 'Add', width = 10,
                                   command = self.add_destination)

        self.clearButton = tk.Button(self.button_Frame, text = 'Clear', width = 10,
                                     command = self.clear_fields)

        self.resetButton = tk.Button(self.button_Frame, text = 'Reset', width = 10,
                                    command = self.reset_program)
        
        self.exitButton = tk.Button(self.button_Frame, text = 'Exit', width = 10,
                                    command = self.exit)

        # pack buttons into frame
        self.addButton.pack(side = 'left', padx = 20)
        self.clearButton.pack(side = 'left', padx = 20)
        self.resetButton.pack(side = 'left', padx = 20)
        self.exitButton.pack(side = 'left', padx = 20)

        # place frame into the window to display it
        self.button_Frame.pack(side = 'top', pady = 5)



       
        
        # ****** LISTBOX/SCROLLBAR *******

        # create frame to display listbox
        self.displayBox_Frame = tk.Frame(self.window)
        self.scrollbar = tk.Scrollbar(self.displayBox_Frame, orient = tk.VERTICAL)
        self.listbox = tk.Listbox(self.displayBox_Frame,
                                  yscrollcommand = self.scrollbar.set,
                                  width = 120,
                                  height = 5)
        self.scrollbar.config(command = self.listbox.yview)

        # pack widgets into the frame
        self.scrollbar.pack(side = 'right', fill = tk.Y)
        self.listbox.pack(side = 'left', fill = tk.BOTH, expand = 1)

        # place listbox frame into the main window
        self.displayBox_Frame.pack(side = 'top', pady = 2)





        # ******* ESTIMATED TOTAL DISPLAY AND TOTAL NUMBER OF DAYS ********

        # create frame to display estimated total
        self.estimatedTotal_Frame = tk.Frame(self.window, bg = 'red4')

        # string variable to display total
        self.diplayEstimated_Total = tk.StringVar()
        self.displayDays_Total = tk.StringVar()


        #labels
        self.estimatedTotal_Text = tk.Label(self.estimatedTotal_Frame, text = 'Estimated total for the trip: ', bg = 'red4', fg = 'yellow', font = ('Helvetica', 14, 'bold'))
        self.estimatedTotal_Result = tk.Label(self.estimatedTotal_Frame, bg = 'red4', textvariable = self.diplayEstimated_Total, fg = 'yellow', font = ('Helvetica', 14, 'bold'))

        
        self.numberOfDays = tk.Label(self.estimatedTotal_Frame, text = 'Trip length: ', bg = 'red4', fg = 'yellow', font = ('Helvetica', 14, 'bold'))
        self.numberOfDays_Result = tk.Label(self.estimatedTotal_Frame, bg = 'red4', textvariable = self.displayDays_Total, fg = 'yellow', font = ('Helvetica', 14, 'bold'))
        
       # place widgets using grid manager
        self.estimatedTotal_Text.grid(row = 0, column = 0)
        self.estimatedTotal_Result.grid(row = 0, column = 1)
        self.numberOfDays.grid(row = 0, column = 2, padx = 20, pady = 2)
        self.numberOfDays_Result.grid(row = 0, column = 3, padx = 10)

        # pack frame into window
        self.estimatedTotal_Frame.pack(side = 'top', anchor = 'center')
                

    

        # start the window event loop
        self.window.mainloop()


    def saveFile(self):
        
        fileName = tk.filedialog.asksaveasfilename(initialdir = '/',
                                                    filetypes = [('Text Files', '*.txt'),
                                                                 ('All Files', '*.*')],
                                                    title = 'Select file',
                                                    defaultextension = '*.txt')

        citiesList = ''
        totalForAllCities, totalDays = self.displayTotal()
        
        citiesList = "******TRAVEL PLAN********" + '\n' + \
                     '\n' + self.displayCitiesList() + '\n' \
                     "TRIP LENGTH: " + str(totalDays) + ' days' + '\n' + \
                     "ESTIMATED TOTAL = " +  "$" + str(format(totalForAllCities, '.2f')) 

        
        if len(fileName) != 0:
            # open file
            self.file_var = open(fileName, 'w')
            # write in file
            self.file_var.write(citiesList)
            #close file
            self.file_var.close()

            
  

    
    def displayCities(self):

        cities = ''

        if self.radio_value.get() == 1:
            cities = tp.Trip.cheapCities()
            self.displayCities.set(cities)
        elif self.radio_value.get() == 2:
            cities = tp.Trip.midRangeCities()
            self.displayCities.set(cities)
        elif self.radio_value.get() == 3:
            cities = tp.Trip.expensiveCities()
            self.displayCities.set(cities)


    def add_destination(self):

        # clear error message
        self.displayError.set("")
  
        city = self.city_entry.get()
        days = self.days_entry.get()

        # if city is in the dictionary and number of days is greater than
        # 0, add it to the list
        if city in tp.Trip.cities and int(days) > 0:

        
            # create an object and add it to the list
            self.__citiesList.append(tp.Trip(city, int(days)))
            
            # display the object you created
            self.displayCitiesList()


            # update the estimated total label
            self.displayTotal()
            
        
        else:
            # display error message
            self.displayError.set("INVALID ENTRIES! PLEASE ENTER A VALID CITY FOLLOWED BY ITS COUNTRY (City, Country) OR MAKE SURE THE NUMBER OF DAYS IS GREATER THAN 0")
            print('incorrect')

        

        # clear and reset display
        self.clear_fields()

      
            
    def reset_program(self):

        # clear all fields
        self.clear_fields()
        
        # clear what's inside the box list
        self.listbox.delete(0, tk.END)

    
        # delete all objects in the citiesList
        self.__citiesList.clear()

        # display current total
        self.displayTotal()

        # hide error message
        self.displayError.set("")

        return
    
    def clear_fields(self):

        # clear city and days entry fields
        self.city_entry.delete(0, tk.END)
        self.days_entry.delete(0, tk.END)

        # set focus to description
        self.city_entry.focus()
        return

    def displayTotal(self):


        # returns total trip cost
        total = 0
        for cities in self.__citiesList:
            total += float(cities.cost)

        self.diplayEstimated_Total.set("$" + str(format(total, '.2f')))


        # returns trip length
        days = 0
        for cities in self.__citiesList:
            days += int(cities.days)
        self.displayDays_Total.set(str(days) + " days")
        
            
        return total, days
            
    def displayCitiesList(self):

        # clear 'old' list box
        self.listbox.delete(0, tk.END)

        # string variable to save in file
        cityListStrings = ''
        
        for cities in self.__citiesList:
        

            citiesStr = format("", '30s') + format(str(cities.city), '40s') + format(str(str(cities.days) + " days"), '30s') + \
                        "Daily cost for expenses: $" + format(str(tp.Trip.cities.get(cities.city)), '20s') + \
                        str("Total: $" + str((format(cities.cost, '.2f'))))


            cityListStrings += \
                      str(cities.city) + "\n" \
                      " Days: " + str(cities.days) +  "\n" \
                      " Daily cost for expenses: $" + str(tp.Trip.cities.get(cities.city)) +  "\n"\
                      " Total Cost:" + "$" + str(format(float(cities.cost), '.2f')) + "\n" + \
                      "--------------------------------------------------------------------------" + \
                      "\n"
            self.listbox.insert(tk.END, citiesStr)
            
        return cityListStrings
    
    def exit(self):
        answer = tk.messagebox.askyesno('Confirmation', 'Are you sure you want to exit?')

        if answer == True:
            self.window.destroy()
        return

if __name__ == '__main__':

    # create window
    travelPlan = Travel_Plan()
