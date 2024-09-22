import math

def calculate_angle_ABM_ABC(AB, BC):
    A = (AB, 0)
    B = (0, 0)
    C = (0, BC)
    
    M = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)

    BM = (M[0] - B[0], M[1] - B[1])
    BC = (C[0] - B[0], C[1] - B[1])
    
    dot_product = BM[0] * BC[0] + BM[1] * BC[1]
    
    magnitude_BM = math.sqrt(BM[0]**2 + BM[1]**2)
    magnitude_BC = math.sqrt(BC[0]**2 + BC[1]**2)
    
    cos_angle = dot_product / (magnitude_BM * magnitude_BC)
    
    angle_MBC = math.degrees(math.acos(cos_angle))
    
    angle_MBC = round(angle_MBC)
    
    return angle_MBC

AB = float(input())
BC = float(input())

angle_MBC = calculate_angle_ABM_ABC(AB, BC)
print(round(angle_MBC))
