import data
import pandas as pd
import math
def main():
    class head_loss_calculator:
        #Object responsable for calculating the head loss using different formulas
        def __init__(self):
            self.g = 9.81  # Acceleration of gravity (m/s^2)
            self.vis = 1.002 * 10**-6 #Kinematic Viscosity (m^2/s)
        def check_data(self,pipe_data,loops,nodal_flows):
            pass
            print("Iniciating Data Verification")
            flow_sum = sum(nodal_flows.values())
            if flow_sum > 0.0001:
                raise ValueError("Sum of the nodal flows has to be equal 0")
            #if pipe_data[]
            print("Data ok")
        def calculate_loss(self,formula,length,diameter,flow,loss_coefficient):
            if formula == "HW":
                c = loss_coefficient
                n = 1.85
                m = 4.87
                R = 10.64 * length * c^-1.85
    #Test Block
    if __name__ == "__main__":
        my_calculator = head_loss_calculator()
        test = my_calculator.check_data(data.pipe_data,data.loops,data.nodal_flows)
        print(test)
main()