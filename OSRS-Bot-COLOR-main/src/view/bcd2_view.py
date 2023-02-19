
from typing import Dict, List
import customtkinter
import cv2
from PIL import Image, ImageTk,ImageOps
import pathlib
import numpy as np


class bcd2view(customtkinter.CTkFrame):
    H_minval = 0
    S_minval = 0
    V_minval = 0
    H_maxval = 179
    S_maxval = 255
    V_maxval = 255
    minimap = False
    gameview = False
    controlpanel = False
    HasFinishedRunning = True
    image_to_load = None

  
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.pack(padx=10, pady=10,expand=True, fill = "both")
        
        # Title
        self.search_label = customtkinter.CTkLabel(master=self.main_frame, text="BCD2 tools for finding colors", text_font=("Roboto Medium", 12))
        self.search_label.pack(padx=10, pady=10,fill="both")
       ################################################################################################################
       #create frame for hsv tools 
        # HSV Tools
        self.hsv_frame = customtkinter.CTkFrame(master=self.main_frame)
        self.hsv_frame.pack(side="left",anchor="w", padx=10, pady=5,fill="y")
        ################################################################################################################
        # create a new frame for the checkboxes
        self.checkbox_frame = customtkinter.CTkFrame(master=self.hsv_frame)
        self.checkbox_frame.pack(side="top", padx=10, pady=5)
        ################################################################################################################
        #creates check boxes
        self.lbl_SelectBotView = customtkinter.CTkLabel(master=self.checkbox_frame, text="Select Bot View", text_font=("Roboto Medium", 12))
        self.lbl_SelectBotView.pack(side="top", padx=10, pady=5)

        self.gameviewBox = customtkinter.CTkCheckBox(master=self.checkbox_frame, text="Game View",command=self.gameview_check)
        self.gameviewBox.pack(side="left", padx=10, pady=5)
        

        self.MiniMapBox = customtkinter.CTkCheckBox(master=self.checkbox_frame, text="Mini-map",command=self.minimap_check)
        self.MiniMapBox.pack(side="left", padx=10, pady=5)

        self.ControlPanelBox = customtkinter.CTkCheckBox(master=self.checkbox_frame, text="Control Panel",command=self.controlpanel_check)
        self.ControlPanelBox.pack(side="left", padx=10, pady=5)

       ################################################################################################################
        # create a new frame for the slider controls
        self.slider_controls_frame = customtkinter.CTkFrame(master=self.hsv_frame)
        self.slider_controls_frame.pack(side="top", padx=10, pady=5,expand=True,fill="both")

       ################################################################################################################
       #H-Min Val Slider
        self.lbl_H_min = customtkinter.CTkLabel(master=self.slider_controls_frame, text="H-min", text_font=("Roboto Medium", 12))
        self.lbl_H_min.pack(side="top", padx=10, pady=1,expand=True,fill="both")

        self.H_min_val = customtkinter.CTkLabel(master=self.slider_controls_frame, text=str(self.H_minval))
        self.H_min_val.pack(side="top", padx=10, pady=1,expand=True,fill="both")

        self.H_min_slider = customtkinter.CTkSlider(master=self.slider_controls_frame, from_=0, to=179,number_of_steps=179, command=self.slider_event_Hmin)
        self.H_min_slider.pack(side="top", padx=10, pady=1,expand=True,fill="both")
        
        
       ################################################################################################################
        #S-Min Val Slider
        
        
        self.lbl_S_min = customtkinter.CTkLabel(master=self.slider_controls_frame, text="S-min", text_font=("Roboto Medium", 12))
        self.lbl_S_min.pack(side="top", padx=10, pady=1,expand=True,fill="both")
        
        self.S_min_val = customtkinter.CTkLabel(master=self.slider_controls_frame, text=str(self.S_minval))
        self.S_min_val.pack(side="top", padx=10, pady=1,expand=True,fill="both")

        self.S_min_slider = customtkinter.CTkSlider(master=self.slider_controls_frame, from_=0, to=255,number_of_steps=255, command=self.slider_event_Smin)
        self.S_min_slider.pack(side="top", padx=10, pady=1,expand=True,fill="both")
       ################################################################################################################
        #V-Min Val Slider
        
        
        self.lbl_V_min = customtkinter.CTkLabel(master=self.slider_controls_frame, text="V-min", text_font=("Roboto Medium", 12))
        self.lbl_V_min.pack(side="top", padx=10, pady=1,expand=True,fill="both")

        self.V_min_val = customtkinter.CTkLabel(master=self.slider_controls_frame, text=str(self.V_minval))
        self.V_min_val.pack(side="top", padx=10, pady=1,expand=True,fill="both")

        self.V_min_slider = customtkinter.CTkSlider(master=self.slider_controls_frame, from_=0, to=255,number_of_steps=255, command=self.slider_event_Vmin)
        self.V_min_slider.pack(side="top", padx=10, pady=1,expand=True,fill="both")
        
       ################################################################################################################
        #H-Max Val Slider
        
        
        self.lbl_H_max = customtkinter.CTkLabel(master=self.slider_controls_frame, text="H-max", text_font=("Roboto Medium", 12))
        self.lbl_H_max.pack(side="top", padx=10, pady=1,expand=True,fill="both")
        
        self.H_max_val = customtkinter.CTkLabel(master=self.slider_controls_frame, text=str(self.H_maxval))
        self.H_max_val.pack(side="top", padx=10, pady=1,expand=True,fill="both")

        self.H_max_slider = customtkinter.CTkSlider(master=self.slider_controls_frame, from_=0, to=179,number_of_steps=179, command=self.slider_event_Hmax)
        self.H_max_slider.pack(side="top", padx=10, pady=1,expand=True,fill="both")
        
       ################################################################################################################
        #S-Max Val Slider
        
        
        self.lbl_S_max = customtkinter.CTkLabel(master=self.slider_controls_frame, text="S-max", text_font=("Roboto Medium", 12))
        self.lbl_S_max.pack(side="top", padx=10, pady=1,expand=True,fill="both")

        self.S_max_val = customtkinter.CTkLabel(master=self.slider_controls_frame, text=str(self.S_maxval))
        self.S_max_val.pack(side="top", padx=10, pady=1,expand=True,fill="both")

        self.S_max_slider = customtkinter.CTkSlider(master=self.slider_controls_frame, from_=0, to=255,number_of_steps=255, command=self.slider_event_Smax)
        self.S_max_slider.pack(side="top", padx=10, pady=10,expand=True,fill="both")
        
       ################################################################################################################
        #V-Max Val Slider
        
        
        self.lbl_V_max = customtkinter.CTkLabel(master=self.slider_controls_frame, text="V-max", text_font=("Roboto Medium", 12))
        self.lbl_V_max.pack(side="top", padx=10, pady=1,expand=True,fill="both")

        self.V_max_val = customtkinter.CTkLabel(master=self.slider_controls_frame, text=str(self.V_maxval))
        self.V_max_val.pack(side="top", padx=10, pady=1,expand=True,fill="both")

        self.V_max_slider = customtkinter.CTkSlider(master=self.slider_controls_frame, from_=0, to=255,number_of_steps=255, command=self.slider_event_Vmax)
        self.V_max_slider.pack(side="top", padx=10, pady=1,expand=True,fill="both")
    
    
       ################################################################################################################
       #save Color Text box
       
        self.enter_color_name = customtkinter.CTkEntry(master=self.slider_controls_frame, placeholder_text="Enter color name")
        self.enter_color_name.pack(side="top", padx=10, pady=10,expand=True,fill="both")
       
       ################################################################################################################
        #save color button
        
        self.save_color_button = customtkinter.CTkButton(master=self.slider_controls_frame,height=64, text="Save Color Proifle", command=self.add_color_to_list)
        self.save_color_button.pack(side="top", padx=10, pady=5,expand=True,fill="both")
  
        ################################################################################################################
        #Frame for images
        
        self.images_frame = customtkinter.CTkFrame(master=self.main_frame)
        self.images_frame.pack(side = "left", anchor="e", padx=10,pady =10,expand=True,fill="both")
        
        ################################################################################################################
        #screenshot frame
        self.screenshot_frame = customtkinter.CTkFrame(master=self.images_frame)
        self.screenshot_frame.pack(side="top", padx=10, pady=10,expand=True, fill="both")
        # schedule resizing code to be executed after a short delay
        self.after(100, self.import_screenshot) 
        
        ################################################################################################################
        #mask frame
        self.mask_frame = customtkinter.CTkFrame(master=self.images_frame)
        self.mask_frame.pack(side="top", padx=10, pady=0,expand=True,fill="both")
        self.after(100, self.imageUpdater)
        
        

