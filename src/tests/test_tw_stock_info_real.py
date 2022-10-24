import unittest
from fin_crawler import FinCrawler
import time
class Test_tw_stock_info_real(unittest.TestCase):

    def test_request(self):
        time.sleep(4)
        result_idx1 = {
            'stock_id': '1102',
            'company_name': '亞洲水泥股份有限公司',
            'stock_name': '亞泥',
            'foreign_register_country': '－ ',
            'industry_type': '01',
            'address': '台北市大安區敦化南路2段207號30、31樓',
            'tax_id': '03244509',
            'chairman': '徐旭東',
            'CEO': '李坤炎',
            'spokesman': '周維崑',
            'spokesman_title': '副總經理',
            'deputy_spokesman': '吳玲綾',
            'phone': '02-2733-8000',
            'establishment_date': '19570321',
            'IPO_date': '19620608',
            'common_shares_price': '新台幣                 10.0000元',
            'paid_in_capital': '35459275570',
            'private_shares_num': '0',
            'special_shares_num': '0',
            'financial_report_type': '1',
            'stock_transfer_agency': '亞東證券股份有限公司',
            'stcok_transfer_phone': '02-7753-1699',
            'stock_transfer_address': '新北市板橋區新站路16號13樓',
            'accounting_firm': '勤業眾信聯合會計師事務所',
            'accountant_1': '戴信維',
            'accountant_2': '陳培德',
            'stock_name_en': 'ACC',
            'address_en': "30-31F., No.207, Sec. 2, Dunhua S. Rd., Da' an Dist., Taipei City 106, TaiwanTAIPEI,TAIWAN,R.O.C",
            'fax': '02-2378-5191',
            'email': 'service@acc.com.tw',
            'website': 'www.acc.com.tw'}
        result_idx3 = {
            'stock_id': '1104',
            'company_name': '環球水泥股份有限公司',
            'stock_name': '環泥',
            'foreign_register_country': '－ ',
            'industry_type': '01',
            'address': '台北市南京東路二段125號10樓',
            'tax_id': '07568009',
            'chairman': '侯博義',
            'CEO': '侯智升',
            'spokesman': '楊宗仁',
            'spokesman_title': '副總經理',
            'deputy_spokesman': '詹志鴻',
            'phone': '02-25077801',
            'establishment_date': '19600321',
            'IPO_date': '19710201',
            'common_shares_price': '新台幣                 10.0000元',
            'paid_in_capital': '6536091920',
            'private_shares_num': '0',
            'special_shares_num': '0',
            'financial_report_type': '1',
            'stock_transfer_agency': '永豐金證券股份有限公司',
            'stcok_transfer_phone': '02-23816288',
            'stock_transfer_address': '台北市博愛路17號3樓',
            'accounting_firm': '勤業眾信聯合會計師事務所',
            'accountant_1': '楊朝欽',
            'accountant_2': '李季珍',
            'stock_name_en': 'UCC',
            'address_en': '10th F1., 125 Nanking E.Rd Sec. 2,Taipei Taiwan',
            'fax': '02-25075870',
            'email': 'ucc@ucctw.com',
            'website': 'www.ucctw.com'}
        data = FinCrawler.get('tw_stock_info',{})
        del data[1]['update_date']
        del data[3]['update_date']
        self.assertEqual(data[1],result_idx1)
        self.assertEqual(data[3],result_idx3)

