import subprocess
profiles = subprocess.check_output("netsh wlan show profiles",shell=True).decode()
names=[line.split(":")[1].strip()
    for line in profiles.split("\n") if "all user Profile" in line]
for i ,names in enumerate(names,1):
    print(f"[i] {names}")
ch=int(input("\n choose wifi number: "))
wifi=names[ch-1]
result=subprocess.check_output(f"netsh wlan show profile \"{wifi}\" key=clear",shell=True).decode
print(f"\nPassword:{result.split(':')[1].strip()}")

