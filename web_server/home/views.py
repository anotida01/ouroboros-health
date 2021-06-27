from datetime import time
from django.shortcuts import render
from home.models import Data

# Create your views here.
def home(request):

    err = False
    try:
        infile = open("data_reading.txt", "r")
    except Exception as e:
        err = True
        print(e)

    if (not err):
        data = infile.readline()
        infile.close()
        data = data.rstrip('\n')
        data = data.split(', ')
        if (len(data) != 3): err = True

    if (err):
        bpm = 0
        spO2 = 0
        timestamp = "N/A"
    else:
        timestamp = data[0]
        bpm =  "%.1f" % float(data[1])
        spO2 = "%.1f" % float(data[2])

        


    context_dict = {"timestamp":timestamp, "bpm":bpm, "spO2":spO2}

    return render(request, "home/home.html", context=context_dict)
