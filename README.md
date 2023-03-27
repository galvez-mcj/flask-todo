# flask-todo
A simple to-do app made with Flask and Bootstrap

Tutorial from: https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=381s

Preview of the app:
![image](https://user-images.githubusercontent.com/123865026/227876535-10bf7906-30ce-40c2-bcef-007467667bea.png)


## How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```
For windows:
```
$ env\Scripts\activate.ps1
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
