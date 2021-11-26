#!/usr/bin/env python
# coding: utf-8

# ### Degree distribution analysis;
# ### Connected components analysis;
# ### Path analysis;
# ### Clustering Coefficient, Density analysis;
# ### Centrality analysis.

# In[2]:


import networkx as nx


# In[3]:


import matplotlib.pyplot as plt


#  (i) random and (ii) preferential attachment graphs

# In[4]:


g = nx.read_edgelist("F:\\Study\\Spring19\\Network\\project\\sna_li.csv", delimiter=",", nodetype=int)


# In[5]:


#nx.info(g)


# In[6]:


g.number_of_nodes()


# In[7]:


for i in range(0, 10001):
    if i not in g.nodes():
        g.add_node(i)
g.number_of_nodes()


# In[8]:


g.number_of_edges()


# In[8]:


#creation of a random graph r
p = 2*g.number_of_edges()/(g.number_of_nodes()*(g.number_of_nodes()-1))
r = nx.erdos_renyi_graph(g.number_of_nodes(), p)


# In[9]:


r.number_of_edges()


# In[10]:


r.number_of_nodes()


# In[11]:


# creation of preferential attachment graph b
m = int(g.number_of_edges()/g.number_of_nodes())
b = nx.barabasi_albert_graph(g.number_of_nodes(), m)


# In[12]:


b.number_of_edges()


# In[13]:


b.number_of_nodes()


# In[14]:


g.number_of_selfloops()


# In[16]:


g.is_directed()


# In[17]:


g.degree(nbunch=[9935]) # compute the degree of a set of nodes (if specified)


# In[16]:


count=0
pop=-1
for n in g.nodes():
    if g.degree(n)>400:
        count=count+1
        pop=n
        print(pop, 'degree:', g.degree(pop))
print('count:', count)


# In[52]:


count=0
for n in r.nodes():
    if r.degree(n)>400:
        count=count+1
print('count:', count)
    


# In[53]:


count=0
for n in b.nodes():
    if b.degree(n)>400:
        count=count+1
        #print(n, 'degree:', g.degree(n), 'count:', count)
print('count:', count)


# In[23]:


a=nx.closeness_centrality(g) # compute the closeness centraliry of all nodes (and access the value of node 0)
print(len(a))


# In[11]:


print(a)


# In[12]:


b=nx.betweenness_centrality(g) # compute the betweenness centraliry of all nodes (and access the value of node 0)
print(len(b))


# In[19]:


hist = nx.degree_histogram(g)
    
plt.plot(range(0, len(hist)), hist, ".")
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("#Nodes")
plt.loglog()
plt.show()


# In[20]:


hist = nx.degree_histogram(r)
    
plt.plot(range(0, len(hist)), hist, ".")
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("#Nodes")
plt.loglog()
plt.show()


# In[21]:


hist = nx.degree_histogram(b)
    
plt.plot(range(0, len(hist)), hist, ".")
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("#Nodes")
plt.loglog()
plt.show()


# In[22]:


nx.number_connected_components(r)


# In[24]:


nx.diameter(r) 


# In[23]:


nx.number_connected_components(b)


# In[25]:


nx.diameter(b) 


# In[15]:


nx.number_connected_components(g)


# In[15]:



comps = list(nx.connected_components(g)) # get a list of connected components (for decreasing size)
for i in range (1, 3436):   
    #comp_1 = nx.subgraph(g, comps[i]) # build a subgraph on the second component
    if len(comps[i])>9:
        print(comps[i], i)
comp_1 = nx.subgraph(g, comps[139]) # build a subgraph on the second component
nx.draw(comp_1)


# In[67]:


comp_0 = comps[0]
print(comp_0)


# In[17]:


print(len(comps[0]))


# In[18]:



print(len(comps[139]))


# In[19]:



list(g.neighbors(139))


# In[20]:



ego = nx.ego_graph(g, 139) # ego network of the node 139
nx.draw(ego, with_labels=True)


# In[21]:


nx.shortest_path(g, source=0, target=30)


# In[22]:


nx.diameter(g.subgraph(comps[0])) 


# In[28]:


nx.diameter(g.subgraph(comps[139])) 


# In[30]:


nx.average_shortest_path_length(g.subgraph(comps[0])) 


# In[19]:


