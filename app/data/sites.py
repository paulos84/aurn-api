from app.models import db, Site

def create_db():
    db.create_all()
    for site in site_list:
        site_info = Site(**get_info(site))
        db.session.add(site_info)
    db.session.commit()

def get_info(site):
    site_code = site_codes.get(site)
    region = regions.get(site)
    environ = environs.get(site)
    defra_url = 'https://uk-air.defra.gov.uk/networks/site-info?site_id=' + site_codes.get(site)
    geo = site_geo.get(site)
    map_url = 'https://maps.google.co.uk/?q=' + ', '.join(geo).replace(' ', '')
    lat = geo[0]
    long = geo[1]
    return {'name': site, 'site_code': site_code, 'region': region, 'environ': environ, 'defra_url': defra_url,
            'map_url': map_url, 'lat': lat, 'long': long}


site_geo = {
    'Aberdeen': ['57.157360', '-2.094278'],
    'Aberdeen Union Street Roadside': ['57.144555', '-2.106472'],
    'Aberdeen Wellington Road': ['57.133888', '-2.094198'],
    'Armagh Roadside': ['54.353728', '-6.654558'],
    'Aston Hill': ['52.503850', '-3.034178'],
    'Auchencorth Moss': ['55.792160', '-3.242900'],
    'Barnsley Gawber': ['53.562920', '-1.510436'],
    'Barnstaple A39': ['51.074793', '-4.041924'],
    'Bath Roadside': ['51.391127', '-2.354155'],
    'Belfast Centre': ['54.599650', '-5.928833'],
    "Belfast Stockman's Lane": ['54.572586', '-5.974944'],
    'Birkenhead Borough Road': ['53.388511', '-3.025014'],
    'Birmingham A4540 Roadside': ['52.476090', '-1.875024'],
    'Birmingham Acocks Green': ['52.437165', '-1.829999'],
    'Blackpool Marton': ['53.804890', '-3.007175'],
    'Bournemouth': ['50.739570', '-1.826744'],
    'Bradford Mayo Avenue': ['53.771245', '-1.759774'],
    'Brighton Preston Park': ['50.840836', '-0.147572'],
    "Bristol St Paul's": ['51.462839', '-2.584482'],
    'Bristol Temple Way': ['51.457968', '-2.583975'],
    'Bury Whitefield Roadside': ['53.559029', '-2.293772'],
    'Cambridge Roadside': ['52.202370', '0.124456'],
    'Camden Kerbside': ['51.544210', '-0.175269'],
    'Cannock A5190 Roadside': ['52.687298', '-1.980821'],
    'Canterbury': ['51.273990', '1.098061'],
    'Cardiff Centre': ['51.481780', '-3.176250'],
    'Carlisle Roadside': ['54.894834', '-2.945307'],
    'Charlton Mackrell': ['51.056250', '-2.683450'],
    'Chatham Roadside': ['51.374264', '0.547970'],
    'Chepstow A48': ['51.638094', '-2.678731'],
    'Chesterfield Loundsley Green': ['53.244131', '-1.454946'],
    'Chesterfield Roadside': ['53.231722', '-1.456944'],
    'Chilbolton Observatory': ['51.149617', '-1.438228'],
    'Christchurch Barrack Road': ['50.735454', '-1.780888'],
    'Coventry Allesley': ['52.411563', '-1.560228'],
    'Coventry Binley Road': ['52.407708', '-1.490082'],
    'Cwmbran': ['51.653800', '-3.006953'],
    "Derby St Alkmund's Way": ['52.922983', '-1.469507'],
    'Doncaster A630 Cleveland Street': ['53.518868', '-1.138073'],
    'Eastbourne': ['50.805778', '0.271611'],
    'Edinburgh St Leonards': ['55.945589', '-3.182186'],
    'Eskdalemuir': ['55.315310', '-3.206111'],
    'Exeter Roadside': ['50.725083', '-3.532465'],
    'Fort William': ['56.822660', '-5.101102'],
    'Glasgow High Street': ['55.860936', '-4.238214'],
    'Glazebury': ['53.460080', '-2.472056'],
    'Grangemouth': ['56.010319', '-3.704399'],
    'Grangemouth Moray': ['56.013142', '-3.710833'],
    'High Muffles': ['54.334944', '-0.808550'],
    'Horley': ['51.165865', '-0.167734'],
    'Hull Freetown': ['53.748780', '-0.341222'],
    'Hull Holderness Road': ['53.758971', '-0.305749'],
    'Inverness': ['57.481308', '-4.241451'],
    'Ladybower': ['53.403370', '-1.752006'],
    'Leamington Spa': ['52.288810', '-1.533119'],
    'Leamington Spa Rugby Road': ['52.294884', '-1.542911'],
    'Leeds Centre': ['53.803780', '-1.546472'],
    'Leeds Headingley Kerbside': ['53.819972', '-1.576361'],
    'Leicester A594 Roadside': ['52.638677', '-1.124228'],
    'Leicester University': ['52.619823', '-1.127311'],
    'Leominster': ['52.221740', '-2.736665'],
    'Liverpool Speke': ['53.346330', '-2.844333'],
    'London Bexley': ['51.466030', '0.184806'],
    'London Bloomsbury': ['51.522290', '-0.125889'],
    'London Eltham': ['51.452580', '0.070766'],
    'London Harlington': ['51.488790', '-0.441614'],
    'London Marylebone Road': ['51.522530', '-0.154611'],
    'London N. Kensington': ['51.521050', '-0.213492'],
    'London Westminster': ['51.494670', '-0.131931'],
    'Lullington Heath': ['50.793700', '0.181250'],
    'Luton A505 Roadside': ['51.892293', '-0.462110'],
    'Manchester Piccadilly': ['53.481520', '-2.237881'],
    'Manchester Sharston': ['53.371306', '-2.239218'],
    'Middlesbrough': ['54.569297', '-1.220874'],
    'Narberth': ['Easting/Northing: 214440', '212663'],
    'Newcastle Centre': ['54.978250', '-1.610528'],
    'Newport': ['51.601203', '-2.977281'],
    'Norwich Lakenfields': ['52.614193', '1.301976'],
    'Nottingham Centre': ['52.954730', '-1.146447'],
    'Nottingham Western Boulevard': ['52.969377', '-1.188851'],
    'Oldbury Birmingham Road': ['52.502436', '-2.003497'],
    'Oxford Centre Roadside': ['51.751745', '-1.257463'],
    'Oxford St Ebbes': ['51.744806', '-1.260278'],
    'Peebles': ['55.657472', '-3.196527'],
    'Plymouth Centre': ['50.371670', '-4.142361'],
    'Plymouth Tavistock Road.': ['50.411058', '-4.130288'],
    'Port Talbot Margam': ['51.583950', '-3.770822'],
    'Portsmouth': ['50.828810', '-1.068583'],
    'Preston': ['53.765590', '-2.680353'],
    'Reading London Road': ['51.454896', '-0.940382'],
    'Reading New Town': ['51.453090', '-0.944067'],
    'Rochester Stoke': ['51.456170', '0.634889'],
    'Salford Eccles': ['53.484810', '-2.334139'],
    'Sandy Roadside': ['52.132417', '-0.300306'],
    'Scunthorpe Town': ['53.586340', '-0.636811'],
    'Shaw Crompton Way': ['53.579283', '-2.093786'],
    'Sheffield Barnsley Road': ['53.404950', '-1.455815'],
    'Sheffield Devonshire Green': ['53.378622', '-1.478096'],
    'Sheffield Tinsley': ['53.410580', '-1.396139'],
    'Southampton A33': ['50.920265', '-1.463484'],
    'Southampton Centre': ['50.908140', '-1.395778'],
    'Southend-on-Sea': ['51.544206', '0.678408'],
    'St Helens Linkway': ['53.451826', '-2.742134'],
    'St Osyth': ['51.777980', '1.049031'],
    'Stanford-le-Hope Roadside': ['51.518167', '0.439548'],
    'Stockton-on-Tees Eaglescliffe': ['54.516667', '-1.358547'],
    'Stoke-on-Trent A50 Roadside': ['52.980436', '-2.111898'],
    'Stoke-on-Trent Centre': ['53.028210', '-2.175133'],
    'Sunderland Silksworth': ['54.883610', '-1.406878'],
    'Sunderland Wessington Way': ['54.918390', '-1.408391'],
    'Swansea Roadside': ['51.632696', '-3.947374'],
    'Thurrock': ['51.477070', '0.317969'],
    'Walsall Woodlands': ['52.605621', '-2.030523'],
    'Warrington': ['53.389280', '-2.615358'],
    'Wicken Fen': ['52.298500', '0.290917'],
    'Widnes Milton Road': ['53.365391', '-2.731680'],
    'Wigan Centre': ['53.549140', '-2.638139'],
    'Wirral Tranmere': ['53.372870', '-3.022722'],
    'Worthing A27 Roadside': ['50.832947', '-0.379916'],
    'Wrexham': ['53.042220', '-3.002778'],
    'Yarner Wood': ['50.597600', '-3.716510'],
    'York Bootham': ['53.967513', '-1.086514'],
    'York Fishergate': ['53.951889', '-1.075861']
}