##############################################################################################################################
    def on_closing(self):
        self.parent.destroy()

    
    def slider_event_Hmin(self,value):
        self.H_minval =int(value)
        self.H_min_val.configure(text=str(self.H_minval))
        self.imageUpdater()
      
        
   
    def slider_event_Smin(self,value):
        self.S_minval =int(value)
        self.S_min_val.configure(text=str(self.S_minval))
        self.imageUpdater()
       
     
        
    def slider_event_Vmin(self,value):
        self.V_minval =int(value)
        self.V_min_val.configure(text=str(self.V_minval))
        self.imageUpdater()
       
    
        
        
    def slider_event_Hmax(self,value):
        self.H_maxval =int(value)
        self.H_max_val.configure(text=str(self.H_maxval))
        self.imageUpdater()
    
    def slider_event_Smax(self,value):
        self.S_maxval =int(value)
        self.S_max_val.configure(text=str(self.S_maxval))
        self.imageUpdater()
       
    def slider_event_Vmax(self,value):
        self.V_maxval =int(value)
        self.V_max_val.configure(text=str(self.V_maxval))
        self.imageUpdater()
    
        
    def add_color_to_list(self):
        utils_path = pathlib.Path(__file__).resolve().parents[2] / "src" / "utilities"
        ColorFile = utils_path / "BetterColorDetection.py"
        color_name = self.enter_color_name.get()
        color_range = f'\t\t"{color_name}": (np.array([{self.H_minval}, {self.S_minval}, {self.V_minval}]), np.array([{self.H_maxval}, {self.S_maxval}, {self.V_maxval}])),\n'
        with open(ColorFile, "r+") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if "color_ranges" in line:
                    lines.insert(i+1, color_range)
                    break
            f.seek(0)
            f.write("".join(lines))
                
        
    def import_screenshot(self):
        height = self.screenshot_frame.winfo_height()
        width = self.screenshot_frame.winfo_width()

        self.screenshot_path = pathlib.Path(__file__).resolve().parents[2] / "src" / "images"/ "screenshots"
        
        if self.minimap:
            screenshot_filename = "screenshotminimap.png"
        elif self.gameview:
            screenshot_filename = "screenshotgameview.png"
        elif self.controlpanel:
            screenshot_filename = "screenshotcontrolpanel.png"
        else:
            # Default screenshot
            screenshot_filename = "splashscreen.png"
            
        self.screenshot = Image.open(f"{self.screenshot_path}/{screenshot_filename}")
        self.screenshot = ImageOps.contain(self.screenshot, (height, width))
        self.screenshot_tk = ImageTk.PhotoImage(self.screenshot)
            
        # Remove previous screenshot label from screenshot_frame
        for child in self.screenshot_frame.winfo_children():
            child.destroy()
        
        # Pack new screenshot label
        self.screenshotlabel = customtkinter.CTkLabel(master=self.screenshot_frame, image=self.screenshot_tk)
        self.screenshotlabel.pack(side='left', anchor='center', expand=True, fill='both')
        
        
    def imageUpdater(self):
        # Check if the image has been loaded already
        if self.image_to_load is None:
            # Load the image from the hard drive
            image_path = pathlib.Path(__file__).resolve().parents[2] / "src" / "images" /"screenshots"
            if self.minimap:
                screenshot_filename = "screenshotminimap.png"
            elif self.gameview:
                screenshot_filename = "screenshotgameview.png"
            elif self.controlpanel:
                screenshot_filename = "screenshotcontrolpanel.png"
            else:
                screenshot_filename = "splashscreen.png"
            image = cv2.imread(f"{image_path}/{screenshot_filename}")
            self.image_to_load = image
        else:
            # Use the image data already in memory
            image = self.image_to_load
        
        
        # Set minimum and maximum HSV values to display
        lower = np.array([self.H_minval, self.S_minval,self.V_minval])
        upper = np.array([self.H_maxval, self.S_maxval, self.V_maxval])

        # Convert to HSV format and color threshold
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(image, image, mask=mask)

        # Convert the OpenCV image to a PIL image
        imageRGB = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        
        pil_image = Image.fromarray(imageRGB)

        # Resize the PIL image to match the dimensions of the maskshot image
        pil_image = ImageOps.contain(pil_image,(420,800))

        # Create a PhotoImage from the resized PIL image
        self.image_to_display = ImageTk.PhotoImage(pil_image)
 

        # Add new screenshot label to screenshot_frame
        maskshotlabel_new = customtkinter.CTkLabel(master=self.mask_frame, image=self.image_to_display)
        maskshotlabel_new.pack(side='left', anchor='center', expand=True, fill='both')

        # Remove previous screenshot label from screenshot_frame
        for child in reversed(self.mask_frame.winfo_children()):
            if child != maskshotlabel_new:
                child.destroy()

        self.maskshotlabel = maskshotlabel_new
        self.HasFinishedRunning = True

        
    def minimap_check(self):
        self.minimap = True
        self.gameview = False
        self.controlpanel = False
        self.image_to_load = None
        self.import_screenshot()
        self.imageUpdater()
 
        
    def gameview_check(self):
        self.minimap = False
        self.gameview = True
        self.controlpanel = False
        self.image_to_load = None
        self.import_screenshot()
        self.imageUpdater()
      
        
    def controlpanel_check(self):
        self.minimap = False
        self.gameview = False
        self.controlpanel = True
        self.image_to_load = None
        self.import_screenshot()
        self.imageUpdater()
           
            
    
