from tkinter import Label, Frame, Text, Scrollbar, Tk, Toplevel, Button
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk
import datetime
import time
import threading

def show_qr_window():
    qr_window = Toplevel()
    qr_window.title("Transaction QR Code")
    qr_window.geometry("400x400")
    
    try:
        qr_image = Image.open("images/QR.png")
        qr_image = qr_image.resize((300, 300), Image.Resampling.LANCZOS)
        qr_tk = ImageTk.PhotoImage(qr_image)

        qr_label = Label(qr_window, image=qr_tk, bg="pink")
        qr_label.image = qr_tk
        qr_label.pack(pady=10)
        
        countdown_time = 30  # Transaction countdown timer in seconds
        time_label = Label(qr_window, text=f"Transaction Time: {countdown_time}s", font=("Arial", 12, "bold"))
        time_label.pack(pady=10)

        def update_timer():
            nonlocal countdown_time
            while countdown_time > 0:
                time.sleep(1)
                countdown_time -= 1
                time_label.config(text=f"Transaction Time: {countdown_time}s")
            qr_window.destroy()

        threading.Thread(target=update_timer, daemon=True).start()
        
        def print_report():
            print("Printing Report...")
            qr_window.destroy()
            # Add actual printing functionality here
            print("Report Printed Successfully!")
        
        print_button = Button(qr_window, text="Print Report", font=("Arial", 12, "bold"), command=print_report, bg="DeepPink2", fg="white")
        print_button.pack(pady=10)
        
    except Exception as e:
        error_label = Label(qr_window, text=f"Error loading QR image: {e}", fg="red")
        error_label.pack()