site_codes = {'Swansea Roadside': 'SWA1', 'Bath Roadside': 'BATH', 'London Haringey Priory Park South': 'HG4',
              'Blackburn Accrington Road': 'BLAR', 'Narberth': 'PEMB', 'Horley': 'HORE', 'Aston Hill': 'AH',
              'Hafod-yr-ynys Roadside': 'CAE6', 'Aberdeen Union Street Roadside': 'ABD7',
              'Bradford Mayo Avenue': 'BDMA', 'London Westminster': 'HORS', 'Ealing Horn Lane': 'EA8',
              'Lullington Heath': 'LH', 'Grangemouth Moray': 'GRA2', 'Lincoln Canwick Road': 'LIN3',
              'Birkenhead Borough Road': 'BBRD', 'Sheffield Tinsley': 'SHE', 'Aberdeen': 'ABD',
              'Greenock A8 Roadside': 'GKA8', 'Portsmouth': 'PMTH', 'York Bootham': 'YK10', 'Armagh Roadside': 'ARM6',
              'Coventry Binley Road': 'COBR', 'Blackpool Marton': 'BLC2', 'Sunderland Wessington Way': 'SUNR',
              'Southampton Centre': 'SOUT', 'Glasgow High Street': 'GHSR', 'Camden Kerbside': 'CA1',
              'Reading London Road': 'REA5', 'Wrexham': 'WREX', 'Yarner Wood': 'YW', 'Aberdeen Wellington Road': 'ABD8',
              'Christchurch Barrack Road': 'CHBR', 'York Fishergate': 'YK11', 'Chatham Roadside': 'CHAT',
              'Storrington Roadside': 'STOR', 'Stockton-on-Tees Eaglescliffe': 'EAGL', 'Leamington Spa': 'LEAM',
              'Exeter Roadside': 'EX', 'Bush Estate': 'BUSH', 'Stanford-le-Hope Roadside': 'HOPE',
              'Grangemouth': 'GRAN', 'Chilbolton Observatory': 'CHBO', 'London Marylebone Road': 'MY1',
              'Leeds Headingley Kerbside': 'LED6', 'Middlesbrough': 'MID', 'Newcastle Cradlewell Roadside': 'NCA3',
              'London Bloomsbury': 'CLL2', 'Barnsley Gawber': 'BAR3', 'London Harlington': 'HRL',
              'Coventry Allesley': 'COAL', 'Tower Hamlets Roadside': 'TH2', 'Brighton Preston Park': 'BRT3',
              'Barnstaple A39': 'BPLE', 'Eskdalemuir': 'ESK', 'Southampton A33': 'SA33', 'Eastbourne': 'EB',
              'Hull Freetown': 'HUL2', 'Worthing A27 Roadside': 'WTHG', 'Southend-on-Sea': 'SEND',
              'Birmingham Acocks Green': 'AGRN', 'Auchencorth Moss': 'ACTH', 'Glazebury': 'GLAZ',
              'Northampton Spring Park': 'NTN4', "Belfast Stockman's Lane": 'BEL1',
              'Sheffield Devonshire Green': 'SHDG', 'Lough Navar': 'LN', 'Chepstow A48': 'CHP',
              'Chesterfield Loundsley Green': 'CHLG', 'Rochester Stoke': 'ROCH', 'Manchester Sharston': 'MAHG',
              "Bristol St Paul's": 'BRS8', 'Plymouth Centre': 'PLYM', 'Leicester A594 Roadside': 'LEIR',
              'Dumbarton Roadside': 'DUMB', 'Charlton Mackrell': 'MACK', 'London Harrow Stanmore': 'HR3',
              'Bournemouth': 'BORN', 'Saltash Callington Road': 'SASH', 'Cambridge Roadside': 'CAM',
              'Birmingham A4540 Roadside': 'BIRR', 'Edinburgh St Leonards': 'ED3', 'Wirral Tranmere': 'TRAN',
              'Fort William': 'FW', 'Sibton': 'SIB', 'Doncaster A630 Cleveland Street': 'DCST',
              'Scunthorpe Town': 'SCN2', 'Honiton': 'HONI', 'Carlisle Roadside': 'CARL', 'Newcastle Centre': 'NEWC',
              'Preston': 'PRES', 'Canterbury': 'CANT', 'St Osyth': 'OSY', 'Nottingham Western Boulevard': 'NWBV',
              'Dumfries': 'DUMF', 'Widnes Milton Road': 'WSMR', 'Haringey Roadside': 'HG1',
              'Ballymena Ballykeel': 'BALM', 'Derry Rosemount': 'DERR', 'Liverpool Speke': 'LVP',
              'Port Talbot Margam': 'PT4', 'Norwich Lakenfields': 'NO12', 'Nottingham Centre': 'NOTT',
              'Reading New Town': 'REA1', 'London N. Kensington': 'KC1', 'High Muffles': 'HM', 'Billingham': 'BIL',
              'London Hillingdon': 'HIL', 'Weybourne': 'WEYB', 'Cwmbran': 'CWMB',
              'Stockton-on-Tees A1305 Roadside': 'SOTR', 'Sandy Roadside': 'SDY', 'Leominster': 'LEOM',
              'Oldbury Birmingham Road': 'BOLD', 'Inverness': 'INV2', 'Newport': 'NPT3',
              'Sunderland Silksworth': 'SUN2', 'London Bexley': 'BEX', 'Cannock A5190 Roadside': 'CANK',
              'Warrington': 'WAR', 'Chesterfield Roadside': 'CHS7', 'Oxford St Ebbes': 'OX8', 'Wicken Fen': 'WFEN',
              'Belfast Centre': 'BEL2', 'London Teddington Bushy Park': 'TED2', 'Stoke-on-Trent A50 Roadside': 'STKR',
              'Shaw Crompton Way': 'CW', 'Walsall Woodlands': 'WAL4', 'London Eltham': 'LON6',
              'Leamington Spa Rugby Road': 'LEAR', 'Luton A505 Roadside': 'LUTR', 'Salford Eccles': 'ECCL',
              'Mace Head': 'MH', 'Ballymena Antrim Road': 'BAAR', 'Oxford Centre Roadside': 'OX',
              'Plymouth Tavistock Road.': 'PLYR', 'Southwark A2 Old Kent Road': 'SK5', 'Leicester University': 'LECU',
              'Leeds Centre': 'LEED', 'Lerwick': 'LERW', 'St Helens Linkway': 'SHLW', 'Glasgow Kerbside': 'GLA4',
              'Peebles': 'PEEB', 'Manchester Piccadilly': 'MAN3', 'Market Harborough': 'MKTH',
              'Bristol Temple Way': 'BR11', 'Stoke-on-Trent Centre': 'STOK', 'Thurrock': 'THUR',
              "Derby St Alkmund's Way": 'DESA', 'Hull Holderness Road': 'HULR', 'Wigan Centre': 'WIG5',
              'Bury Whitefield Roadside': 'BURW', 'Strathvaich': 'SV', 'Glasgow Townhead': 'GLKP',
              'Sheffield Barnsley Road': 'SHBR', 'Glasgow Great Western Road': 'GGWR', 'Ladybower': 'LB',
              'Cardiff Centre': 'CARD'}

