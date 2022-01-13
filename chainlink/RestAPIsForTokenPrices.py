import json
from web3 import Web3
#from web3.middleware import geth_poa_middleware
from flask import Flask, jsonify, request

#This program shows the latest Avax-USD and Joe-USD price with using chainlink's oracle price feeds
#Designed for avalanche mainnet
#Returns description and token price 
# API address for localhost http://127.0.0.1:5000/api/prices/ 
w3 = Web3(Web3.HTTPProvider('https://api.avax.network/ext/bc/C/rpc'))
#w3.middleware_onion.inject(geth_poa_middleware, layer=0)
abi = '[{"inputs":[{"internalType":"address","name":"_aggregator","type":"address"},{"internalType":"address","name":"_accessController","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"int256","name":"current","type":"int256"},{"indexed":true,"internalType":"uint256","name":"roundId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"updatedAt","type":"uint256"}],"name":"AnswerUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"roundId","type":"uint256"},{"indexed":true,"internalType":"address","name":"startedBy","type":"address"},{"indexed":false,"internalType":"uint256","name":"startedAt","type":"uint256"}],"name":"NewRound","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"OwnershipTransferRequested","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"acceptOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"accessController","outputs":[{"internalType":"contract AccessControllerInterface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"aggregator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_aggregator","type":"address"}],"name":"confirmAggregator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_roundId","type":"uint256"}],"name":"getAnswer","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_roundId","type":"uint256"}],"name":"getTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestAnswer","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRound","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestTimestamp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"phaseAggregators","outputs":[{"internalType":"contract AggregatorV2V3Interface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"phaseId","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_aggregator","type":"address"}],"name":"proposeAggregator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"proposedAggregator","outputs":[{"internalType":"contract AggregatorV2V3Interface","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"proposedGetRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proposedLatestRoundData","outputs":[{"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer","type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256","name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_accessController","type":"address"}],"name":"setController","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
addrBTC = '0x2779D32d5166BAaa2B2b658333bA7e6Ec0C65743'
addrETH = '0x976B3D034E162d8bD72D6b9C989d545b839003b0'
addrAvax = '0x0A77230d17318075983913bC2145DB16C7366156'  #avax-usd pair See for ref:https://docs.chain.link/docs/avalanche-price-feeds/
addrJoe = '0x02D35d3a8aC3e1626d3eE09A78Dd87286F5E8e3a' #Joe-USD pair
addrLink= '0x49ccd9ca821EfEab2b98c60dC60F518E765EDe9a' #Link-USD pair
app = Flask(__name__)


@app.route('/')
def home():
    return 'In order to see token prices please go to /api/prices endpoint'

@app.route('/api/prices/')
async def getPrices():
  contractBtc = await getContract(addrBTC)
  contractEth = await getContract(addrETH)
  contractAvax = await getContract(addrAvax)
  contractJoe = await getContract(addrJoe)
  contractLink = await getContract(addrLink)
  
  latestDataBTC = contractBtc.functions.latestRoundData().call()  
  currentBtcPrice = latestDataBTC[1]/100000000
  
  latestDataETH = contractEth.functions.latestRoundData().call()  
  currentEthPrice = latestDataETH[1]/100000000
  
  latestDataAvax = contractAvax.functions.latestRoundData().call()  
  currentAvaxPrice = latestDataAvax[1]/100000000
  
  latestDataJoe = contractJoe.functions.latestRoundData().call()  
  currentJoePrice = latestDataJoe[1]/100000000
  
  latestDataLink = contractLink.functions.latestRoundData().call()  
  currentLinkPrice = latestDataLink[1]/100000000
  
  jsonResponse = [{ 'pair': 'BTC-USD', 'price': str(currentBtcPrice)},{ 'pair': 'ETH-USD', 'price': str(currentEthPrice)},{ 'pair': 'AVAX-USD', 'price': str(currentAvaxPrice)},{ 'pair': 'JOE-USD', 'price': str(currentJoePrice)}, { 'pair': 'LINK-USD', 'price': str(currentLinkPrice)}]
  return jsonify(jsonResponse)

@app.route('/api/prices/BTC-USD')
def getBTCPrice():
  contract =  w3.eth.contract(address=addrBTC, abi=abi)
  latestData = contract.functions.latestRoundData().call()  
  currentBTCPrice = latestData[1]/100000000
  jsonResponse = [{ 'pair': 'BTC-USD', 'price': str(currentBTCPrice)}]
  return jsonify(jsonResponse)
  
@app.route('/api/prices/ETH-USD')
def getETHPrice():
  contract =  w3.eth.contract(address=addrETH, abi=abi)
  latestData = contract.functions.latestRoundData().call()  
  currentETHPrice = latestData[1]/100000000
  jsonResponse = [{ 'pair': 'ETH-USD', 'price': str(currentETHPrice)}]
  return jsonify(jsonResponse)  

@app.route('/api/prices/AVAX-USD')
def getAvaxPrice():
  contract =  w3.eth.contract(address=addrAvax, abi=abi)
  latestDataAvax = contract.functions.latestRoundData().call()  
  currentAvaxPrice = latestDataAvax[1]/100000000
  jsonResponse = [{ 'pair': 'AVAX-USD', 'price': str(currentAvaxPrice)}]
  return jsonify(jsonResponse)
  
@app.route('/api/prices/JOE-USD')
def getJoePrice():
  contract =  w3.eth.contract(address=addrJoe, abi=abi)
  latestDataJoe = contract.functions.latestRoundData().call()  
  currentJoePrice = latestDataJoe[1]/100000000
  jsonResponse = [{ 'pair': 'JOE-USD', 'price': str(currentJoePrice)}]
  return jsonify(jsonResponse) 
  
@app.route('/api/prices/LINK-USD')
def getLinkPrice():
  contract =  w3.eth.contract(address=addrLink, abi=abi)
  latestDataLink = contract.functions.latestRoundData().call()  
  currentLinkPrice = latestDataLink[1]/100000000
  jsonResponse = [{ 'pair': 'LINK-USD', 'price': str(currentLinkPrice)}]
  return jsonify(jsonResponse)   
  

async def getContract(addr):
   contract =  w3.eth.contract(address=addr, abi=abi)
   return contract

if __name__ == '__main__':
    app.run()  # run our Flask app