def dodont():
    dodont_window = Toplevel()
    dodont_window.title("Dos and Don'ts for Heart Patients")
    dodont_window.state("zoomed")

    try:
        bg_image = Image.open("images/dobackground.png")
        bg_image = bg_image.resize((dodont_window.winfo_screenwidth(), dodont_window.winfo_screenheight()), Image.Resampling.LANCZOS)
        bg_tk = ImageTk.PhotoImage(bg_image)

        bg_label = Label(dodont_window, image=bg_tk)
        bg_label.image = bg_tk
        bg_label.place(relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error loading background image: {e}")

    Label(dodont_window, text="✅ Dos", font=("Arial", 20, "bold"), fg="green", bg="white").pack(pady=10)
    dos_text = "\n• Maintain a healthy diet\n• Exercise regularly\n• Manage stress\n• Take medications as prescribed\n• Regular health checkups"
    Label(dodont_window, text=dos_text, font=("Arial", 16), bg="white").pack(pady=5)
    
    Label(dodont_window, text="❌ Don'ts", font=("Arial", 20, "bold"), fg="red", bg="white").pack(pady=10)
    donts_text = "\n• Avoid smoking and alcohol\n• Reduce salt and sugar intake\n• Don't skip medications\n• Avoid excessive stress\n• Don't ignore chest pain"
    Label(dodont_window, text=donts_text, font=("Arial", 16), bg="white").pack(pady=5)
    
    Button(dodont_window, text="Close", font=("Arial", 16, "bold"), command=dodont_window.destroy, bg="DeepPink2", fg="white").pack(pady=20)


def generate_report(window):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="992922",
            database="Heart_Data"
        )
        mycursor = mydb.cursor()
    except:
        Label(window, text="❌ Database Connection Failed!", fg="red", font=("Arial", 14, "bold")).place(relx=0.5, rely=0.5, anchor="center")
        return

    mycursor.execute("SELECT Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, result FROM data ORDER BY user DESC LIMIT 1")
    record = mycursor.fetchone()

    report_frame = Frame(window, bg="white", bd=5, relief="solid")
    report_frame.place(relx=0.5, rely=0.05, anchor="center", width=700, height=70)

    report_heading = Label(report_frame, text="📄 HEART HEALTH REPORT 📄", font=("Arial", 22, "bold"), fg="DeepPink2", bg="white")
    report_heading.pack(fill="both", expand=True)

    report_frame2 = Frame(window, bg="white", bd=5, relief="solid")
    report_frame2.place(relx=0.5, rely=0.15, anchor="center", width=700, height=60)

    report_label = Label(report_frame2, text="🩺 Patient's Medical Summary 🩺", font=("Arial", 18, "bold"), fg="DeepPink2", bg="white")
    report_label.pack(fill="both", expand=True)

    if record:
        name, date, dob, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, result = record
        sex = "Male ♂️" if sex == "1" else "Female ♀️"
        fbs = "Yes ✅" if fbs == "1" else "No ❌"
        exang = "Yes ⚠️" if exang == "1" else "No ✅"
        result = "⚠️ You HAVE Heart Disease" if result == "1" else "✅ You DO NOT Have Heart Disease"

        record_text = (
            f"🆔 Patient Name: {name}\n"
            f"📅 Report Date: {date}\n"
            f"🎂 Date of Birth: {dob}\n"
            f"🔢 Age: {age} years\n"
            f"⚧ Sex: {sex}\n\n"
            f"🔵 Medical Readings:\n"
            f"💓 Chest Pain Type (CP): {cp}\n"
            f"🔴 Resting Blood Pressure (Trestbps): {trestbps} mmHg\n"
            f"🩸 Cholesterol Level (Chol): {chol} mg/dL\n"
            f"🍬 Fasting Blood Sugar (FBS > 120 mg/dL): {fbs}\n"
            f"🫀 Resting Electrocardiographic Result (RestECG): {restecg}\n"
            f"❤️ Maximum Heart Rate Achieved (Thalach): {thalach} bpm\n"
            f"🚶‍♂️ Exercise-Induced Angina (Exang): {exang}\n\n"
            f"📉 ST Depression Induced by Exercise (Oldpeak): {oldpeak}\n"
            f"📈 Slope of Peak Exercise ST Segment: {slope}\n"
            f"🏥 Number of Major Vessels Colored by Fluoroscopy (CA): {ca}\n"
            f"🧬 Thalassemia (Thal): {thal}\n\n"
            f"📊 Final Diagnosis: {result}"
        )

        report_frame3 = Frame(window, bg="white", bd=5, relief="solid")
        report_frame3.place(relx=0.02, rely=0.25, anchor="nw", width=600, height=550)

        scrollbar = Scrollbar(report_frame3)
        scrollbar.pack(side="right", fill="y")

        report_text_widget = Text(report_frame3, font=("Arial", 14, "bold"), fg="DeepPink2", bg="white", wrap="word", yscrollcommand=scrollbar.set)
        report_text_widget.pack(fill="both", expand=True, padx=20, pady=20)
        report_text_widget.insert("1.0", record_text)
        report_text_widget.config(state="disabled")
        scrollbar.config(command=report_text_widget.yview)
        # ECG Waveform Generation
        ecg_frame = Frame(window, bg="white", bd=5, relief="solid")
        ecg_frame.place(relx=0.45, rely=0.25, anchor="nw", width=600, height=550)

        fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
        t = np.linspace(0, 1, 300)
        if restecg == 0:
            ecg_wave = np.sin(2 * np.pi * 5 * t) * np.exp(-3 * t)
        elif restecg == 1:
            ecg_wave = np.sin(2 * np.pi * 5 * t) * np.exp(-3 * t) + 0.1 * np.sin(2 * np.pi * 50 * t)
        else:
            ecg_wave = np.sin(2 * np.pi * 5 * t) * np.exp(-3 * t) + 0.3 * np.sin(2 * np.pi * 20 * t)
        ax.plot(t, ecg_wave, color='red')
        ax.set_title("ECG Signal")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        ax.grid()

        canvas = FigureCanvasTkAgg(fig, master=ecg_frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        canvas.draw()


        try:
            image = Image.open("images/print.png")
            image = image.resize((100, 100), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(image)

            img_label = Label(window, image=img_tk, bg="white", cursor="hand2")
            img_label.image = img_tk
            img_label.place(relx=0.88, rely=0.8)
            img_label.bind("<Button-1>", lambda e: show_qr_window())
        except Exception as e:
            print(f"Error loading image: {e}")
        try:
            image = Image.open("images/do.png")
            image = image.resize((100, 100), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(image)

            img_label = Label(window, image=img_tk, bg="white", cursor="hand2")
            img_label.image = img_tk
            img_label.place(relx=0.88, rely=0.5)
            img_label.bind("<Button-1>", lambda e: dodont())
        except Exception as e:
            print(f"Error loading image: {e}")
    
    mydb.close()
