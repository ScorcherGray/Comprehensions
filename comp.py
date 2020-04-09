"""This script reads in files to perform exercizes on set comprehension"""

from collections import namedtuple

Suppliers = set()
Supplier = namedtuple('Supplier', ['sno', 'sname', 'status', 'city'])
sList = open('suppliers.txt')
supList = sList.readlines()
sList.close()
for line in supList:
    supSplit = line.split()
    #print(supSplit)
    for item in supSplit:
        Supp = item.split(',')
        Suppliers.add(Supplier(*Supp))
        #print(Supp)
#print(Suppliers)
Parts = set()
Part = namedtuple('Part', ['pno', 'pname', 'color', 'weight', 'city'])
pList = open('parts.txt')
partList = pList.readlines()
pList.close()
for line in partList:
    partSplit = line.split()
    #print(supSplit)
    for item in partSplit:
        prt = item.split(',')
        Parts.add(Part(*prt))
Projects = set()
Project = namedtuple('Project', ['jno', 'jname', 'city'])
prList = open('projects.txt')
projList = prList.readlines()
prList.close()
for line in projList:
    projSplit = line.split()
    for item in projSplit:
        prj = item.split(',')
        Projects.add(Project(*prj))
SPJs = set()
SPJ = namedtuple('SPJ', ['sno', 'pno', 'jno', 'qty'])
spjList = open('spj.txt')
spj_List = spjList.readlines()
spjList.close()
for line in spj_List:
    spjSplit = line.split()
    for item in spjSplit:
        spjq = item.split(',')
        SPJs.add(SPJ(*spjq))

bolt_suppliers = {p.pno for p in Parts if p.pname == 'Bolt'}
bolt_supp_ids = {r.sno for r in SPJs if r.pno in bolt_suppliers}
supplier_names = {s.sname for s in Suppliers if s.sno in bolt_supp_ids}
print('1. ', supplier_names)

blue_parts = {p.pno for p in Parts if p.color == 'Blue'}
blue_supp_ids = {r.sno for r in SPJs if r.pno in blue_parts}
blue_names = {s.sname for s in Suppliers if s.sno in blue_supp_ids}
print('2. ', blue_names)

not_Athens = {j.jno for j in Projects if j.city != 'Athens'}
not_Athens_ids = {r.sno for r in SPJs if r.jno in not_Athens}
athens_names = {s.sname for s in Suppliers if s.sno in not_Athens_ids}
print('3. ', athens_names)

not_oslo = {j.jno for j in Projects if j.city != 'Oslo'}
not_oslo_id = {r.pno for r in SPJs if r.jno in not_oslo}
name_color = {(p.pname, p.color) for p in Parts if p.pno in not_oslo_id}
print('4. ', name_color)

name_city = {(s.sname, s.city) for s in Suppliers}
name_suppliers = {s.city: (name, s.sname) for s in Suppliers for (name, city) in name_city if s.city == city if s.sname != name}
#names = {(name1, name2) for (name1, name2) in name_suppliers}
print('5. ', name_suppliers)

#supplier_city = {s.city: s.sname for s in Suppliers for s.sname in {s.sname for s in Suppliers }}
#print('6. ', supplier_city)
