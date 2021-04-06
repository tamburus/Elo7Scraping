# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 09:31:43 2021

@author: fabio.tamburus
"""


class manageLoginElo():
    
    def __init__(self, login):
        if (login == 1):
                self.cookies = {
                 'UserSource': '{\\"origin\\":\\"DIRECT\\",\\"locked\\":false}',
                 '_trck': '12631027-b7bc-4ad5-a4cd-89aee8075d2c',
                 'e7bid': '7fe05b3d-ab23-486c-9da4-7b6c0466fad8',
                 'e7auid': 'anon-08034fda-cdfc-4311-8f01-9611484cdc70',
                 'JSESSIONID': '404F28112E9EBF4FD43A5C3F524771EF',
                 'e7sid': '1617029694_0f4c687e-7534-4dac-8cb9-d8d9b1d29204',
                 'AWSELB': '1BFB71A71C4160337F9029C91F85CC1E4091AA9511B6D7981FDE8182E6764636C88212208FFF9B755879C5DD76DAABF68535BF95645CFF9911D66A9A765545415FF7A32303',
                 '_bktc': '22565176',
                 '_gid': 'GA1.3.1137617952.1617029712',
                 '_gat': '1',
                 '_dvs': '0:kmupqmpq:aiFukguE9ZzeKP1Af3u1gT8kyAjWd_Z9',
                 '_dvp': '0:kmupqmpq:Fjn7iXdaMsDF_0dTcQuaKXjVpkhC9lBF',
                 '_gat_UA-3692628-34': '1',
                 '_uetsid': 'c3685400909e11ebb0b8efe6fe6669c2',
                 '_uetvid': 'c3689b30909e11eb87a55f5adec8b709',
                 '__kdtv': 't%3D1617029712464%3Bi%3D459dae024fc8711e485ce684b1428d6d114db1d0',
                 '_kdt': '%7B%22t%22%3A1617029712464%2C%22i%22%3A%22459dae024fc8711e485ce684b1428d6d114db1d0%22%7D',
                 '_fbp': 'fb.2.1617029713023.1731073145',
                 'chaordic_testGroup': '%7B%22experiment%22%3Anull%2C%22group%22%3Anull%2C%22testCode%22%3Anull%2C%22code%22%3Anull%2C%22session%22%3Anull%7D',
                 'chaordic_browserId': '0-Yk6XBnsH6A10ynwD0nYGz86RfIDkOTfK-8Ps16170296969044644',
                 'chaordic_session': '1617029713041-0.9796757617769463',
                 'chaordic_anonymousUserId': 'anon-0-Yk6XBnsH6A10ynwD0nYGz86RfIDkOTfK-8Ps16170296969044644',
                 '_st_ses': '07321979106057186',
                 '_sptid': '5662',
                 '_st_no_script': '1',
                 '_spcid': '4971',
                 '_spl_pv': '1',
                 '_st_no_user': '1',
                 '_cm_ads_activation_retry': 'false',
                 '_ga_22YVRK2WCW': 'GS1.1.1617029711.1.0.1617029713.0',
                 '_ga': 'GA1.3.950426844.1617029712',
                 '_cookies_acceptance': 'true',
                 }
                
                self.headers = {
                     'Connection': 'keep-alive',
                     'Cache-Control': 'max-age=0',
                     'Upgrade-Insecure-Requests': '1',
                     'Origin': 'https://www.elo7.com.br',
                     'Content-Type': 'application/x-www-form-urlencoded',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63',
                     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                     'Sec-Fetch-Site': 'same-origin',
                     'Sec-Fetch-Mode': 'navigate',
                     'Sec-Fetch-User': '?1',
                     'Sec-Fetch-Dest': 'document',
                     'Referer': 'https://www.elo7.com.br/login.do?usregsrc=HEADER_REGISTER&redirectAfterLogin=%2F',
                     'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                 }
                
                self.data = {
                   'redirect': '/',
                   'usregsrc': 'HEADER_REGISTER',
                   'command': 'login',
                   'email': 'doluz@doluz.com.br',
                   'password': 'vesygady10!'
                 }
        else:
            self.cookies = {
            'UserSource': '{\\"origin\\":\\"ORGANIC\\",\\"locked\\":false}',
            '_trck': 'fbaefe45-c287-42d3-891c-1c2fdb977146',
            'e7bid': '30b7c68a-1661-48b8-9056-0139f2ef6c31',
            'e7auid': 'anon-44c7f994-bbea-44b7-b149-ce5f6fd4a738',
            'JSESSIONID': '162A8F879C2951C6BC2DF644C15A8E87',
            'e7sid': '1617028709_9dbd57e5-59b1-41e4-8c83-f57f350786c8',
            'AWSELB': '1BFB71A71C4160337F9029C91F85CC1E4091AA95116F28D1304D4B6C25A3615688714D8120922319A879C7F7F3A97CFD825779853E1C27339564BC438EBC272C360028524C',
            '_bktc': '22498506',
            '_gid': 'GA1.3.1677808621.1617028726',
            '_gat': '1',
            '_dvp': '0:kmup5i10:2gYmaSspkjwwd~6XqAGuWDKfs2fVbf5_',
            '_dvs': '0:kmup5i10:UqAfL3qXj5WKO~M6LIdFeGxfyuj2196R',
            '_gat_UA-3692628-34': '1',
            '__kdtv': 't%3D1617028725996%3Bi%3Dfd318c2e96c0547476d9e63a32634ba4d50c5723',
            '_kdt': '%7B%22t%22%3A1617028725996%2C%22i%22%3A%22fd318c2e96c0547476d9e63a32634ba4d50c5723%22%7D',
            '_uetsid': '77c69fd0909c11eba48a079d62e4ab6a',
            '_uetvid': '77c6f0a0909c11ebafd60123fec5a05b',
            '_fbp': 'fb.2.1617028726626.363204417',
            '_st_ses': '3653121892354414',
            '_st_no_script': '1',
            '_st_no_user': '1',
            'chaordic_testGroup': '%7B%22experiment%22%3Anull%2C%22group%22%3Anull%2C%22testCode%22%3Anull%2C%22code%22%3Anull%2C%22session%22%3Anull%7D',
            'chaordic_browserId': '0-Fmismd8-L5q87KzV2HrGe-BYqx4jakfkgyVp16170287107787852',
            'chaordic_session': '1617028726920-0.0486305722737963',
            'chaordic_anonymousUserId': 'anon-0-Fmismd8-L5q87KzV2HrGe-BYqx4jakfkgyVp16170287107787852',
            '_sptid': '5662',
            '_spcid': '4971',
            '_spl_pv': '1',
            'sback_browser': '0-99546400-1617028710f8bcddb6140b338b4f3b81fc16d930b8c08e045812333045176061e666f30975-37075701-20116220145,524643163-1617028710',
            '_cm_ads_activation_retry': 'false',
            '_ga_22YVRK2WCW': 'GS1.1.1617028725.1.0.1617028727.0',
            '_ga': 'GA1.3.756915171.1617028726',
            '_cookies_acceptance': 'true',
        }
        
        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'https://www.elo7.com.br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.elo7.com.br/login.do?usregsrc=HEADER_REGISTER&redirectAfterLogin=%2F',
            'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        }
        
        self.data = {
          'redirect': '/',
          'usregsrc': 'HEADER_REGISTER',
          'command': 'login',
          'email': 'thais@doluz.com.br',
          'password': 'doluz2020',
          'g-recaptcha-response': '03AGdBq25NJjixYgjq7XxkfISHtgO6uyesdvUL8WeLs4lk4JB9ZeJVTZ4RulqaR_tfS4eI_VM6wr33Uwyu9y_DYhLLYgUBuyQ_Ys62tULoJIzuk2xaGV2-egqBrS6PHIZjJuHrhEU6lCIEpFzfPYvLJ2PGDxYr_IfLSR7TAokLSQpBgDB6GVa70Iht0zUeNCZnn6qga23oANOpwJcSPgqs4zh2iPxDSoQmNH_nmQyM47QOmhvllValrvpKUtEKl4uRO9rOMPJwWnqTMtmc8Ixb95RxpimPXmoVjpb5f8TJTKQjma5CTKycsHL3nHkWDyVL-648bfWeLF7Ym0Kh7wHczCNSxTsj0cEq1IkwWUVJ18FkIdnLeaKsVAdhsNgAfb_EXOGPoWe4eTVXHN1HLSGZtVliLxHwWwCoHHLAfv9fZ7eLYHjStkQa1WGQQqd-wNinvG6_31J8wdYf'
        }

        