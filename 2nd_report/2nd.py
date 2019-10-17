# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:52:39 2019

@author: User
"""

import networkx as nx
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats

import requests

def readNetwork(url=None, splitter=","):
  # ネットワークを読み込む
  if url == None:
    uploaded = files.upload()
    edge_text = list(uploaded.values())[0].decode()
  else:
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    edge_text = res.text

  # edgeとして読み込める形式に変換
  edge_list = list(item.split(splitter) for item in edge_text.split("\n"))
  edge_list = [a for a in edge_list if len(a) != 1]
  # 無向グラフを作成
  G = nx.Graph() 

  # ネットワークの作成
  G.add_edges_from(edge_list)
  return G

def showNetwork(G, node_value=None):
  #描画する
  # 描画サイズ
  plt.figure(figsize=(10,10))
  # ノードをバネモデルで配置する
  pos = nx.spring_layout(G, k=0.3, seed=0)
  # ノード，エッジ，ラベルの描画
  nx.draw_networkx_edges(G, pos, edge_color='red', width=1.5)
  if node_value == None:
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_nodes(G, pos, node_color='white', edgecolors="black")
  else:
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_nodes(G, pos, node_color=list(node_value.values()), cmap=plt.cm.Reds, edgecolors="black")
  
  # 描画
  plt.show()


G = readNetwork()
showNetwork(G)