pip install scikit-learn

import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('stress_level_trained.sav', 'rb'))

def stresslevel_prediction(input_data):
    id_np_array = np.asarray(input_data)
    id_reshaped = id_np_array.reshape(1, -1)

    # # Perform prediction
    # prediction = loaded_model.predict(id_reshaped)
    # predict_proba = loaded_model.predict_proba(id_reshaped)

    # # Print the predicted value
    # if prediction[0] == 0:
    #     return "No", predict_proba[0][1]
    # elif prediction[0] == 1:
    #     return "Yes", predict_proba[0][1]
    # else:
    #     return "Can't Detect", predict_proba[0][1]

    # Lakukan prediksi
    predict_proba = loaded_model.predict_proba(id_reshaped)[0]  # Ambil probabilitas dari prediksi

    # Tentukan level stres berdasarkan probabilitas yang diprediksi
    if predict_proba[1] >= 0 and predict_proba[1] <= 0.33:
        return "Rendah", predict_proba[1]
    elif predict_proba[1] > 0.33 and predict_proba[1] <= 0.65:
        return "Menengah", predict_proba[1]
    elif predict_proba[1] > 0.65 and predict_proba[1] <= 1:
        return "Tinggi", predict_proba[1]
    else:
        return "Tidak bisa di deteksi", predict_proba[1]

