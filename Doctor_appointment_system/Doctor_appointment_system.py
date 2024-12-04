import mysql.connector
from mysql.connector import Error

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',     
        password='Surabhi@445',   
        database='doctor_appointments'
    )

def add_doctor(name, specialization):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO doctors (name, specialization) VALUES (%s, %s)', (name, specialization))
    conn.commit()
    cursor.close()
    conn.close()

def add_patient(name, age):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO patients (name, age) VALUES (%s, %s)', (name, age))
    conn.commit()
    cursor.close()
    conn.close()

def schedule_appointment(doctor_id, patient_id, appointment_time):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO appointments (doctor_id, patient_id, appointment_time) VALUES (%s, %s, %s)', 
                   (doctor_id, patient_id, appointment_time))
    conn.commit()
    cursor.close()
    conn.close()

def list_appointments():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT a.appointment_id, d.name AS doctor_name, p.name AS patient_name, a.appointment_time
        FROM appointments a
        JOIN doctors d ON a.doctor_id = d.doctor_id
        JOIN patients p ON a.patient_id = p.patient_id
    ''')
    appointments = cursor.fetchall()
    cursor.close()
    conn.close()
    return appointments

def cancel_appointment(appointment_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM appointments WHERE appointment_id = %s', (appointment_id,))
    conn.commit()
    cursor.close()
    conn.close()

def main():
    while True:
        print("\n1. Add Doctor\n2. Add Patient\n3. Schedule Appointment\n4. List Appointments\n5. Cancel Appointment\n6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter doctor's name: ")
            specialization = input("Enter specialization: ")
            add_doctor(name, specialization)

        elif choice == '2':
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            add_patient(name, age)

        elif choice == '3':
            doctor_id = int(input("Enter doctor ID: "))
            patient_id = int(input("Enter patient ID: "))
            appointment_time = input("Enter appointment time (YYYY-MM-DD HH:MM): ")
            schedule_appointment(doctor_id, patient_id, appointment_time)

        elif choice == '4':
            appointments = list_appointments()
            if appointments:
                for appointment in appointments:
                    print(f"Appointment ID: {appointment[0]}, Doctor: {appointment[1]}, Patient: {appointment[2]}, Time: {appointment[3]}")
            else:
                print("No appointments found.")

        elif choice == '5':
            appointment_id = int(input("Enter appointment ID to cancel: "))
            cancel_appointment(appointment_id)
            print(f"Appointment ID {appointment_id} has been canceled.")

        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