nx.average_shortest_path_length(r) 


# In[20]:


nx.average_shortest_path_length(b) 


# In[ ]:


from networkx.algorithms import tournament


# In[ ]:


tournament.is_tournament(h)


# In[ ]:


h = g.to_directed()
#h.edges()


# In[ ]:


#def hamilton(G):
#    F = [(G,[G.nodes()[0]])]
#    n = G.number_of_nodes()
#    while F:
#        graph,path = F.pop()
#        confs = []
#        for node in graph.neighbors(path[-1]):
#            conf_p = path[:]
#            conf_p.append(node)
#            conf_g = nx.Graph(graph)
#            conf_g.remove_node(path[-1])
#            confs.append((conf_g,conf_p))
#        for g,p in confs:
#            if len(p)==n:
#                return p
#            else:
#                F.append((g,p))
#    return None


# In[26]:


nx.has_path(r, 2, 24)


# In[ ]:


nx.is_biconnected(h)


# In[58]:


nx.density(g)


# In[28]:


nx.density(r)


# In[29]:


nx.density(b)


# In[ ]:


c=nx.triangles(g)
print(len(c))


# In[25]:


cr=nx.triangles(r)
print(len(cr))


# In[40]:


#cb[155]

ego = nx.ego_graph(r, 1) # ego network of the node 0
nx.draw(ego, with_labels=True)


# In[27]:


cr[444]


# In[29]:


cb=nx.triangles(b)
print(len(cb))


# In[54]:


c[139]


# In[ ]:


ClCoef=nx.clustering(g)[139]
ClCoef


# In[32]:


ClCoefr=nx.clustering(r)
ClCoefr


# In[33]:


ClCoefb=nx.clustering(b)
ClCoefb


# In[32]:


ClCoefr[1]


# In[34]:


nx.average_clustering(g)


# In[35]:


nx.average_clustering(r)


# In[36]:


nx.average_clustering(b)


# In[39]:


ClCen = nx.closeness_centrality(g)


# In[37]:


ClCenr = nx.closeness_centrality(r)


# In[38]:


ClCenb = nx.closeness_centrality(b)


# In[59]:


ClCenr[139]


# In[ ]:


ClCen[9935]


# In[18]:


for i in range (0, 10001):
    if g.degree[i]==0:
        print(i)
        break
    


# In[64]:


for i in range (0, 10001):
    if b.degree[i]>5:
        print(i)
        break


# In[42]:


ClCen[8]


# In[43]:


ma=0
ind=-1
for i in ClCenr:
    if ClCenr[i]>ma:
        ma=ClCenr[i]
        ind=i
print(ma, ind)


# In[44]:


ma=0
ind=-1
for i in ClCenb:
    if ClCenb[i]>ma:
        ma=ClCenb[i]
        ind=i
print(ma, ind)


# In[45]:


ma=0
ind=-1
for i in ClCen:
    if ClCen[i]>ma:
        ma=ClCen[i]
        ind=i
print(ma, ind)


# In[56]:


BetwC=nx.betweenness_centrality(g)


# In[14]:


BeCe = nx.edge_betweenness_centrality(g)


# In[16]:


BeCe


# In[19]:


ma=0
ind=-1
for i in BeCe:
    if BeCe[i] > ma:
        ma = BeCe[i]
        ind = i
print(ma, ind)


# In[17]:


BeCer = nx.edge_betweenness_centrality(r)


# In[57]:


BetwCr = nx.betweenness_centrality(r)


# In[27]:


m_becer=0
ind_becer = -1
for i in BeCer:
    if BeCer[i] > m_becer:
        m_becer = BeCer[i]
        ind_becer = i
print(m_becer, ind_becer)


# In[21]:


BeCeb = nx.edge_betweenness_centrality(b)


# In[26]:


m_beceb = 0
ind_beceb = -1
for i in BeCeb:
    if BeCeb[i] > m_beceb:
        m_beceb = BeCeb[i]
        ind_beceb = i
print(m_beceb, ind_beceb)


# In[30]:


mi_bece = 1000000
indi_bece = 100000
for i in BeCe:
    if BeCe[i] < mi_bece:
        mi_bece = BeCe[i]
        indi_bece = i
print(mi_bece, indi_bece)


# In[29]:


