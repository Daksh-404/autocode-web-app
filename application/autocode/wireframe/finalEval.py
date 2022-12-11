from Sampler import *
from compiler.formatfile import *
from compiler.webCompiler import *
import os

modelpath = "weights-epoch-0010--val_loss-0.0064--loss-0.0115.h5"
modeljson = "model_json.json"
outputpath = "output"
pngpath = "examples/drawn_example1.png"
png_filename = os.path.basename(pngpath)
sample_id = png_filename[:png_filename.find('.png')]
smp_obj = Sampler(model_json_path=modeljson ,model_weights_path=modelpath)
smp_obj.generate_gui(png_path=pngpath, print_generated_output=1,output_folder=outputpath, sample_id=sample_id)
gui_path = "output/{}.gui".format(sample_id)
compileHTML(gui_path)