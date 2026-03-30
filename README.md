# hey-ozwell-demo
To convert a .pt model to a .onnx model, place the .pt model in `src/python` and set the variables `input_filename` and `output_filename` in `convert.py` accordingly, then `cd src/python` and run `convert.py`

To run demo, run the following:
    `cd src/js`
    `npm run build`
    `npm run start`
Then navigate to the address provided in your browser.

Code from the [hey-buddy](https://github.com/painebenjamin/hey-buddy) library was used to create this demo as well as to train the wake-word model.