mi_becer = 1000000
indi_becer = 100000
for i in BeCer:
    if BeCer[i] < mi_becer:
        mi_becer = BeCer[i]
        indi_becer = i
print(mi_becer, indi_becer)


# In[28]:


mi_beceb = 1000000
indi_beceb = 100000
for i in BeCeb:
    if BeCeb[i] < mi_beceb:
        mi_beceb = BeCeb[i]
        indi_beceb = i
print(mi_beceb, indi_beceb)


# In[58]:


BetwCb=nx.betweenness_centrality(b)


# In[59]:


BetwC[139]


# In[50]:


BetwC[9935]


# In[51]:


BetwC[139]


# In[52]:


maxim = 0
inde = -1
for i in BetwC:
    if BetwC[i] > maxim:
        maxim = BetwC[i]
        inde = i
print(maxim, inde)


# In[53]:


maxim=0
inde=-1
for i in BetwCr:
    if BetwCr[i]>maxim:
        maxim=BetwCr[i]
        inde=i
print(maxim, inde)


# In[54]:


maxim=0
inde=-1
for i in BetwCb:
    if BetwCb[i]>maxim:
        maxim=BetwCb[i]
        inde=i
print(maxim, inde)


# In[55]:


ego = nx.ego_graph(g, 5358) # ego network of the node 0
nx.draw(ego, with_labels=True)


# In[31]:


ego = nx.ego_graph(r, 1
                  ) # ego network of the node 0
nx.draw(ego, with_labels=True)


# In[57]:


ego = nx.ego_graph(b, 53) # ego network of the node 0
nx.draw(ego, with_labels=True)


# In[ ]:


BetwC[10000]


# In[43]:


#ego = nx.ego_graph(b, 10) # ego network of the node 0
#nx.draw(ego, with_labels=True)


# In[ ]:


nx.shortest_path(g.subgraph(comps[0]))


# In[ ]:


nx.average_shortest_path_length(g.subgraph(comps[]))


# In[15]:


sh_l = nx.shortest_path(g.subgraph(comps[0]))


# In[18]:


#plt.plot(range (0, len(sh_l)), sh_l, ".")
#plt.title("Shortest Path Distribution")
#plt.xlabel("Paths")
#plt.ylabel("Nodes")
#plt.loglog()
#plt.show()


# In[17]:


#sh_l


# In[19]:


#sh_l[16]


# In[31]:


sh_with = nx.shortest_path_length(g)
    


# In[34]:


sh_with = list (sh_with)


# In[36]:


sh_with[0]


# In[46]:


for i in range (0, 10000):
    if sh_l[i] == 16:
        print(sh_l[i])


# In[47]:


sing = nx.single_source_shortest_path(g, 139)


# In[48]:


sing


# In[1]:


si = nx.single_source_shortest_path_length(g, 139)


# In[52]:


if si == 5:
    print ('gh')


# In[56]:


import hvplot.networkx as hvnx


# In[ ]:


t = nx.path_graph(g)
hvnx.draw(t)


# In[24]:


dece = nx.degree_centrality(g)


# In[25]:


dece[5358]


# In[27]:


dece[33]


# In[30]:


ma_dece = 0
i_dece = -1
for i in dece:
    if dece[i] > ma_dece:
        ma_dece = dece[i]
        inde = i
print(ma_dece, inde)


# In[154]:


ne = list(g.neighbors(139))


# In[155]:


print(ne)


# In[79]:


lis = []
#lis.append(li)

for i in comps[0]: 
    sha = list(g.neighbors(i))
    lis.append(len(sha))
print(lis)


#1570, 1255, 6472, 4522, 4523, 4524, 1262, 1871, 2672, 7730, 1878, 6326, 1563, 4379


# In[69]:


betw = nx.betweenness_centrality(g.subgraph(comps[0]))


# In[70]:


betw.values()


# In[71]:


clo = nx.closeness_centrality(g.subgraph(comps[0]))


# In[72]:


dee = nx.degree_centrality(g.subgraph(comps[0]))


# In[75]:


len(lis)


# In[138]:


plt.plot(lis, clo.values(), "*")
plt.plot(lis, betw.values(), "-")
plt.plot(lis, dee.values(), ".")
plt.title("All metrics")
plt.xlabel("Number of neighbors")
plt.ylabel("Closeness Centrality")

