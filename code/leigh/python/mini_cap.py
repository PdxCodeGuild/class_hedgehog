# Mini Capstone
# Stock Recommendation
# Leigh Fair-Smiley
# 6/17/2022

import requests
from urllib.request import urlopen
import certifi
import json

def get_jsonparsed_data(url):

    res = requests.get(url)
    #print(res)
    if str(res) == "<Response [200]>":
        response = urlopen(url, cafile=certifi.where())
        data = response.read().decode("utf-8")
        return json.loads(data)

def main():

    top_200 = ["2222.SR", "AAPL", "MSFT", "GOOG", "AMZN", "TSLA", "BRK-B", "TCEHY", "TSM", "JNJ", "META", "UNH", "V", "NVDA", "600519.SS", "XOM", "JPM", "WMT", "PG", "005930.KS", "NESN.SW", "MA", "CVX", "MC.PA", "BABA", "HD", "LLY", "ROG.SW", "PFE", 'KO', 'BAC', 'ABBV', 'NVO', '1398.HK', 'RELIANCE.NS', 'PEP', 'MRK', 'VS', 'ASML', 'AVGO', 'COST', 'TMO', 'AZN', 'SHEL', 'ORCL', 'CSCO', 'ABT', 'NVS', '601939.SS', 'ACN', 'DHR', 'CMCSA', 'MCD', 'OR.PA', 'DIS', 'ADBE', 'NKE', '300750.SZ', 'CRM', 'PRX.AS', 'TMUS', 'BMY', '3690.HK', '601288.SS', 'PM', '3968.HK', 'INTC', 'UPS', 'BHP', 'LIN', 'WFC', 'TCS.NS', 'PTR', 'NEE', 'T', 'TXN', 'TTE', '0941.HK', 'QCOM', 'RY', '601988.SS', 'AMD', 'RTX', '002594.SZ', 'GAZP.ME', 'UNP', 'MS', 'AMGN', 'HSBC', '601318.SS', 'SNY', 'HON', 'COP', '1299.HK', 'IBM', 'TD', 'MDT', 'CVS', 'SCHW', 'EQNR', 'SAP', 'UL', 'LOW', 'AMT', 'SPGI', 'AXP', 'LMT', 'ANTM', 'SONY', 'RMS.PS', 'GSK', '000858.SZ', 'RIO', 'INTU', 'CBA.AX', 'JK', 'CAT', 'CDI.PA', 'LFC', 'VOW3.DE', 'NPPXF', 'HDB', 'DE', 'DEO', 'GS', 'BTI', 'DTE.DE', '1120.SR', 'BUD', 'BP', '601088.SS', 'C', 'NOW', 'BLK', 'SIE.DE', 'CSL.AX', 'EL', 'PYPL', 'ADP', '6861.T', '2010.SR', 'SBUX', 'ENB', 'MO', 'PDL', 'MDLZ', 'BA', 'CB', '600900.SS', 'ALV.DE', '1180.SR', 'AMAT', 'NFLX', 'AIR.PA', 'CI', 'BKNG', '373220.KS', 'PBR', 'DUK', 'ADI', 'CNI', 'ZTS', 'GLCNF', 'PDD', 'INFY', 'CHTR', 'GILD', 'MMM', 'SYK', 'BNS', 'VALE', 'GE', 'MMC', 'MRK.DE', 'CME', 'FMX', 'BAM', 'IDEXY', '9433.T', 'AI.PA', '601658.SS', 'MBG.DE', 'SO', 'NOC', 'ISRG', '601012.SS', 'MUFG', 'SU.PA', 'SNP', 'CCI', 'USB', 'VRTX', 'BDX', 'TJX', 'BAYZF', 'EOG', 'BX', 'IBE.MC', 'ROSN.ME']
    pct_change = []
    for company in top_200:
        data = get_jsonparsed_data(f"https://financialmodelingprep.com/api/v3/quote/{company}?apikey=insert_key_here")
        #print(company)
        if data:
            pct_change.append({"company": company, "pct_change": float(data[0]["changesPercentage"])})


    pct_change.sort(key=lambda item: item.get("pct_change"))

    print(pct_change[len(pct_change) - 1]["company"], "might be a bull")

main()