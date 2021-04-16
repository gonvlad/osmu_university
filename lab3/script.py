import subprocess
import os

# Say hello and get number of virtual machines
print("=> Hello")
number_of_machines = int(input("Enter number of machines: "))
if number_of_machines < 1 or number_of_machines > 253:
    print("=> Entered WRONG number of virtual machines")
    exit(0)
else:
    print("=> Entered RIGHT number of virtual machines")

# List of tuples with network parameters
network_settings_list = []

# Set network parameters for each virtual machine
for i in range(number_of_machines):
    print("\tConfiguring machine number " + str(i + 1) + ":")
    ip_address = "192.168.50." + str(i + 1)
    network_name = "goncharov_vmid_" + str(i + 1)
    os.mkdir("./vmid" + str(i + 1))
    vagrantfile_path = "./vmid" + str(i + 1) + "/Vagrantfile"
    with open(vagrantfile_path, "w") as file:
        print("\t" + ip_address)
        print("\t" + network_name)
        file.write('Vagrant.configure("2") do |config|\n')
        file.write('\tconfig.vm.define "vmid' + str(i + 1) + '" do |vmid' + str(i + 1) + '|\n')
        file.write('\t\tconfig.vm.box = "ubuntu/trusty64"\n')
        file.write('\t\tconfig.vm.network "private_network", ip: "' + ip_address + '"\n')
        file.write('\t\tconfig.vm.hostname = "' + network_name + '"\n')
        file.write('\t\tconfig.vm.provider :virtualbox do |vb|\n')
        file.write('\t\t\tvb.name = "' + "goncharovVMID" + str(i + 1) + '" \n')
        file.write('\t\t\tvb.gui = true\n')
        file.write('\t\t\tvb.cpus = 1\n')
        file.write('\t\t\tvb.memory = "512"\n')
        file.write('\t\tend\n')
        file.write('\tend\n')
        file.write('end')
        print("\t=> VagrantFile was created in folder - vmid" + str(i + 1))
    print("\t=> Running virtual machine VMID" + str(i + 1))
    return_code = subprocess.call(("cd ./vmid" + str(i + 1) + " | vagrant up"), shell=True)  
    network_settings_list.append((ip_address, network_name))

