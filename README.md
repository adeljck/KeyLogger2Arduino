# KeyLogger2Arduino

------

### Record Your Keyboard Input And Trans It To A Adruino Code,Help You To Build A BadUSB.

- Requirements

```shell
Jinja2==3.1.2
MarkupSafe==2.1.2
pynput==1.7.6
pyobjc-core==9.1.1
pyobjc-framework-ApplicationServices==9.1.1
pyobjc-framework-Cocoa==9.1.1
pyobjc-framework-Quartz==9.1.1
six==1.16.0
```

- Usage

​	Step 1 make a virtual environment use virtualenv modules with command below.

```shell
python -m virtualenv venv
```

​	Step2 install requirements with command below.

```shell
pip install -r requirements.txt
```

​	Step3 run main.py with command below then type your keyboard that you want your badusb behavior like.

​	Step4 finally the badusb Arduino code will generate at file "final_sketch.ino".