from flask import jsonify, Blueprint
from app.models import Data, Site


hourly_data = Blueprint('hourly', __name__, url_prefix='/data')

parameters = {'o3': 'ozone, µg/m-3', 'no2': 'nitrogen dioxide, µg/m-3', 'so2': 'sulfur dioxide, µg/m-3',
              'pm25': 'PM2.5 particles, µg/m-3', 'pm10': 'PM10 particles, µg/m-3'}


@hourly_data.route('/recent/all')
def all_recent_data():
    all_data = {}
    site_names = {i[1]: i[0] for i in site_codes.items()}
    def site_dict(code):
        site_name = site_names.get(code)
        d = {}
        d['info'] = get_info(site_name)
        d['latest_data'] = 'assign to a dict'
        return d
        # {'site_code': {'info': 'assign to a dict', 'latest_data': 'assign to a dict'}}
    codes = [site_codes.get(b) for b in site_list]
    for a in codes:
        all_data[a] = site_dict(a)
    return jsonify(all_data)
    if True:
        pass
    else:
        return jsonify({'message': 'no data'})
   


@hourly_data.route('/<pollutant>/<name>/')
def hourly_data_1(pollutant, name):
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper())
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/<pollutant>/<name>/<start>/')
def hourly_data_2(pollutant, name, start):
    date = reversed(start.split('-'))
    try:
        start = '{}/{}/{} 00:00:00'.format(*date)
    except IndexError:
        return jsonify({'message': 'no data'})
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper(), Data.time >= start)
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('<pollutant>/<name>/<start>/<end>')
def hourly_data_3(pollutant, name, start, end):
    start = reversed(start.split('-'))
    end = reversed(end.split('-'))
    try:
        start = '{}/{}/{} 00:00:00'.format(*start)
        end = '{}/{}/{} 00:00:00'.format(*end)
    except IndexError:
        return jsonify({'message': 'no data'})
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper(), Data.time >= start, Data.time <= end)
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/pollutants')
def pollutants():
    return jsonify({b: a for a, b in parameters.items()})
