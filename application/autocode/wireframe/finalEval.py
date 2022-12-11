from autocode.wireframe.Sampler import *
from autocode.wireframe.compiler.formatfile import *
from autocode.wireframe.compiler.webCompiler import *
import os

def runCode(pngpath):
    modelpath = "autocode/wireframe/weights-epoch-0010--val_loss-0.0064--loss-0.0115.h5"
    modeljson = "autocode/wireframe/model_json.json"
    outputpath = "autocode/wireframe/output"
    png_filename = os.path.basename(pngpath)
    sample_id = png_filename[:png_filename.find('.png')]
    smp_obj = Sampler(model_json_path=modeljson ,model_weights_path=modelpath)
    smp_obj.generate_gui(png_path=pngpath, print_generated_output=1,output_folder=outputpath, sample_id=sample_id)
    gui_path = "autocode/wireframe/output/{}.gui".format(sample_id)
    compileHTML(gui_path)
    return outputpath + "/" + sample_id + ".html"