def display_probability(proba):
    proba_percentage = int(proba * 100)
    st.markdown(f"""
        <div style="position: relative; width: 100%; height: 30px; background: linear-gradient(to right, green 33%, yellow 33%, yellow 66%, red 66%); border-radius: 5px;">
            <div style="position: absolute; left: {proba_percentage}%; top: -10px; width: 0; height: 0; border-left: 10px solid transparent; border-right: 10px solid transparent; border-bottom: 20px solid black;">
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.write(f"Kemungkinan mengalami stress: {proba:.2f}")

def page0():
    st.markdown("""
        <div style="text-align: center;">
            <h1>STRESS LEVEL PREDICTION</h1>
        </div>
    """, unsafe_allow_html=True)
    st.image("mental.png")
    if st.button('Mulai', use_container_width=True):
        st.session_state.page_number = 1
        st.experimental_rerun()

def page1():
    st.markdown("""
        <div style="text-align: center">
            <h1>Gender</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    Gender = st.radio('APA JENIS KELAMIN ANDA?', ['Laki - Laki', 'Perempuan'])

    if Gender == "Perempuan":
        Gender = 0
    elif Gender == "Laki - Laki":
        Gender = 1
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.gender = Gender
            st.session_state.page_number = 2
            st.experimental_rerun()

    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 0
            st.experimental_rerun()

def page2():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Age</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    Age = st.radio('BERAPA UMUR ANDA?', ['Kurang dari 21', '21 - 35', '36 - 50', 'Lebih dari 50'])

    
    if Age == "Kurang dari 21":
        Age = 0
    elif Age == "21 - 35":
        Age = 1
    elif Age == "36 - 50":
        Age = 2
    elif Age == "Lebih dari 50":
        Age = 3
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.age = Age
            st.session_state.page_number = 3
            st.experimental_rerun()

    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 1
            st.experimental_rerun()

def page3():
    st.markdown("""
        <div style="text-align: center;">
            <h1>BMI Range</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    BMIRange = st.radio('Berdasarkan perhitungan BMI, Anda termasuk dalam kategori apa? (Normal BMI<=25.0, OverWeight BMI > 25.0)', ['Normal', 'Overweight'])
    
    if BMIRange == "Normal":
        BMIRange = 0
    elif BMIRange == "Overweight":
        BMIRange = 1

    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.bmiRange = BMIRange
            st.session_state.page_number = 4
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 2
            st.experimental_rerun()
    
    st.write("BB = Berat Badan (Kg)")
    st.write("TB = Tinggi Badan (m))")
    st.write("Perhitungan BMI = BB : (TB x TB)")

def page4():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Daily Shouting</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    DailyShouting = st.select_slider('SEBERAPA SERING KAMU BERTERIAK ATAU MERAJUK PADA SESEORANG?', 
                                     options=["Tidak Pernah", "Hampir Tidak Pernah", "Jarang", "Sangat Jarang", "Kadang-Kadang", "Sering", "Sangat Sering", "Biasanya","Hampir Selalu", "Selalu"])
    if DailyShouting == "Tidak Pernah" :
        DailyShouting = 1
    elif DailyShouting == "Hampir Tidak Pernah" :
        DailyShouting = 2
    elif DailyShouting == "Jarang" :
        DailyShouting = 3
    elif DailyShouting == "Sangat Jarang" :
        DailyShouting = 4
    elif DailyShouting == "Kadang-Kadang" :
        DailyShouting = 5
    elif DailyShouting == "Sering" :
        DailyShouting = 6
    elif DailyShouting == "Sangat Sering" :
        DailyShouting = 7
    elif DailyShouting == "Biasanya" :
        DailyShouting = 8
    elif DailyShouting == "Hampir Selalu" :
        DailyShouting = 9
    elif DailyShouting == "Selalu" :
        DailyShouting = 10

    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.dailyShouting = DailyShouting
            st.session_state.page_number = 5
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 3
            st.experimental_rerun()

def page5():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Daily Steps</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    DailySteps = st.slider('BERAPA LANGKAH YANG BIASANYA ANDA BERJALAN SETIAP HARI? (1000 Langkah = 1)', min_value=1, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.dailySteps = DailySteps
            st.session_state.page_number = 6
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 4
            st.experimental_rerun()

def page6():
    st.markdown("""
        <div style="text-align: center;">
            <h1> Sleep Hours</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    SleepHours = st.slider('BERAPA LAMA ANDA BIASANYA TIDUR? (Dalam Jam)', min_value=1, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.sleepHours = SleepHours
            st.session_state.page_number = 7
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 5
            st.experimental_rerun()

def page7():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Fruits & Veggies</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    FruitsVeggies = st.slider('BERAPA BANYAK BUAH ATAU SAYUR YANG ANDA MAKAN SETIAP HARI? (Dalam Jumlah)', min_value=1, max_value=5, value=3)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.fruitsVeggies = FruitsVeggies
            st.session_state.page_number = 8
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 6
            st.experimental_rerun()

def page8():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Time For Passion</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    TimeForPassion = st.slider('BERAPA JAM YANG ANDA HABISKAN SETIAP HARI UNTUK MELAKUKAN APA YANG ANDA INGINKAN? (Dalam Jam)', min_value=1, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.timeForPassion = TimeForPassion
            st.session_state.page_number = 9
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 7
            st.experimental_rerun()

def page9():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Weekly Meditation</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    WeeklyMeditation = st.select_slider('DALAM SEMINGGU, SEBERAPA SERING ANDA PUNYA KESEMPATAN UNTUK BERPIKIR TENTANG DIRI SENDIRI?', 
                                        options=["Tidak Pernah", "Hampir Tidak Pernah", "Jarang", "Sangat Jarang", "Kadang-Kadang", "Sering", "Sangat Sering", "Biasanya","Hampir Selalu", "Selalu"])
    
    if WeeklyMeditation == "Tidak Pernah" :
        WeeklyMeditation = 1
    elif WeeklyMeditation == "Hampir Tidak Pernah" :
        WeeklyMeditation = 2
    elif WeeklyMeditation == "Jarang" :
        WeeklyMeditation = 3
    elif WeeklyMeditation == "Sangat Jarang" :
        WeeklyMeditation = 4
    elif WeeklyMeditation == "Kadang-Kadang" :
        WeeklyMeditation = 5
    elif WeeklyMeditation == "Sering" :
        WeeklyMeditation = 6
    elif WeeklyMeditation == "Sangat Sering" :
        WeeklyMeditation = 7
    elif WeeklyMeditation == "Biasanya" :
        WeeklyMeditation = 8
    elif WeeklyMeditation == "Hampir Selalu" :
        WeeklyMeditation = 9
    elif WeeklyMeditation == "Selalu" :
        WeeklyMeditation = 10

    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.weeklyMeditation = WeeklyMeditation
            st.session_state.page_number = 10
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 8
            st.experimental_rerun()

def page10():
    st.markdown("""
        <div style="text-align: center;">
            <h1>To Do Completed</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    ToDoCompleted = st.select_slider('SEBERAPA SERING ANDA MENYELESAIKAN DAFTAR YANG HARUS DILAKUKAN MINGGUAN?', 
                                     options=["Tidak Pernah", "Hampir Tidak Pernah", "Jarang", "Sangat Jarang", "Kadang-Kadang", "Sering", "Sangat Sering", "Biasanya","Hampir Selalu", "Selalu"])
    
    if ToDoCompleted == "Tidak Pernah" :
        ToDoCompleted = 1
    elif ToDoCompleted == "Hampir Tidak Pernah" :
        ToDoCompleted = 2
    elif ToDoCompleted == "Jarang" :
        ToDoCompleted = 3
    elif ToDoCompleted == "Sangat Jarang" :
        ToDoCompleted = 4
    elif ToDoCompleted == "Kadang-Kadang" :
        ToDoCompleted = 5
    elif ToDoCompleted == "Sering" :
        ToDoCompleted = 6
    elif ToDoCompleted == "Sangat Sering" :
        ToDoCompleted = 7
    elif ToDoCompleted == "Biasanya" :
        ToDoCompleted = 8
    elif ToDoCompleted == "Hampir Selalu" :
        ToDoCompleted = 9
    elif ToDoCompleted == "Selalu" :
        ToDoCompleted = 10

    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.toDoCompleted = ToDoCompleted
            st.session_state.page_number = 11
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 9
            st.experimental_rerun()

def page11():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Core Circle</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    CoreCircle = st.slider('BERAPA BANYAK ORANG YANG SANGAT DEKAT DENGAN ANDA?', min_value=1, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.coreCircle = CoreCircle
            st.session_state.page_number = 12
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 10
            st.experimental_rerun()

def page12():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Achievement</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    Achievement = st.slider('BERAPA PENCAPAIAN LUAR BIASA YANG ANDA BANGGAKAN?', min_value=0, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.achievement = Achievement
            st.session_state.page_number = 13
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 11
            st.experimental_rerun()

def page13():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Flow</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    Flow = st.slider('DALAM SEHARI, BERAPA JAM ANDA MERASA HANYA MENGIKUTI ALUR? (MELAKUKAN HAL YANG SAMA DENGAN HARI SEBELUMNYA)', min_value=0, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.flow = Flow
            st.session_state.page_number = 14
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 12
            st.experimental_rerun()

def page14():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Personal Awards</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    PersonalAwards = st.slider('BERAPA BANYAK PENGAKUAN YANG TELAH ANDA TERIMA DALAM HIDUP ANDA? (PENCAPAIAN HIDUP)', min_value=0, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.personalAwards = PersonalAwards
            st.session_state.page_number = 15
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 13
            st.experimental_rerun()

def page15():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Live Vision</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    LiveVision = st.slider('SEBERAPA JAUH ANDA MEMILIKI PANDANGAN TENTANG HIDUP ANDA KEDEPANNYA? (DALAM TAHUN)', min_value=0, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.liveVision = LiveVision
            st.session_state.page_number = 16
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 14
            st.experimental_rerun()

def page16():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Places Visited</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    PlacesVisited = st.slider('BERAPA BANYAK TEMPAT BARU YANG ANDA KUNJUNGI DALAM TIGA BULAN TERAKHIR?', min_value=0, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.placesVisited = PlacesVisited
            st.session_state.page_number = 17
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 15
            st.experimental_rerun()

def page17():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Supporting Other</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    SupportingOthers = st.slider('BERAPA BANYAK ORANG YANG ANDA BANTU MENCAPAI HIDUP YANG LEBIH BAIK? (MEMBERI BANTUAN SARAN, DANA, DLL)', min_value=0, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.supportingOthers = SupportingOthers
            st.session_state.page_number = 18
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 16
            st.experimental_rerun()

def page18():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Social Network</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    SocialNetwork = st.slider('BIASANYA BERAPA BANYAK ORANG YANG BERINTERAKSI DENGAN ANDA DALAM SEHARI?', min_value=0, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.socialNetwork = SocialNetwork
            st.session_state.page_number = 19
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 17
            st.experimental_rerun()

def page19():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Day Vacation</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    LostVacation = st.slider('BERAPA HARI BIASANYA ANDA HABISKAN UNTUK LIBURAN (PERJALANAN JAUH/LIBURAN TAHUNAN)?', min_value=0, max_value=10, value=5)
    
    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.lostVacation = LostVacation
            st.session_state.page_number = 20
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 18
            st.experimental_rerun()

def page20():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Income</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)

    SufficientIncome = st.radio('CUKUPKAH PENGHASILAN ANDA UNTUK MENUTUP BIAYA HIDUP DASAR?', ['Tidak Mencukupi', 'Mencukupi'])
    
    if SufficientIncome == "Tidak Mencukupi":
        SufficientIncome = 1
    elif SufficientIncome == "Mencukupi":
        SufficientIncome = 2

    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('Selanjutnya', use_container_width=True):
            st.session_state.sufficientIncome = SufficientIncome
            st.session_state.page_number = 21
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 19
            st.experimental_rerun()

def page21():
    
    st.markdown("""
        <div style="text-align: center;">
            <h1>Donation</h1>
                <br><br>
        </div>
    """, unsafe_allow_html=True)
    
    Donation = st.slider('SEBERAPA SERING ANDA MENYEDIAKAN WAKTU ATAU UANG ANDA UNTUK TUJUAN BAIK?', min_value=1, max_value=5, value=3)

    FruitsVeggies = st.session_state.fruitsVeggies
    PlacesVisited = st.session_state.placesVisited
    CoreCircle = st.session_state.coreCircle
    SupportingOthers = st.session_state.supportingOthers
    SocialNetwork = st.session_state.socialNetwork
    Achievement = st.session_state.achievement
    BMIRange = st.session_state.bmiRange
    ToDoCompleted = st.session_state.toDoCompleted
    Flow = st.session_state.flow
    DailySteps = st.session_state.dailySteps
    LiveVision = st.session_state.liveVision
    SleepHours = st.session_state.sleepHours
    LostVacation = st.session_state.lostVacation
    DailyShouting = st.session_state.dailyShouting
    SufficientIncome = st.session_state.sufficientIncome
    PersonalAwards = st.session_state.personalAwards
    TimeForPassion = st.session_state.timeForPassion
    WeeklyMeditation = st.session_state.weeklyMeditation
    Gender = st.session_state.gender
    Age = st.session_state.age

    backCol,nextCol  = st.columns([1,1])
    with nextCol:
        if st.button('PREDIKSI', use_container_width=True):
            diagnosis, proba = stresslevel_prediction([
                FruitsVeggies, PlacesVisited, CoreCircle, SupportingOthers, SocialNetwork,
                Achievement, Donation, BMIRange, ToDoCompleted, Flow, DailySteps, LiveVision,
                SleepHours, LostVacation, DailyShouting, SufficientIncome, PersonalAwards,
                TimeForPassion, WeeklyMeditation, Age, Gender
            ])
            st.session_state.result = diagnosis
            st.session_state.proba = proba
            st.session_state.page_number = 22
            st.experimental_rerun()
    with backCol:
        if st.button('Kembali', use_container_width=True):
            st.session_state.page_number = 20
            st.experimental_rerun()

def hasil():
    st.markdown("""
        <div style="text-align: center;">
            <h1>Kesimpulan</h1>
        </div>
    """, unsafe_allow_html=True)
    if "result" in st.session_state:
        st.markdown(f"""
            <div style="text-align: center;">
                <h2>{st.session_state.result}</h2>
            </div>
        """, unsafe_allow_html=True)
        if "proba" in st.session_state:
            display_probability(st.session_state.proba)
        if st.session_state.result == "Rendah":
            st.markdown("""
                            <style>
                                .justified-text {
                                    text-align: justify;
                                    text-indent: 40px;
                                }
                            </style>
                            """, unsafe_allow_html=True)
            st.write("""
                        <div class="justified-text">
                            Berdasarkan data yang Anda berikan, Anda tergolong mengalami Stres Tingkat Rendah. Terus pertahankan level ini
                        </div>
                        """, unsafe_allow_html=True)
        elif st.session_state.result == "Menengah":
            st.markdown("""
                            <style>
                                .justified-text {
                                    text-align: justify;
                                    text-indent: 40px;
                                }
                            </style>
                            """, unsafe_allow_html=True)
            st.write("""
                        <div class="justified-text">
                            Berdasarkan data yang Anda berikan, Anda tergolong mengalami Stres Tingkat Menengah. Pada level ini, Anda mungkin mengalami stres secara tiba-tiba. Disarankan untuk mengurangi tingkat stres.
                            Anda dapat mengunjungi halaman berikut untuk mendapatkan tips mengurangi tingkat stres<div>    
                            <ol>
                                <li><a href="https://www.mentalhealth.org.uk/explore-mental-health/publications/how-manage-and-reduce-stress">How to Manage Stress (Mental Health Foundation)</a></li>
                                <li><a href="https://www.alodokter.com/ternyata-tidak-sulit-mengatasi-stres">Cara Mengatasi Stress (Alodokter)</a></li>
                            </ol>
                        </div>
                        """, unsafe_allow_html=True)
        elif st.session_state.result == "Tinggi":
            st.markdown("""
                            <style>
                                .justified-text {
                                    text-align: justify;
                                    text-indent: 40px;
                                }
                            </style>
                            """, unsafe_allow_html=True)
            st.write("""
                        <div class="justified-text">
                            Berdasarkan data yang Anda berikan, Anda tergolong mengalami Stres Tingkat Tinggi. sangat disarankan untuk mengurangi tingkat stres Anda. bila perlu konsultasikan ke psikolog untuk penanganan lebih lanjut
                            Anda dapat mengunjungi halaman berikut untuk mendapatkan tips mengurangi tingkat stres<br>
                        </div>
                     <div>    
                            <ol>
                                <li><a href="https://www.mentalhealth.org.uk/explore-mental-health/publications/how-manage-and-reduce-stress">How to Manage Stress (Mental Health Foundation)</a></li>
                                <li><a href="https://www.alodokter.com/ternyata-tidak-sulit-mengatasi-stres">Cara Mengatasi Stress (Alodokter)</a></li>
                            </ol>
                        </div>
                        """, unsafe_allow_html=True)

    

def main():
    if "page_number" not in st.session_state:
        st.session_state.page_number = 0

    if st.session_state.page_number == 0:
        page0()
    elif st.session_state.page_number == 1:
        page1()
    elif st.session_state.page_number == 2:
        page2()
    elif st.session_state.page_number == 3:
        page3()
    elif st.session_state.page_number == 4:
        page4()
    elif st.session_state.page_number == 5:
        page5()
    elif st.session_state.page_number == 6:
        page6()
    elif st.session_state.page_number == 7:
        page7()
    elif st.session_state.page_number == 8:
        page8()
    elif st.session_state.page_number == 9:
        page9()
    elif st.session_state.page_number == 10:
        page10()
    elif st.session_state.page_number == 11:
        page11()
    elif st.session_state.page_number == 12:
        page12()
    elif st.session_state.page_number == 13:
        page13()
    elif st.session_state.page_number == 14:
        page14()
    elif st.session_state.page_number == 15:
        page15()
    elif st.session_state.page_number == 16:
        page16()
    elif st.session_state.page_number == 17:
        page17()
    elif st.session_state.page_number == 18:
        page18()
    elif st.session_state.page_number == 19:
        page19()
    elif st.session_state.page_number == 20:
        page20()
    elif st.session_state.page_number == 21:
        page21()
    elif st.session_state.page_number == 22:
        hasil()
    
if __name__ == '__main__':
    main()