site_names = {i[1]: i[0] for i in site_codes.items()}

site_list = [
    'Aberdeen',
    'Aberdeen Union Street Roadside',
    'Aberdeen Wellington Road',
    'Armagh Roadside',
    'Aston Hill',
    'Auchencorth Moss',
    'Barnsley Gawber',
    'Barnstaple A39',
    'Bath Roadside',
    'Belfast Centre',
    "Belfast Stockman's Lane",
    'Birkenhead Borough Road',
    'Birmingham A4540 Roadside',
    'Birmingham Acocks Green',
    'Blackpool Marton',
    'Bournemouth',
    'Bradford Mayo Avenue',
    'Brighton Preston Park',
    "Bristol St Paul's",
    'Bristol Temple Way',
    'Bury Whitefield Roadside',
    'Cambridge Roadside',
    'Camden Kerbside',
    'Cannock A5190 Roadside',
    'Canterbury',
    'Cardiff Centre',
    'Carlisle Roadside',
    'Charlton Mackrell',
    'Chatham Roadside',
    'Chepstow A48',
    'Chesterfield Loundsley Green',
    'Chesterfield Roadside',
    'Chilbolton Observatory',
    'Christchurch Barrack Road',
    'Coventry Allesley',
    'Coventry Binley Road',
    'Cwmbran',
    "Derby St Alkmund's Way",
    'Doncaster A630 Cleveland Street',
    'Eastbourne',
    'Edinburgh St Leonards',
    'Eskdalemuir',
    'Exeter Roadside',
    'Fort William',
    'Glasgow High Street',
    'Glazebury',
    'Grangemouth',
    'Grangemouth Moray',
    'High Muffles',
    'Horley',
    'Hull Freetown',
    'Hull Holderness Road',
    'Inverness',
    'Ladybower',
    'Leamington Spa',
    'Leamington Spa Rugby Road',
    'Leeds Centre',
    'Leeds Headingley Kerbside',
    'Leicester A594 Roadside',
    'Leicester University',
    'Leominster',
    'Liverpool Speke',
    'London Bexley',
    'London Bloomsbury',
    'London Eltham',
    'London Harlington',
    'London Marylebone Road',
    'London N. Kensington',
    'London Westminster',
    'Lullington Heath',
    'Luton A505 Roadside',
    'Manchester Piccadilly',
    'Manchester Sharston',
    'Middlesbrough',
    'Narberth',
    'Newcastle Centre',
    'Newport',
    'Norwich Lakenfields',
    'Nottingham Centre',
    'Nottingham Western Boulevard',
    'Oldbury Birmingham Road',
    'Oxford Centre Roadside',
    'Oxford St Ebbes',
    'Peebles',
    'Plymouth Centre',
    'Plymouth Tavistock Road.',
    'Port Talbot Margam',
    'Portsmouth',
    'Preston',
    'Reading London Road',
    'Reading New Town',
    'Rochester Stoke',
    'Salford Eccles',
    'Sandy Roadside',
    'Scunthorpe Town',
    'Shaw Crompton Way',
    'Sheffield Barnsley Road',
    'Sheffield Devonshire Green',
    'Sheffield Tinsley',
    'Southampton A33',
    'Southampton Centre',
    'Southend-on-Sea',
    'St Helens Linkway',
    'St Osyth',
    'Stanford-le-Hope Roadside',
    'Stockton-on-Tees Eaglescliffe',
    'Stoke-on-Trent A50 Roadside',
    'Stoke-on-Trent Centre',
    'Sunderland Silksworth',
    'Sunderland Wessington Way',
    'Swansea Roadside',
    'Thurrock',
    'Walsall Woodlands',
    'Warrington',
    'Wicken Fen',
    'Widnes Milton Road',
    'Wigan Centre',
    'Wirral Tranmere',
    'Worthing A27 Roadside',
    'Wrexham',
    'Yarner Wood',
    'York Bootham',
    'York Fishergate'
]

