from model.osrs.osrs_bot import OSRSBot
from model.runelite_bot import BotStatus
import utilities.game_launcher as launcher
import pathlib
import cv2
import os




class ScreenShotBot(OSRSBot, launcher.Launchable):
    screenshotfolder_path = pathlib.Path(__file__).parent.parent.parent.parent.resolve()
    screensfolder = os.path.join(screenshotfolder_path, "images", "screenshots")
    def __init__(self):
        bot_title = "BCD Tools Helper"
        description = "BCD Tools Helper"
        super().__init__(bot_title=bot_title, description=description)
        self.options_set = True
    def create_options(self):
       pass

    def save_options(self, options: dict):
            self.options_set = True   
            
    def launch_game(self):
        settings = pathlib.Path(__file__).parent.joinpath("custom_settings.properties")
        launcher.launch_runelite_with_settings(self, settings)

    def main_loop(self):
        self.Bot_view_game_view()
        self.Bot_view_MiniMap_view()
        self.Bot_view_ControlPanel_view()
        self.stop()

    def Bot_view_game_view(self):   
        print(self.screensfolder)
        image = self.bot_view(self.win.game_view)
        cv2.imwrite(os.path.join(self.screensfolder, "screenshotgameview.png"), image)
        self.log_msg(f"Game View Screenshot Saved")
      
    def Bot_view_ControlPanel_view(self):
        image = self.bot_view(self.win.control_panel)
        cv2.imwrite(os.path.join(self.screensfolder, "screenshotcontrolpanel.png"), image)
        self.log_msg(f"Control Panel Screenshot Saved")
   
        
    def Bot_view_MiniMap_view(self):
        image = self.bot_view(self.win.minimap)
        cv2.imwrite(os.path.join(self.screensfolder, "screenshotminimap.png"), image)
        self.log_msg(f"MiniMap Screenshot Saved")
       
                    

                            
   