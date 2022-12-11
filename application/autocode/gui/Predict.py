import sys

from os.path import basename
from autocode.gui.Sampler import *
from autocode.gui.px2cd import *

def predictGUI(path):
    
    trained_weights_path = "autocode/gui/bin"
    trained_model_name = "Code-Automaton"
    input_path = path
    output_path = "autocode/gui/output"
    search_method = "greedy"

    meta_dataset = np.load("{}/meta_dataset.npy".format(trained_weights_path), allow_pickle=True)
    input_shape = meta_dataset[0]
    output_size = meta_dataset[1]

    model = AutoCode(input_shape, output_size, trained_weights_path)
    model.load(trained_model_name)

    sampler = Sampler(trained_weights_path, input_shape, output_size, CONTEXT_LENGTH)

    file_name = basename(input_path)[:basename(input_path).find(".")]
    evaluation_img = Utils.imgPreprocess(input_path, IMAGE_SIZE)

    result = None
    if search_method == "greedy":
        result, _ = sampler.predict_greedy(model, np.array([evaluation_img]))
        print("Result greedy: {}".format(result))
    else:
        beam_width = int(search_method)
        print("Search with beam width: {}".format(beam_width))
        result, _ = sampler.predict_beam_search(model, np.array([evaluation_img]), beam_width=beam_width)
        print("Result beam: {}".format(result))

    with open("{}/{}.gui".format(output_path, file_name), 'w') as out_f:
        out_f.write(result.replace(START_TOKEN, "").replace(END_TOKEN, ""))