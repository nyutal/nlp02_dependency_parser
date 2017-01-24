# nlp02_dependency_parser

uses a python implementation of Chu-Liu/Edmond's algorithm
to find the minimum spanning tree in a directed graph.

Usage:
import edmonds

Below, g is graph representation of minimum spanning tree
root is the starting node of the MST, and G is the input graph
g = edmonds.mst(root,G)

References
----------

* http://en.wikipedia.org/wiki/Edmonds's_algorithm
* http://algowiki.net/wiki/index.php/Edmonds's_algorithm

## how to run tests from weight file:
*in the configuration file set the following:*  
test_file_name = 'HW2-files/test.labeled' #(instead None)       
test_max_samples = 0    
weights_src = <path to weight file name> #(instead None)    
weak_root = False #for basic_train     
weak_root = True # for basic_train_weeker_root_connection, basic_train_with_filters    
is_complex = False  

at each run you will get accuracy, please produce graphs with acccuracy from 10..100 to all models.   
you can put them in one graph side by side in order to compare them...
