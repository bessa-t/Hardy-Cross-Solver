import pandas as pd
#Head Loss formula and tolerance

flow_tolerance = 0.1 #Given in [L/s]
head_loss_tolerance = 0.05 #Given in [m]
head_loss_formula = "HW" #Type "HW" for Hazen-Williams and "DW" for Darcy Weisbach!

#Data:
pipe_data = {
    "pipe_ID" : [1,2,3],
    "nodes_connected" : ["1-2","2-3","3-1"],
    "length_m": [100,70,74],
    "Diameter_mm" : [100,50,75],
    "C_HW" : [100,100,100],
    "initial_flow_LPS" : [4,-1,-3]
}
loops = {
    "Loop 1" :[1,2,3] #List of Pipe IDs in the loop.
}
nodal_flows = {
    1: 7.0,
    2: -5.0,
    3: -2.0
}
#Transforming Data into a sheet with pd:
pipes = pd.DataFrame(pipe_data)
pipes = pipes.set_index("pipe_ID")

#Test Block
if __name__ == "__main__":
    print("--- Nodal Flows (Boundary Conditions) ---")
    print(nodal_flows)
    print("\n--- Pipe Data (Iterative Network) ---")
    print(pipes)
    print("\n--- Loop Definitions ---")
    print(loops)
    