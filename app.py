from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        popu = float(request.form['population'])
        demand = float(request.form['demand'])
        deten_period = float(request.form['detention_period'])
        flow_vel = float(request.form['flow_velocity'])
        d = int(request.form['sludge_depth'])
        
        if d == 1:
            sludge_depth = float(request.form['sludge_depth_value'])
            free_board = float(request.form['free_board'])
        else:
            sludge_depth = 0.5
            free_board = 0.5
        
        peak_demand = demand * popu * 1.5
        avg_demand = popu * demand
        
        vol = (deten_period * (peak_demand / 10)) / 24
        
        tank_length = deten_period * flow_vel
        
        tank_width = tank_length / 6
        
        tank_depth = (vol * 2 )/ (tank_length * tank_width)
        overall_depth = free_board + sludge_depth + tank_depth
        
        return render_template('result.html', vol=vol, tank_length=tank_length, tank_width=tank_width, tank_depth=tank_depth, overall_depth=overall_depth)
    
    return render_template('index.html')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(port=8000)

