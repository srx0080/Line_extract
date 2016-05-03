# Extract the line in the experiment result txt files
#ext = open("C:/Users/user/Dropbox/Master/Prism/Experiment/20160422_test/extract.txt", 'a') 
ext = open("D:/Registry/Dropbox/Master/Prism/Experiment/20160425/extract.txt", 'a')
ext.write("#Degree #Wavelength(nm) #Wavenumber(1/cm) #Intensity(Counts)\n")
for i in range(-45,46, 5):
    #loc_ref = "C:/Users/user/Dropbox/Master/Prism/Experiment/20160422_test/20160422_%d.txt" %i
    loc_ref = "D:/Registry/Dropbox/Master/Prism/Experiment/20160425/20160425_%d.txt" %i
    ref = open(loc_ref, 'r')
    line = ref.readlines()
    de = i #inverse the sequence of degrees
    degree = "%d\t\t" %de 
    ext_data = degree + line[244] 
    ext.write(ext_data)
    ref.close()
ext.close()


