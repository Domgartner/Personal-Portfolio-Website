import mysql.connector              #Import required modules
from tabulate import tabulate

def search(table, choice, input):
    cur.execute("SELECT {}.{} FROM {} WHERE {}.{} = '{}'".format(table, choice, table, table, choice, input))
    var2 = cur.fetchall()
    empty_list_1 = []
    for row in var2:
        for val in row:
            empty_list_1.append(str(val))
    if (str(input) in empty_list_1):
        my_function(table, choice, input)
    else:
        print("\n** {} does not exist in database **".format(input))
    print()

def my_function(table,choice, input):
    select = "SELECT * FROM {} WHERE {}.{} = '{}'".format(table, table, choice, str(input))
    cur.execute(select)
    col_names=cur.column_names
    search_result=cur.fetchall()
    # Use tabulate to print the table
    print(tabulate(search_result, headers = col_names))

def nested_search_ID(table, table_nested, choice, choice_nested, name, var):
    select = "SELECT * FROM {} WHERE {}.{} IN (SELECT {}.{} From {} where {}.{} = '{}')".format(table, table, choice, table_nested, choice_nested, table_nested, table_nested, name, var)
    cur.execute(select)
    col_names = [d[0] for d in cur.description]
    search_result = cur.fetchall()
    print("Search found ",len(search_result)," Entries:\n")
    print(tabulate(search_result, headers = col_names, missingval= 'NULL'))
    print()

def browse_by_all(table):
    select = "SELECT * FROM {}".format(table)
    cur.execute(select)
    col_names = cur.column_names
    search_result = cur.fetchall()
    # Use the tabulate function to create a table
    print(tabulate(search_result, headers = col_names, missingval= 'NULL'))
    print()


