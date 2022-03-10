from django.shortcuts import render, redirect
import pandas as pd
import pickle

def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['Name']
        year = request.POST['year']
        km = request.POST['km']
        fuel = request.POST['fuel']
        dealer = request.POST['dealer']
        trans = request.POST['trans']
        seats = request.POST['seats']
        rpm = request.POST['rpm']
        mil = request.POST['mil']
        eng = request.POST['eng']
        power = request.POST['power']
        owner = request.POST['owner']
        print('#####################')

        if name != "":
            df = pd.DataFrame(columns=['year','km_driven','fuel',
                                           'seller_type','transmission','seats',
                                           'torque_rpm','mil_kmpl','engine_cc','max_power_new',
                                           'First Owner','Fourth & Above Owner','Second Owner',
                                           'Test Drive Car','Third Owner'])
            Ownership = Helper(owner)
            df2 = {'year': int(year),'km_driven': float(km),'fuel': float(fuel),
                       'seller_type': int(dealer),'transmission': int(trans),'seats': int(seats),
                        'torque_rpm': float(rpm),'mil_kmpl': float(mil),'engine_cc': float(eng),
                       'max_power_new': float(power),'First Owner': Ownership[0],'Fourth & Above Owner':
                        Ownership[1],'Second Owner': Ownership[2],'Test Drive Car': Ownership[3],
                       'Third Owner': Ownership[4]}

            df = df.append(df2, ignore_index=True)
            # load the model from disk
            filename = 'polls/mypickle.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            res = loaded_model.predict(df)
            print(res)
        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})


def Helper(x):
    if x == '1':
        return [1, 0, 0, 0, 0]
    elif x == '2':
        return [0, 0, 1, 0, 0]
    elif x == '3':
        return [0, 0, 0, 0, 1]
    if x == '4':
        return [0, 1, 0, 0, 0]
    if x == '5':
        return [0, 0, 0, 1, 0]

