# encoding:utf-8

import base64
import pprint
import requests
from pathlib import Path
import pandas as pd
import os

class InvoiceFile:
    def __init__(self, file_path, api_key, secret_key):
        self.file_path = file_path
        self.api_key = api_key
        self.secret_key = secret_key

def get_file_content(file_path):
    """
    获取指定目录下的所有PDF文件路径。

    参数:
    file_path (str): 文件夹路径

    返回:
    generator: 包含PDF文件路径的生成器
    """
    file_folder = Path(file_path)
    pdf_files = file_folder.glob('*.pdf')
    for pdf_file in pdf_files:
        if pdf_file.exists():
            yield str(pdf_file)

def extract_file_names(file_paths):
    """
    从文件路径列表中提取文件名，并返回一个包含这些文件名的列表。

    参数:
    file_paths (list): 文件路径列表

    返回:
    list: 包含文件名的列表
    """
    return [path.name for path in file_paths]

def get_access_token(api_key, secret_key):
    """
    获取API访问令牌。

    参数:
    api_key (str): API密钥
    secret_key (str): 密钥

    返回:
    str: 访问令牌
    """
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()["access_token"]

# 增值税发票识别
def vat_invoice_recognition(file_path, api_key, secret_key):
    """
    识别增值税发票并保存结果到Excel文件。

    参数:
    file_path (str): 文件路径
    api_key (str): API密钥
    secret_key (str): 密钥
    """
    try:

        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice"
        with open(file_path, 'rb') as f:
            img = base64.b64encode(f.read())
        params = {"pdf_file": img}
        access_token = get_access_token(api_key, secret_key)
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            pprint.pprint(response.json())
            append_data_to_excel(response.json())
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
    except requests.RequestException as e:
        print(f"网络请求错误: {e}")
    except KeyError as e:
        print(f"数据提取错误: {e}")

def append_data_to_excel(data, filename='output.xlsx'):
    """
    将数据追加到Excel文件中。

    参数:
    data (dict): 从API获取的数据
    filename (str): 输出文件名
    """
    try:
        keys_to_extract = [
            'Agent', 'AmountInFiguers', 'AmountInWords', 'CheckCode', 'Checker',
            'City', 'InvoiceCode', 'InvoiceCodeConfirm', 'InvoiceDate',
            'InvoiceNum', 'InvoiceNumConfirm', 'InvoiceTag', 'InvoiceType',
            'InvoiceTypeOrg', 'MachineCode', 'NoteDrawer', 'Password', 'Payee',
            'Province', 'PurchaserAddress', 'PurchaserBank', 'PurchaserName',
            'PurchaserRegisterNum', 'Remarks', 'SellerAddress', 'SellerBank',
            'SellerName', 'SellerRegisterNum', 'ServiceType', 'SheetNum',
            'TotalAmount', 'TotalTax'
        ]
        extracted_data = {key: data['words_result'].get(key, '') for key in keys_to_extract}
        commodity_data = data['words_result'].get('CommodityAmount', [])
        for i, item in enumerate(commodity_data):
            extracted_data[f'CommodityAmount_{i+1}'] = item['word']
        commodity_name = data['words_result'].get('CommodityName', [])
        for i, item in enumerate(commodity_name):
            extracted_data[f'CommodityName_{i+1}'] = item['word']
        df_new = pd.DataFrame([extracted_data])
        if os.path.exists(filename):
            df_existing = pd.read_excel(filename)
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_combined = df_new
        df_combined.to_excel(filename, index=False)
    except PermissionError:
        print(f"文件写入错误: 没有权限写入文件 {filename}")
    except KeyError as e:
        print(f"数据提取错误: {e}")

if __name__ == '__main__':
    folder_path = r"E:\workspace\python\python_patitace\file"
    api_key = 'wLFcy02oqkm06BbmOMJ04xoJ'
    secret_key = 'qCBAsjbPyTJQhKSo6lM8w369o4Z2IpTZ'
    pdf_file_paths = get_file_content(folder_path)
    for pdf_file_path in pdf_file_paths:
        vat_invoice_recognition(pdf_file_path, api_key, secret_key)


