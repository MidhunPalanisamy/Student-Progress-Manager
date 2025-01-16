import mysql.connector as mc
import matplotlib.pyplot as mp

a = mc.connect(host='your_hostname', passwd='your_password', user='your_user')
b = a.cursor()

b.execute("use tmm")

pas = int(input("Enter the Password:"))

if pas == 120021:

    nm = input("Enter your Name:")
    sb = input("Enter the subject you are handling:")

    b.execute("insert into tv values('{}','{}',date(now()))".format(nm, sb))

    a.commit()

    print('(a)Add record')
    print('(b)View record')
    print('(c)Delete record')
    print('(d)View all the records')
    print('(e)Graphical representation of a student in several tests')

    x = input("a/b/c/d/e:").lower()

    nn = int(input("Enter how many times you want to repeat the process:"))

    for xx in range(0, nn):
        print("Process count:", xx+1)

        if x == 'a':

            y = input("Enter the Student ID:")
            p = input("Enter the Test number :")
            q = input("Enter the Name of the student:")
            r = input("Enter IP mark :")
            s = input("Enter Maths mark :")
            t = input("Enter English mark :")
            u = input("Enter Physics mark :")
            v = input("Enter Chemistry mark :")
            rs = input("Enter the Rank of the student :")
            tot = float(r) + float(s) + float(t) + float(u) + float(v)

            b.execute("insert into tm values({},{},'{}',{},{},{},{},{},{},{})".format(y, p, q, r, s, t, u, v, tot, rs))

            a.commit()

            b.execute("select * from tm where id={}".format(y))

            for i in b:
                print(i)

            print('The record is added successfully!!')

        elif x == 'b':

            y = int(input("Enter the Student ID:"))

            b.execute("select * from tm where id={}".format(y))

            for i in b:
                print(i)

        elif x == 'c':
            nm = int(input('Enter the Student ID you want to delete:'))

            b.execute("Select * from tm where id={}".format(nm))

            for i in b:
                print(i)
            print('You are trying to delete the above record.')
            ss = input('Do you want to continue?(Y/N)').lower()

            if ss == 'y' or ss == 'yes':

                b.execute('delete from tm where id={}'.format(nm))

                a.commit()

                print('Record removed successfully!!!')

            elif ss == 'n' or ss == 'no':

                print('Process has been killed!')

            else:
                print('Error!!!')
                exit()

        elif x == 'd':

            b.execute("select * from tm")

            for i in b:
                print(i)

        elif x == 'e':

            id=int(input("Enter the respected Student's ID:"))

            b.execute("select * from tm where ID={}".format(id))

            for dt in b:
                print(dt)

            b.execute("select T_NO from tm where ID={}".format(id))
            tst=list(b)
            a.commit()

            b.execute("select IP from tm where ID={}".format(id))
            ip=list(b)
            a.commit()

            b.execute("select Phy from tm where ID={}".format(id))
            phy=list(b)
            a.commit()

            b.execute("select Che from tm where ID={}".format(id))
            che=list(b)
            a.commit()

            b.execute("select Mat from tm where ID={}".format(id))
            mat=list(b)
            a.commit()

            b.execute("select Eng from tm where ID={}".format(id))
            eng=list(b)
            a.commit()

            mp.xticks(range(1,len(tst)+1))

            mp.plot(tst, ip, color='blue', label='IP')
            mp.plot(tst, mat, color='red', label='MATHS')
            mp.plot(tst, phy, color='yellow', label='Physics')
            mp.plot(tst, che, color='g', label='Chemistry')
            mp.plot(tst, eng, color='#903600', label='English')

            mp.xlabel('TEST NO.')
            mp.ylabel('Marks')

            mp.legend(loc='upper right')

            mp.show()

        else:
            print('Something went wrong....')

            exit()

else:
    print("You are not authorized user.")
    exit()
