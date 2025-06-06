########################
## File: src/main.py ##
#######################

from pyautocad import Autocad
from files_handler import layers_config, beams_data, columns_data
from layer_manager import setup_layers
from beams import draw_beam_outline, draw_rebar

def main():
    """The main runner function
    """
    acad = Autocad(create_if_not_exists=True)
    
    # Layer Manager
    setup_layers(acad, layers_config)
    
    # Beams Manager
    draw_beam_outline(acad, beams_data,layer_name="beam_outline")
    draw_rebar(acad, beams_data, layer_name="beam_bottom_rebar")
    
    
    
    
    
    
if __name__ == "__main__":
    main()
   