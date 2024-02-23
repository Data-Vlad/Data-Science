import requests
import networkx as nx
import scipy as sp


#cateogry_list
category_list =[]
category_list.append("Category:Ice_hockey")
category_list.append("Category:American_football")
category_list.append("Category:Baseball")
category_list.append("Category:Basketball")


# The function below retrieve page titles for the specific categories. Then we will add pages (values) for each category (keys) to a dictionary
# and return the dictionary
def get_page_titles(category_list):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    dict ={}
    #FOR EACH CATEGORY
    for category in category_list:
       PARAMS = {
           "cmdir": "desc",
           "format": "json",
           "list": "categorymembers",
           "action": "query",
           "cmtitle": category,
           "cmsort": "timestamp"
}
       R = S.get(url=URL, params=PARAMS)
       DATA = R.json()

       PAGES = DATA["query"]["categorymembers"]

       for page in PAGES:
         #key/value pair to dictionary. key will be category and value will be page.
         dict[category] = page["title"]
         
         return dict



#The function below will  assist in constructing a network where nodes are pages and edges are connections and return the constructed graph
def construct_graph(category_list):
     graph=nx.Graph()
     dict = get_page_titles(category_list)
    

     for category,pages in dict.items():
        graph.add_nodes_from(pages,Category=category)
        for page in pages:
            for linked_page in pages:
              if page!= linked_page:
                graph.add_edge(page,linked_page)
                return graph




#I will now calculate the degree centrality
degree_centrality = nx.degree_centrality(construct_graph(category_list))
print(degree_centrality)

#I will now calculate eigenvector centrality
eigenvector_centrality = nx.eigenvector_centrality_numpy(construct_graph(category_list))
print(eigenvector_centrality )
