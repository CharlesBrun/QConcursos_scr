import requests

def generatedHTML(html):
    with open("debug.html", 'wb') as file:
        file.write(html)

class EstrategiaConcursos():
    def __init__(self):
        self.session = requests.session()
        self.paginaError = []

    def consulta(self):
        pagina = 1
        self.login()
        self.getTopics()
        qntPaginas = self.getQuantidadePags()
        print(f'Encontrou {qntPaginas} questoes')

        while pagina <= int(qntPaginas):
            try:
                self.pegaQuestoesJson(pagina)
                pagina += 1
                print(f'Paginas que foram capturadas {self.paginaError}')
            except Exception as ex:
                print(ex)

        for repete in self.paginaError:
            self.pegaQuestoesJson(repete)
            print(repete)

    def login(self):
        try:
            headers = {
                'authority': 'api.accounts.estrategia.com',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                'accept': 'application/json, text/plain, */*',
                'content-type': 'application/json;charset=UTF-8',
                'x-requester-id': 'perfil',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://perfil.estrategia.com',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://perfil.estrategia.com/',
                'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
                'cookie': '_gcl_au=1.1.1672655143.1644963869; _fbp=fb.1.1644963869157.717985197; _BEAMER_USER_ID_LfFHNPFX28976=2da2ab2a-a413-43dd-a713-121c25543566; _BEAMER_FIRST_VISIT_LfFHNPFX28976=2022-02-15T22:24:42.420Z; _hjSessionUser_2136642=eyJpZCI6ImU0OGUzY2UwLWJjYWEtNTNlMy05ODEzLWE1ZDlhODlkNWY5MSIsImNyZWF0ZWQiOjE2NDUwNDk4NjM5MzAsImV4aXN0aW5nIjp0cnVlfQ==; _BEAMER_LAST_UPDATE_LfFHNPFX28976=1645055342579; _BEAMER_DATE_LfFHNPFX28976_cb0fdfd1-0bd7-4c1b-9a89-d3735c077022=2022-02-27T02:19:19.000Z; _gid=GA1.2.285134711.1647557510; __Secure-SID=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNiMGZkZmQxLTBiZDctNGMxYi05YTg5LWQzNzM1YzA3NzAyMiIsImVtYWlsIjoicXVlbHNqMjAwNEB5YWhvby5jb20uYnIiLCJmdWxsX25hbWUiOiJSYXF1ZWwgTy4gUG9udGVzICIsImxvZ2luX3JlcXVlc3RfaWQiOiJsd2lUZWxFeE5YbFBFUEVCUVJlbVEzVDdoRWlZOVZ6SSIsImV4cCI6MTY1MDE0OTUzMCwiaWF0IjoxNjQ3NTU3NTMwLCJzdWIiOiJjYjBmZGZkMS0wYmQ3LTRjMWItOWE4OS1kMzczNWMwNzcwMjIifQ.-pKo28jbrq0JKsHvXlXpbHgsao52NM4a6WZbgLCSwiI; _hjSession_2136642=eyJpZCI6IjI3NTUzNDg3LTkxYTEtNDYwNy04NjRiLWI3NDRlNGYxMmQ5ZSIsImNyZWF0ZWQiOjE2NDc1NTc1NTQ0MDEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _BEAMER_FILTER_BY_URL_LfFHNPFX28976=false; _ga=GA1.1.2058698184.1644963869; _ga_T3NJ4E7E00=GS1.1.1647557509.4.1.1647557901.60; _ga_F4P2471F3H=GS1.1.1647557555.4.1.1647557901.60',
            }

            data = '{"email":{login},"password":{senha}}'#Inserir login e senha aqui

            self.session.post('https://api.accounts.estrategia.com/auth/login', headers=headers, data=data)

        except Exception as ex:
            print(ex)

    def getTopics(self):
        headers = {
            'authority': 'api.estrategia.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'accept': 'application/json, text/plain, */*',
            'x-requester-id': 'front-student',
            'x-vertical': 'concursos',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://concursos.estrategia.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://concursos.estrategia.com/',
            'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
        }

        params = (
            ('page', '1'),
            ('perPage', '30'),
        )

        response = self.session.get('https://api.estrategia.com/v3/questions/topics', headers=headers, params=params)

        quantidade_paginas = response.json()['pagination']['total']
        for resposta in response.json()['data']:
            print(resposta)

    def getQuantidadePags(self):
        try:
            headers = {
                'authority': 'api.estrategia.com',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                'x-requester-id': 'front-student',
                'x-vertical': 'concursos',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                'accept': 'application/json, text/plain, */*',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://concursos.estrategia.com',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://concursos.estrategia.com/',
                'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8',
            }

            params = (
                ('page', '1'),
                ('per_page', '20'),
            )

            json_data = {
                'filters': [
                    {
                        'add': True,
                        'entity': 'topic',
                        'entity_ids': [
                            '4491881',
                        ],
                        'origin': 'questions',
                    },
                    {
                        'add': False,
                        'entity': 'label',
                        'entity_ids': [
                            'OUTDATED',
                        ],
                    },
                    {
                        'add': False,
                        'entity': 'label',
                        'entity_ids': [
                            'CANCELED',
                        ],
                    },
                    {
                        'add': False,
                        'entity': 'solution',
                        'entity_ids': [],
                    },
                    {
                        'add': False,
                        'entity': 'answer_type',
                        'entity_ids': [
                            'DISCURSIVE',
                        ],
                    },
                ],
            }

            resp = self.session.post('https://api.estrategia.com/v3/questions/search', headers=headers, params=params,
                                json=json_data)
            qntPaginas = resp.json()['pagination']['total']

            return qntPaginas

        except Exception as ex:
            print(ex)

    def pegaQuestoesJson(self, pagina):
        try:
            print('Pagina = '+str(pagina))
            headers = {
                'authority': 'api.estrategia.com',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                'x-requester-id': 'front-student',
                'x-vertical': 'concursos',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                'accept': 'application/json, text/plain, */*',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://concursos.estrategia.com',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://concursos.estrategia.com/',
                'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8',
            }

            params = (
                ('page', str(pagina)),
                ('per_page', '20'),
            )

            json_data = {
                'filters': [
                    {
                        'add': True,
                        'entity': 'topic',
                        'entity_ids': [
                            '4491881',
                        ],
                        'origin': 'questions',
                    },
                    {
                        'add': False,
                        'entity': 'label',
                        'entity_ids': [
                            'OUTDATED',
                        ],
                    },
                    {
                        'add': False,
                        'entity': 'label',
                        'entity_ids': [
                            'CANCELED',
                        ],
                    },
                    {
                        'add': False,
                        'entity': 'solution',
                        'entity_ids': [],
                    },
                    {
                        'add': False,
                        'entity': 'answer_type',
                        'entity_ids': [
                            'DISCURSIVE',
                        ],
                    },
                ],
            }

            resp = self.session.post('https://api.estrategia.com/v3/questions/search', headers=headers, params=params,
                                     json=json_data)

            dados = resp.json()['data']
            for data in dados:
                print(data)

        except Exception as ex:
            print(ex)
            print(f'Pagina= {pagina} deu erro e não foi possivel pegar informações')
            self.paginaError.append(pagina)

EstrategiaConcursos().consulta()