def browse_function():
    while(1):
        if(login == 'guest'):
            print("1.Browse Art Pieces\n2.Browse Artists\n3.Browse Permanent Collection\n4.Browse Borrowed Collection\n5.Browse Exhibitions\n6. Quit")
        else:
            print("1.Browse Art Pieces\n2.Browse Artists\n3.Browse Permanent Collection\n4.Browse Borrowed Collection\n5.Browse Exhibitions\n6. Go Back")
        print()
        browse_selection = input("What would you like to browse? ")
        print()
        if (browse_selection == "1"):
            print("1. Browse by Artist\n2. Browse by Title\n3. Browse by Art Type\n4. Browse by Collection names\n5. Browse by Culture origin\n6. Browse by Year created\n7. Browse by Epoch\n8. Browse by ID number\n9. Browse by Exhibition\n10. Browse by collection\n11. Browse by ALL\n12. Go back\n") 
            browse_selection = input("What would you like to browse? ")
            print()
            table = "Art_Objects"
            if (browse_selection == "1"):
                #Artist
                choice = "Artist"
                artist_name = input("Which Artist Would You Like To Access? ")
                search(table, choice, artist_name)
            elif (browse_selection == "2"):
                #Title
                choice = "Title"
                artist_title = input("Which Title Would You Like To Access? ")
                print()
                search(table, choice, artist_title)  
            elif (browse_selection == "3"):
                print("1. Browse by Paintings\n2. Browse by Sculptures\n3. Browse by Statues\n4. Browse by Other\n5. Go Back")
                type_selection = input("What would you like to browse? ")
                if(type_selection == '1'):
                    print()
                    browse_by_all('Painting')
                elif(type_selection == '2'):
                    print()
                    browse_by_all('Sculpture')
                elif(type_selection == '3'):
                    print()
                    browse_by_all('Statue')
                elif(type_selection == '4'):
                    print()
                    browse_by_all('Other')
                elif(type_selection == '5'):
                    print("\nRe-directing...\n")
                    quit
                else:
                    print("** Invalid input **\n")
            elif (browse_selection == "4"):
                #Collection_name
                choice = "Collection_name"
                artist_Collection = input("Which Permanent Collection Would You Like To Access? ")
                search(table, choice, artist_Collection)               
            elif (browse_selection == "5"):
                # Culture origin
                choice = "Culture_origin"
                Culture_origin = input("Which Culture origin Would You Like To Access? ")
                search(table, choice, Culture_origin)              
            elif (browse_selection == "6"):
                # year created
                choice = "Year_created"
                Year_created_1 = input("Which Year created Would You Like To Access? ")
                search(table, choice, Year_created_1)             
            elif (browse_selection == "7"):
                choice = "Epoch"
                Epoch_1 = input("Which Epoch Would You Like To Access? ")
                search(table, choice, Epoch_1)              
            elif (browse_selection == "8"):
                choice = "ID_number"
                ID_num = input("Which ID number Would You Like To Access? ")
                search(table, choice, ID_num)               
            elif (browse_selection == "9"):
                table_nested = "Exhibition"
                choice = "ID_number"
                choice_nested = "Object_ID"
                ex_name = "Exhibition_name"
                Exhibition_name_var = input("Which exhibition name Would You Like To Access? ")
                nested_search_ID(table, table_nested, choice, choice_nested, ex_name, Exhibition_name_var)              
            # Collections
            elif (browse_selection == "10"):
                table_nested = "Collections"
                choice = "Collection_name"
                choice_nested = "Col_name"
                ex_name = "Col_type"
                Col_type_var = input("Which Collections type would You Like To Access (Museum / Personal)? ")
                nested_search_ID(table, table_nested, choice, choice_nested, ex_name, Col_type_var)             
            elif (browse_selection == "11"):
                browse_by_all(table)
            elif (browse_selection == "12"):
                print("\nRe-directing back to main menu...\n")
                quit
            else:
                print("** Choice is invalid. Please enter choice again. **\n")      
        elif (browse_selection == "2"):
            print("1. Browse by Artist name\n2. Browse by Epoch\n3. Browse by Country of origin\n4. Browse by main style\n5. Browse by ALL\n6. Go back\n")
            browse_selection = input("What would you like to browse? ")
            print()
            table = "Artist"
            if (browse_selection == "1"):
                #Artist name
                choice = "Artist_name"
                artist_name = input("Which Artist name Would You Like To Access? ")
                search(table, choice, artist_name)               
            elif (browse_selection == "2"):
                #epoch
                choice = "Epoch"
                Epoch = input("Which Epoch Would You Like To Access? ")
                search(table, choice, Epoch)              
            elif (browse_selection == "3"):
                #Country_origin
                choice = "Country_origin"
                Country_origin = input("Which Country of origin Would You Like To Access? ")
                search(table, choice, Country_origin)             
            elif (browse_selection == "4"):
                #Country_origin
                choice = "Main_style"
                Main_style = input("Which Main style Would You Like To Access? ")
                search(table, choice, Main_style)                
            elif (browse_selection == "5"):
                browse_by_all(table)
            elif (browse_selection == "6"):
                print("\nRe-directing back to main menu...\n")
                quit
            else:
                print("** Choice is invalid. Please enter choice again. **\n")   
        elif (browse_selection == "3"):
            print("1. Browse by Collection name\n2. Browse by Collection type\n3. Browse by ALL\n4. Go back\n")
            browse_selection = input("What would you like to browse? ")
            print()
            table = "Collections"
            if (browse_selection == "1"):
                #col_name
                choice = "Col_name"
                Collection_name = input("Which Collection name Would You Like To Access? ")
                search(table, choice, Collection_name)              
            elif (browse_selection == "2"):
                #col_name
                choice = "Col_type"
                Collection_type = input("Which Collection type Would You Like To Access (Museum / Personal)? ")
                search(table, choice, Collection_type)              
            elif (browse_selection == "3"):
                browse_by_all(table)
            elif (browse_selection == "4"):
                print("\nRe-directing back to main menu...\n")
                quit
            else:
                print("** Choice is invalid. Please enter choice again. **\n") 
        elif (browse_selection == "4"):
            print("1. Browse by Date borrowed\n2. Browse by Date returned \n3. Browse by Collection\n4. Browse by ID Number\n5.Browse by All\n6.Go Back")
            browse_selection = input("What would you like to browse? ")
            print()
            table = "Borrowed"
            if (browse_selection == "1"):
                #Artist
                choice = "Date_borrowed"
                borrowed_date = input("Which Date Would You Like To Access? ")
                search(table, choice, borrowed_date)               
            elif (browse_selection == "2"):
                #Title
                choice = "Date_returned"
                return_date = input("Which Return Date Would You Like To Access? ")
                search(table, choice, return_date)               
            elif (browse_selection == "3"):
                #Collection_name
                choice = "Collection_from"
                artist_Collection = input("Which Borrowed Collection Would You Like To Access? ")
                search(table, choice, artist_Collection)
            elif (browse_selection == "4"):
                # Culture origin
                choice = "ID_Number"
                ID_chosen = input("Which ID Number Would You Like To Access? ")
                search(table, choice, ID_chosen)              
            elif (browse_selection == "5"):
                browse_by_all(table)
            elif (browse_selection == "6"):
                print("\nRe-directing back to main menu...\n")
                quit
            else:
                print("** Entry is Invalid. **")                            
        elif (browse_selection == "5"):
            print("1.Browse by Exhibition name\n2.Browse by All\n3.Go back")
            exhibition = input("What Would You Like To Access? ")
            table = "Exhibition"
            if(exhibition == '1'):
                choice = 'Exhibition_name'
                exhibition_name = input("Which Exhibition Would You Like To Access? ")
                search(table, choice, exhibition_name)  
            elif(exhibition == '2'):
                browse_by_all(table)
            elif(exhibition == '3'):
                print("\nRe-directing back to main menu...\n")
            else:
                print("** Choice is Invalid. **")
        elif (browse_selection == "6"):
            if(login == 'admin' or login == 'user'):
                print("\nre-directing to main menu...\n")
                return
            else:
                cnx.close()
                print("\nArt Museum server connection closed successully...\nThank you For Visiting the Art Museum Database.\nGoodbye\n")
                exit(1)
        else:
            print("** Choice is invalid. Please enter choice again. **\n")

