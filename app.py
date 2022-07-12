######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
drinks=['Coca-Cola', 'Gatorade', 'Cranberry Juice', 'Apple Juice', 'Coconut Water']
sugar_values=[10, 5, 11, 10, 5]
calorie_values=[14, 9.7, 20.5, 15.9, 9.9]
color1='darkblue'
color2='lightblue'
mytitle='Beverage Comparison'

label1='Sugar, tsp'
label2='Calories, divided by 10'

########### Set up the chart

def make_that_cool_barchart(drinks, sugar_values, calorie_values, color1, color2, mytitle):
    sugar_content = go.Bar(
        x=drinks,
        y=sugar_values,
        name=label1,
        marker={'color':color1}
    )
    calories = go.Bar(
        x=drinks,
        y=calorie_values,
        name=label2,
        marker={'color':color2}
    )

    drink_data = [sugar_content, calories]
    drink_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    drink_fig = go.Figure(data=drink_data, layout=drink_layout)
    return drink_fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(drinks, sugar_values, calorie_values, color1, color2, mytitle)
    fig.write_html('docs/barchart.html')
    print('Barchart update successful.')
