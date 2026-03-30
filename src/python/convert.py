from heybuddy.wakeword import WakeWordMLPModel, WakeWordTransformerModel
import onnx
import onnxruntime

if __name__ == '__main__':
    MLP = True
    input_filename = "ozwell_i_m_done_final.pt"
    output_filename = "ozwell-i'm-done.onnx"
    if MLP:
        model = WakeWordMLPModel.from_file(f'./{input_filename}')
    else:
        model = WakeWordTransformerModel.from_file(f'./{input_filename}')
    model.save_onnx(f'../js/models/{output_filename}', opset_version=19, external_data=False)
    onnx.checker.check_model(f'../js/models/{output_filename}')
    