if __name__ == "__main__":
    #Introduction
    print("\n\t\t\t\t----- Welcome to the Art Museum Database -----\n\t\t\t----------------------------------------------------------------\n")
    login = input("Would you like to login for Admin or User access or browse as a guest (Admin / User / Guest)? ").lower()
    while(login not in ['admin', 'user', 'guest']):
        print("\n** Login choice does not exist **\n")
        login = input("Please enter a correct login declaration for database access (Admin / User / Guest)? ").lower()

    #User is an Admin
    #Admin connection information for database
    if(login == "admin" or login == 'user'):
        while(1):
            user_username = input("Enter username to connect to Art Museum database: ")
            user_password = input("Enter password for {}: ".format(user_username))
            print("\nConnecting to Server...")
            #connect to server
            try:
                cnx = mysql.connector.connect(
                        host = "127.0.0.1",
                        port = 3306,
                        user = user_username,
                        password = user_password
                )
                break
            except mysql.connector.Error:
                print("\n** login Information Incorrect. Please provide the correct login information to connect to the server. **\n")
        
    #User is guest
    elif(login == "guest"):
        print("Connecting to Server...")
        cnx = mysql.connector.connect(
            host = "127.0.0.1",
            port = 3306,
            user = 'guest',
            password = None
    )

    print("\nLogged in Successfully.\n")
    input("<<<  Press Enter to Continue  >>>\n")
    #Get a cursor and open art museum database
    cur = cnx.cursor()
    cur.execute("use ARTMUSEUM")

     #Admin Menu
    if(login == "admin" or login == "user" ):
        while(1):
            if(login == 'admin'):
                print("1. Write a Query\n2. Manage Art Objects\n3. User Management\n4. Browse the Collection\n5. Quit")
            else:
                print("1. Write a Query\n2. Manage Art Objects\n3. Browse the Collection\n4. Quit")
            choice = input("What action do you want to take: ")
            print()
            if (choice == "1"):
                #Write query for database
                admin_input = input("Write your query here: ")
                print()
                try: 
                    cur.execute(admin_input)
                    col_names=cur.column_names
                    search_result=cur.fetchall()
                    # Use tabulate to print the table
                    print(tabulate(search_result, headers = col_names))
                except:
                    print("** ERROR with query input **")
                print()
            elif (choice == "2"):
                #Manipulate database
                print("What Manipulate function would you like to execute?")
                print("1. Insert data\n2. Update data\n3. Delete data")
                manipulate_choice = input("Please Enter Selection: ")
                if (manipulate_choice == '1'):
                    print("How will you be inserting the data into the art objects table?")
                    print("1. Enter through text file\n2. Enter data manually")
                    insert_choice = input("Please Enter Selection: ")
                    if (insert_choice == '1'):
                        user_sqlfile = input("Please Enter the name of the SQL file: ")
                        try:
                           with open(user_sqlfile, 'r') as sql_file:
                               sql_script = sql_file.read()
                               cur.execute(sql_script)
                               cnx.commit()
                        except IOError:
                           print("\nUnable to open the file\n")
                           print()

                    elif (insert_choice == '2'):
                        table = input("Enter the name of the table: ")
                        data = []
                        num_columns = int(input("Enter the number of columns in the table: "))
                        for i in range(num_columns):
                            column_value = input(f"Enter the value for column {i+1}: ")
                            data.append(column_value)
                        sql = f"INSERT INTO {table} VALUES ({','.join(['%s'] * len(data))})"
                        try:
                            cur.execute(sql, data)
                            cnx.commit()
                            print("** Succesfully committed and inserted. **")
                        except mysql.connector.IntegrityError:
                            print('\n** Error Inserting data. **\n')
                    else:
                        print("\n** Choice is Invalid **\n")
                elif (manipulate_choice == '2'):
                    table_name = input("Please enter the table you would like to update (use the correct table name with capitals): ")
                    attribute_name = input("What attribute would you like to update (use the correct attribute name with capitals): ")
                    current_name =str(input("What is the current value of " + attribute_name + " you would like to change? "))
                    search_field = input("What is the new value of " + attribute_name + " : ")
                    sql_com = "UPDATE {} SET {} = '{}' WHERE {}.{} = '{}'".format(table_name, attribute_name, search_field, table_name, attribute_name, current_name)
                    try:
                        cur.execute(sql_com)
                        if cur.rowcount > 0:
                            print('\n** Tuple updated successfully **\n')
                        else:
                            print('\n** Failed to update tuple: no matching tuple found **\n')
                        cnx.commit()
                    except mysql.connector.IntegrityError:
                        print('Error: The update statement failed. A primary key or foreign key constraint was violated.')
                elif (manipulate_choice == '3'):
                    table_name = input("Please enter the table you would like to delete from (use the correct table name with capitals): ")
                    attribute_name = input("What attribute would you like to delete (use the correct attribute name with capitals): ")
                    current_name =str(input("What is the current value of " + attribute_name + " you would like to delete? "))
                    sql_com = "DELETE {}.* FROM {} WHERE {}.{} = '{}'".format(table_name, table_name, table_name, attribute_name, current_name)
                    try:
                        cur.execute(sql_com)
                        if cur.rowcount > 0:
                            print('\n** Tuple deleted successfully **\n')
                        else:
                            print('\n** Failed to delete tuple: no matching tuple found **\n')
                        cnx.commit()
                    except mysql.connector.IntegrityError:
                        print('\n** Error: The delete statement failed. A primary key or foreign key constraint was violated. **\n')
                else:
                    print("\n** Please enter a valid number (1,2,3) **\n")

            elif(choice == '3' and login == 'user'):
                browse_function()
            elif(choice == "3" and login == 'admin'):
                #User Management (Add, Block, Edit, Suspend)
                print("What management function would you like to execute?")
                print("1. Add User\n2. Edit User\n3. Block User")
                management_choice = input("Please Enter Selection: ")
                if (management_choice == "1"):
                    user_add = input("Please enter the username of the user you want to add: ")
                    role = input(f"Enter the role of {user_add}: ")
                    sqlline = "INSERT INTO users VALUES ('{}', '{}');".format(user_add, role)
                    if (role.lower() in ["user", "admin"]):
                        try:
                            cur.execute(sqlline)
                            cnx.commit()
                            print("\n** User added successfully. **\n")
                        except mysql.connector.IntegrityError:
                            print("\n** Error: Adding user failed. **\n")
                    else:
                        print("\n** Error: Adding user failed **\n")
                elif (management_choice == "2"):
                    user_old = input("Please enter the old username: ")
                    user_add = input(f"Please enter the new username for {user_old}: ")
                    role = input(f"Please enter the new role for {user_add}: ")
                    if (role.lower() in ["user", "admin"]):
                        try:
                            sqlline = "UPDATE users SET username = '{}' WHERE username = '{}';".format(user_add,user_old)
                            sqlline_2 = "UPDATE users SET user_role = '{}' WHERE username = '{}';".format(role,user_add)
                            cur.execute(sqlline)
                            cur.execute(sqlline_2)
                            cnx.commit()
                            print("\n** Update successful. **\n")
                        except mysql.connector.DataError:
                            print("\n** Error: Updating user failed. **\n")
                    else:
                        print("\n** Error: Updating user failed **\n")
                elif (management_choice == "3"):
                    user_block = input("Please enter the username of the user you want to block: ")
                    sqlline = "DELETE FROM users WHERE username = '{}';".format(user_block)
                    try:
                        cur.execute(sqlline)
                        cnx.commit()
                        print(f"\n** {user_block} has been blocked from viewing the database ARTMUSEUM **\n")
                    except mysql.connector.DataError:
                        print("\n** Error: Blocking user failed **\n")
                else:
                    print("\n** Choice is invalid. Please enter choice again. **\n")
            elif(choice == "4" and login == 'user'):
                cnx.close()
                print("\nArt Museum server connection closed successully...\nProgram Terminated\n")
                exit(1)
            elif(choice == "4" and login == 'admin'):
                #Browse Database (Also a Guest Function)
                browse_function()
            elif(choice == "5" and login == 'admin'):
                #Close server connection and exit
                cnx.close()
                print("\nArt Museum server connection closed successully...\nProgram Terminated.\n")
                exit(1)
            else:
                print("** Choice is invalid. Please enter choice again. **\n")

    #Guest Menu
    if(login == "guest"):
        browse_function()