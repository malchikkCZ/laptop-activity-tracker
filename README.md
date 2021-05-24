# Laptop Activity Tracker

## Created by MalchikkCZ

This simple python script is designed to run in preset interval of time in the background to keep track of my laptop uptime using [pixe.la](https://pixe.la) website.

> Pixela is the API service. With this service, you can get a GitHub like graph that expresses the degree of your daily various activities on a basis with a vivid gradation. All operations are performed by API. And, it's free.

Enjoy this script and feel free to improve it to your own needs!

---

To successfully run this script on your own computer, you have to make a few changes. Firstly you have to set your own credentials to [pixe.la](https://pixe.la) API.

It is easy as setting `"token"` key in `ACCOUNT` dictionary to random string and setting `"username"` key in same dictionary to your own username. For more info visit [pixe.la](https://pixe.la) documentation [here](https://docs.pixe.la/).\

---

The next thing you need to set up is some automatization to run this script repeatedly, e.g. in *linux* you may use this set of commands:

   1. Go to your linux terminal (e.g. `ctrl-alt-T` on Ubuntu based systems)
   2. Type: `crontab -e`
   3. Scroll to the end of the document and add new line: 

      `*/5 * * * * /path/to/python3 /path/to/this/script`

      *e.g.*

      `*/5 * * * * /usr/bin/python3 /home/myusername/Downloads/main.py`

   3. Save the file and that's it!

If you are runnig Windows or MAC, you should try to google the right procedure to setting some kind of automatization yourself.

---

If you want this script to run more (or less) frequently, you need to change the constant `INTERVAL` inside of the script code, as well as to adjust the crontab entry. You may use the [crontab.guru](https://crontab.guru) website to help you with that.

## Follow me at [twitter](https://twitter.com/malchikkcz)!
