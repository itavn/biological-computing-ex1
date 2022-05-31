# Biological Computing - Exercise 1
## Roy Assa 322542226     
## Itav Nissim 322713488
###  20/05/2022


# Question #1: 
In this question we created a code file named: "Exercise1_Question1.py" <br>
In order to successfully run the code, you can choose between 2 options:

	1. Run the code in terminal. 
	   In this case, please follow the next steps carefully:
		1.1 Locate the directory the code is placed.
		
		1.2 Open the command propt in the current directory 
			by entering "cmd" in the directory's path search
			
		1.3 Inside the command prompt please enter the
			following command: "python Exercise1_Question1.py"
			
	2. Run the code in PyCharm. 
	   In this case, please follow the next steps carefully:
		2.1 Create new project by File -> New Project. 
		
		2.2 Place our code files inside the project's directory.
		
		2.2 Install all libraries we've imported in the codes. 
		
		2.3 Press Shift+F10 or press on "Run" button inside the GUI.
		
While running the code, you will be required to enter a value for n (number of vertices in the sub-graph). <br>
In addition, please enter a positive natural number. 

### Important Notice <br>
If you enter n>=5, the code will run for a significant amount of time. This is due to the complexity of the algorithm. After the code terminated, you will have a txt file "sub_graphs_with_n_nodes.txt" placed in the same directory of the codes, where n is the number of nodes in each sub-graph.


# Question #2:

In this question we created a code file named: "Exercise1_Question2.py" <br>
Please follow the nex instructions carefully: 

	1. Prior to running the code, you are required to run the first question 
	   in order to generate the "sub_graphs_with_n_nodes.txt" file that will
	   be used in this question. Failure to run the code from question 1 will
	   raise an exception, indication that the "sub_graphs_with_n_nodes.txt"
	   file is missing. 
	   
    2. Prepare a txt file (i.e. "edges_list.txt") inside the current directory
	   in the following format:
					   1 2
					   1 4
					   2 3
	   where each row represents a directed edge from left vertex to the right node.
	   These edges represent the test graph's edges.
	   
	2. Run the code using one of the suggested options above.
	
	3. While running the code, you will be asked to enter a value for n, the number 
	   of nodes in the motifs. Then, you will be asked to enter the file's path of 
	   the edges list of the given graph. As mentioned earlier, this file should
	   contain list of edges int he test graph.
	   
    4. Upon termination, you will have a new txt file inside the current directory 
	   named: "sub_graphs_isomorphic_count_with_n_nodes", where n stands for the number
	   of nodes in motifs searched in the test graph.



# Answers to questions 	  
## question #1:
	Part c):
	The maximal number n for which our program completed within 1 hour is n=4

   	Part d):
	The maximal number n for which our program completed within 2,4,8 hours is n=5
