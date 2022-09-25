# Proof of Concept Visual Inspection Testbed 

This presumes that [tensorflow](https://www.tensorflow.org/install) has been installed on your machine. <br>

It is recommended to create a [virtual environment](https://docs.python.org/3/library/venv.html) before following the steps below.

### Usage

This code creates a clock inspection environment

```bash
pip3 install -r requirements.txt
```

In the same terminal, you should be able to then run
```bash
cd source
python3 webservice.py
```

In the different terminal, you should be able to then run, and place clocks in the right half of the screen.
```bash
cd source
python3 clocks_detection.py
```

If everything went well, when you point your browser to http://127.0.0.1:5000/static/chai_pointerlock.html, you should see something like:

![](https://github.ibm.com/ungana/Inspection-Testbed/blob/main/sample.gif)

This assumes that you kept the default settings for the webservice.