environs = {
    'Aberdeen': 'urban-background',
    'Aberdeen Union Street Roadside': 'urban-traffic',
    'Aberdeen Wellington Road': 'urban-traffic',
    'Armagh Roadside': 'urban-traffic',
    'Aston Hill': 'rural-background',
    'Auchencorth Moss': 'rural-background',
    'Barnsley Gawber': 'urban-background',
    'Barnstaple A39': 'urban-traffic',
    'Bath Roadside': 'urban-traffic',
    'Belfast Centre': 'urban-background',
    "Belfast Stockman's Lane": 'urban-traffic',
    'Birkenhead Borough Road': 'urban-traffic',
    'Birmingham A4540 Roadside': 'urban-traffic',
    'Birmingham Acocks Green': 'urban-background',
    'Blackpool Marton': 'urban-background',
    'Bournemouth': 'urban-background',
    'Bradford Mayo Avenue': 'urban-traffic',
    'Brighton Preston Park': 'urban-background',
    "Bristol St Paul's": 'urban-background',
    'Bristol Temple Way': 'urban-traffic',
    'Bury Whitefield Roadside': 'urban-traffic',
    'Cambridge Roadside': 'urban-traffic',
    'Camden Kerbside': 'urban-traffic',
    'Cannock A5190 Roadside': 'urban-traffic',
    'Canterbury': 'urban-background',
    'Cardiff Centre': 'urban-background',
    'Carlisle Roadside': 'urban-traffic',
    'Charlton Mackrell': 'rural-background',
    'Chatham Roadside': 'urban-traffic',
    'Chepstow A48': 'urban-traffic',
    'Chesterfield Loundsley Green': 'urban-background',
    'Chesterfield Roadside': 'urban-traffic',
    'Chilbolton Observatory': 'rural-background',
    'Christchurch Barrack Road': 'urban-traffic',
    'Coventry Allesley': 'urban-background',
    'Coventry Binley Road': 'urban-traffic',
    'Cwmbran': 'urban-background',
    "Derby St Alkmund's Way": 'urban-traffic',
    'Doncaster A630 Cleveland Street': 'urban-traffic',
    'Eastbourne': 'urban-background',
    'Edinburgh St Leonards': 'urban-background',
    'Eskdalemuir': 'rural-background',
    'Exeter Roadside': 'urban-traffic',
    'Fort William': 'suburban-background',
    'Glasgow High Street': 'urban-traffic',
    'Glazebury': 'rural-background',
    'Grangemouth': 'urban-industrial',
    'Grangemouth Moray': 'urban-industrial',
    'High Muffles': 'rural-background',
    'Horley': 'suburban-industrial',
    'Hull Freetown': 'urban-background',
    'Hull Holderness Road': 'urban-traffic',
    'Inverness': 'urban-traffic',
    'Ladybower': 'rural-background',
    'Leamington Spa': 'urban-background',
    'Leamington Spa Rugby Road': 'urban-traffic',
    'Leeds Centre': 'urban-background',
    'Leeds Headingley Kerbside': 'urban-traffic',
    'Leicester A594 Roadside': 'urban-traffic',
    'Leicester University': 'urban-background',
    'Leominster': 'suburban-background',
    'Liverpool Speke': 'urban-industrial',
    'London Bexley': 'suburban-background',
    'London Bloomsbury': 'urban-background',
    'London Eltham': 'suburban-background',
    'London Harlington': 'urban-industrial',
    'London Marylebone Road': 'urban-traffic',
    'London N. Kensington': 'urban-background',
    'London Westminster': 'urban-background',
    'Lullington Heath': 'rural-background',
    'Luton A505 Roadside': 'urban-traffic',
    'Manchester Piccadilly': 'urban-background',
    'Manchester Sharston': 'suburban-industrial',
    'Middlesbrough': 'urban-industrial',
    'Narberth': 'rural-background',
    'Newcastle Centre': 'urban-background',
    'Newport': 'urban-background',
    'Norwich Lakenfields': 'urban-background',
    'Nottingham Centre': 'urban-background',
    'Nottingham Western Boulevard': 'urban-traffic',
    'Oldbury Birmingham Road': 'urban-traffic',
    'Oxford Centre Roadside': 'urban-traffic',
    'Oxford St Ebbes': 'urban-background',
    'Peebles': 'urban-background',
    'Plymouth Centre': 'urban-background',
    'Plymouth Tavistock Road.': 'urban-traffic',
    'Port Talbot Margam': 'urban-industrial',
    'Portsmouth': 'urban-background',
    'Preston': 'urban-background',
    'Reading London Road': 'urban-traffic',
    'Reading New Town': 'urban-background',
    'Rochester Stoke': 'rural-background',
    'Salford Eccles': 'urban-background',
    'Sandy Roadside': 'urban-traffic',
    'Scunthorpe Town': 'urban-industrial',
    'Shaw Crompton Way': 'urban-traffic',
    'Sheffield Barnsley Road': 'urban-traffic',
    'Sheffield Devonshire Green': 'urban-background',
    'Sheffield Tinsley': 'urban-background',
    'Southampton A33': 'urban-traffic',
    'Southampton Centre': 'urban-background',
    'Southend-on-Sea': 'urban-background',
    'St Helens Linkway': 'urban-traffic',
    'St Osyth': 'rural-background',
    'Stanford-le-Hope Roadside': 'urban-traffic',
    'Stockton-on-Tees Eaglescliffe': 'urban-traffic',
    'Stoke-on-Trent A50 Roadside': 'urban-traffic',
    'Stoke-on-Trent Centre': 'urban-background',
    'Sunderland Silksworth': 'urban-background',
    'Sunderland Wessington Way': 'urban-traffic',
    'Swansea Roadside': 'urban-traffic',
    'Thurrock': 'urban-background',
    'Walsall Woodlands': 'urban-background',
    'Warrington': 'urban-industrial',
    'Wicken Fen': 'rural-background',
    'Widnes Milton Road': 'urban-traffic',
    'Wigan Centre': 'urban-background',
    'Wirral Tranmere': 'urban-background',
    'Worthing A27 Roadside': 'urban-traffic',
    'Wrexham': 'urban-traffic',
    'Yarner Wood': 'rural-background',
    'York Bootham': 'urban-background',
    'York Fishergate': 'urban-traffic'
}
regions = {
    'Aberdeen': 'north-east-scotland',
    'Aberdeen Union Street Roadside': 'north-east-scotland',
    'Aberdeen Wellington Road': 'north-east-scotland',
    'Armagh Roadside': 'northern-ireland',
    'Aston Hill': 'north-wales',
    'Auchencorth Moss': 'central-scotland',
    'Barnsley Gawber': 'yorkshire',
    'Barnstaple A39': 'south-west',
    'Bath Roadside': 'south-west',
    'Belfast Centre': 'northern-ireland',
    "Belfast Stockman's Lane": 'northern-ireland',
    'Birkenhead Borough Road': 'north-west',
    'Birmingham A4540 Roadside': 'west-midlands',
    'Birmingham Acocks Green': 'west-midlands',
    'Blackpool Marton': 'north-west',
    'Bournemouth': 'south-west',
    'Bradford Mayo Avenue': 'yorkshire',
    'Brighton Preston Park': 'south-east',
    "Bristol St Paul's": 'south-west',
    'Bristol Temple Way': 'south-west',
    'Bury Whitefield Roadside': 'north-west',
    'Cambridge Roadside': 'eastern',
    'Camden Kerbside': 'greater-london',
    'Cannock A5190 Roadside': 'west-midlands',
    'Canterbury': 'south-east',
    'Cardiff Centre': 'south-wales',
    'Carlisle Roadside': 'north-west',
    'Charlton Mackrell': 'south-west',
    'Chatham Roadside': 'south-east',
    'Chepstow A48': 'south-wales',
    'Chesterfield Loundsley Green': 'east-midlands',
    'Chesterfield Roadside': 'east-midlands',
    'Chilbolton Observatory': 'south-east',
    'Christchurch Barrack Road': 'south-west',
    'Coventry Allesley': 'west-midlands',
    'Coventry Binley Road.': 'west-midlands',
    'Cwmbran': 'south-wales',
    "Derby St Alkmund's Way": 'east-midlands',
    'Doncaster A630 Cleveland Street': 'yorkshire',
    'Eastbourne': 'south-east',
    'Edinburgh St Leonards': 'central-scotland',
    'Eskdalemuir': 'scottish-borders',
    'Exeter Roadside': 'south-west',
    'Fort William': 'highlands',
    'Glasgow High Street': 'central-scotland',
    'Glazebury': 'north-west',
    'Grangemouth': 'central-scotland',
    'Grangemouth Moray': 'central-scotland',
    'High Muffles': 'yorkshire',
    'Horley': 'south-east',
    'Hull Freetown': 'yorkshire',
    'Hull Holderness Road': 'yorkshire',
    'Inverness': 'highlands',
    'Ladybower': 'east-midlands',
    'Leamington Spa': 'west-midlands',
    'Leamington Spa Rugby Road': 'west-midlands',
    'Leeds Centre': 'yorkshire',
    'Leeds Headingley Kerbside': 'yorkshire',
    'Leicester A594 Roadside': 'east-midlands',
    'Leicester University': 'east-midlands',
    'Leominster': 'west-midlands',
    'Liverpool Speke': 'north-west',
    'London Bexley': 'greater-london',
    'London Bloomsbury': 'greater-london',
    'London Eltham': 'greater-london',
    'London Harlington': 'greater-london',
    'London Marylebone Road': 'greater-london',
    'London N. Kensington': 'greater-london',
    'London Westminster': 'greater-london',
    'Lullington Heath': 'south-east',
    'Luton A505 Roadside': 'eastern',
    'Manchester Piccadilly': 'north-west',
    'Manchester Sharston': 'north-west',
    'Middlesbrough': 'north-east',
    'Narberth': 'south-wales',
    'Newcastle Centre': 'north-east',
    'Newport': 'south-wales',
    'Norwich Lakenfields': 'eastern',
    'Nottingham Centre': 'east-midlands',
    'Nottingham Western Boulevard': 'east-midlands',
    'Oldbury Birmingham Road': 'west-midlands',
    'Oxford Centre Roadside': 'south-east',
    'Oxford St Ebbes': 'south-east',
    'Peebles': 'scottish-borders',
    'Plymouth Centre': 'south-west',
    'Plymouth Tavistock Road.': 'south-west',
    'Port Talbot Margam': 'south-wales',
    'Portsmouth': 'south-east',
    'Preston': 'north-west',
    'Reading London Road': 'south-east',
    'Reading New Town': 'south-east',
    'Rochester Stoke': 'south-east',
    'Salford Eccles': 'north-west',
    'Sandy Roadside': 'eastern',
    'Scunthorpe Town': 'yorkshire',
    'Shaw Crompton Way': 'north-west',
    'Sheffield Barnsley Road': 'yorkshire',
    'Sheffield Devonshire Green': 'yorkshire',
    'Sheffield Tinsley': 'yorkshire',
    'Southampton A33': 'south-east',
    'Southampton Centre': 'south-east',
    'Southend-on-Sea': 'eastern',
    'St Helens Linkway': 'north-west',
    'St Osyth': 'eastern',
    'Stanford-le-Hope Roadside': 'eastern',
    'Stockton-on-Tees Eaglescliffe': 'north-east',
    'Stoke-on-Trent A50 Roadside': 'west-midlands',
    'Stoke-on-Trent Centre': 'west-midlands',
    'Sunderland Silksworth': 'north-east',
    'Sunderland Wessington Way': 'north-east',
    'Swansea Roadside': 'south-wales',
    'Thurrock': 'eastern',
    'Walsall Woodlands': 'west-midlands',
    'Warrington': 'north-west',
    'Wicken Fen': 'eastern',
    'Widnes Milton Road': 'north-west',
    'Wigan Centre': 'north-west',
    'Wirral Tranmere': 'north-west',
    'Worthing A27 Roadside': 'south-east',
    'Wrexham': 'north-wales',
    'Yarner Wood': 'south-west',
    'York Bootham': 'yorkshire',
    'York Fishergate': 'yorkshire'
}
