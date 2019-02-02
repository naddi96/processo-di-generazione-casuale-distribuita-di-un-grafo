import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import math
from itertools import chain, combinations
import time
import random



def salvaConclusioni(G,d,c,n,raund):
    #calcolo grado medio
    totDegree = 0
    for node in list(G.nodes):
        totDegree = totDegree + G.degree(node)
    gradomedio = totDegree/G.number_of_nodes()
    
    #calcolo deviazione standard
    k=0
    for node in list(G.nodes):
        k = k + pow(G.degree(node)-gradomedio,2)
    devStandard = pow(k/G.number_of_nodes(),1/2)
    
    #calcolo cammino minimo massimo tra due nodi
    pmax =0
    for x in list(G.nodes):
       path=nx.shortest_path_length(G,source=x) 
       for k in list(G.nodes):
          try:
               if path[k] > pmax:
                   pmax = path[k]
          except:
              pmax = pmax
    #formattazione dell output
    stri = "----------------------------------------------------------------\n"
    stri = stri+"numero di nodi: "+ str(n) +"\n"
    stri = stri+"valore di target 'd': "+ str(d)+"\n"
    stri = stri+"valore di tolleranza 'c': "+ str(c)+"\n"
    stri = stri+"numero totale di archi: "+ str(len(G.edges))+"\n"
    stri = stri+"numero di raund: "+ str(raund)+"\n"
    stri = stri+"grado medio dei nodi: "+ str(gradomedio)+"\n"
    stri = stri+"deviazione standard: "+ str(devStandard)+"\n"
    stri = stri+"cammino minimo massimo tra due nodi: "+ str(pmax) +"\n"
    stri = stri+"----------------------------------------------------------------\n"

    print(stri)
    f = open("risultati.txt","a")
    f.write(stri)
    f.close()
   


def check(G,c,d):
    for node in list(G.nodes):
        
        if(d > G.degree(node) or G.degree(node) > c*d):
            return True
    return False


def esegui(d,c,n):
    G = nx.Graph()
    G.add_nodes_from(range(1,n))
    
    raund=0
    while(check(G,c,d)):
        for node in list(G.nodes):
            if G.degree(node) < d:
                #lista dei possibibi nuovi vicini di node   
                l = list(set(list(G.nodes)) - set(G.neighbors(node))) 
                G.add_edge(node,random.choice(l))


        for node in list(G.nodes):
            if G.degree(node) > c*d:
                G.remove_edge(node,random.choice(list(G.neighbors(node))))

        raund = raund+1
    salvaConclusioni(G,d,c,n,raund)




def main():
    dlist = [2,3,4]
    clist = [2,3,4]
    nlist= [2**6,2**7,2**8,2**9,2**10]
    for n in nlist:
        for d in dlist:
            for c in clist:
                esegui(d,c,n)




if __name__ == "__main__":
    main()

