# -*- coding: utf-8 -*-
from odoo import models, fields, api

CURRENCY_PROVIDER_SELECTION = [
    ([], 'ecb', 'European Central Bank'),
    ([], 'xe_com', 'xe.com'),
    (['AE'], 'cbuae', 'UAE Central Bank'),
    (['AZ'], 'cbar', 'Central Bank of Azerbaijan'),
    (['CA'], 'boc', 'Bank Of Canada'),
    (['CH'], 'fta', 'Federal Tax Administration (Switzerland)'),
    (['CL'], 'mindicador', 'Chilean mindicador.cl'),
    (['EG'], 'cbegy', 'Central Bank of Egypt'),
    (['MX'], 'banxico', 'Mexican Bank'),
    (['PE'], 'bcrp', 'SUNAT (replaces Bank of Peru)'),
    (['RO'], 'bnr', 'National Bank Of Romania'),
    (['TR'], 'tcmb', 'Turkey Republic Central Bank'),
    (['PL'], 'nbp', 'National Bank of Poland'),
    (['BR'], 'bbr', 'Central Bank of Brazil'),
]

class cbar_currency_rate(models.Model):
    _inherit = 'res.company'

    def _parse_cbar_data(self, available_currencies):
        ''' This method is used to update the currencies by using CBA service provider.
            Rates are given against AZN
        '''
        request_url = "https://www.cbar.az/currencies/{}.xml".format(fields.Date.today().strftime('%d.%m.%Y'))
        response = requests.get(request_url, timeout=30)
        response.raise_for_status()
    
        xmlstr = etree.fromstring(response.content)
        available_currency_names = available_currencies.mapped('name')
        rslt = {}
        for valute in xmlstr.xpath('//Valute'):
            currency_code = valute.get('Code')
            nominal_text = valute.xpath('Nominal/text()')[0]
            nominal = float(''.join(filter(str.isdigit, nominal_text)) or "1")
            rate = valute.xpath('Value/text()')[0]
            rate = float(rate.replace(',', '.'))
            if currency_code in available_currency_names:
                rslt[currency_code] = (nominal / rate, fields.Date.today())
    
        if rslt and 'AZN' in available_currency_names:
            rslt['AZN'] = (1.0, fields.Date.today())
    
        return rslt


