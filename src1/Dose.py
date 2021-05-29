import numpy as np

def dose(Gy,mean_energy_dep):
    eV=1.60218e-19  # ev to Joule
    volume =  1.161e-5#1.161e-5  # mass of volume in kg -> 1.161e-5:  cell nucleus volume -> 1.131e-13
    deposit2Joule = eV*mean_energy_dep
    numberProt = Gy*volume/deposit2Joule
    print(numberProt)
    return int(numberProt)


if __name__=='__main__':  # test function
    print(dose(np.array([1,2,3,5,8,10]),75369))
