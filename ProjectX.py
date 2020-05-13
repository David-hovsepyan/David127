##############################################################################################
print('project management tool')
num1 = input('input total design resources(integer):\t')
num2 = input('input total manufacturing resources(integer):\t')
design_resources_total = int(num1)
man_resources_total = int(num2)

##############################################################################################
def design_department(scale):
    global design_resources_total
    design_hours= scale*0.4
    if design_hours == 240:
        des_busy_resources = 3
        wasted_time = design_hours/3
    elif design_hours ==120:
        des_busy_resources = 2
        wasted_time = design_hours/2
    elif design_hours ==40:
        des_busy_resources = 1
        wasted_time = design_hours
    if design_resources_total - des_busy_resources < 0:
        print('no design resources for this project')
        print ('for design team you need\t\t', des_busy_resources, 'additional resources')
    else:
        design_resources_total = design_resources_total - des_busy_resources
        print ('design wasted time\t\t\t\t', round(wasted_time))
        print('busy design resources\t\t\t', des_busy_resources, 'resources')
        print('free design resources\t\t\t', design_resources_total, 'resources')
#############################################################################################
def manufacturing_department(scale):
    global man_resources_total
    man_hours= scale*0.6
    if man_hours == 360:
        man_busy_resources = 3
        man_wasted_time = man_hours/3
    elif man_hours ==180:
        man_busy_resources = 2
        man_wasted_time = man_hours/2
    elif man_hours ==60:
        man_busy_resources = 1
        man_wasted_time = man_hours
    if man_resources_total - man_busy_resources < 0:
        print('no manufacturing resources for this project')
        print ('for manufacturing team you need\t', man_busy_resources, 'additional resources')
    else:
        man_resources_total = man_resources_total - man_busy_resources
        print ('manufacturing wasted time\t\t', round(man_wasted_time))
        print('busy manufacturing resources\t', man_busy_resources, 'resources')
        print('free manufacturing resources\t', man_resources_total, 'resources')
#############################################################################################
def sorting(lists):
    for i in range(len(lists)):
        proj_name1 = lists[i][0]
        scale1 = lists[i][1]
        priority1 = lists[i][2]
        if (scale1=='large-scale' or scale1=='large'):
            scale = 600
        elif (scale1 =='medium-scale' or scale1 =='medium'):
            scale = 300
        elif (scale1=='small-scale' or scale1=='small'):
            scale = 100
        print ('project name\t\t\t\t\t', proj_name1)
        print('total hours for project\t\t\t', scale1,scale,'hours',priority1)
        design_department(int(scale))
        manufacturing_department(int(scale))
        print('_' * 70)
#############################################################################################
def priority_sort(priority):
    if (priority == 'urgent'):
        lst1.append(line)
    elif (priority == 'planned'):
        lst2.append(line)
    elif (priority == 'flexible'):
        lst3.append(line)
    else:
        lst3.append(line)
        print('no priority for this project, added as flexible')
#############################################################################################
def main():
    action = input("choose Enter file name or inout a project fn/pr:\t")
    if (action=='fn'):
        name = input ("enter file name:\t")
        if len(name) < 1 : name = "ProjectX.txt"
        handle = open(name)
        lst1= list()
        lst2= list()
        lst3= list()
        for line in handle:
            line = line.split()
            prior = line[2]
            priority_sort(prior)
        sorting(lst1)
        sorting(lst2)
        sorting(lst3)
    elif (action=='pr'):
        lst1 = list()
        lst2 = list()
        lst3 = list()
        while True:
            name1 = input ('enter project name, enter project scale(large/medium/small), enter progect priority(urgent/planned/flexible:)\t')
            if name1 == 'done':
                break
            else:
                line1 = list()
                line1.append(name1)
                for line in line1:
                    line = line.split(', ')
                    prior = line[2]
                    priority_sort(prior)
        sorting(lst1)
        sorting(lst2)
        sorting(lst3)
main()
#############################################################################################