plt.show()


# In[153]:



plt.plot(lis, clo.values(),"*")

#plt.plot(lis, betw.values(), "-")
#plt.plot(lis, dee.values(), ".")
#plt.title("Что-то такое")
plt.xlabel("Number of neighbors")
plt.ylabel("Closeness Centrality")

plt.show()


# In[136]:


#plt.plot(lis, clo.values(), "*")
plt.plot(lis, betw.values(), "*")
#plt.plot(lis, dee.values(), ".")
#plt.title("Что-то такое")
plt.xlabel("Number of neighbors")
plt.ylabel("Betweenness Centrality")

plt.show()


# In[135]:


#plt.plot(lis, clo.values(), "*")
#plt.plot(lis, betw.values(), "-")
plt.plot(lis, dee.values(), ".")
#plt.title("Что-то такое")
plt.xlabel("Number of neighbors")
plt.ylabel("Degree Centrality")

plt.show()


# In[131]:


cou = 0
for i in lis: 
    if (i > 200) and (i < 299):
        #print(i)
        cou = cou + 1
        print(i, lis[i])
        break
print(cou)


# In[ ]:





# In[134]:


#plt.plot(lis, clo.values(), "*")
plt.plot(lis, range (0, len(lis)), "*")
#plt.plot(lis, dee.values(), ".")
plt.title("Distribution of number of neighbors")
plt.xlabel("Number of neighbors")
plt.ylabel("#Nodes")

plt.show()


# In[161]:


compsb = list(nx.connected_components(b))


# In[168]:


#list(b.neighbors(44))


# In[170]:


lisb = []
shab = []
#lis.append(li)

for i in compsb[0]: 
    shab = list(b.neighbors(i))
    lisb.append(len(shab))
print(lisb)

betwb = nx.betweenness_centrality(b)

betwb.values()

clob = nx.closeness_centrality(b)

deeb = nx.degree_centrality(b)

len(lisb)


# In[189]:


plt.plot(lisb, clob.values(), "*")
#plt.plot(lisb, betwb.values(), "-")
#plt.plot(lisb, deeb.values(), ".")
#plt.title("All metrics")
plt.xlabel("Number of neighbors")
plt.ylabel("Closeness Centrality")

plt.show()


# In[186]:


#plt.plot(lisb, clob.values(), "*")
plt.plot(lisb, betwb.values(), "*")
#plt.plot(lisb, deeb.values(), ".")
#plt.title("All metrics")
plt.xlabel("Number of neighbors")
plt.ylabel("Betweenness Centrality")

plt.show()


# In[176]:


#plt.plot(lisb, clob.values(), "*")
#plt.plot(lisb, betwb.values(), "-")
plt.plot(lisb, deeb.values(), ".")
#plt.title("All metrics")
plt.xlabel("Number of neighbors")
plt.ylabel("Closeness Centrality")

plt.show()


# In[172]:


len(compsb[0])


# In[179]:


compsr = list(nx.connected_components(r))


# In[180]:


lisr = []
shar = []
#lis.append(li)

for i in compsr[0]: 
    shar = list(r.neighbors(i))
    lisr.append(len(shar))
print(lisr)

betwr = nx.betweenness_centrality(r)

betwr.values()

clor = nx.closeness_centrality(r)

deer = nx.degree_centrality(r)

len(lisr)


# In[181]:


plt.plot(lisr, clor.values(), "*")
#plt.plot(lisr, betwr.values(), "-")
#plt.plot(lisr, deer.values(), ".")
#plt.title("All metrics")
plt.xlabel("Number of neighbors")
plt.ylabel("Closeness Centrality")

plt.show()


# In[187]:


#plt.plot(lisr, clor.values(), "*")
plt.plot(lisr, betwr.values(), "*")
#plt.plot(lisr, deer.values(), ".")
#plt.title("All metrics")
plt.xlabel("Number of neighbors")
plt.ylabel("Betweenness Centrality")

plt.show()


# In[183]:


#plt.plot(lisr, clor.values(), "*")
#plt.plot(lisr, betwr.values(), "-")
plt.plot(lisr, deer.values(), "*")
#plt.title("All metrics")
plt.xlabel("Number of neighbors")
plt.ylabel("Closeness Centrality")

plt.show()


# In[ ]:




