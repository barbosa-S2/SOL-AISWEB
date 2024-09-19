!pip install xmltodict
import requests
import json
import pprint
import xmltodict

def make_request():
  api_key = "1737636254"
  api_pass = "cf334dde-eb8c-11ee-8b18-0050569ac2e1"
  icao_code = input('Informe o codigo ICAO desejado: ')

  url = f"http://aisweb.decea.gov.br/api/?apiKey={api_key}&apiPass={api_pass}&area=sol&icaoCode={icao_code}"

  resposta = requests.get(url)

  return resposta

def json_response(resposta):
  json_response = xmltodict.parse(resposta.content)

  return json_response

def get_icao_code(json_response):
  icao_code = json_response.get('aisweb').get('day').get('aero')

  return icao_code

def get_date(json_response):
  date = json_response.get('aisweb').get('day').get('date')

  data = date.split("-")
  day = data[2]
  month = data[1]
  year = data[0]

  formated_date = f"{day}/{month}/{year}"
  return formated_date

def get_sunrise(json_response):
  sunrise = json_response.get('aisweb').get('day').get('sunrise')

  hour_sunrise = int(sunrise[0:2])-3

  sunrise_time = f"{hour_sunrise}.{sunrise[3:]}"

  return sunrise_time

def get_sunset(json_response):
  sunset = json_response.get('aisweb').get('day').get('sunset')

  hour_sunset = int(sunset[0:2])-3

  sunset_time = f"{hour_sunset}.{sunset[3:]}"

  return sunset_time

def get_result(icao_code, date, sunrise, sunset):
  print(f"\nPara {icao_code.upper()}, no dia {date}, o nascer do Sol acontecerá ás {sunrise} e o pôr do sol, ás {sunset}.")

def main():
  dados = make_request()
  dados_json = json_response(dados)
  icao_code = get_icao_code(dados_json)
  data_observacao = get_date(dados_json)
  nascer_do_sol = get_sunrise(dados_json)
  por_do_sol = get_sunset(dados_json)
  get_result(icao_code, data_observacao, nascer_do_sol, por_do_sol)

#--------------------------------------------------------------------------------------------------------------
main()
