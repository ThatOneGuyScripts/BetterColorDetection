# BetterColorDetection
This is my color detection and CV files for Kelltoms OSBC.

Download files and merge them with your OSRS-Bot-COLOR-main or unpack them manually. 


This is a two part project part one in the screenshot bot. Make sure to initialize the bot in your OSRS init.py

```python
from.ScreenShotBot.ScreenShotBot import ScreenShotBot
```

Once you launch OSBC navigate to the osrs section and launch BCD Tools helper with runelite open (this can be used with other games as long as they have gameviews set up)

There are no options for the bot just press save. 

![image](https://user-images.githubusercontent.com/125089137/219783499-f3f7fe63-41cd-47b8-af30-adf0b6323438.png)

Now everytime you press play the bot will take a screenshot of the 3 main screen spaces we call to in bots. self.win._gameview, self.win.minimap, and self.win.control panel. The bot will only automatically stop. 

![image](https://user-images.githubusercontent.com/125089137/219784111-ada6f825-3579-49dc-ac20-cc852a0ca12f.png)

Now you can navigate back to "select a game" via the drop down menue. You should see a button called BCD 2.0.

![image](https://user-images.githubusercontent.com/125089137/219784399-4f2be156-be16-417d-afdd-bb7a4dae992b.png)

Once you press it the BCD2 Tools screen will open. 

![image](https://user-images.githubusercontent.com/125089137/219784815-69e890a6-c2a9-48a9-9e21-90bc35a81e1e.png)

Here you can select a one of the Bot views to open. These are the screen shot images ScreenShotBot previously made. (there is a glitch with the checkboxes currently every time you press one it will load an image independent of being checked on or off)

lets select game view. 

![image](https://user-images.githubusercontent.com/125089137/219785175-f989f025-9fe0-419c-93fa-763758cc4bf7.png)

this loads the bot views of the self.win.game_view. The upper picture is your screenshot and the lower picture is changed by the sliders. These dertermine your sliders determine your color profile threshholds. By moving the sliders you can determine your perfect hsv upper and lower values for the color you are trying to find. In the following picture I target the GE tellers purple shirt. 

![image](https://user-images.githubusercontent.com/125089137/219786041-618a0f09-df5f-487b-8a08-ee677d0642ac.png)

Underneath the color sliders you have a text box. Here is where you want to name the color you want to save. Here I'm naming it GeTellerPurple. Below the text entry box is a button called save color profile. When you press this button the color name and hsv values will automatically be saved into BCD's color library. ( DO NOT USE SPACES IN YOUR NAME! If you must use spaces use underscores such as GE_Teller_purple.

![image](https://user-images.githubusercontent.com/125089137/219786906-b6b76671-beac-4dc3-88d8-3cdc502d47e3.png)

Next is how you call this function from your bots. This function is called by using self.findcolor(gameview,"color") for example see below. The first line is using OSBC orignal call. The second line is using BCD. 

```python

#orignal code 
banks = self.get_all_tagged_in_rect(self.win.game_view, clr.OFF_ORANGE)

#code updated to work with BCD
banks = self.find_color(self.win.game_view, "orange")
```

