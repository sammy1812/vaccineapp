import justpy as jp
import pandas
from pytz import utc
data = pandas.read_csv("Book3.csv")
day_number = data.groupby(['date'])['Numberofdoses'].count()
chart_def = """
{

  chart: {
    type: 'lollipop'
  },

  accessibility: {
    point: {
      valueDescriptionFormat: '{index}. {xDescription}, {point.y}.'
    }
  },

  legend: {
    enabled: false
  },

  subtitle: {
    text: 'According to covid19india.org      '
  },

  title: {
    text: 'No. of vaccine doses in India'
  },

  tooltip: {
    shared: true
  },

  xAxis: {
    type: 'category',
    title: {
        text: 'Date'
    },
  },

  yAxis: {
    title: {
      text: 'No. of doses administered'
    },
  },

  series: [{
    name: 'No. of doses administered',
    data: [{
      name: 'China',
      low: 1427647786
    }, {
      name: 'India',
      low: 1352642280
    }, {
      name: 'United States',
      low: 327096265
    }, {
      name: 'Indonesia',
      low: 267670543
    }, {
      name: 'Pakistan',
      low: 212228286
    }, {
      name: 'Brazil',
      low: 209469323
    }, {
      name: 'Nigeria',
      low: 195874683
    }, {
      name: 'Bangladesh',
      low: 161376708
    }, {
      name: 'Russia',
      low: 145734038
    }, {
      name: 'Mexico',
      low: 126190788
    }]
  }]

}
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp,text="No. of Covid-19 vaccine doses",classes="text-h2 text-center q-pa-md")
    h2 = jp.QDiv(a=wp,text="This graph represents no. of Covid-19 vaccine doses in India",classes="text-h5 text-left")
    hc = jp.HighCharts(a=wp,options=chart_def)
    hc_data = [{"name":v1,"low":v2} for v1, v2 in zip(day_number.index, data['Numberofdoses'])]
    hc.options.series[0].data = hc_data
    return wp




jp.justpy(app)